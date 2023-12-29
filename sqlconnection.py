import mysql.connector
import pandas as pd

connection = mysql.connector.connect(host = "localhost",user = "root",password = "Corp@123",database ="student_db")
# Printing the connection object
print(mydb)
print("Hello this is my 1st change")
print("Hello this is my 2nd change")

#Function to execute a SQL Query and return result in dataframe.
def execute_query(query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cols = [column[0] for column in cursor.description]
        df = pd.DataFrame(result,columns=cols)
        return df
    except Exception as e:
        print("Errof: {e}")
    finally:
        cursor.close()

select_query = "select * from student_details"
result_df = execute_query(select_query)
print(result_df)

join_query = "select * from student_details as sd JOIN students_score as sc ON sd.id = sc.id;"
result_df = execute_query(join_query)
print(result_df)

connection.commit()
connection.close()
