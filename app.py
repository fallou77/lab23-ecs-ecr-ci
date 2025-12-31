from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def hello():
    hostname = socket.gethostname()
    return f"""
    <html>
      <head><title>Lab 21 - ECS + ECR</title></head>
      <body>
        <h1>DevOps Easy Learning - Lab 21</h1>
        <p>This response is served from container: {hostname}</p>
      </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
