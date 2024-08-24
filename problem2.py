import random

# 2. Double Scoop with Nested Loops

# Task 1: Your Mood Tracker
moods = ['happy', 'sad', 'angry', 'confused', 'relaxed', 'surprised', 'scared', 'anxious', 'bored', 'excited']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
times = ['morning', 'afternoon', 'evening']

for day in days:
    for time in times:
        print(f"On {day} {time}, I felt {random.choice(moods)}.")
    print('\n')