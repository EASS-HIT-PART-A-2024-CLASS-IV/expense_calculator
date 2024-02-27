About the app:
In this app you can manage your expences.
You can creart, update, delete and calculate your expenses.

How to run the backend part?
1. Enter the "Backend" folder
2. Run the following commands:
    docker build . -t expense_calcolation -f Dockerfile
    docker run -p8070:80 app-dot-prod