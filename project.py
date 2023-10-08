
import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'team12',
    user = 'root',
    password = '1234',
    autocommit = True
)


def get_airport_info(icao):
    sql = f'''SELECT iso_country, ident, name, latitude_deg, longitude_deg
                  FROM airport
                  WHERE ident = %s'''
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result

def calculate_distance(current, target):
    from geopy import distance
    start = get_airport_info(current)
    end = get_airport_info(target)
    distance = distance.distance((start['latitude_deg'], start['longitude_deg']),
                             (end['latitude_deg'], end['longitude_deg'])).km

    sql = "INSERT INTO distance (departure_code, destination_code, distance_km) VALUES (%s, %s, %s)"
    cursor = connection.cursor()
    cursor.execute(sql, (current, target,distance))
    connection.commit()
    return distance
print(calculate_distance("00A","00AZ"))
