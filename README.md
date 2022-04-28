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
sqlite3 laptop_store.db
```
3. Import data from both .csv files into the database.
```sql
sqlite> .mode csv
sqlite> .import data/customer.csv customer
sqlite> .import data/laptop.csv laptop
```
## Domain Model
![image](https://user-images.githubusercontent.com/72879083/165693162-2b981e67-b84f-4965-8709-845a2bb35684.png)  
## Package Diagram  
![Package Diagram](https://user-images.githubusercontent.com/72879083/165730399-6534457a-50b3-4a32-b4a6-d7ddd4524ae3.jpg)  
## Class Diagram
![Class Diagram](https://user-images.githubusercontent.com/72879083/165750793-f32de0c4-d0f7-4b06-b293-ab4e08833783.jpg)  
