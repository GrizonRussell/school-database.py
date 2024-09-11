import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

host = 'localhost'
user = 'root'
password = ''
database = 'school_database'

def get_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
def read_grade_data_average_above_85():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        sql = """
        SELECT 
            student_id,
            name,
            subject,
            prelim,
            midterm,
            final_exam,
            (prelim + midterm + final_exam) / 3 AS average
            FROM grades_data 
            HAVING average > 85;
            """
        cursor.execute(sql)
        results = cursor.fetchall()

        headers = ["Student ID", "Name", "Subject", "Prelim", "Midterm", "Final Exam", "Average"]

        print(tabulate(results, headers=headers, tablefmt='grid'))
        
    finally:
        cursor.close()
        connection.close()
        
def read_grade_data():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM grades_data ORDER BY name"
        cursor.execute(sql)
        results = cursor.fetchall()

        headers = ["Student ID", "Name", "Subject", "Prelim", "Midterm", "Final Exam"]

        print(tabulate(results, headers=headers, tablefmt='grid'))
        
    finally:
        cursor.close()
        connection.close()

def read_grade_data_with_average():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        sql = """
        SELECT 
            student_id,
            name,
            subject,
            prelim,
            midterm,
            final_exam,
            (prelim + midterm + final_exam) / 3 AS average
        FROM grades_data 
        ORDER BY name
        """
        cursor.execute(sql)
        results = cursor.fetchall()

        headers = ["Student ID", "Name", "Subject", "Prelim", "Midterm", "Final Exam", "Average"]

        print(tabulate(results, headers=headers, tablefmt='grid'))
        
    finally:
        cursor.close()
        connection.close()

        
def read_sales_data():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM sales_data"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        headers = ["Store ID", "City", "Date", "Product ID", "Product Name", "Units Sold", "Total Sales"]
        
        print(tabulate(results, headers=headers, tablefmt='grid'))
        
    finally:
        cursor.close()
        connection.close()
        
def read_users_log():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM users_log"
        cursor.execute(sql)
        results = cursor.fetchall()

        headers = ["User ID","Timestamp", "IP Address", "Action"]

        print(tabulate(results, headers=headers, tablefmt='grid'))
        
    finally:
        cursor.close()
        connection.close()


def menu():
    while True:
        print("\nSelect an option:")
        print("1. Show Grades")
        print("2. Show Grades with Average")
        print("3. Show Grades with Average and Above 85 Grade")
        print("4. Show Sales Data")
        print("5. Show Users Log")
        print("6. Exit")
        choice = input("Enter your choice (1/5): ")
        
        if choice == '1':
            read_grade_data()
        elif choice == '2':
            read_grade_data_with_average()
        elif choice == '3':
            read_grade_data_average_above_85()
        elif choice == '4':
            read_sales_data()
        elif choice == '5':
            read_users_log()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
