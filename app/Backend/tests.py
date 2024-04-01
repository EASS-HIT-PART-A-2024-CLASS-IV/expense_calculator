from fastapi.testclient import TestClient
from Backend.main import app
from Backend.models import expense
import pytest

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome!"

def test_create_expense():
    testExpense = {"Amount" : 100, "Description": "Food", "Date": "2024-01-01"}
    response = client.get("/createExpense", json = testExpense)
    assert response.status_code == 200
    assert response.json() == "Expense created!"

def test_get_all_expenses():
    testExpense = {"Amount" : 100, "Description": "Food", "Date": "2024-01-01"}
    response = client.get("/allExpenses")
    assert response.status_code == 200
    expenses = response.json()
    assert isinstance(expenses, list)

def test_delete_expense():
    #create expense
    testExpense = {"Amount" : 100, "Description": "Food", "Date": "2024-01-01"}
    createResponse = client.post("/createExpense", json=testExpense)
    assert createResponse.status_code == 200
    expenses_response = client.get("/allExpenses")
    assert expenses_response.status_code == 200
    expenses = expenses_response.json()
    assert isinstance(expenses, list)
    assert len(expenses) > 0  
    expenseID = expenses[0].get("id")
    # delete expense
    deleteResponse = client.delete(f"/deleteExpense?expenseDescriptions={expenseID}")
    assert deleteResponse.status_code == 200
    assert deleteResponse.text == "Expense deleted!"    

