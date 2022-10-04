from flask import Flask, jsonify, request

app = Flask(__name__)
temp=[
    {
        "temp_id": "1",
        "date": "October 1, 2022",
        "temperature": "28 Degrees"
    }
]

@app.route('/temp', methods=['POST'])
def addTemp():
    tempe = request.get_json()
    temp.append(tempe)
    return {'id': len(temp)},200

@app.route('/temp', methods=['GET'])
def displayTemp():
    return jsonify(temp)

@app.route('/temp/<int:index>', methods=['DELETE'])
def deleteTemp(index):
    temp.pop(index)
    return 'Temperature was successfully deleted',200

if __name__ == '__main__':
    app.run()