from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "This is a REST API response."})

@socketio.on('connect', namespace='/socket')
def handle_connect():
    print("Client connected via Socket.IO")
    emit('response', {'message': 'Connected to Socket.IO!'})

@socketio.on('disconnect', namespace='/socket')
def handle_disconnect():
    print("Client disconnected from Socket.IO")

if __name__ == '__main__':
    socketio.run(app, debug=True)
