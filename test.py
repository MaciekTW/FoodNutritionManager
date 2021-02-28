import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

import sqlite3


class DBoperation:
    def __init__(self, ):
        self.db = sqlite3.connect('tests.db')
        self.c = self.db.cursor()
        self.DB_create()

        self.productCoutner=0;
        self.mealCoutner=0;
        self.typeCoutner=0;

    def DB_create(self):
        try:
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
            self.db.commit()
        except:
            pass

    def DB_outside_query(self, sql):
        self.c.execute("{}".format(sql))
        if sql.startswith("SELECT"):
            print(self.c.fetchall())


    def DB_meal_insert(self, name, typeID,Recipe):
        self.c.execute("INSERT INTO Meal VALUES(?,?,?,?)", (self.mealCoutner, name, typeID, Recipe))
        self.mealCoutner+=1
        self.db.commit()

    def DB_product_insert(self,productName, kcal, carbo , sugar , protein , fat , packagePrice , packageWeight ):
        self.c.execute(
            "INSERT INTO Product VALUES(?,?,?,?,?,?,?,?,?)",
            (self.productCoutner, productName, kcal, carbo, sugar, protein, fat, packagePrice,packageWeight))
        self.productCoutner+=1
        self.db.commit()

    def DB_type_insert(self, name):
        self.c.execute(
            "INSERT INTO Type VALUES(?,?)",
            (self.typeCoutner, name))
        self.typeCoutner+=1
        self.db.commit()


    def DB_product_meal_insert(self, mealID,productID):
       self.c.execute("INSERT INTO Product_Meal VALUES(?,?)", (mealID,productID))
       self.db.commit()

    def DB_record_insert(self, mealID,productID,productWeight):
       self.c.execute("INSERT INTO Record VALUES(?,?,?,?)", (self.recordCounter,mealID,productID,productWeight))
       self.db.commit()


class MealAdd:
    def __init__(self):
        self.DB=DBoperation()

        self.DB.DB_product_insert("Product1",1,10,10.10,10,10,10,10)
        self.DB.DB_type_insert("diner")
        self.DB.DB_meal_insert("meal1",0,"BlaBla")
        self.DB.DB_meal_insert("meal2",0,"BlaBLa")
        self.DB.DB_meal_insert("meal3",0,"BlaBLa")
        self.DB.DB_meal_insert("meal2",0,"BlaBLa")
        self.DB.DB_meal_insert("meal3",0,"BlaBLa")

if __name__ == "__main__":
    obj=MealAdd()
    obj.DB.DB_outside_query("SELECT * FROM Meal")
