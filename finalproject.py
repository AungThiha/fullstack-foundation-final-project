from flask import Flask, render_template

__author__ = 'aungthiha'

app = Flask(__name__)

restaurant = {'name': 'The CRUDdy Crab', 'id': '1', 'address': 'address 1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1', 'address': 'address 1'}, {'name':'Blue Burgers', 'id' : '2', 'address': 'address 2'},{'name':'Taco Hut', 'id':'3', 'address': 'address 3'}]

items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item = {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


@app.route('/restaurants/')
def show_restaurants():
    return render_template('restaurants.html', restaurants=restaurants)


@app.route('/restaurant/new')
def new_restaurant():
    return render_template('new_restaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit')
def edit_restaurant(restaurant_id):
    return render_template('edit_restaurant.html', restaurant=restaurants[restaurant_id-1])


@app.route('/restaurant/<int:restaurant_id>/delete')
def delete_restaurant(restaurant_id):
    return render_template('delete_restaurant.html', restaurant=restaurants[restaurant_id-1])


@app.route('/restaurant/<int:restaurant_id>/')
def show_menu(restaurant_id):
    return render_template('menu.html', items=items, restaurant=restaurants[restaurant_id-1])


@app.route('/restaurant/<int:restaurant_id>/new')
def new_menu(restaurant_id):
    return render_template('new_menu.html', restaurant=restaurants[restaurant_id-1])


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit')
def edit_menu(restaurant_id, menu_id):
    return render_template('edit_menu.html', c_list= ['Appetizer', 'Entree', 'Dessert', 'Beverage'],
                           item=items[menu_id-1], restaurant=restaurants[restaurant_id-1])


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete')
def delete_menu(restaurant_id, menu_id):
    return render_template('delete_menu.html', item=items[menu_id-1], restaurant=restaurants[restaurant_id-1])


if __name__ == '__main__':
    app.debug = True
    app.run(host='',port=8080)