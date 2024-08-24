import random

# 1. The Range Riddle

# Task 1: Your Mood Today
moods = ['happy', 'sad', 'angry', 'confused', 'relaxed', 'surprised', 'scared', 'anxious', 'bored', 'excited']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days:
    print(f"On {day}, I felt {random.choice(moods)}.")