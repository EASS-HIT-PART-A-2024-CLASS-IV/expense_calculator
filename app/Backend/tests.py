from fastapi.testclient import TestClient
from Backend.main import app
import pytest

client = TestClient(app)

#Data for testing
expense_for_test = { "amount" : 500, "description" : "Test" , "date" : "2024-01-01" }

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome!"

def test_create_expense():
    response = client.get("/createExpense", json = expense_for_test)
    assert response.status_code == 200
    assert response.json() == "Expense created!"

def test_delete_expense():
    #create expense
    create_response = client.post("/createExpense" , json = expense_for_test)
    assert response.status_code == 200
    expense_id = create_response.json().get("id")

    #delete expense
    response = client.delete(f"/deleteExpense?expenseID={expense_id}")
    assert response.status_code == 200
    assert response.json() == "Expense deleted!"
    
def test_update_expense():
    #create expense
    create_response = client.post("/createExpense" , json = expense_for_test)
    assert response.status_code == 200
    expense_id = create_response.json().get("id")

    #update expense
    updated_expense_data = {"amount" : 250, "description" : "update test" , "date" : "2024-02-01" }
    response = client.put(f"/updateExpense?expenseID={expense_id}" , json = expense_for_test)
    assert response.status_code == 200
    assert response.json() == "Expense updated!"    

def test_get_all_expenses():
    response = client.get("/allExpenses", json = expense_for_test)
    assert response.status_code == 200
    assert response.json() == {"message" : []}