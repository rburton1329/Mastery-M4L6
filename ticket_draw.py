import random

items = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 'A', 'B', 'C', 'D', 'E']
winning_ticket = random.sample(items, 4)
print(f"Any ticket matching these 4 numbers or letters wins a prize: {winning_ticket}")
