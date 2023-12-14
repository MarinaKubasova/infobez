from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/addition', methods=['POST'])
def add():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return jsonify({'result': result})

@app.route('/subtraction', methods=['POST'])
def subtract():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 - num2
    return jsonify({'result': result})

@app.route('/multiplication', methods=['POST'])
def multiply():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 * num2
    return jsonify({'result': result})

@app.route('/division', methods=['POST'])
def divide():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    if num2 != 0:
        result = num1 / num2
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Cannot divide by zero'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
