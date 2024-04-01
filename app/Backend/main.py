from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import expense
from typing import List
import expenseDB
from expenseDB import createNewExpense, allExpenses, deleteExpense, sumOfExpenses
import uvicorn

app = FastAPI()
    
@app.get("/")
def root():
    return "Welcome to the expenses calculator!"

#create expence
@app.post("/createExpense")
def creatExpense(expense: expense):
    newExpense = {"Amount" : expense.Amount, "Description" : expense.Description, "Date" : expense.Date.isoformat()}
    response = createNewExpense(newExpense)
    return "Expense created!"

#get list of all the expenses
@app.get("/allExpenses")
def allExpenses():
    listOfAllExpenses = expenseDB.allExpenses()
    if listOfAllExpenses is None:
        raise HTTPException (status_code=500, detail="No expenses to show")
    return listOfAllExpenses

#delete expence
@app.delete("/deleteExpense")
def deleteExpense(expenseDescriptions: List[str]): 
    for expenseDescription in expenseDescriptions:
        expenseDB.deleteExpense(expenseDescription)
    return "Expense deleted"

#calculate the sum of all the expenses
@app.get("/calculateExpenses")
def calculateExpenses():
    return expenseDB.sumOfExpenses()

if __name__ == "__main__":
    uvicorn.run("Backend:app", host="0.0.0.0", port=2345)

  



