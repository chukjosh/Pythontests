import mysql.connector
# """
#     learnt from w3schools
#     course name: Python MySQL
# """

# connect to database
mydb = mysql.connector.connect(
    host="localhost",  #hostname
    port="3307",  #Port
    user="root",  #user
    password="password",  #password
    database="mydatabase"  #database
)

# create a cursor to do some work
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("SHOW TABLES")

# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")  # this is used if the table already exists instead of the one above

# for x in mycursor:
#   print(x)

# print(f"{mydb}: Database connected")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()  # It is required to make the changes, otherwise no changes are made to the table.

# print(mycursor.rowcount, "record inserted.")


# # INSERTING MUTIPLE ROWS
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "rows were inserted.")


# # Get Inserted ID
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)

# mydb.commit()

# print("1 record inserted, ID:", mycursor.lastrowid)

# # Select From a Table
# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# # Selecting Columns
# mycursor.execute("SELECT name, address FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# # Using the fetchone() Method
# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchone()

# print(myresult)


# # Select With a Filter
# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# # Wildcard Characters
# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# # Prevent SQL Injection
# # Escape query values by using the placholder %s method:
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# # Python MySQL Order By
# sql = "SELECT * FROM customers ORDER BY name"  #name

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# # ORDER BY DESC - descending order
# sql = "SELECT * FROM customers ORDER BY name DESC"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# # ORDER BY ASC - ascending order
# sql = "SELECT * FROM customers ORDER BY name ASC"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# # Delete Record
# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# # The WHERE clause specifies which record(s) that should be deleted. If you omit the WHERE clause, all records will be deleted!

# mycursor.execute(sql)

# mydb.commit()  # It is required to make the changes, otherwise no changes are made to the table.

# print(mycursor.rowcount, "record(s) deleted")

# # Prevent SQL Injection
# # It is considered a good practice to escape the values of any query, also in delete statements.
# # This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
# # The mysql.connector module uses the placeholder %s to escape values in the delete statement:
# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")


# # Delete a Table
# # You can delete an existing table by using the "DROP TABLE" statement:

# # Delete the table "customers":
# sql = "DROP TABLE customers"

# mycursor.execute(sql)

# # Drop Only if Exist
# # If the table you want to delete is already deleted, or for any other reason does not exist, you can use the IF EXISTS keyword to avoid getting an error
# # Delete the table "customers" if it exists:
# sql = "DROP TABLE IF EXISTS customers"

# mycursor.execute(sql)


# # Update Table
# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")

# # Prevent SQL Injection
# # It is considered a good practice to escape the values of any query, also in update statements.
# # This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
# # The mysql.connector module uses the placeholder %s to escape values in the update statement:
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")

# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")


# # Limit the Result
# mycursor.execute("SELECT * FROM customers LIMIT 5")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# Start From Another Position
# If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# # users
# { id: 1, name: 'John', fav: 154},
# { id: 2, name: 'Peter', fav: 154},
# { id: 3, name: 'Amy', fav: 155},
# { id: 4, name: 'Hannah', fav:},
# { id: 5, name: 'Michael', fav:}

# # products
# { id: 154, name: 'Chocolate Heaven' },
# { id: 155, name: 'Tasty Lemons' },
# { id: 156, name: 'Vanilla Dreams' }

# # MySQL JOIN
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   INNER JOIN products ON users.fav = products.id"

# # Note: You can use JOIN instead of INNER JOIN. They will both give you the same result.

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# # LEFT JOIN
# # In the example above, Hannah, and Michael were excluded from the result, that is because INNER JOIN only shows the records where there is a match.
# # If you want to show all users, even if they do not have a favorite product, use the LEFT JOIN statement:
# # Select all users and their favorite product:
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   LEFT JOIN products ON users.fav = products.id"


# # RIGHT JOIN
# # If you want to return all products, and the users who have them as their favorite, even if no user have them as their favorite, use the RIGHT JOIN statement:
# # Select all products, and the user(s) who have them as their favorite:
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   RIGHT JOIN products ON users.fav = products.id"