from datetime import datetime
from datetime import date

now = datetime.now()
today = date.today()
d1 = today.strftime("%d/%m/%Y")

current_time = now.strftime("%H:%M:%S")

company_name = "RH Store"

company_adress = "Dubai"
company_city = "Dubai"

def generate_receipt(customer_name, items_purchased, total_amount):
    receipt = f"{'-'*30}\n"
    receipt += f"MONEY RECEIPT\n"
    receipt += f"{'-'*30}\n"
    receipt += f"{company_name}\n"
    receipt += f"{company_adress}\n"
    receipt += f"{company_city}\n"
    receipt += f"Date: {d1}\n"
    receipt += f"Time: {current_time}\n"
    receipt += f"{'-'*30}\n"
    receipt += f"Customer Name: {customer_name}\n"
    receipt += f"{'-'*30}\n"
    receipt += f"{'Item':<15}{'Amount ($)':>15}\n"
    receipt += f"{'-'*30}\n"
    for item, amount in items_purchased.items():
        receipt += f"{item:<15}{amount:>15.2f}\n"
    receipt += f"{'-'*30}\n"
    receipt += f"Total Amount: {total_amount:.2f} $\n"
    receipt += f"{'-'*30}\n"
    return receipt

customer_name = input("Enter Customer Name: ")
num_items = int(input("How many items did the customer purchase?\nPlease Amount The Product: "))

items_purchased = {}
for i in range(num_items):
    item = input("Enter item name: ")
    amount = float(input("Enter amount for item in $: "))
    items_purchased[item] = amount

total_amount = sum(items_purchased.values())

receipt = generate_receipt(customer_name, items_purchased, total_amount)
print(receipt)