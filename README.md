# Laptop-Store
## Setup
1. Create database with schema
```sqllite
sqlite3 laptop_store.sqlite3 < laptop_store.schema
```
If the command above isn't working, try this instead.
```sqllite
sqlite3 laptop_store.db -init laptop_store.schema
```
2. open the database
```sqllite
sqlite3 laptop_store.sqlite3
```
3. Import data from both .csv files into the database.
```sqllite
sqlite> .mode csv
sqlite> .import data/customer.csv customer
sqlite> .import data/laptop.csv laptop
```