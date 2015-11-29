# fullstack-foundation-final-project
Final Project From Udacity Full-Stack Foundation Course<br>
The project is a restaurant menu app with dummy data.<br>
The project consists of:<br>
* Setting up database
* CRUD operation
* Showing Flash Messages
* Implementing API end point
* Styling and improving user experience

### Requirements
* Python 2.7 or above
* SQLite 3
* Flask
* sqlalchemy
* Git
* Terminal or command prompt

### How to download
Open up your terminal or command prompt and enter the following command to download
* $ git git@github.com:AungThiha/fullstack-foundation-final-project.git

### How To create database and add dummy data
Make sure the current directly is where all the codes downloaded under.<br>
In your terminal or command prompt, run the following command<br>
* $ python restaurant_data

You will see a sqlite database file named "restaurant.db" is created.

### How To run the application
Open up your terminal or command prompt and run the command below:<br>
* $ python finalproject.py

### API end points
* get all restaurants

> {base_url}/restaurants/JSON

* get all menu items in a restaurant

> {base_url}/restaurant/<int:restaurant_id>/JSON

* get a menu item

> {base_url}/restaurant/<int:restaurant_id>/<int:menu_id>/JSON

Note: base_url will be printed out when you run the app.
for example, say you get base_url of "localhost:8080"<br>
and you wanna get all menu items in a restaurant with an id of 1,
you can get it with "localhost:8080/restaurant/1/JSON"