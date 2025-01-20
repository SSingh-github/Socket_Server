from flask import Flask, jsonify, request
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)


@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, this is a REST API endpoint!"})

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    return jsonify({"received": data, "status": "success"})

@sockets.route('/socket')
def echo_socket(ws):
    print("A client connected")
    while not ws.closed:
        message = ws.receive()
        if message:
            print(f"Received message: {message}")
            ws.send(f"Echo: {message}")

if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
    print("Server running at http://127.0.0.1:5000")
    server.serve_forever()
