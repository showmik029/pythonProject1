import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )
def get_icao():
    enter_icao=input("Please enter the ICAO: ")
    sql = f"SELECT name,municipality from airport WHERE ident = '{enter_icao}'  "
    print(sql)
    cursor= connection.cursor()
    cursor.execute(sql)
    result= cursor.fetchall()
    return result
print(get_icao())









