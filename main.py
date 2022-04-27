from utilities.session import LaptopDB

session = LaptopDB()

print(session.customer().get_all_customer())
print(session.laptop().get_all_laptop())
print(session.laptop().get_laptop_price_more_than_or_equal(500))
print(session.laptop().get_laptop_price_more_than_or_equal(1000))
print(session.laptop().get_laptop_by_type_name("2 in 1 Convertible"))

