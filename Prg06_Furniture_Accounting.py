choice_company_name = input("Please enter your company's name: ")
capital = 100000
print("You have", capital, "dollars as your capital amount.")

monthly_assets = {
    "DeliveryVan" : 2000,
    "Showroom" : 750,
    "Warehouse" : 1300,
    "Inventory" : 15000,
    "Machinery" : 10000
    }
total_monthly_assets = sum(monthly_assets.values())
print("Your total assets value is : " ,total_monthly_assets)

monthly_liabilities = {
    "BankLoan" : 1000,
    "Rent" : 5000,
    "Taxes" : 750,
    "SuppliesDebt" : 1000
    }
total_monthly_liabilities = sum(monthly_liabilities.values())
print("Your total liabilities value is : " ,total_monthly_liabilities)

monthly_owner_equity = total_monthly_assets - total_monthly_liabilities
print("Your monthly owner equity is: ", monthly_owner_equity)
 

monthly_expenses = {
    "Advertising" : 1000,
    "Materials" : 5000,
    "UtilityBills" : 750,
    "EmployeeSalaries" : 10000
    }
total_monthly_expenses = sum(monthly_expenses.values())
print("Your total expenses value is : " ,total_monthly_expenses)

price_of_furniture = float(input("Enter the price of each item: "))
furniture_quantities = int(input("Enter the quantities of the furniture: "))
daily_revenue = price_of_furniture * furniture_quantities
monthly_revenue = daily_revenue * 30
print("Your monthly revenue is: ", monthly_revenue)


monthly_profit = monthly_revenue - total_monthly_expenses
print("Your monthly profit is: ", monthly_profit)

print("Your final balance is: ", capital + monthly_profit)

 




