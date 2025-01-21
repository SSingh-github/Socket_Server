import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to the server!")

@sio.event
def disconnect():
    print("Disconnected from the server.")

@sio.on('response')
def handle_response(data):
    print(f"Message from server: {data['message']}")

try:
    sio.connect('http://localhost:5000/socket')
    print("Client connected. Sending a test message...")

    sio.emit('test_event', {'message': 'Hello from Python client!'})
except Exception as e:
    print(f"Failed to connect: {e}")

input("Press Enter to disconnect...")
sio.disconnect()
