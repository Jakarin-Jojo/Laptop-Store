# Laptop-Store
## Setup
1. Create database with schema
```sql
sqlite3 laptop_store.sqlite3 < laptop_store.schema
```
If the command above isn't working, try this instead.
```sql
sqlite3 laptop_store.db -init laptop_store.schema
```
2. open the database
```sql
sqlite3 laptop_store.sqlite3
```
3. Import data from both .csv files into the database.
```sql
sqlite> .mode csv
sqlite> .import data/customer.csv customer
sqlite> .import data/laptop.csv laptop
```