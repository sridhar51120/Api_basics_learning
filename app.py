from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    value = request.args.get('value')
    if not value:
        return jsonify({'error': 'Input value is empty'})
    else:
        return jsonify({'msg': value})

if __name__ == '__main__':
    app.run(debug=True)
