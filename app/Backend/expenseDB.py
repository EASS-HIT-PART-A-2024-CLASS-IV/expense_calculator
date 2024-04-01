import pymongo
from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb://root:root@mongodb:27017/?authMechanism=DEFAULT")
db = client['expenseCalculator']
expensesCollection = db['expensesCollection']

def createNewExpense(expenseData):
    try:
        result = expensesCollection.insert_one(expenseData)
        return result 
    except Exception as e:
        print ("An error occurred while creating the expense:", e)
        return None

def allExpenses():
    try:
        result = expensesCollection.find({}, {"_id": 0})
        listOfExpenses = list(result)
        return listOfExpenses
    except Exception as e:
        print ("An error occurred while showing the expense:", e)
        return None
    
def deleteExpense(Description):
    try:
        expensesCollection.delete_one({"Description": Description})
        return True
    except Exception as e:
        print ("An error occurred while showing the expense:", e)
        return False

def sumOfExpenses():
    result = expensesCollection.aggregate([{"$group": {"_id": None, "total": {"$sum": "$amount"}}}])
    total = list(result)[0]['total'] if result.alive else 0
    return {"totalAmount": total}
        
    
    