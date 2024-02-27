from fastapi import FastAPI
from pydantic import BaseModel
from models import expense
from typing import List
import expenseDB
from expenseDB import createExpense, deleteExpense, updateExpense, allExpenses, sumOfExpenses
import uvicorn

app = FastAPI()
    
@app.get("/")
def root():
    return ("Welcome to the expenses calculator!")

#create expence
@app.post("/createExpense")
def creatExpense(expense: expense):
    newExpense = {"amount" : expense.amount, "description" : expense.description, "date" : expense.date}
    return expenseDB.createExpense(newExpense)

#delete expence
@app.post("/deleteExpense")
def deleteExpense(expenseID: int):
    return expenseDB.deleteExpense(expenseID)

#update expence
@app.put("/updateExpense")
def updateExpense(expense: expense, expenseID: int):
    expense = {"amount" : expense.amount, "description" : expense.description, "date" : expense.date}
    return expenseDB.updateExpense(expense, expenseID)   
  

#get list of all the expenses
@app.get("/allExpenses")
def allExpenses():
    return expenseDB.allExpenses()

#calculate the sum of all the expenses
@app.get("/calculateExpensesByMonthORYear")
def calculateExpenses():
    return expenseDB.sumOfExpenses()
