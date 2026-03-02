from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

client = MongoClient("mongodb+srv://username:password@cluster0.ofrcmkp.mongodb.net/?retryWrites=true&w=majority")
db = client["github"]
collection = db["events"]

@app.route("/")
def home():
    return "Server running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    event = request.headers.get("X-GitHub-Event")

    if event == "push":
        collection.insert_one({
            "author": data["pusher"]["name"],
            "action": "push",
            "to_branch": data["ref"].split("/")[-1],
            "timestamp": str(datetime.utcnow())
        })

    return "ok"

@app.route("/events")
def events():
    data = list(collection.find().sort("_id", -1).limit(10))
    for d in data:
        d["_id"] = str(d["_id"])
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5000)

