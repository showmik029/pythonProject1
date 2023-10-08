import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'team12',
    user = 'root',
    password = '1234',
    autocommit = True
)

#akib's function
def choose_destination(lst1):
    user_input = input("Choose from the choices Displayed: ")
    for i in lst1:
        if i[0] == user_input:
            dist = i.split('|')[4].strip()
    print(dist)
    return dist
#check below to see my edits
def range_in (airplane_size, userid, current = 'EFHK'):
    global airportCode, range, co2_emission

    sql = f'''SELECT ident, airport.name, airport.continent, country.name as country, airplane.max_range, airplane.co2_emission_per_km, airplane.capacity
            FROM airport 
            INNER JOIN airplane on (airplane.size = airport.type)
            INNER JOIN country on (airport.iso_country = country.iso_country)
            WHERE airport.type = '{airplane_size}' ORDER BY RAND () LIMIT 5'''
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print("\nHere are possible destinations you can choose!\n")
    print("continent |  country  |      airport      |  distance  | expected co2 emission")
    print("-----------------------------------------")
#akib's empty list declaration
    lst1=[]
    if cursor.rowcount > 0:
        for index, row in enumerate(result, start=1):
            # print(f"{row[0]}")
            airportCode = row[0]
            range = row[4]
            distance = calculate_distance(current, airportCode)
            co2_emission = distance * row[4] / row[5]
#akib's edit of range_in
            if (range > distance) and (co2_emission < left_budget(userid)):
                display=(f"{index}   |  {row[2]}    | {row[3]} | {row[1]} | {round(distance)} km | {round(co2_emission)}")
                lst1.append(display)
                print(display)

        choose_destination(lst1)


    return
#test
x=0