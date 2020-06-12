#Imports all the needed modules to make the program work
import os
import random
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from os import path
if path.exists("env.py"):
  import env 
#Starts a version of flask and a connection to the database
app = Flask(__name__)

app.config["MONGO_DBNAME"] = "DnDDatabase"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

#This is the first director the page opens on
@app.route("/")
@app.route("/entry")
def entry():
    return render_template("entry.html")

"""
This response to the name entered on the entry page form,
it works out whether the user has created any characters before.
Then directs then to there characters if they have and to the 
creation page if they haven't.
"""
@app.route("/user-enter", methods=["POST"])
def user_enter():
    name = request.form["name"].lower()
    user = mongo.db.characters.find_one({"user": name})
    print(user)
    if user == None:
        #This sets the value of the character number to one on the page so that the other navigation buttons the user can't use yet are hidden
        char_numb = 1
        return render_template("new_character.html", name=name, char_numb=char_numb, race=mongo.db.race.find(), classes=mongo.db.classes.find(),  cls=mongo.db.classes.find())
    else:
        return render_template("character.html",  name=name, char=mongo.db.characters.find({'user': name}), url=mongo.db.characters.find({'user': name}))

"""
This response to a search being entered on the entry page
or the search page. It checks the search category returned from the form
to get the appropriate database search function, then the search put in the bar
is ran through the database and send all results to the page for display.
"""
@app.route("/search", methods=["POST"])
def search():
    search = request.form["search"]
    search_category = request.form["search_category"]
    if search_category == "race":
        """
        This is capitalized so that accidental caps doesn't mess with the search. 
        And so the database search works properly if the search is spelt right.
        """
        search = search.capitalize()
        return render_template("search.html", char=mongo.db.characters.find({'race': search}), url=mongo.db.characters.find({'race': search}))
    elif search_category == "class":
        """
        This is capitalized so that accidental caps doesn't mess with the search. 
        And so the database search works properly if the search is spelt right.
        """
        search = search.capitalize()
        return render_template("search.html", char=mongo.db.characters.find({'clss1': search}), url=mongo.db.characters.find({'clss1': search}))
    elif search_category == "user":
        """
        This is capitalized so that accidental caps doesn't mess with the search. 
        And so the database search works properly if the search is spelt right.
        """
        search = search.lower()
        return render_template("search.html", char=mongo.db.characters.find({'user': search}), url=mongo.db.characters.find({'user': search}))

"""
This renders the search page from other pages 
accessing it from the navigation instead of through a form
"""
@app.route("/search")
def search_url():
    return render_template("search.html")

"""
This renders the character page from other pages 
accessing it from the navigation instead of through a form
"""
@app.route("/character/<name>")
def character_url(name):
    return render_template("character.html",  name=name, char=mongo.db.characters.find({'user': name}), url=mongo.db.characters.find({'user': name}))

"""
This renders the new character page from other pages 
accessing it from the navigation instead of through a form
"""
@app.route("/new-character/<name>")
def new_character(name):
    char_numb = 2
    return render_template("new_character.html", name=name, char_numb=char_numb, race=mongo.db.race.find(), classes=mongo.db.classes.find(),  cls=mongo.db.classes.find())

"""
This renders the update character page from other pages 
accessing it from the navigation instead of through a form
"""
@app.route("/update-character/<name>")
def update_character(name):
    return render_template("update.html", name=name, race=mongo.db.race.find(), classes=mongo.db.classes.find(),  cls=mongo.db.classes.find(), char=mongo.db.characters.find({'user': name}), url=mongo.db.characters.find({'user': name}))

"""
This take the response from the update page form
and formats the data for the database, 
then sends the data to the database to update the record
"""
@app.route("/character/<name>", methods=["POST"])
def update(name):
    #This identifies the character they want to change
    char_id = request.form["char_id"]
    #This changes it's format type so it matchs the database
    char_id = float(char_id)
    user = request.form["username"].lower()
    character_name = request.form["character_name"]
    clss1 = request.form["class1"]
    clss2 = request.form["class2"]
    subclass = request.form["subclass"]
    level = request.form["level"]
    subclass_level = request.form["subclass_level"]
    race = request.form["race"]
    gender = request.form["gender"]
    hit_points = request.form["hit_points"]
    strength = request.form["strength"]
    dexterity = request.form["dexterity"]
    constitution = request.form["constitution"]
    intelligence = request.form["intelligence"]
    wisdom = request.form["wisdom"]
    charisma = request.form["charisma"]
    acrobatics = request.form["acrobatics"]
    animal_handling = request.form["animal_handling"]
    arcana = request.form["arcana"]
    athletics = request.form["athletics"]
    deception = request.form["deception"]
    history = request.form["history"]
    insight = request.form["insight"]
    intimidation = request.form["intimidation"]
    investigation = request.form["investigation"]
    medicine = request.form["medicine"]
    nature = request.form["nature"]
    perception = request.form["perception"]
    performance = request.form["performance"]
    persuasion = request.form["persuasion"]
    religion = request.form["religion"]
    slight_of_hand = request.form["slight_of_hand"]
    stealth = request.form["stealth"]
    survival = request.form["survival"]
    cantrip1 = request.form["cantrip1"]
    cantrip2 = request.form["cantrip2"]
    cantrip3 = request.form["cantrip3"]
    cantrip4 = request.form["cantrip4"]
    cantrip5 = request.form["cantrip5"]
    first1 = request.form["first1"]
    first2 = request.form["first2"]
    first3 = request.form["first3"]
    first4 = request.form["first4"]
    first5 = request.form["first5"]
    second1 = request.form["second1"]
    second2 = request.form["second2"]
    second3 = request.form["second3"]
    second4 = request.form["second4"]
    second5 = request.form["second5"]
    third1 = request.form["third1"]
    third2 = request.form["third2"]
    third3 = request.form["third3"]
    third4 = request.form["third4"]
    third5 = request.form["third5"]
    fourth1 = request.form["fourth1"]
    fourth2 = request.form["fourth2"]
    fourth3 = request.form["fourth3"]
    fourth4 = request.form["fourth4"]
    fourth5 = request.form["fourth5"]
    fifth1 = request.form["fifth1"]
    fifth2 = request.form["fifth2"]
    fifth3 = request.form["fifth3"]
    fifth4 = request.form["fifth4"]
    fifth5 = request.form["fifth5"]
    sixth1 = request.form["sixth1"]
    sixth2 = request.form["sixth2"]
    sixth3 = request.form["sixth3"]
    sixth4 = request.form["sixth4"]
    sixth5 = request.form["sixth5"]
    seventh1 = request.form["seventh1"]
    seventh2 = request.form["seventh2"]
    seventh3 = request.form["seventh3"]
    seventh4 = request.form["seventh4"]
    seventh5 = request.form["seventh5"]
    eighth1 = request.form["eighth1"]
    eighth2 = request.form["eighth2"]
    eighth3 = request.form["eighth3"]
    eighth4 = request.form["eighth4"]
    eighth5 = request.form["eighth5"]
    ninth1 = request.form["ninth1"]
    ninth2 = request.form["ninth2"]
    ninth3 = request.form["ninth3"]
    ninth4 = request.form["ninth4"]
    ninth5 = request.form["ninth5"]
    weapon1 = request.form["weapon1"]
    weapon2 = request.form["weapon2"]
    weapon3 = request.form["weapon3"]
    weapon4 = request.form["weapon4"]
    weapon5 = request.form["weapon5"]
    weapon6 = request.form["weapon6"]
    weapon7 = request.form["weapon7"]
    weapon8 = request.form["weapon8"]
    weapon9 = request.form["weapon9"]
    weapon10 = request.form["weapon10"]
    armor1 = request.form["armor1"]
    armor2 = request.form["armor2"]
    armor3 = request.form["armor3"]
    armor4 = request.form["armor4"]
    armor5 = request.form["armor5"]
    armor6 = request.form["armor6"]
    armor7 = request.form["armor7"]
    armor8 = request.form["armor8"]
    armor9 = request.form["armor9"]
    armor10 = request.form["armor10"]
    tool1 = request.form["tool1"]
    tool2 = request.form["tool2"]
    tool3 = request.form["tool3"]
    tool4 = request.form["tool4"]
    tool5 = request.form["tool5"]
    tool6 = request.form["tool6"]
    tool7 = request.form["tool7"]
    tool8 = request.form["tool8"]
    tool9 = request.form["tool9"]
    tool10 = request.form["tool10"]
    class_features1 = request.form["class_features1"]
    class_features2 = request.form["class_features2"]
    class_features3 = request.form["class_features3"]
    class_features4 = request.form["class_features4"]
    class_features5 = request.form["class_features5"]
    class_features6 = request.form["class_features6"]
    class_features7 = request.form["class_features7"]
    class_features8 = request.form["class_features8"]
    class_features9 = request.form["class_features9"]
    class_features10 = request.form["class_features10"]
    race_features1 = request.form["race_features1"]
    race_features2 = request.form["race_features2"]
    race_features3 = request.form["race_features3"]
    race_features4 = request.form["race_features4"]
    race_features5 = request.form["race_features5"]
    race_features6 = request.form["race_features6"]
    race_features7 = request.form["race_features7"]
    race_features8 = request.form["race_features8"]
    race_features9 = request.form["race_features9"]
    race_features10 = request.form["race_features10"]
    feats1 = request.form["feats1"]
    feats2 = request.form["feats2"]
    feats3 = request.form["feats3"]
    feats4 = request.form["feats4"]
    feats5 = request.form["feats5"]
    feats6 = request.form["feats6"]
    feats7 = request.form["feats7"]
    feats8 = request.form["feats8"]
    feats9 = request.form["feats9"]
    feats10 = request.form["feats10"]
    #This is the format for the database
    character = { "$set": {
        "character_name": character_name,
        "clss1": clss1,
        "clss2": clss2,
        "subclass": subclass,
        "level": int(level),
        "subclass_level": subclass_level,
        "race": race,
        "gender": gender,
        "hit_points": int(hit_points),
        "strength": int(strength),
        "dexterity": int(dexterity),
        "constitution": int(constitution),
        "intelligence": int(intelligence),
        "wisdom": int(wisdom),
        "charisma": int(charisma),
        "skill": {
            "acrobatics": acrobatics,
            "animal_handling": animal_handling,
            "arcana": arcana,
            "athletics": athletics,
            "deception": deception,
            "history": history,
            "insight": insight,
            "intimidation": intimidation,
            "investigation": investigation,
            "medicine": medicine,
            "nature": nature,
            "perception": perception,
            "performance": performance,
            "persuasion": persuasion,
            "religion": religion,
            "slight_of_hand": slight_of_hand,
            "stealth": stealth,
            "survival": survival
        },
        "spells": {
            "cantrip": [cantrip1, cantrip2, cantrip3, cantrip4, cantrip5],
            "first": [first1, first2, first3, first4, first5],
            "second": [second1, second2, second3, second4, second5],
            "third": [third1, third2, third3, third4, third5],
            "fourth": [fourth1, fourth2, fourth3, fourth4, fourth5],
            "fifth": [fifth1, fifth2, fifth3, fifth4, fifth5],
            "sixth": [sixth1, sixth2, sixth3, sixth4, sixth5],
            "seventh": [seventh1, seventh2, seventh3, seventh4, seventh5],
            "eighth": [eighth1, eighth2, eighth3, eighth4, eighth5],
            "ninth": [ninth1, ninth2, ninth3, ninth4, ninth5],
        },
        "item": {
            "weapons": [weapon1, weapon2, weapon3, weapon4, weapon5, weapon6, weapon7, weapon8, weapon9, weapon10],
            "armors": [armor1, armor2, armor3, armor4, armor5, armor6, armor7, armor8, armor9, armor10],
            "tools": [tool1, tool2, tool3, tool4, tool5, tool6, tool7, tool8, tool9, tool10]
        },
        "features": {
            "class_features": [class_features1, class_features2, class_features3, class_features4,  class_features5, class_features6, class_features7, class_features8, class_features9, class_features10],
            "race_features": [race_features1, race_features2, race_features3, race_features4, race_features5, race_features6, race_features7, race_features8, race_features9, race_features10],
            "feats": [feats1, feats2, feats3, feats4, feats5, feats6, feats7, feats8, feats9, feats10],
        }
    }
    }
    select = {"char_id": char_id}
    update = mongo.db.characters.update_one(select, character)
    #This takes them back to there character page and loads the new updates
    return render_template("character.html",  name=user, char=mongo.db.characters.find({'user': user}))

"""
This take the response from the new character page form
and formats the data for the database, 
then sends the data to the database to add a new record
"""
@app.route("/character", methods=["POST"])
def character():
    #This creates a random number to help identify individual character later
    char_id = random.random()
    user = request.form["username"].lower()
    char_numb = request.form["char_numb"]
    character_name = request.form["character_name"]
    clss1 = request.form["class1"]
    clss2 = request.form["class2"]
    subclass1 = request.form["subclass1"]
    subclass2 = request.form["subclass2"]
    level = request.form["level"]
    subclass_level = request.form["subclass_level"]
    race = request.form["race"]
    gender = request.form["gender"]
    hit_points = request.form["hit_points"]
    strength = request.form["strength"]
    dexterity = request.form["dexterity"]
    constitution = request.form["constitution"]
    intelligence = request.form["intelligence"]
    wisdom = request.form["wisdom"]
    charisma = request.form["charisma"]
    acrobatics = request.form["acrobatics"]
    animal_handling = request.form["animal_handling"]
    arcana = request.form["arcana"]
    athletics = request.form["athletics"]
    deception = request.form["deception"]
    history = request.form["history"]
    insight = request.form["insight"]
    intimidation = request.form["intimidation"]
    investigation = request.form["investigation"]
    medicine = request.form["medicine"]
    nature = request.form["nature"]
    perception = request.form["perception"]
    performance = request.form["performance"]
    persuasion = request.form["persuasion"]
    religion = request.form["religion"]
    slight_of_hand = request.form["slight_of_hand"]
    stealth = request.form["stealth"]
    survival = request.form["survival"]
    """
    These are requested as individual
    variables because of the way they are formated
    on the database
    """
    cantrip1 = request.form["cantrip1"]
    cantrip2 = request.form["cantrip2"]
    cantrip3 = request.form["cantrip3"]
    cantrip4 = request.form["cantrip4"]
    cantrip5 = request.form["cantrip5"]
    first1 = request.form["first1"]
    first2 = request.form["first2"]
    first3 = request.form["first3"]
    first4 = request.form["first4"]
    first5 = request.form["first5"]
    second1 = request.form["second1"]
    second2 = request.form["second2"]
    second3 = request.form["second3"]
    second4 = request.form["second4"]
    second5 = request.form["second5"]
    third1 = request.form["third1"]
    third2 = request.form["third2"]
    third3 = request.form["third3"]
    third4 = request.form["third4"]
    third5 = request.form["third5"]
    fourth1 = request.form["fourth1"]
    fourth2 = request.form["fourth2"]
    fourth3 = request.form["fourth3"]
    fourth4 = request.form["fourth4"]
    fourth5 = request.form["fourth5"]
    fifth1 = request.form["fifth1"]
    fifth2 = request.form["fifth2"]
    fifth3 = request.form["fifth3"]
    fifth4 = request.form["fifth4"]
    fifth5 = request.form["fifth5"]
    sixth1 = request.form["sixth1"]
    sixth2 = request.form["sixth2"]
    sixth3 = request.form["sixth3"]
    sixth4 = request.form["sixth4"]
    sixth5 = request.form["sixth5"]
    seventh1 = request.form["seventh1"]
    seventh2 = request.form["seventh2"]
    seventh3 = request.form["seventh3"]
    seventh4 = request.form["seventh4"]
    seventh5 = request.form["seventh5"]
    eighth1 = request.form["eighth1"]
    eighth2 = request.form["eighth2"]
    eighth3 = request.form["eighth3"]
    eighth4 = request.form["eighth4"]
    eighth5 = request.form["eighth5"]
    ninth1 = request.form["ninth1"]
    ninth2 = request.form["ninth2"]
    ninth3 = request.form["ninth3"]
    ninth4 = request.form["ninth4"]
    ninth5 = request.form["ninth5"]
    """
    These are requested as individual
    variables because of the way they are formated
    on the database
    """
    weapon1 = request.form["weapon1"]
    weapon2 = request.form["weapon2"]
    weapon3 = request.form["weapon3"]
    weapon4 = request.form["weapon4"]
    weapon5 = request.form["weapon5"]
    weapon6 = request.form["weapon6"]
    weapon7 = request.form["weapon7"]
    weapon8 = request.form["weapon8"]
    weapon9 = request.form["weapon9"]
    weapon10 = request.form["weapon10"]
    armor1 = request.form["armor1"]
    armor2 = request.form["armor2"]
    armor3 = request.form["armor3"]
    armor4 = request.form["armor4"]
    armor5 = request.form["armor5"]
    armor6 = request.form["armor6"]
    armor7 = request.form["armor7"]
    armor8 = request.form["armor8"]
    armor9 = request.form["armor9"]
    armor10 = request.form["armor10"]
    tool1 = request.form["tool1"]
    tool2 = request.form["tool2"]
    tool3 = request.form["tool3"]
    tool4 = request.form["tool4"]
    tool5 = request.form["tool5"]
    tool6 = request.form["tool6"]
    tool7 = request.form["tool7"]
    tool8 = request.form["tool8"]
    tool9 = request.form["tool9"]
    tool10 = request.form["tool10"]
    """
    These are requested as individual
    variables because of the way they are formated
    on the database
    """
    class_features1 = request.form["class_features1"]
    class_features2 = request.form["class_features2"]
    class_features3 = request.form["class_features3"]
    class_features4 = request.form["class_features4"]
    class_features5 = request.form["class_features5"]
    class_features6 = request.form["class_features6"]
    class_features7 = request.form["class_features7"]
    class_features8 = request.form["class_features8"]
    class_features9 = request.form["class_features9"]
    class_features10 = request.form["class_features10"]
    race_features1 = request.form["race_features1"]
    race_features2 = request.form["race_features2"]
    race_features3 = request.form["race_features3"]
    race_features4 = request.form["race_features4"]
    race_features5 = request.form["race_features5"]
    race_features6 = request.form["race_features6"]
    race_features7 = request.form["race_features7"]
    race_features8 = request.form["race_features8"]
    race_features9 = request.form["race_features9"]
    race_features10 = request.form["race_features10"]
    feats1 = request.form["feats1"]
    feats2 = request.form["feats2"]
    feats3 = request.form["feats3"]
    feats4 = request.form["feats4"]
    feats5 = request.form["feats5"]
    feats6 = request.form["feats6"]
    feats7 = request.form["feats7"]
    feats8 = request.form["feats8"]
    feats9 = request.form["feats9"]
    feats10 = request.form["feats10"]
    #This is the format for the database
    character = {
        "char_id": float(char_id),
        "user": user,
        "char_numb": int(char_numb),
        "character_name": character_name,
        "clss1": clss1,
        "clss2": clss2,
        "subclass": subclass1 + "/" + subclass2,
        "level": int(level),
        "subclass_level": subclass_level,
        "race": race,
        "gender": gender,
        "hit_points": int(hit_points),
        "strength": int(strength),
        "dexterity": int(dexterity),
        "constitution": int(constitution),
        "intelligence": int(intelligence),
        "wisdom": int(wisdom),
        "charisma": int(charisma),
        "skill": {
            "acrobatics": acrobatics,
            "animal_handling": animal_handling,
            "arcana": arcana,
            "athletics": athletics,
            "deception": deception,
            "history": history,
            "insight": insight,
            "intimidation": intimidation,
            "investigation": investigation,
            "medicine": medicine,
            "nature": nature,
            "perception": perception,
            "performance": performance,
            "persuasion": persuasion,
            "religion": religion,
            "slight_of_hand": slight_of_hand,
            "stealth": stealth,
            "survival": survival
        },
        "spells": {
            "cantrip": [cantrip1, cantrip2, cantrip3, cantrip4, cantrip5],
            "first": [first1, first2, first3, first4, first5],
            "second": [second1, second2, second3, second4, second5],
            "third": [third1, third2, third3, third4, third5],
            "fourth": [fourth1, fourth2, fourth3, fourth4, fourth5],
            "fifth": [fifth1, fifth2, fifth3, fifth4, fifth5],
            "sixth": [sixth1, sixth2, sixth3, sixth4, sixth5],
            "seventh": [seventh1, seventh2, seventh3, seventh4, seventh5],
            "eighth": [eighth1, eighth2, eighth3, eighth4, eighth5],
            "ninth": [ninth1, ninth2, ninth3, ninth4, ninth5],
        },
        "item": {
            "weapons": [weapon1, weapon2, weapon3, weapon4, weapon5, weapon6, weapon7, weapon8, weapon9, weapon10],
            "armors": [armor1, armor2, armor3, armor4, armor5, armor6, armor7, armor8, armor9, armor10],
            "tools": [tool1, tool2, tool3, tool4, tool5, tool6, tool7, tool8, tool9, tool10]
        },
        "features": {
            "class_features": [class_features1, class_features2, class_features3, class_features4,  class_features5, class_features6, class_features7, class_features8, class_features9, class_features10],
            "race_features": [race_features1, race_features2, race_features3, race_features4, race_features5, race_features6, race_features7, race_features8, race_features9, race_features10],
            "feats": [feats1, feats2, feats3, feats4, feats5, feats6, feats7, feats8, feats9, feats10],
        }
    }
    connection = mongo.db.characters.insert_one(character)
    #This displays the users new character to them
    return render_template("character.html",  name=user, char=mongo.db.characters.find({'user': user})) 

"""
This renders the delete page from other pages 
accessing it from the navigation or button
"""
@app.route("/delete/<name>")
def delete_page(name):
    return render_template("delete.html",  name=name, char=mongo.db.characters.find({'user': name}), url=mongo.db.characters.find({'user': name})) 

"""
The basic information about a character
is displayed on the delete page by the
delete_page function, the user then selects
the one they want to delete by clicking the delete
button under that characters data. This take that data
and deletes the corrisponding character, then redirects them
to confirmation page where they can navigate to the rest of the page
"""
@app.route("/delete-confirmation", methods=["POST"])
def delete():
    char_id = request.form["char_id"]
    char_id = float(char_id)
    user = request.form["username"].lower()
    delete = mongo.db.characters.delete_one({"char_id": char_id})
    return render_template("confirmation.html", name=user)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
