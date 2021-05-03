from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello from docker</h1>"

@app.route('/nome', methods=['GET'])
def nome():
    data = {"nome" : "Victor" , "idade" : "22", "email": "victor.alves19@outlook.com.br"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)