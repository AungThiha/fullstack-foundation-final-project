from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from sqlalchemy.orm.exc import NoResultFound
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

__author__ = 'aungthiha'

app = Flask(__name__)

engine = create_engine('sqlite:///restaurant.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def show_home():
    return render_template('home.html')


def get_restaurants():
    try:
        restaurants = session.query(Restaurant).all()
    except NoResultFound, e:
        print e
    return restaurants


@app.route('/restaurants/')
def show_restaurants():
    restaurants = get_restaurants()
    return render_template('restaurants.html', restaurants=restaurants)


@app.route('/restaurants/JSON')
def show_restaurants_json():
    restaurants = get_restaurants()
    return jsonify(restaurants=[r.serialize for r in restaurants])


@app.route('/restaurant/new', methods=['GET', 'POST'])
def new_restaurant():
    if request.method == 'POST':
        restaurant = Restaurant(name=request.form['name'],
                                address=request.form['address'])
        session.add(restaurant)
        session.commit()
        flash('new restaurant created!')
        return redirect(url_for('show_menu', restaurant_id=restaurant.id))
    else:
        return render_template('new_restaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit', methods=['POST', 'GET'])
def edit_restaurant(restaurant_id):
    try:
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        if request.method == 'POST':
            restaurant.name = request.form['name']
            restaurant.address = request.form['address']
            session.add(restaurant)
            session.commit()
            flash('%s updated!' % restaurant.name)
            return redirect(url_for('show_menu', restaurant_id=restaurant.id))
        else:
            return render_template('edit_restaurant.html', restaurant=restaurant)
    except NoResultFound, e:
        print e
        return "No restaurant with the id %d found" % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def delete_restaurant(restaurant_id):
    try:
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        if request.method == 'POST':
            session.delete(restaurant)
            session.commit()
            flash('%s deleted!' % restaurant.name)
            return redirect(url_for('show_restaurants'))
        else:
            return render_template('delete_restaurant.html', restaurant=restaurant)
    except NoResultFound, e:
        print e
        return "No restaurant with the id %d found" % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/')
def show_menu(restaurant_id):
    try:
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    except NoResultFound, e:
        print e
    if restaurant:
        return render_template('menu.html', items=items, restaurant=restaurant)
    else:
        return "No restaurant with the id %d found" % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/JSON')
def show_menu_json(restaurant_id):
    try:
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one().serialize
        items = [i.serialize for i in session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()]
    except NoResultFound, e:
        print e
    if restaurant:
        restaurant['menus'] = items
        return jsonify(restaurant=restaurant)
    else:
        return "No restaurant with the id %d found" % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/new', methods=['GET', 'POST'])
def new_menu(restaurant_id):
    try:
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        if request.method == 'POST':
            item = MenuItem(name=request.form['name'],
                            price=request.form['price'],
                            course=request.form['course'],
                            description=request.form['description'],
                            restaurant_id=restaurant_id)
            session.add(item)
            session.commit()
            flash('new menu item created!')
            return redirect(url_for('show_menu', restaurant_id=restaurant_id))
        else:
            return render_template('new_menu.html', restaurant=restaurant)
    except NoResultFound, e:
        print e
        return "No restaurant with the id %d found" % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit', methods=['POST', 'GET'])
def edit_menu(restaurant_id, menu_id):
    try:
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        item = session.query(MenuItem).filter_by(id=menu_id,restaurant_id=restaurant_id).one()
        if request.method == 'POST':
            item.name = request.form['name']
            item.price = request.form['price']
            item.course = request.form['course']
            item.description = request.form['description']
            session.add(item)
            session.commit()
            flash('%s updated!' % item.name)
            return redirect(url_for('show_menu', restaurant_id=restaurant_id))
        else:
            return render_template('edit_menu.html', c_list=['Appetizer', 'Entree', 'Dessert', 'Beverage'],
                                   item=item, restaurant=restaurant)
    except NoResultFound, e:
        print e
        return "No menu item with the id %d found" % menu_id


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete', methods=['POST', 'GET'])
def delete_menu(restaurant_id, menu_id):
    try:
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        item = session.query(MenuItem).filter_by(id=menu_id,restaurant_id=restaurant_id).one()
        if request.method == 'POST':
            session.delete(item)
            session.commit()
            flash('%s deleted' % item.name)
            return redirect(url_for('show_menu', restaurant_id=restaurant_id))
        else:
            return render_template('delete_menu.html', item=item, restaurant=restaurant)
    except NoResultFound, e:
        print e
        return "No Menu Item With the id %d found" % menu_id


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/JSON')
def show_only_menu_json(restaurant_id, menu_id):
    try:
        item = session.query(MenuItem).filter_by(id=menu_id,restaurant_id=restaurant_id).one().serialize
    except NoResultFound, e:
        print e
    if item:
        return jsonify(item=item)
    else:
        return "No menu item with the id %d found" % menu_id


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    print "///**** base_url is localhost:8080 ****////"
    app.run(host='',port=8080)
