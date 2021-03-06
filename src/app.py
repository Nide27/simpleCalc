from flask import Flask, request

app = Flask(__name__)


@app.route('/api/add', methods=['GET'])
def add():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    num1 = int(num1)
    num2 = int(num2)

    result = num1 + num2

    return str(result)


@app.route('/api/subtract', methods=['GET'])
def subtract():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    num1 = int(num1)
    num2 = int(num2)

    result = num1 - num2

    return str(result)


@app.route('/api/multiply', methods=['GET'])
def multiply():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    num1 = int(num1)
    num2 = int(num2)

    result = num1 * num2

    return str(result)


@app.route('/api/divide', methods=['GET'])
def divide():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    num1 = int(num1)
    num2 = int(num2)

    result = num1 / num2

    return str(result)


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
