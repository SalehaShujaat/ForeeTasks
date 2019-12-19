from flask import Flask, request, jsonify # importing flask framework
import operator
app = Flask(__name__) #constructor

def inverse_decorator(function):
    #function()
    def wrapper():
        req_data = request.get_json()
        op_char = req_data['operator']
        if op_char == '+':
            req_data['operator'] = "-"
        elif op_char == '-':
            req_data['operator'] = "+"
        elif op_char == '*':
            req_data['operator'] = "/"
        elif op_char == '/':
            req_data['operator'] = "*"
        res = function()
        return res
    return wrapper

def calculate(op, a, b):
    if op == '+':
        result = a + b
        return result
    elif op == '-' :
        result = a - b
        return result
    elif op == '*':
        result = a * b
        return result
    elif op == '/':
        result = a / b
    return result

@app.route('/calc', methods=['POST']) #GET requests will be blocked
@inverse_decorator
def calc():
    req_data = request.get_json()
    # Store input numbers and operator
    operand1 = req_data['operand1']
    operand2 = req_data['operand2']
    op_char = req_data['operator']
    result = calculate(op_char, operand1, operand2)
    return jsonify('result', result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # run app in debug mode on port 5000