from flask import Flask

__author__ = 'aungthiha'

app = Flask(__name__)


@app.route('/restaurants/')
def show_restaurants():
    return 'show all restaurants'


@app.route('/restaurant/new')
def new_restaurant():
    return 'create new restaurant'


@app.route('/restaurant/<int:restaurant_id>/edit')
def edit_restaurant(restaurant_id):
    return 'edit restaurant %d' % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/delete')
def delete_restaurant(restaurant_id):
    return 'delete restaurant %d' % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/')
def show_menu(restaurant_id):
    return 'show all menu at restaurant %d' % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/new')
def new_menu(restaurant_id):
    return 'create new menu at restaurant %d' % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit')
def edit_menu(restaurant_id, menu_id):
    return 'edit menu %d restaurant %d' % (menu_id, restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete')
def delete_menu(restaurant_id, menu_id):
    return 'delete menu %d restaurant %d' % (menu_id, restaurant_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host='',port=8080)