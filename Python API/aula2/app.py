#app.py

from flask import Flask, request, jsonify, abort
from blueprints.items import bp as items_bp

app = Flask(__name__)
app.register_blueprint(items_bp)

@app.route('/') #decorator
def index():
    return 'Hello, Flask!'

@app.route('/ping')
def ping():
    data = {'message': 'pong'}
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)