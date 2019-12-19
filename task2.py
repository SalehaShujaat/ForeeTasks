from flask import Flask, request, jsonify # importing flask framework
import operator
app = Flask(__name__) #constructor

@app.route('/calc', methods=['POST']) #GET requests will be blocked
def calc():
    req_data = request.get_json()
    operand1 = req_data['operand1']
    operand2 = req_data['operand2']
    operator = req_data['operator']

    if operator == '+':
        result = operand1 + operand2
    elif operator == '-' :
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
    return jsonify('result',result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # run app in debug mode on port 5000