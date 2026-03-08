from flask import Flask, jsonify

# Create an instance of Flask
app = Flask(__name__)

# 映射请求
@app.route('/')
def hello_world():
    person = {'name': '张三', 'age': 18}
    return jsonify(person)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
