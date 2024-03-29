import mysql.connector as connector

# Establish connection between Python and MySQL database via connector API
connection = connector.connect(
    user="root",
    password="",
)
print("Connection between MySQL and Python is established.\n")

# Create cursor object to communicate with entire MySQL database
cursor = connection.cursor()
print("Cursor is created to communicate with the MySQL using Python.\n")

# If exist, drop the database first, and create again
try:
    cursor.execute("CREATE DATABASE little_lemon")
except:
    cursor.execute("drop database little_lemon")
    cursor.execute("CREATE DATABASE little_lemon")
print("The database little_lemon is created.\n")

# Set little_lemon database for use
cursor.execute("USE little_lemon")
print("The database little_lemon is set for use.\n")

# The SQL query for MenuItems table is:
create_menuitem_table = """
CREATE TABLE MenuItems (
ItemID INT AUTO_INCREMENT,
Name VARCHAR(200),
Type VARCHAR(100),
Price INT,
PRIMARY KEY (ItemID)
);"""

# Create MenuItems table
cursor.execute(create_menuitem_table)
print("MenuItmes table is created.\n")

# The SQL query for Menu table is:
create_menu_table = """
CREATE TABLE Menus (
MenuID INT,
ItemID INT,
Cuisine VARCHAR(100),
PRIMARY KEY (MenuID,ItemID)
);"""

# Create Menu table
cursor.execute(create_menu_table)
print("Menu table is created.\n")

# The SQL query for Bookings table is:
create_booking_table = """
CREATE TABLE Bookings (
BookingID INT AUTO_INCREMENT,
TableNo INT,
GuestFirstName VARCHAR(100) NOT NULL,
GuestLastName VARCHAR(100) NOT NULL,
BookingSlot TIME NOT NULL,
EmployeeID INT,
PRIMARY KEY (BookingID)
);"""

# Create Bookings table
cursor.execute(create_booking_table)
print("Bookings table is created.\n")

# The SQL query for Bookings table is:
create_orders_table = """
CREATE TABLE Orders (
OrderID INT,
TableNo INT,
MenuID INT,
BookingID INT,
BillAmount INT,
Quantity INT,
PRIMARY KEY (OrderID,TableNo)
);"""

# Create Orders table
cursor.execute(create_orders_table)
print("Orders table is created.\n")

# *******************************************************#
# Insert query to populate "MenuItems" table is:
# *******************************************************#
insert_menuitmes = """
INSERT INTO MenuItems (ItemID, Name, Type, Price)
VALUES
(1,'Olives','Starters',5),
(2,'Flatbread','Starters', 5),
(3, 'Minestrone', 'Starters', 8),
(4, 'Tomato bread','Starters', 8),
(5, 'Falafel', 'Starters', 7),
(6, 'Hummus', 'Starters', 5),
(7, 'Greek salad', 'Main Courses', 15),
(8, 'Bean soup', 'Main Courses', 12),
(9, 'Pizza', 'Main Courses', 15),
(10,'Greek yoghurt','Desserts', 7),
(11, 'Ice cream', 'Desserts', 6),
(12, 'Cheesecake', 'Desserts', 4),
(13, 'Athens White wine', 'Drinks', 25),
(14, 'Corfu Red Wine', 'Drinks', 30),
(15, 'Turkish Coffee', 'Drinks', 10),
(16, 'Turkish Coffee', 'Drinks', 10),
(17, 'Kabasa', 'Main Courses', 17);"""

# *******************************************************#
# Insert query to populate "Menu" table is:
# *******************************************************#
insert_menu = """
INSERT INTO Menus (MenuID,ItemID,Cuisine)
VALUES
(1, 1, 'Greek'),
(1, 7, 'Greek'),
(1, 10, 'Greek'),
(1, 13, 'Greek'),
(2, 3, 'Italian'),
(2, 9, 'Italian'),
(2, 12, 'Italian'),
(2, 15, 'Italian'),
(3, 5, 'Turkish'),
(3, 17, 'Turkish'),
(3, 11, 'Turkish'),
(3, 16, 'Turkish');"""

# *******************************************************#
# Insert query to populate "Bookings" table is:
# *******************************************************#
insert_bookings = """
INSERT INTO Bookings (BookingID, TableNo, GuestFirstName, 
GuestLastName, BookingSlot, EmployeeID)
VALUES
(1,12,'Anna','Iversen','19:00:00',1),
(2, 12, 'Joakim', 'Iversen', '19:00:00', 1),
(3, 19, 'Vanessa', 'McCarthy', '15:00:00', 3),
(4, 15, 'Marcos', 'Romero', '17:30:00', 4),
(5, 5, 'Hiroki', 'Yamane', '18:30:00', 2),
(6, 8, 'Diana', 'Pinto', '20:00:00', 5);"""

# *******************************************************#
# Insert query to populate "Orders" table is:
# *******************************************************#
insert_orders = """
INSERT INTO Orders (OrderID, TableNo, MenuID, BookingID, Quantity, BillAmount)
VALUES
(1, 12, 1, 1, 2, 86),
(2, 19, 2, 2, 1, 37),
(3, 15, 2, 3, 1, 37),
(4, 5, 3, 4, 1, 40),
(5, 8, 1, 5, 1, 43);"""

print("Inserting data in MenuItems table.")
# Populate MenuItems table
cursor.execute(insert_menuitmes)
print("Total number of rows in MenuItem table: {}\n".format(cursor.rowcount))
# Once the query is executed, you commit the change into the database
connection.commit()

print("Inserting data in Menus table.")
# Populate MenuItems table
cursor.execute(insert_menu)
print("Total number of rows in Menu table: {}\n".format(cursor.rowcount))
connection.commit()

print("Inserting data in Bookings table.")
# Populate Bookings table
cursor.execute(insert_bookings)
print("Total number of rows in Bookings table: {}\n".format(cursor.rowcount))
connection.commit()

print("Inserting data in Orders table.")
# Populate Orders table
cursor.execute(insert_orders)
print("Total number of rows in Orders table: {}\n".format(cursor.rowcount))
connection.commit()

print("""The database "little_lemon" is ready for use.""")

# Task 1

# The SQL query is:
sql_query="""
SELECT 
BookingID AS ID,
UPPER(CONCAT(GuestFirstName,' ',GuestLastName)) 
AS GuestFullName 
FROM bookings;"""

# Execute query
cursor.execute(sql_query)

# Fetch records
results = cursor.fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Just add an empty line using print statement
print()

# Print query results
for result in results:
    print(result)

# Task 2

# The SQL query is:
sql_query="""
SELECT 
COUNT(BookingID) AS n_bookings,
SUM(BillAmount) AS Total_sale,
AVG(BillAmount) AS Avg_sale
FROM Orders;"""

# Execute query
cursor.execute(sql_query)

# Fetch records
results=cursor.fetchall()

# Print results
print("Today's statistics:")
for result in results:
    print("Number of bookings:",result[0])
    print("Total sale:",result[1])
    print("Average sale:",result[2])

# Task 3

# The SQL query is:
sql_query="""SELECT 
TableNo AS 'Table number', 
COUNT(TableNo) AS n_booking
FROM Bookings 
GROUP BY TableNo 
ORDER BY n_booking DESC;"""

# Execute query
cursor.execute(sql_query)

# Fetch records
results = cursor.fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Print query results
for result in results:
    print(result)

# Task 4

# The SQL query is:
sql_query="""
SELECT
BookingID,
CONCAT(GuestFirstName,' ',GuestLastName) AS Guest_Name,

CASE
WHEN HOUR(BookingSlot) IN (15,16) THEN "Late afternoon" 
WHEN HOUR(BookingSlot) IN (17,18) THEN "Evening" 
WHEN HOUR(BookingSlot) IN (19,20) THEN "Night"
ELSE "Time not available" 
END AS Arrival_slot

FROM Bookings;"""

# Execute query
cursor.execute(sql_query)

# Fetch records
results = cursor.fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Print query results
for result in results:
    print(result)

# Task 1
sql_query = """SELECT 
COUNT(BookingID) AS n_bookings,
HOUR(BookingSlot) AS Hour 
FROM Bookings
GROUP BY Hour
ORDER BY Hour ASC;"""

# Execute the query
cursor.execute(sql_query)

# Fetch all results that satisfy the query
results = cursor.fetchall()

# Print records in the required format using for loop
print("""Upcoming Bookings:\n""")
for result in results:
    print("Hour: ",result[1],"<<>>", result[0], "Booking/s")

import datetime as dt

# The SQL query is:
sql_query = """SELECT 
TableNo, 
GuestFirstName, 
GuestLastName, 
BookingSlot 
FROM Bookings 
ORDER BY BookingSlot;"""

# Execute query
cursor.execute(sql_query)

# Fetch all results that satisfy the query
results = cursor.fetchall()

# Print records in the required format
print("The guests and their booking slots are:\n")
for result in results:
    time = str(result[3])
    hour = dt.datetime.strptime(time,'%H:%M:%S').hour
    minute = dt.datetime.strptime(time,'%H:%M:%S').minute
    print("[Table no:]",result[0],">>",result[1],result[2], "is expected to arrive at:",
          hour,"hrs and", minute, "mins")

# The SQL query is:
sql_query = """SELECT 
BookingID, 
TableNo, 
BookingSlot, 
ADDTIME(BookingSlot,"1:00:00") as NewTime 
FROM Bookings
WHERE TableNo = 12 AND BookingID = 2;"""

# Execute query
cursor.execute(sql_query)

# Fetch all results that satisfy the query
results = cursor.fetchall()

# Print time change alert.
print("Booking time change ALERT!!")
for result in results:
    print("Booking ID:",result[0])
    print("Table number:",result[1])
    print("Booked slot:",result[2])
    print("New arrival time:",result[3])

cursor.execute("DROP PROCEDURE IF EXISTS TopSpender;")
# Task 1
# Stored procedure name >> TopSpender
# Our stored procedure query is
stored_procedure_query="""
CREATE PROCEDURE TopSpender()

BEGIN

SELECT bookings.BookingID, 
CONCAT(
bookings.GuestFirstname,
' ',
bookings.GuestLastname
) AS CustomerName,
Orders.BillAmount 
FROM Bookings
INNER JOIN
Orders ON bookings.BookingID=Orders.BookingID
ORDER BY BillAmount DESC LIMIT 1;

END

"""

# Execute the query
cursor.execute(stored_procedure_query)

#********************************************#

# Call the stored procedure with its name
cursor.callproc("TopSpender")

# Retrieve recrods in "dataset"
results = next( cursor.stored_results() )
dataset = results.fetchall()

# Retrieve column names using list comprehension in a 'for' loop
for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]

# Print column names
print(columns)

# Print data
for data in dataset:
    print(data)

cursor.execute("DROP PROCEDURE IF EXISTS NoArrival;")

# Task 2
# Stored procedure name >> NoArrival
# Our stored procedure query is
stored_procedure_query="""
CREATE PROCEDURE NoArrival()

BEGIN

SELECT bookings.BookingID, 
Orders.BillAmount 
FROM Bookings
LEFT JOIN
Orders ON Bookings.BookingID=Orders.BookingID
WHERE BillAmount IS NULL;

END

"""

# Execute the query
cursor.execute(stored_procedure_query)

#********************************************#

# Call the stored procedure with its name
cursor.callproc("NoArrival")

# Retrieve recrods in "dataset"
results = next( cursor.stored_results() )
dataset = results.fetchall()

# Retrieve column names using list comprehension in a 'for' loop
for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]

# Print column names
print(columns)

# Print data
for data in dataset:
    print(data)

cursor.execute("DROP PROCEDURE IF EXISTS OrderStatus;")

# Task 3
# Stored procedure name >> OrderStatus
# Our stored procedure query is
stored_procedure_query="""
CREATE PROCEDURE OrderStatus()

BEGIN

SELECT bookingID, 
CASE
WHEN employeeID IN (1,2,3) THEN "Order Served" 
WHEN employeeID IN (4,5) THEN "Preparing Order" 
ELSE "In Queue" 
END AS Status
FROM Bookings;

END

"""

# Execute the query
cursor.execute(stored_procedure_query)

#********************************************#

# Call the stored procedure with its name
cursor.callproc("OrderStatus")

# Retrieve recrods in "dataset"
results = next( cursor.stored_results() )
dataset = results.fetchall()

# Retrieve column names using list comprehension in a 'for' loop
for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]

# Print column names
print(columns)

# Print data
for data in dataset:
    print(data)

# Let's close the cursor and the connection
if connection.is_connected():
    cursor.close()
    print("The cursor is closed.")
    connection.close()
    print("MySQL connection is closed.")
else:
    print("Connection is already closed")

