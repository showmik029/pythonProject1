from flask import Flask

app = Flask(__name__)

@app.route('/check_prime/<int:num>')
def check_prime(num):
    for divisor in range(2, num):
        if num % divisor == 0:
            response = {"Number": num, "Prime": False}
            return response

    response = {"Number": num, "Prime": True}
    return response

if __name__ == '__main__':
    app.run(debug=True)
