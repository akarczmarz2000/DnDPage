import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "DnDDatabase"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route("/")
@app.route("/entry")
def entry():
    return render_template("entry.html")


@app.route("/username", methods=["POST"])
def username():
    name = request.form["name"].lower()
    user = mongo.db.characters.find_one({"user": name})
    print(user)
    if user == None:
        return render_template("new_character.html", user=user, race=mongo.db.race.find(), classes=mongo.db.classes.find())
    else:
        return render_template("character.html", char=mongo.db.characters.find({'user': name}))
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
