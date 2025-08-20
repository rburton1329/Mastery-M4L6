"""
ticket_draw.py

This program simulates a simple lottery ticket draw.
- It creates a list of numbers and letters.
- It randomly selects 4 of them.
- The selected items are printed as the “winning ticket.”
Plain-English: It’s like a mini lottery that randomly picks 4 characters as the winning combo.
"""

import random

items = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 'A', 'B', 'C', 'D', 'E']
winning_ticket = random.sample(items, 4)
print(f"Any ticket matching these 4 numbers or letters wins a prize: {winning_ticket}")
