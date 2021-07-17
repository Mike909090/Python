import mysql.connector
db_connection = mysql.connector.connect(
	host="localhost",
	 user="username",
	 passwd="password",
	 database="your_database_name"
)
#Returns a cursor object that we can execute SQL queries.
cursor = db.cursor()

#This makes a table that we can insert things into.
cursor.execute ("CREATE TABLE People (Name varchar(50), Age int, City varchar(50)")

#This inserts in tems into the SQL database I made.
cursor.execute("INSERT INTO People (Name , Age, City) "
			   "VALUES ('Jack',26,'Sydney'), "
			   "('Maxi',32,'New York'),"
			   "('John',36,'Mexico') "
			   )

#This method returns a cursor object. Using a cursor object, we can execute SQL queries.
sql_statement1 = "SELECT * FROM People"
#Used to execute statements
cursor.execute(sql_statement1)
#Used to return all the result sets as a list of tuples.
output = cursor.fetchall()
for x in output:
	print(x)

#Used to update information in the People's table.
sql_statement2 = "UPDATE People SET Age ='15' where Name='Isaac'"
cursor.execute(sql_statement2)
db_connection.commit()

#Deleting statements from a table.
sql_statement3 = "DELETE FROM People where Age ='36'"
cursor.execute(sql_statement3)
cursor.commit()
print("Row(s) deleted successfully!")
