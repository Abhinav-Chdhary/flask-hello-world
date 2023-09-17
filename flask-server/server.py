from flask import Flask

from flask_cors import CORS

app = Flask(__name__)

# enable CORS for all routes
CORS(app)

# Members API Route


@app.route("/members")
def members():
    return {"members": ["mem1", "mem2", "mem3"]}


if __name__ == "__main__":
    app.run(debug=True)
