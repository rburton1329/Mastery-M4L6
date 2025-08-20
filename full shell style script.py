"""
full shell style script.py

This program demonstrates running Python code in a shell-style script format.
- It contains multiple sections that run one after another.
- It shows examples of loops, calculations, and print statements.
- Each section works like commands typed in a Python shell, but saved in a file.
Plain-English: It’s a practice file that shows how different Python commands work step by step.
"""

question 1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


restaurant = Restaurant("Tasty Bites", "Italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant("Sushi World", "Japanese")
restaurant2 = Restaurant("Curry House", "Indian")
restaurant3 = Restaurant("Burger Barn", "American")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


class User:
    def __init__(self, first_name, last_name, age, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.username = username

    def describe_user(self):
        print(f"User Profile:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}\nUsername: {self.username}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")


user1 = User("Ryan", "Burton", 30, "ryan.burton@example.com", "ryanb")

question 2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant("Tasty Bites", "Italian")
print(f"Number served: {restaurant.number_served}")
restaurant.number_served = 25
print(f"Number served after update: {restaurant.number_served}")
restaurant.set_number_served(40)
print(f"Number served after set_number_served(): {restaurant.number_served}")
restaurant.increment_number_served(100)
print(f"Number served after increment_number_served(): {restaurant.number_served}")


class User:
    def __init__(self, first_name, last_name, age, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Profile:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}\nUsername: {self.username}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Ryan", "Burton", 30, "ryan.burton@example.com", "ryanb")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}"

question 3
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors=[]):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream_stand = IceCreamStand("Sweet Scoops", "Dessert", ["Vanilla", "Chocolate", "Strawberry", "Mint"])
ice_cream_stand.display_flavors()


class User:
    def __init__(self, first_name, last_name, age, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Profile:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}\nUsername: {self.username}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, email, username, privileges=[]):
        super().__init__(first_name, last_name, age, email, username)
        self.privileges = Privileges(privileges)


admin1 = Admin("Alice", "Smith", 35, "alice.smith@example.com", "adminAlice", ["can add post", "can delete post", "can ban user"])
admin1.privileges.show_privileges()
Privileges:
- can add post
- can delete post
- can ban user
