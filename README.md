# DnD Ideas Page - v1
The idea of this page is to allow users to create, share and help each other with Dungeons and Dragons 5e (DnD5e) Characters.
I want a way for users to be able to enter a name and be directed to either the characters they have made or to
the character creation page if they haven't made any before. On the opening page I would also like to provide a
search function that will look through the database and display the results to the page. 
I want to design the look of the site to resemble a simple character sheet to help users who have played DnD5e. 
I hope to help users with this style of page because I find with other DnD5e sites have quite a lot going on with there
pages and all of that confuses me sometimes when looking for specific stats.

## UX

### Why I Think People will use my site
I think people will like to use my site because it will have simplified character sheets and design. I believe this to be useful
because it will help new players get into making character as it removes a lot of the maths and the complex parts that most of the
other sites have with there character creations and character sheets. I think this will also be helpful to seasoned players
like myself who get irked by how flashing other sites have become. Basically, I want to bring things back to basics because other
sites have become to much.

### User Stories:
As a new player, I want to look at people ideas for a specific class characters, so I have ideas how to create my own on the character creation.\
As a veteran player, I want to recreate my favourite characters, so others can see my ideas.\
As a player whos created a character, I want to change somethings about my character, so I can see how it will effect the characters stats.\
As a player unhappy with my idea, I want to delete my character, so I can start from scratch.\
As a new player, I want to create a character, so I can get started in DnD5e.\
As a player, I want to see other people ideas for a specific race, so I can get class ideas for that race.\
As a veteran player, I want to compair my builds to another veteran player builds, so I can see if there simular or better.

### Wireframe and Mockups
This is the sites wireframe, hosted on Google Docs - [D&D Page Wireframe](https://docs.google.com/document/d/1HBWEmxW6Csu9PLlzB-Y_rj-32A4sCNc1NknZ7uXQdbE/edit?usp=sharing)

#### Entry Page Mockup -  
![Entry Page Mockup](/static/assets/SiteMockupEntry.png)

#### Site Mockup (The character sheet design to use on most other pages) -  
![Site Mockup](/static/assets/SiteMockup.png)

#### Site Diagram -  
![Site Diagram](/static/assets/SiteDiagram.png)

## Features

### Entry Page
1. Allow the user to enter name to enter the site. 
This should lead to the new character page if they haven't 
been on the site before and there characters on the character page if they have.
2. Allow the user to search the database with a keyword they enter, 
this should lead to a results page

### New Character Page
1. Allow the user to navigate using sidenav that hides itself, 
they should be able to go to the search page if this is there first time on the page. 
If they are a returning user they should be able to navigate to all pages.
2. Allow the user to fill out the new character form and submit there character to the database.
The form shouldn't let users place varibles that shouldn't be in certain field they shouldn't be in.
As in strings in integer, this is to stop the math functions I want to make from breaking.
3. The page should formate itself in a character sheet design to help users understand the 
information they are putting in.
4. The page title should say "Welcome (Username)!".

### Character Page
1. Allow the user to navigate using sidenav that hides itself, they should be able to navigate to all pages.
2. Allow the user to view all their characters in the character sheet formate made for the site.
3. Allow the user to click the delete button underneathe each character sheet and be navigated to the delete page.
4. Allow the user to navigate through the page with links to each character and to the top.
These links will be in the sidenav under the characters link in the sidenav.
5. The character sheet should take the needed numbers and do the maths for the user to work
out modifiers (for skill, stats ect).

### Update Page
1. Allow the user to navigate using sidenav that hides itself, they should be able to navigate to all pages.
2. Allow the user to navigate through the page with links to each character and to the top.
These links will be in the sidenav under the update link in the sidenav.
3. Allow the user to view all their characters in the character sheet formate made for the site, 
this will be like the new characters page but the user can't change character number, id or user name.
4. All the characters stats and information should be place into the approriate boxes.
5. Like the new character page the user shouldn't be able to place invalid variables in certain boxes.
6. Allow the user to click an update button at the bottom once they are done, 
the update should be sent to the database then the character page should be loaded with the
new data.

### Delete Page
1. Allow the user to navigate using sidenav that hides itself, they should be able to navigate to all pages.
2. Allow the user to navigate through the page with links to each character and to the top.
These links will be in the sidenav under the delete link in the sidenav.
3. Allow the user to select the character they want to delete by having some of the characters details displated.
4. Allow the user to delete the choosen character by clicking the delete button under the character, this should
send the delete to the database and remove the character. Then they should be redirected to a confirmation page 
which they will be prompted to direct to their disired page from there.

### Search Page
1. Allow the user to navigate using sidenav that hides itself, they should be able use a new character link
which will go to the entry page so they can enter there name.
2. Allow the user to navigate through the page with links to each character that comes up from the search 
and to the top. These links will be in the sidenav under the delete link in the sidenav.
4. Allow the user to search a new keyword with a search form at the top of the search page.
5. Allow user to leave a comment on the characters returned from a search.
6. Display all characters returned from the search in the character sheet formate.

## Existing Features

### Entry Page
1. Name Entry - The entry page has a form for the user to enter their name and the app.py deals with it.
```python
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
```
2. Search - This is slightly differnet from the first idea,
 when writing the code I realized I'd need to focus the search 
 at a category so the user can select a category and put in a keyword linked to the category.
 ```html
 <div class="row justify-content-center m-1">
	<form action="{{ url_for('search') }}" name="search" method="post">
        <!--- This allow the user to search the characters made by race,
         class or user and with a keyword corrisponding to there choosen category--->
        <label for="search_category">Search by:</label><br>
        <!--- This allows them to choose there category which selects the corrisponding mongodb find code in the app.py --->
        <select class="form-control" id="search_category" name="search_category" required>
		    <option value="" readonly selected>Choose Your Search Category</option>
            <option value="race">Race</option>
            <option value="class">Class</option>
            <option value="user">Creator</option>
        </select>
        <!--- This allows the user to enter the keyword that they want to 
        search there category with, cap doesn't matter but spelling does--->
		<label for="seach">Search Keyword:</label><br>
		<input type="text" class="form-control" id="search" name="search" placeholder="Search" required><br>
		<button type="submit" class="form-control" name="action">Search Builds!</button>
    </form>
</div>
 ```
 ```python
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
 ```

### Navigation
1. Hidden Sidenav - It's put into each html and is controlled by javascript and some css.
[Side Navigation CSS](static/css/style.css)
```javascript
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  document.getElementById("openbtn").style.display = "none";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
  document.getElementById("openbtn").style.display = "block";
}
```
```html
<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="{{ url_for('new_character', name=name) }}">New Character</a>
  <a href="{{ url_for('character_url', name=name) }}">Characters</a>
  <a href="{{ url_for('update', name=name) }}">Update</a>
  <a href="{{ url_for('delete_page', name=name) }}">Delete</a>
</div>
<button id="openbtn" class="m-1 pt-1 sticky-top" onclick="openNav()">Open</button>
<div id="main">
```
2. Page Navigation - Certain pages allow for navigation 
between characters and the top of the page using the sidenav
```html
<a class="active" href="#">Delete</a>
    <ul>
        <li><a href="#top">Top</a></li>  
        <!--- This creates a link for each character
        that is found when finding the users characters. 
        Then when displaying
        the characters a div with corrisponding char_id as the 
        divs id is created allowing users to jump to that 
        characters sheet through the navigation--->      
        {% for urls in url %}
        <li><a href="#{{urls.char_id}}">{{urls.character_name}}</a></li>
        {% endfor %}
    </ul>
```

### New Character Page, Search Page, Character Page, Delete Page and Update Page
Character formate - The page will formate itself in a character sheet layout
the user can enter the information for the character on there
```html
<div class="row justify-content-center m-1">
	<h1 class="text-center">Welcome! - Create your character!</h1>
</div>
<div class="row justify-content-center m-1">
	<p>If you require information not supplied here for the creating of your character, please use an official retailer
		to obtain a copy
		of the books. We will not supply any information about specifics as this would be a copyright infringement,
		thank you.</p>
	<form action="{{ url_for('character') }}" name="character" method="post" class="m-1">
    <div class="form-row">
		<div class="form-group col-4">
            <!--- This will have the users name that they inputted at the entry page, 
            it is passed through all the page link except search so will still be 
            set to this when navigating from the other pages --->
			<label for="username">Users Name:</label>
			<input type="text" class="form-control" id="username" name="username" value="{{name}}" required>
        </div>
        <div class="form-group col-4">
            <!--- This is set to one on first entry and two once a character is made, 
            I would like this to increase by one for each new charater 
            but at the moment this is done manually after the first two --->
			<label for="char_numb">Character Number:</label>
			<input type="number" step="1" min="1" class="form-control" id="char_numb" name="char_numb" value="{{char_numb}}" required>
        </div>
		<div class="form-group col-4">
            <!--- This allows the user to write the 
            name the user has choosen for the character --->
			<label for="character_name">Character Name:</label>
			<input type="text" class="form-control" id="character_name" name="character_name" required>
        </div>
    </div>
```
This is a small scetion of the character formate the rest can be found on [Search Page](template/seach.html), [Character Page](template/character.html), 
[New Character Page](template/new_character.html) and the [Update Page](template/update.html). 
The character page and the search page are different as they don't display the data as input boxes 
and the delete one is different as it only shows some details about the character.

### New Character Page
Page Title - It shows "Welcome (Username)!".
```html
<!-- Base Page -->
<title>{% block title %}{%  endblock %}</title>
<!--- New Character Page --->
{% block title %}Welcome {{name}}!{% endblock %}
```

### Character Page
1. Delete Button - There is a delete button rendered at the bottom of each character which leads to the delete page
```html
<div class="col-xl-4">
    <div class="d-flex justify-content-center">
        <button><a href="{{ url_for('delete_page', name=name) }}">Delete Character</a></button>
    </div>
</div>
```
2. Modifiers - There are different if statement that work out the correct values based on thing like level and level in stats ect
```html
{% if chars.dexterity == 3 %}
                {% if chars.skill.stealth == "Yes" %}
                    {% if chars.level <= 4 %}
			            <li class="list-group-item text-center">-2</li>
                    {% elif chars.level <= 8 and chars.level >= 5 %}
			            <li class="list-group-item text-center">-1</li>
                    {% elif chars.level <= 12 and chars.level >= 9 %}
			            <li class="list-group-item text-center">0</li>
                    {% elif chars.level <= 16 and chars.level >= 13 %}
			            <li class="list-group-item text-center">+1</li>
                    {% elif chars.level <= 20 and chars.level >= 17 %}
			            <li class="list-group-item text-center">+2</li>
                    {% endif %}
                {% else %}
                        <li class="list-group-item text-center">-4</li>
                {% endif %}
            {% elif chars.dexterity == 4 or chars.dexterity == 5 %}
```
This is a small part of one of the equations.

### Update Page
1. Stats and Information - the stats will be place in the correct boxes if they exist
```html
<input type="text" class="form-control" id="username" name="username" readonly value="{{chars.user}}" required>
```
2. Update Button and Function - the button will call the update function and redirect to the character page
```html
<form action="{{ url_for('update', name=name) }}" name="character" method="post" class="m-1">
<div class="form-row d-flex justify-content-center">
            <input type="submit" value="Update Character!">
        </div>
```
```python
@app.route("/character/<name>", methods=["POST"])
def update(name):
    #This identifies the character they want to change
    char_id = request.form["char_id"]
    #This changes it's format type so it matchs the database
    char_id = float(char_id)
    user = request.form["username"].lower()
    character_name = request.form["character_name"]
    select = {"char_id": char_id}
    update = mongo.db.characters.update_one(select, character)
    #This takes them back to there character page and loads the new updates
    return render_template("character.html",  name=user, char=mongo.db.characters.find({'user': user}))
```

### Delete Page
1. Delete Details - There is less information displayed for easier delete choice
2. Delete Button and Function - The button will send the delete request and redirect
to confirmation page
```html
<form action="{{ url_for('delete', name=name) }}" name="character" method="post" class="m-1">
<div class="form-group col-4">
            <div class="d-flex justify-content-center">
                <input type="submit" value="Delete">
            </div>
        </div>
```
```python
@app.route("/delete-confirmation", methods=["POST"])
def delete():
    char_id = request.form["char_id"]
    char_id = float(char_id)
    user = request.form["username"].lower()
    delete = mongo.db.characters.delete_one({"char_id": char_id})
    return render_template("confirmation.html", name=user)
```

### Search Page
1. Re-Searching - At the top of the page is a search form
```html
<form action="{{ url_for('search') }}" name="search" method="post">
        <label for="search_category">Search by:</label><br>
        <select class="form-control" id="search_category" name="search_category" required>
		    <option value="" readonly selected>Choose Your Search Category</option>
            <!--- This will ditermine the way 
            the app.py searchs the database, i.e 
            which find() code line it will use --->
            <option value="race">Race</option>
            <option value="class">Class</option>
            <option value="user">Creator</option>
        </select>
		<label for="seach">Search Keyword:</label><br>
		<input type="text" class="form-control" id="search" name="search" placeholder="Search" required><br>
		<button type="submit" class="form-control" name="action">Search Builds!</button>
    </form>
```

## Features Left to Implement

### Search Page
I would like to have a way to comment on characters and have these comments saved with a time stamp and the users name

## Technologies Used

JQuery
The project uses JQuery to simplify DOM manipulation when changing style of the sidenav.

Bootstrap
Bootstrap is used to structure and stlye the page in this project, its also used to respond to screen size changes.

## Testing
### Stat Testing
Initally I tried running the maths that I needed to work out through a javascript 
program but I couldn't work out how to get the data to pass to the javascript code. 
To fix this issue I did the equation in the template using if, elif and else statements.
This does make the code long and I am looking to in time reduce this code down but at the
moment it works as it is ment to.

### Delete Testing
When I orignally wrote the delete I wanted it to either go to a confirmation page or to redirect back
to the character page, when I attempted to load the character page after deleting a record it wouldn't load.
So, because of this I decide to have the confirmation page I had initally thought off.

### User Test
1. Tester 1 Matt Cox - I used the program to see if it could handle me inuptting an old NPC quickly and efficiently. 
It was fast and simple to use, the only problem was that I needed to use the official resources 
in places where I couldn't simply recall the information from memory. This is a common issue amongst 
programs like this as you would need to be officially licensed to have that information as part of the program. 
The only other noteworthy thing was that names using more than one word lost their capitalization when processed, 
I reported the bug and it was promptly fixed. This report is by me -Matt Cox-, 
I am a professional beta tester and have been playing D&D for around 30 years.
2. Tester 2 Shakeira Joyce - I was asked to test whether the program would work, 
and to see if values of stats where calculated correctly in response to the stats I put in at creation.
This all seemed to work well, I had no issues making a character except some areas were hard to understand what they 
were for, but in reporting this back and start to create a character again it has been made clear what each section is for.
When I view my character all stats where already calculated for me and checking the maths it seems to all be correct. The 
program doesn't seem to account for certain bonuses like racial bonuses, class bonuses or feats but these can be added at the
bottom of the character sheet and added not in the program. It works well as a simple character sheet but for more advanced characters
it maybe lacking some of the necessities of higher level characters.
3. Tester 3 Adam Langford - I used the program to see if I could find any errors in it, or to try and break the program, 
I did this by using a variety of characters, numbers and symbols inside of any box meant for text, 
to see what allowances there are for it, as well as testing the limits on the numbers that are supposed to be capped at specific values. 
This all worked as planned, and all symbols converted successfully on the page, and all the inputted values wouldn't exceed the predetermined caps. 
I was unable to find any obvious issues that can break the program, at least by inputting different characters. 

## Deployment
1. I connected my database by a env.py so I transfered this information to the Heroku server as a key value, along with the IP and the PORT.
2. I then reconnected my master git repository to the Heroku server.
3. I commented out the code used for my virtual environment
4. I double checked the Procfile and requirement.txt that I created at the start of the program
5. I have pushed the code to GitHub and Heroku in pushing it to GitHub
6. I have checked to see if the server runs with the same functionality of the site without error

After testing on the deployment all things seem to be running normally, no issues. Data can be created read, updated and deleted. The seach works as it should.

## Credits
Acknowledgements
I received inspiration for this project from the DnDBeyond character sheet design.  
The races, classes and stats are from the Dungeons and Dragons 5e Player's Handbook, 
Eberron: Rising from the Last War, Critical Role, Explorer's Guide to Wildemount, 
Mythic Odysseys of Theros, Elemental Evil Player's Companion, Volo's Guide to Monsters, 
Sword Coast Adventurer's Guide, The Tortle Package, Mordenkainen's Tome of Foes, 
Guildmasters' Guide to Ravnica, Acquisitions Incorporated, Locathah Rising and One Grung Above.
