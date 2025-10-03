from flask import Flask
from my_app import calculator

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Python CI/CD Lab! 2+3 = " + str(calculator.add(2, 3))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
