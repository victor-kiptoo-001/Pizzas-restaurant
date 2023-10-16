from app import app, db
from models.pizza import Pizza
from models.restaurant import Restaurant

def populate_database():
    with app.app_context():
        # Sample Pizza Data
        pizza_data = [
            {"name": "Margherita", "ingredients": "Tomato, Mozzarella, Basil"},
            {"name": "Pepperoni", "ingredients": "Tomato, Mozzarella, Pepperoni"},
            # Add more pizza data as needed
        ]

        # Sample Restaurant Data
        restaurant_data = [
            {"name": "Pizza Hut", "address": "123 Main St, City"},
            {"name": "Domino's", "address": "456 Elm St, City"},
            # Add more restaurant data as needed
        ]

        # Seed Pizzas
        for pizza_info in pizza_data:
            pizza = Pizza(name=pizza_info["name"], ingredients=pizza_info["ingredients"])
            db.session.add(pizza)

        # Seed Restaurants
        for restaurant_info in restaurant_data:
            restaurant = Restaurant(name=restaurant_info["name"], address=restaurant_info["address"])
            db.session.add(restaurant)

        db.session.commit()

if __name__ == "__main__":
    populate_database()
