from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Python Docker App 🚀</h1><p>Flask app is running inside Docker.</p>"

@app.route("/about")
def about():
    return "<h2>About Page</h2><p>This is a sample Dockerized Python project.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
