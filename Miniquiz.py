# Mini Quiz

# This is a simple Python quiz game for beginners. It asks 3 multiple-choice math questions, checks your answers, and shows your score.

# How to Run
# 1. Make sure Python is installed on your computer.
# 2. Open terminal or command prompt.
# 3. Navigate to the folder containing `miniquiz.py`.
# 4. Run the program with `python miniquiz.py`.
# 5. Answer the questions by typing the option number.

# Future Improvements
# - Add more questions
# - Include loops to reduce repetitive code
# - Randomize questions


# Miniquiz.py

score = 0

# Question 1
print("What is 5 * 6?")
print("1) 30")
print("2) 11")
print("3) 50")
print("4) 60")
answer1 = int(input("Choose the correct option number: "))
if answer1 == 1:
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")

# Question 2
print("What is 12 / 4?")
print("1) 2")
print("2) 3")
print("3) 4")
print("4) 6")
answer2 = int(input("Choose the correct option number: "))
if answer2 == 2:
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")

# Question 3
print("What is 15 - 7?")
print("1) 7")
print("2) 10")
print("3) 9")
print("4) 8")
answer3 = int(input("Choose the correct option number: "))
if answer3 == 4:
    print("CORRECT")
    score += 1
else:
    print("INCORRECT")

# Score
print(f"YOU SCORED {score} OUT OF 3")
