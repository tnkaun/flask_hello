from app import create_app
import os
from flask_socketio import SocketIO
socketio = SocketIO()
app = create_app()



if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
