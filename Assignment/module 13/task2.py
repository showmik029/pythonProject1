import mysql.connector

from flask import Flask

def icao_search(icao):
    sql = "SELECT ident AS 'ICAO',name AS 'Name',municipality AS 'Location' FROM airport WHERE ident = '"+icao+"'"
    cursor=connection.cursor(dictionary=True)
    cursor.execute(sql)
    result=cursor.fetchall()
    return result

connection=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='1234',
    autocommit=True
)

app=Flask(__name__)
@app.route('/airport/<icao>')
def get_info_with_icao(icao):
    result = icao_search(icao)[0]
    response={
        "ICAO":result["ICAO"],
        "Name":result["Name"],
        "location":result["Location"]
    }

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)