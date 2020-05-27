import os
from flask import Flask, render_template, request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "DnDDatabase"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route("/")
@app.route("/entry")
def character():
    return render_template("entry.html")


@app.route("/username", method=["POST"])
def username(user):
    user = request.form["name"]
    username = mongo.db.characters
    username.mongo.db.characters.find({"user": user}, function (err, user){
        if (err) {
            console.log(err)
        };
        if (!user.length){
            return render_template("new_character.html", 
            classes=mongo.db.classes.find(), race=mongo.db.race.findOne({"user": user}))
        }
        else{
            return render_template("character.html", char=mongo.db.characters.find("user"))
        }
    });


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
