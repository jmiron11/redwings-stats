# redwings-stats

Webscrapes for information and stores it in a database. Information in the database is manipulated for statistics.


Currently must run webscrape.py before SQLiteJDBC
run webscraper with: 
	python3.4 webscrape.py to create the database of information
compile SQLiteJDBC with: 
	javac SQLiteJDBC.java
and run with:
	java -classpath ".:sqlite-jdbc-3.8.7.jar" SQLiteJDBC
