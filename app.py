from app import create_app
import os
from flask_socketio import SocketIO

app = create_app()
socketio = SocketIO()
socketio.init_app(app)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
