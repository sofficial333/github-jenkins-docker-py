from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Jenkins Docker Demo</title>
        </head>
        <body>
            <h1>Hello from Jenkins + Docker!</h1>
            <p>Python Flask application deployed using CI/CD.</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return "Application is healthy!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
