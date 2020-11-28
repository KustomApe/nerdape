from flask import Flask, jsonify, request
app = Flask(__name__)

incomes = [
    {'description': 'salary', 'amount': 5000}
]


@app.route('/')
def hello_world():
    return 'Hello world.'