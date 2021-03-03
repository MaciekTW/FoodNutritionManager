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
            self.recordCounter = recordCounter[0] + 1

        self.c.close()

    def __del__(self):
        self.c.close()
        self.db.close()

    def DB_create(self):
        try:
            self.c = self.db.cursor()
            self.c.execute(
                "CREATE TABLE Product(productID INT,productName TEXT, kcal REAL, carbo REAL, sugar REAL, protein REAL, fat REAL, packagePrice REAL, packageWeight REAL,desc TEXT)")
            self.c.execute("CREATE TABLE Meal(mealID INT,mealName TEXT, typeID INT,recipe TEXT)")
            self.c.execute("CREATE TABLE Type(typeID INT, typeName TEXT)")
            self.c.execute("CREATE TABLE Product_Meal(mealID INT, productID INT)")
            self.c.execute("CREATE TABLE Record(recordID INT,mealID INT, productID INT,productWeight INT)")
            self.c.execute("CREATE TABLE DailyRecord(dailyID INT,recordID INT, userID INT, date TEXT)")
            self.c.execute(
                "CREATE TABLE User(userID INT,userName TEXT,userHeight INT, userWeightID INT, userWeightGoal REAL, userKcalLimit INT)")
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

    def DB_meal_insert(self, name, typeID, Recipe):
        self.c = self.db.cursor()
        self.c.execute("INSERT INTO Meal VALUES(?,?,?,?)", (self.Set_meal_ID(), name, typeID, Recipe))
        self.db.commit()
        self.c.close()

    def DB_product_insert(self, productName, kcal, carbo, sugar, protein, fat, packagePrice, packageWeight,desc):
        self.c = self.db.cursor()
        self.c.execute(
            "INSERT INTO Product VALUES(?,?,?,?,?,?,?,?,?,?)",
            (self.Set_product_ID(), productName, kcal, carbo, sugar, protein, fat, packagePrice, packageWeight,desc))
        self.db.commit()
        self.c.close()

    def DB_type_insert(self, name):
        self.c = self.db.cursor()
        self.c.execute(
            "INSERT INTO Type VALUES(?,?)",
            (self.Set_type_ID(), name))
        self.db.commit()
        self.c.close()

    def DB_user_insert(self, name,height,weight,weightGoal,kcalLimit):
        self.DB_weight_insert(self.Set_user_ID(),weight,self.today())
        self.c = self.db.cursor()
        self.c.execute(
            "INSERT INTO User VALUES(?,?,?,?,?,?)",
            (self.Get_user_Counter(), name,height,self.weightCounter,weightGoal,kcalLimit))
        self.db.commit()
        self.c.close()

    def DB_weight_insert(self, userID,weight,data):
        self.c = self.db.cursor()
        self.c.execute(
            "INSERT INTO Weight VALUES(?,?,?,?)",
            (self.Set_weight_ID(), userID,weight,data))
        self.db.commit()
        self.c.close()

    def DB_product_meal_insert(self, mealID, productID):
        self.c = self.db.cursor()
        self.c.execute("INSERT INTO Product_Meal VALUES(?,?)", (mealID, productID))
        self.db.commit()
        self.c.close()

    def DB_record_insert(self, mealID, productID, productWeight):
        self.c = self.db.cursor()
        self.c.execute("INSERT INTO Record VALUES(?,?,?,?)", (self.recordCounter, mealID, productID, productWeight))
        self.db.commit()
        self.c.close()

    def DB_daily_record_insert(self, recordID, UserID):
        self.c = self.db.cursor()
        self.c.execute("INSERT INTO DailyRecord VALUES(?,?,?,?)", (self.Set_daily_ID(), recordID, UserID, self.today()))
        self.db.commit()
        self.c.close()

    def Set_product_ID(self):
        self.productCounter += 1
        return self.productCounter

    def Set_user_ID(self):
        self.userCounter += 1
        return self.userCounter

    def Get_user_Counter(self):
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

    def add_record(self, list, type, meal, desc):
        typeID = self.DB_type_find(type)
        self.c = self.db.cursor()
        self.c.execute("INSERT INTO Meal VALUES(?,?,?,?)", (self.Set_meal_ID(), meal, typeID, desc))
        self.db.commit()
        mealID = self.DB_meal_find(meal)
        self.c = self.db.cursor()
        for ingredient in list:
            self.c.execute("INSERT INTO Product_Meal VALUES(?,?)", (mealID, ingredient['nameID']))
            self.db.commit()
            self.c.execute("INSERT INTO Record VALUES(?,?,?,?)",
                           (self.recordCounter, mealID, ingredient['nameID'], ingredient['weight']))
            self.db.commit()

        self.c.close()

    def DB_get_product_name(self, productID):
        self.c = self.db.cursor()
        self.c.execute("SELECT productName FROM Product WHERE productId=?", (productID,))
        self.db.commit()
        temp = self.c.fetchone()[0]
        self.c.close()
        return temp

    def DB_get_product_weight(self, productID, recordID):
        self.c = self.db.cursor()
        self.c.execute("SELECT productWeight FROM Record WHERE productId=? AND recordID-?", (productID, recordID))
        self.db.commit()
        temp = self.c.fetchone()[0]
        self.c.close()
        return temp

    def DB_get_meal_name(self, mealID):
        self.c = self.db.cursor()
        self.c.execute("SELECT mealName FROM Meal WHERE mealID=?", (mealID,))
        self.db.commit()
        temp = self.c.fetchone()[0]
        self.c.close()
        return temp

    def today(self):
        self.c = self.db.cursor()
        self.c.execute("SELECT DATE('NOW')")
        self.db.commit()
        temp = self.c.fetchone()[0]
        self.c.close()
        return temp

    def DB_type_find(self, Type):
        self.c = self.db.cursor()
        self.c.execute("SELECT typeID FROM Type WHERE typeName=?", (Type,))
        temp = self.c.fetchone()
        self.db.commit()
        self.c.close()
        if temp is None:
            return -1
        else:
            return temp[0]

    def DB_meal_find(self, meal):
        self.c = self.db.cursor()
        self.c.execute("SELECT mealID FROM Meal WHERE mealName=?", (meal,))
        temp = self.c.fetchone()
        self.db.commit()
        self.c.close()
        if temp is None:
            return -1
        else:
            return temp[0]

    def DB_product_find(self, product):
        self.c = self.db.cursor()
        self.c.execute("SELECT productID FROM Product WHERE productName=?", (product,))
        temp = self.c.fetchone()
        self.db.commit()
        self.c.close()
        if temp is None:
            return -1
        else:
            return temp[0]

    def DB_record_find(self, mealID):
        self.c = self.db.cursor()
        self.c.execute("SELECT DISTINCT recordID FROM Record WHERE mealID=? ORDER BY recordID DESC", (mealID,))
        temp = self.c.fetchone()
        self.db.commit()
        self.c.close()
        if temp is None:
            return -1
        else:
            return temp[0]

    def get_products_names(self):
        self.c = self.db.cursor()
        self.c.execute("SELECT productName FROM Product")
        temp = self.c.fetchall()
        self.db.commit()
        templist = []
        for tuple in temp:
            templist.append(tuple[0])
        self.c.close()
        return templist

    def get_meals_names(self):
        self.c = self.db.cursor()
        self.c.execute("SELECT mealName FROM Meal")
        temp = self.c.fetchall()
        self.db.commit()
        templist = []
        for tuple in temp:
            templist.append(tuple[0])
        self.c.close()
        return templist

    def get_meal_kcal(self, mealID):
        self.c = self.db.cursor()
        self.c.execute(
            "SELECT SUM(kcal*(CAST(productWeight AS REAL)/100)) FROM Record LEFT JOIN Product ON Product.productID=Record.productID WHERE mealID=? GROUP BY(recordID) ORDER BY recordID,Product.productID DESC",
            (mealID,))
        temp = self.c.fetchone()
        self.c.close()
        return temp

    def get_meal_ingredients(self, mealID):
        recordID = self.DB_record_find(mealID)
        self.c = self.db.cursor()
        self.c.execute(
            "SELECT productName,productWeight FROM Record LEFT JOIN Product ON Product.productID=Record.productID WHERE mealID=? AND recordID=? ORDER BY recordID DESC",
            (mealID, recordID))
        temp = self.c.fetchall()
        self.c.close()
        return temp

    def DB_all_table_clear(self):
        self.c = self.db.cursor()
        self.c.execute("DELETE FROM Product")
        self.c.execute("DELETE FROM Meal")
        self.c.execute("DELETE FROM Type")
        self.c.execute("DELETE FROM Product_Meal")
        self.c.execute("DELETE FROM DailyRecord")
        self.c.execute("DELETE FROM User")
        self.c.execute("DELETE FROM Weight")
        self.typeCounter = 0
        self.mealCounter = 0
        self.productCounter = 0
        self.recordCounter = 0
        self.userCounter = 0
        self.dailyCounter = 0
        self.weightCounter = 0
        self.db.commit()
        self.c.close()

    def day_meals_print(self, day):
        self.c = self.db.cursor()
        self.c.execute(
            "SELECT DISTINCT Meal.mealID,dailyRecord.recordID FROM Meal LEFT JOIN Record ON Meal.mealID=Record.mealID LEFT JOIN DailyRecord ON Record.recordID=DailyRecord.recordID WHERE date=?",
            (day,))

        temp = self.c.fetchall()
        self.c.close()
        return temp

    def meal_name_from_record(self,recordID,mealID):
        self.c = self.db.cursor()

        self.c.execute("SELECT DISTINCT mealName FROM Meal LEFT JOIN Record ON Record.mealID=Meal.mealID WHERE Meal.mealID=? AND Record.recordID=?",(mealID,recordID))
        temp=self.c.fetchall()
        self.c.close()
        return temp

    def meal_kcal_from_record(self,recordID,mealID):
        self.c = self.db.cursor()
        self.c.execute(
            "SELECT SUM(kcal*(CAST(productWeight AS REAL)/100)) FROM Record LEFT JOIN Product ON Product.productID=Record.productID WHERE mealID=? AND recordID=? GROUP BY(recordID) ORDER BY Product.productID DESC",
            (mealID,recordID))
        temp = self.c.fetchone()
        self.c.close()
        return temp

    def meal_carbo_from_record(self,recordID,mealID):
        self.c = self.db.cursor()

        self.c.execute(
            "SELECT SUM(carbo*(CAST(productWeight AS REAL)/100)) FROM Record LEFT JOIN Product ON Product.productID=Record.productID WHERE mealID=? AND recordID=? GROUP BY(recordID) ORDER BY Product.productID DESC",
            (mealID, recordID))
        temp=self.c.fetchall()
        self.c.close()
        return temp

    def meal_sugar_from_record(self,recordID,mealID):
        self.c = self.db.cursor()

        self.c.execute(
            "SELECT SUM(sugar*(CAST(productWeight AS REAL)/100)) FROM Record LEFT JOIN Product ON Product.productID=Record.productID WHERE mealID=? AND recordID=? GROUP BY(recordID) ORDER BY Product.productID DESC",
            (mealID, recordID))
        temp=self.c.fetchall()
        self.c.close()
        return temp

    def meal_protein_from_record(self,recordID,mealID):
        self.c = self.db.cursor()

        self.c.execute(
            "SELECT SUM(protein*(CAST(productWeight AS REAL)/100)) FROM Record LEFT JOIN Product ON Product.productID=Record.productID WHERE mealID=? AND recordID=? GROUP BY(recordID) ORDER BY Product.productID DESC",
            (mealID, recordID))
        temp=self.c.fetchall()
        self.c.close()
        return temp

    def meal_fat_from_record(self,recordID,mealID):
        self.c = self.db.cursor()

        self.c.execute(
            "SELECT SUM(fat*(CAST(productWeight AS REAL)/100)) FROM Record LEFT JOIN Product ON Product.productID=Record.productID WHERE mealID=? AND recordID=? GROUP BY(recordID) ORDER BY Product.productID DESC",
            (mealID, recordID))
        temp=self.c.fetchall()
        self.c.close()
        return temp

    def kcal_from_day(self,day):
        self.c = self.db.cursor()
        self.c.execute(
            """SELECT SUM(kcal*(CAST(productWeight AS REAL)/100)) 
            FROM Product 
            LEFT JOIN Record ON Product.productID=Record.productID 
            LEFT JOIN DailyRecord ON DailyRecord.recordID=Record.recordID 
            WHERE date=? GROUP BY(dailyID) ORDER BY Product.productID DESC""",
            (day,))
        temp = self.c.fetchall()
        sum=0
        for meal in temp:
            sum+=meal[0]
        self.c.close()
        return round(sum,0)

    def get_user_kcal_limit(self,userID):
        self.c = self.db.cursor()
        self.c.execute("SELECT userKcalLimit FROM User WHERE userID=?",(userID,))
        temp=self.c.fetchone()
        self.c.close()
        return temp

    def get_active_user(self):
        self.c = self.db.cursor()
        self.c.execute("SELECT User.userID FROM User LEFT JOIN DailyRecord ON DailyRecord.userID=User.userID ORDER BY date DESC")
        temp = self.c.fetchone()
        self.c.close()
        return temp

    def get_user_height(self,userID):
        self.c = self.db.cursor()
        self.c.execute("SELECT userHeight FROM User WHERE userID=?",(userID,))
        temp=self.c.fetchone()
        self.c.close()
        return temp

    def get_user_weight_goal(self,userID):
        self.c = self.db.cursor()
        self.c.execute("SELECT userWeightGoal FROM User WHERE userID=?",(userID,))
        temp=self.c.fetchone()
        self.c.close()
        return temp

    def get_user_weight(self,userID):
        self.c = self.db.cursor()
        self.c.execute("SELECT Weight FROM User WHERE userID=?",(userID,))
        temp=self.c.fetchone()
        self.c.close()
        return temp

# db.DB_outside_query("SELECT * FROM Meal")
# db.DB_outside_query("SELECT * FROM Type")
# print(db.get_products_names())

# options = ["Breakfast", "Dinner", "Supper", "Snack", " Desert"]
obj = DBoperation("tw.db")
print(obj.kcal_from_day("obj.today()"))
obj.DB_outside_query("SELECT * FROM Weight")
# # obj.DB_outside_query("SELECT * FROM Meal")
# # obj.DB_outside_query("SELECT * FROM Type")
# obj.DB_outside_query("SELECT * FROM Product_Meal")
# obj.DB_outside_query("SELECT * FROM DailyRecord")
#
# print(obj.day_meals_print(obj.today()))
# print(obj.meal_kcal_from_record(1,1))
# for i in options:
#     obj.DB_type_insert(i)


# obj.DB_outside_query("SELECT * FROM products")
# obj.DB_outside_query("SELECT * FROM meal_type")
# obj.DB_all_table_clear()
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
