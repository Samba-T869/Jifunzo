from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

messages=[]

@app.route('/')
def index():
	return render_template('index.html')

@socketio.on('connect')
def connect(data):
	emit('connect', {'data': "User connected"}, broadcast=True)
	
@socketio.on('disconnect')
def disconnect(data):
	emit('disconnect', {'data': 'User disconnected'}, broadcast=True)	
	
@socketio.on('new_message')
def new_message(data):
	messages.append(data['message'])
	emit('new_message', {'message': data['message']}, broadcast=True)	

if __name__ == "__main__":
    socketio.run(app, debug=True)