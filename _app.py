from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
	
@app.route("/about")
def about():
    return render_template("about.html")
	
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway 需要讀取環境變數 PORT
    app.run(host="0.0.0.0", port=port)



