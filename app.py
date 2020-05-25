import os
from flask import Flask, render_template
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "DnDDatabase"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route("/")
@app.route("/character")
def character():
    return render_template("character.html", char=mongo.db.characters.find())


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
