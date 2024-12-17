# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructType, StructField
import pyodbc

# Create a SparkSession
spark = SparkSession.builder.appName("Read CSV and write to DB").getOrCreate()

# Read CSV file into a DataFrame
df = spark.read.csv('path_to_your_csv_file.csv', header=True, inferSchema=True)

# Define database connection parameters
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

# Create a database connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Write DataFrame to database
df.write.format("jdbc") \
    .option("url", "jdbc:sqlserver://"+server+";databaseName="+database) \
    .option("query", "your_table_name") \
    .option("user", username) \
    .option("password", password) \
    .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
    .save()