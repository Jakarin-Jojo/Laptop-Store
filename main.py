from utilities.session import LaptopDB

session = LaptopDB()

print(session.laptop().get_all_laptop())
print(session.customer().get_all_customer())
