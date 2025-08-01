import os
from config import Config
from flask import Flask


app= Flask(__name__)
app.config.from_object(Config)
print(app.config['UPLOAD_FOLDER'])
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)