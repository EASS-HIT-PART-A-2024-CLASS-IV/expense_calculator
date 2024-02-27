import pymongo
from pymongo import MongoClient
from datetime import datetime

host = 'localhost'
port = 27017
dbname = 'expenseCalculator'

client = pymongo.MongoClient(f'mongodb://{host}:{port}/')
db = client[dbname]
expensesCollection = db['expenses']

try:
    def createExpense(expenseData):
        result = expensesCollection.insert_one(expenseData)
        return "Expense created succesfully"

    def deleteExpense(expenseID):
        result = expensesCollection.delete_one({"expenseID" : expenseID})
        return "Expense deleted succesfully" if result.deleted_count else "No expense found with that expense ID"

    def updateExpense(expenseID, expenseData):
        result = expensesCollection.update_one({{"expenseID" : expenseID}}, {"$set" : expenseData})
        return "Expense updated succesfully" if result.modified_count else "No expense found with that expense ID"

    def allExpenses():
        result = expensesCollection.find()
        return list(result)

    def sumOfExpenses():
        result = expensesCollection.aggregate([{"$group": {"_id": None, "total": {"$sum": "$amount"}}}])
        total = list(result)[0]['total'] if result.alive else 0
        return {"totalAmount": total}
        
    # Fetch all the records
    results = expensesCollection.find({})
    for result in results:
        print(result)

finally:
    client.close()
    