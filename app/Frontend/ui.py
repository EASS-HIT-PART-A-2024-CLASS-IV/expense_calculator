import streamlit as st
import requests
import json
import pandas as pd

st.set_page_config(page_title= "Expenses Calculator")
st.sidebar.image('expenseCalc.jpeg')

createExpenseURL = 'http://Backend:2345/createExpense'
deleteExpenseURL = "http://Backend:2345/deleteExpense"
allExpensesURL = "http://Backend:2345/allExpenses"
sumOfExpensesURL = "http://Backend:2345/calculateExpenses"

st.sidebar.title("Select your action")
action = st.sidebar.selectbox("Menu" , ["Create Expense", "Show All My Expenses", "Delete Expense", "Calculate Expenses"]) 

if action == "Create Expense":
    st.subheader("Create New Expense")
    Amount = st.number_input("Amount", min_value=0, value=0, step=1)
    Description = st.text_input("Description")
    Date = st.date_input("Date")

    if st.button("Create"):
        payload = {"Amount": Amount , "Description": Description , "Date": str(Date)}
        respones = requests.post(createExpenseURL, json = payload)
        if respones.status_code == 200:
            st.success("Expense created!")
            df = pd.DataFrame([{"Amount": Amount , "Description": Description , "Date": str(Date)}])
            st.write("Created expense:")
            st.dataframe(df)
        else:
            st.error("Falied to create expense, please try again")

elif action == "Show All My Expenses":
    st.subheader("All My Expenses")
    response = requests.get(allExpensesURL)
    if response.status_code == 200:
        allExpensesData = response.json()
        if allExpensesData:
            df = pd.DataFrame(allExpensesData)
            df = df.sort_values(by='Date',ascending=True)
            st.dataframe(df)
        else:
            st.info("No expenses to show")
    else:
       st.error("Falied to show expenses, please try again")


elif action == "Delete Expense":
    st.subheader("Delete Expense")
    response = requests.get(allExpensesURL)
    if response.status_code == 200:
        allExpensesData = response.json()
        if allExpensesData:
            df = pd.DataFrame(allExpensesData)
            selectedExpense = st.multiselect("Select the expense you want to delete", df["Description"])
            if st.button("Delete"):
                respones = requests.delete(deleteExpenseURL, json=selectedExpense)
                if respones.status_code == 200:
                    st.success("Expense deleted!")
                    df = df[~df["Description"].isin(selectedExpense)]
                    st.dataframe(df)
                    st.rerun()
                else:
                    st.error("Failed to delete the expense, please try again")
        else:
            st.info("No expenses to delete")
    else:
        st.error("Failed to delete expenses, please try again")

elif action == "Calculate Expenses":
    st.subheader("Calculate My Expenses")
    response = requests.get(allExpensesURL)
    if response.status_code == 200:
        allExpensesData = response.json()
        if allExpensesData:
            df = pd.DataFrame(allExpensesData)
            df = df.sort_values(by='Date',ascending=True)
            st.dataframe(df)
            sumOfExpenses = sum(df['Amount'])
            st.write(f"The total amount of all my expenses: ${sumOfExpenses}")
        else:
            st.info("No expenses to calculate")
    else:
        st.error("Failed to calculate expenses, please try again")






