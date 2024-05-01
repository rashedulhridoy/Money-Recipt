from datetime import datetime
from datetime import date

now = datetime.now()
today = date.today()
d1 = today.strftime("%d/%m/%Y")

current_time = now.strftime("%H:%M:%S")

result = """\

$ Money Recipt


                    """
print(result) 

p1_name = input("Product: ")
p1_price= int(input("Price: "))
p2_name = input("Product: ")
p2_price= int(input("Price: "))
p3_name = input("Product: ")
p3_price= int(input("Price: "))

company_name = "RH Store"

company_adress = "Dubai"
company_city = "Dubai"

Message = "Thank You For Shopping With Us!"


#ok





print("*"*50)

print("\t{}".format(company_name))
print("\t{}".format(company_adress))
print("\t{}".format(company_city))
print("\t{}".format("Time: " + current_time))
print("\t{}\n".format("Date: " + d1))


print("*"*50)

print("\tName \tPrice")
print("\t{}\t${}".format(p1_name.title(), p1_price))
print("\t{}\t${}".format(p2_name.title(), p2_price))
print("\t{}\t${}".format(p3_name.title(), p3_price))

print("="*50)

print("\t\tTotal")

total = p1_price + p2_price + p3_price
print("\t\t${}".format(total))

print("="*50)

print("\n\t{}\n".format(Message))

print("*"*50)