

# Task 1

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='1234',
    autocommit=True
)

def getICAOairport(ident):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident ='" + ident + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The Airport name is: {row[0]} and municipality is: {row[1]}")
    return


ident = input("Enter the ICAO: ")
getICAOairport(ident)

# Task 2

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='1234',
    autocommit=True
)

def airport(iso_country):
    sql = "select name from airport"
    sql = sql + " Where iso_country='" + iso_country + "' " + "order by type "
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"the name of airport {row[0]}")
    return

user = input("enter area code:")
airport(user)

# Task 3

import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='1234',
    autocommit=True
)

def get_coordinates(ident):
    sql = "select latitude_deg, longitude_deg from airport"
    sql = sql + " Where ident='" + ident + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    if cursor.rowcount > 0:
        return result[0]
    return None

user_a = input("enter ICAO for point A: ")
user_b = input("enter ICAO for point B: ")

coordinates_a = get_coordinates(user_a)
coordinates_b = get_coordinates(user_b)

if coordinates_a and coordinates_b:
    distance = geodesic(coordinates_a, coordinates_b).km
    print(f"Total distance is: {distance} km")
else:
    print("Invalid ICAO code or coordinates not found.")

