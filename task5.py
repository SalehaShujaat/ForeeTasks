from flask import Flask, request, jsonify  # importing flask framework
import pymongo  # importing pymongo for db connection
from bson.json_util import dumps
app = Flask(__name__)  # constructor

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
collections_1 = mydb["calculations2"]
collections_2 = mydb["last_operations"]
mycollection = mydb["my_operations"]

@app.route('/calculations', methods=['POST', 'GET'])  # GET requests will be blocked
def calc():
    req_data = request.get_json()
    operand1 = req_data['operand1']
    operand2 = req_data['operand2']
    op_char = req_data['op_char']
    if op_char == '+':
        result = operand1 + operand2
    elif op_char == '-':
        result = operand1 - operand2
    elif op_char == '*':
        result = operand1 * operand2
    elif op_char == '/':
        result = operand1 / operand2

    
    mydict = {"operand1": operand1, "operand2": operand2, "op_char": op_char, "result": result}


    if  not mycollection.find({},{"op_char":op_char}):

        mycollection.insert_one(mydict)
    else:
        myquery = {"op_char": op_char}
        newvalues = {"$set": {"operand1": operand1, "operand2": operand2, "result":result}}
        mycollection.update_many(myquery, newvalues)

    y1 = mycollection.find({}, {'_id': False})
    mylist = []
    for records in y1:
        mylist.append(records)
    print(mylist)
    total_records = mycollection.count()

    return jsonify('result', result, 'records',mylist,'total_records', total_records)#"total_records", total_records)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # run app in debug mode on port 5000
