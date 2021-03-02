import sqlite3


class DBoperation:
    def __init__(self, DBname):
        self.db = sqlite3.connect('testy.db')
        self.DB_create()
        self.c = self.db.cursor()

        self.c.execute("SELECT mealID FROM Meal ORDER BY mealID DESC")
        mealCounter = self.c.fetchone()
        self.c.execute("SELECT productID FROM Product ORDER BY productID DESC")
        productCounter = self.c.fetchone()
        self.c.execute("SELECT typeID FROM Type ORDER BY typeID DESC")
        typeCounter = self.c.fetchone()
        self.c.execute("SELECT dailyID FROM DailyRecord ORDER BY dailyID DESC")
        dailyCounter = self.c.fetchone()
        self.c.execute("SELECT userID FROM User ORDER BY userID DESC")
        userCounter = self.c.fetchone()
        self.c.execute("SELECT userWeightID FROM Weight ORDER BY userWeightID DESC")
        weightCounter = self.c.fetchone()
        self.c.execute("SELECT recordID FROM Record ORDER BY recordID DESC")
        recordCounter = self.c.fetchone()
        self.db.commit()

        if mealCounter is None:
            self.mealCounter = 0
        else:
            self.mealCounter = mealCounter[0]

        if productCounter is None:
            self.productCounter = 0
        else:
            self.productCounter = productCounter[0]

        if typeCounter is None:
            self.typeCounter = 0
        else:
            self.typeCounter = typeCounter[0]

        if dailyCounter is None:
            self.dailyCounter = 0
        else:
            self.dailyCounter = dailyCounter[0]

        if userCounter is None:
            self.userCounter = 0
        else:
            self.userCounter = userCounter[0]

        if weightCounter is None:
            self.weightCounter = 0
        else:
            self.weightCounter = weightCounter[0]

        if recordCounter is None:
            self.recordCounter = 0
        else:
            self.recordCounter = recordCounter[0]+1


        self.c.close()

    def __del__(self):
        self.c.close()
        self.db.close()



    def DB_create(self):
        try:
            self.c = self.db.cursor()
            self.c.execute(
                "CREATE TABLE Product(productID INT,productName TEXT, kcal REAL, carbo REAL, sugar REAL, protein REAL, fat REAL, packagePrice REAL, packageWeight REAL)")
            self.c.execute("CREATE TABLE Meal(mealID INT,mealName TEXT, typeID INT,recipe TEXT)")
            self.c.execute("CREATE TABLE Type(typeID INT, typeName TEXT)")
            self.c.execute("CREATE TABLE Product_Meal(mealID INT, productID INT)")
            self.c.execute("CREATE TABLE Record(recordID INT,mealID INT, productID INT,productWeight INT)")
            self.c.execute("CREATE TABLE DailyRecord(dailyID INT,recordID INT, userID INT, date TEXT)")
            self.c.execute("CREATE TABLE User(userID INT,userName TEXT,userHeight INT, userWeightID INT, userWeightGoal REAL, userKcalLimit INT)")
            self.c.execute(
                "CREATE TABLE Weight(userWeightID INT,userID INT,weight REAL, data TEXT)")
            self.c.close()
            self.db.commit()

        except:
            pass

    def DB_outside_query(self, sql):
        self.c = self.db.cursor()
        self.c.execute("{}".format(sql))
        self.db.commit()
        if sql.startswith("SELECT"):
            print(self.c.fetchall())
        self.c.close()
        self.c.close()

    def DB_meal_product_insert(self, mealID, productID):
        self.c = self.db.cursor()
        self.c.execute("INSERT INTO Product_Meal VALUES(?,?)", (mealID, productID))
        self.db.commit()
        self.c.close()

    def DB_meal_insert(self, name, typeID,Recipe):
        self.c = self.db.cursor()
        self.c.execute("INSERT INTO Meal VALUES(?,?,?,?)", (self.Set_meal_ID(), name, typeID, Recipe))
        self.db.commit()
        self.c.close()

    def DB_product_insert(self,productName, kcal, carbo , sugar , protein , fat , packagePrice , packageWeight ):
        self.c = self.db.cursor()
        self.c.execute(
            "INSERT INTO Product VALUES(?,?,?,?,?,?,?,?,?)",
            (self.Set_product_ID(), productName, kcal, carbo, sugar, protein, fat, packagePrice,packageWeight))
        self.db.commit()
        self.c.close()

    def DB_type_insert(self, name):
        self.c = self.db.cursor()
        self.c.execute(
            "INSERT INTO Type VALUES(?,?)",
            (self.Set_type_ID(), name))
        self.db.commit()
        self.c.close()


    def DB_product_meal_insert(self, mealID,productID):
        self.c = self.db.cursor()
        self.c.execute("INSERT INTO Product_Meal VALUES(?,?)", (mealID,productID))
        self.db.commit()
        self.c.close()

    def DB_record_insert(self, mealID,productID,productWeight):
        self.c = self.db.cursor()
        self.c.execute("INSERT INTO Record VALUES(?,?,?,?)", (self.recordCounter,mealID,productID,productWeight))
        self.db.commit()
        self.c.close()

    def DB_daily_record_insert(self, recordID,UserID):
        self.c = self.db.cursor()
        self.c.execute("INSERT INTO Record VALUES(?,?,?,?)", (self.Set_daily_ID(),recordID,UserID,self.today()))
        self.db.commit()
        self.c.close()

    def Set_product_ID(self):
        self.productCounter += 1
        return self.productCounter

    def Set_user_ID(self):
        self.userCounter += 1
        return self.userCounter

    def Set_meal_ID(self):
        self.mealCounter += 1
        return self.mealCounter

    def Set_weight_ID(self):
        self.weightCounter += 1
        return self.weightCounter

    def Set_record_ID(self):
        self.recordCounter += 1
        return self.recordCounter

    def Set_type_ID(self):
        self.typeCounter += 1
        return self.typeCounter

    def Set_daily_ID(self):
        self.dailyCounter += 1
        return self.dailyCounter

    def add_record(self,list,type,meal,desc):
        typeID=self.DB_type_find(type)
        self.c = self.db.cursor()
        self.c.execute("INSERT INTO Meal VALUES(?,?,?,?)", (self.Set_meal_ID(), meal, typeID, desc))
        self.db.commit()
        mealID=self.DB_meal_find(meal)
        self.c = self.db.cursor()
        for ingredient in list:
             self.c.execute("INSERT INTO Product_Meal VALUES(?,?)", (mealID, ingredient['nameID']))
             self.db.commit()
             self.c.execute("INSERT INTO Record VALUES(?,?,?,?)",
                            (self.recordCounter, mealID, ingredient['nameID'], ingredient['weight']))
             self.db.commit()

        self.c.close()


    def DB_get_product_name(self,productID):
        self.c = self.db.cursor()
        self.c.execute("SELECT productName FROM Product WHERE productId=?",(productID,))
        self.db.commit()
        temp=self.c.fetchone()[0]
        self.c.close()
        return temp

    def DB_get_product_weight(self,productID,recordID):
        self.c = self.db.cursor()
        self.c.execute("SELECT productWeight FROM Record WHERE productId=? AND recordID-?",(productID,recordID))
        self.db.commit()
        temp=self.c.fetchone()[0]
        self.c.close()
        return temp

    def DB_get_meal_name(self,mealID):
        self.c = self.db.cursor()
        self.c.execute("SELECT mealName FROM Meal WHERE mealID=?",(mealID,))
        self.db.commit()
        temp= self.c.fetchone()[0]
        self.c.close()
        return temp

    def today(self):
        self.c = self.db.cursor()
        self.c.execute("SELECT DATE('NOW')")
        self.db.commit()
        temp=self.c.fetchone()[0]
        self.c.close()
        return temp

    def DB_type_find(self, Type):
        self.c = self.db.cursor()
        self.c.execute("SELECT typeID FROM Type WHERE typeName=?",(Type,))
        temp=self.c.fetchone()
        self.db.commit()
        self.c.close()
        if temp is None:
            return -1
        else:
            return temp[0]

    def DB_meal_find(self, meal):
        self.c = self.db.cursor()
        self.c.execute("SELECT mealID FROM Meal WHERE mealName=?",(meal,))
        temp=self.c.fetchone()
        self.db.commit()
        self.c.close()
        if temp is None:
            return -1
        else:
            return temp[0]

    def DB_product_find(self, product):
        self.c = self.db.cursor()
        self.c.execute("SELECT productID FROM Product WHERE productName=?",(product,))
        temp=self.c.fetchone()
        self.db.commit()
        self.c.close()
        if temp is None:
            return -1
        else:
            return temp[0]

    def get_products_names(self):
        self.c = self.db.cursor()
        self.c.execute("SELECT productName FROM Product")
        temp=self.c.fetchall()
        self.db.commit()
        templist=[]
        for tuple in temp:
            templist.append(tuple[0])
        self.c.close()
        return templist

    def get_meals_names(self):
        self.c = self.db.cursor()
        self.c.execute("SELECT mealName FROM Meal")
        temp=self.c.fetchall()
        self.db.commit()
        templist=[]
        for tuple in temp:
            templist.append(tuple[0])
        self.c.close()
        return templist

    def get_meal_kcal(self,mealID):
        self.c=self.db.cursor()
        self.c.execute("SELECT SUM(kcal*(CAST(productWeight AS REAL)/100)) FROM Record LEFT JOIN Product ON Product.productID=Record.productID WHERE mealID=? GROUP BY(recordID) ORDER BY recordID DESC",(mealID,))
        temp=self.c.fetchone()
        self.c.close()
        return temp

    def get_meal_ingredients(self,mealID):
        self.c=self.db.cursor()
        self.c.execute("SELECT productName,productWeight FROM Record LEFT JOIN Product ON Product.productID=Record.productID WHERE mealID=? ORDER BY recordID DESC",(mealID,))
        temp=self.c.fetchall()
        self.c.close()
        return temp



    #
    #
    # def DB_print_product(self, n="all"):
    #     self.c.execute("SELECT * FROM products")
    #     if n == "all":
    #         return self.c.fetchall()
    #     else:
    #         return self.c.fetchmany(n)
    #
    # def DB_print_meals_from_day(self,day):
    #     self.c.execute("SELECT mealID FROM food_record WHERE date=?",(day,))
    #     return self.c.fetchall()
    #
    # def DB_print_meal(self, n="all"):
    #     self.c.execute("SELECT * FROM meal")
    #     if n == "all":
    #         return self.c.fetchall()
    #     else:
    #         return self.c.fetchmany(n)
    #
    # def DB_print_meal_products(self, mealID):
    #     self.c.execute("SELECT productID FROM meal_product WHERE mealID=?",(mealID,))
    #     if mealID == -1:
    #         return -1
    #     else:
    #         return self.c.fetchall()
    #
    # def DB_print_type(self, n="all"):
    #     self.c.execute("SELECT * FROM meal_type")
    #     if n == "all":
    #         return self.c.fetchall()
    #     else:
    #         return self.c.fetchmany(n)
    #
    # def DB_all_table_clear(self):
    #     self.c.execute("DELETE FROM products")
    #     self.c.execute("DELETE FROM meal")
    #     self.c.execute("DELETE FROM meal_type")
    #     self.c.execute("DELETE FROM food_record")
    #     self.c.execute("DELETE FROM meal_product")
    #     self.typeCounter = 0
    #     self.mealCounter = 0
    #     self.productCounter = 0
    #     self.recordID = 0
    #     self.db.commit()
    #
    # def DB_product_nutrition(self, id, meal):
    #     self.c.execute(
    #         """SELECT ROUND(products.kcal*(CAST(meal_product.weigth AS REAL)/100),2),
    #             ROUND(products.carbo*(CAST(meal_product.weigth AS REAL)/100),2),
    #             ROUND(products.sugar*(CAST(meal_product.weigth AS REAL)/100),2),
    #             ROUND(products.protein*(CAST(meal_product.weigth AS REAL)/100),2),
    #             ROUND(products.fat*(CAST(meal_product.weigth AS REAL)/100),2)
    #             FROM products LEFT JOIN meal_product ON products.productID=meal_product.productID
    #             WHERE products.productID=? AND meal_product.mealID=?""", (id, meal))
    #
    #     temp = self.c.fetchone()
    #     nutrition = {'kcal': temp[0], 'carbo': temp[1], 'sugar': temp[2], 'protein': temp[3], 'fat': temp[4]}
    #     return nutrition
    #
    # def DB_meal_nutriton(self, meal):
    #     self.c.execute("SELECT productID FROM meal_product WHERE mealID=?", (meal,))
    #     t = {'kcal': 0, 'carbo': 0, 'sugar': 0, 'protein': 0, 'fat': 0}
    #     for i in self.c.fetchall():
    #         for key in t:
    #             t[key] += self.DB_product_nutrition(i[0], meal)[key]
    #
    #     return t
    #
    # def DB_meal_price(self, meal):
    #     self.c.execute(
    #         "SELECT ROUND(price*weigth/100,2) FROM products LEFT JOIN meal_product ON products.productID=meal_product.productID WHERE mealID=?",
    #         (meal,))
    #     price = 0
    #     for i in self.c.fetchall():
    #         price += i[0]
    #
    #     return price
    #
    # def DB_add_meal(self, meal):
    #     self.c.execute("INSERT INTO food_record VALUES(?,?,DATE('NOW'))", (self.Set_record_ID(), meal))
    #     self.db.commit()
    #
    # def Set_record_ID(self):
    #     self.recordID += 1
    #     return self.recordID
    #
    # def today(self):
    #     self.c.execute("SELECT DATE('NOW')")
    #     return self.c.fetchone()[0]
    #
    # def DB_day_nutrition(self, day):
    #     self.c.execute("SELECT mealID FROM food_record WHERE date=?", (day,))
    #     t = {'kcal': 0, 'carbo': 0, 'sugar': 0, 'protein': 0, 'fat': 0}
    #     for i in self.c.fetchall():
    #         for key in t:
    #             t[key] += self.DB_meal_nutriton(i[0])[key]
    #
    #     return t
    #
    #
    #
    # def DB_meal_weight_update(self,meal,product,weight):
    #     self.c.execute("UPDATE meal_product SET weigth=? WHERE mealID=? AND productID=?",(weight,meal,product))
    #     self.db.commit()
    #
    # def DB_meal_product_delete(self,meal,product):
    #     self.c.execute("DELETE FROM meal_product WHERE mealID=? AND productID=?",(meal,product))
    #     self.db.commit()
    #
    # def DB_meal_delete(self,meal):
    #     self.c.execute("DELETE FROM meal_product WHERE mealID=?",(meal,))
    #     self.c.execute("DELETE FROM meal WHERE mealID=?",(meal,))
    #     self.mealCounter-=1
    #     self.db.commit()
    #
    # def mealCheck(self,id):
    #     self.c.execute("SELECT * FROM meal WHERE mealID=?",(id,))
    #     if self.c.fetchone() is None:
    #         return False
    #     else:
    #         return True
    #
    # def typeCheck(self,id):
    #     self.c.execute("SELECT * FROM meal_type WHERE typeID=?",(id,))
    #     if self.c.fetchone() is None:
    #         return False
    #     else:
    #         return True
    #
    # def mealFind(self,name):
    #     self.c.execute("SELECT mealID FROM meal WHERE name=?",(name,))
    #     temp=self.c.fetchone()
    #     if temp is None:
    #         return -1
    #     else:
    #         return temp[0]
    #

    #
    # def productFind(self,productName):
    #     self.c.execute("SELECT productID,kcal FROM products LEFT JOIN  ON WHERE name=?",(productName,))
    #     temp=self.c.fetchone()[0]
    #     return temp


# db.DB_outside_query("SELECT * FROM Meal")
# db.DB_outside_query("SELECT * FROM Type")
# print(db.get_products_names())

# options = ["Breakfast", "Dinner", "Supper", "Snack", " Desert"]
obj=DBoperation("tw.db")
# obj.DB_outside_query("SELECT * FROM Meal")
# obj.DB_outside_query("SELECT * FROM Type")
obj.DB_outside_query("SELECT * FROM Product_Meal")
obj.DB_outside_query("SELECT * FROM Record")
for i in obj.get_meal_ingredients(6):
    print(i)
# for i in options:
#     obj.DB_type_insert(i)


#obj.DB_outside_query("SELECT * FROM products")
# obj.DB_outside_query("SELECT * FROM meal_type")
#obj.DB_all_table_clear()
# obj.DB_outside_query("SELECT * FROM products")
# obj.DB_type_insert("dinner")
# obj.DB_type_insert("supper")
#
# obj.DB_product_insert("ser", 120, 123, 34.2, 42, 12, 12.60)
# obj.DB_product_insert("chleb", 135, 123, 34, 42, 12, 10.50)
#
# obj.DB_meal_insert("kanapka", 1)
#
# obj.DB_meal_insert("kanapka2", 1)
#
# obj.DB_meal_product_insert(1, 1, 85)
# obj.DB_meal_product_insert(1, 2, 150)
#
# obj.DB_meal_product_insert(2, 1, 100)
# obj.DB_meal_product_insert(2, 2, 150)
#
# # print(obj.DB_product_nutrition(1,1))
#
#
# obj.DB_add_meal(1)
# obj.DB_add_meal(2)
#
#
# obj.DB_meal_delete(1)
# obj.DB_outside_query("SELECT * FROM meal")
#
# print(obj.mealFind("kanapka"))
# print(obj.mealCheck(2))

