import json
from datetime import datetime

USER_DATA_FILE = "user_data.json"


def load_user_data():
    try:
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
    
def save_user_data(data):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

user_data = load_user_data()


name = input('Please enter your name: ')

# Verify if the student already exists
if name in user_data:
    print(f"Welcome back, {name}!")
    for score, date in user_data[name]:
        print(f"Score: {score}, Date: {date}")
else:
    print(f"Welcome, {name}! This is your first time playing.")
    user_data[name] = []

questions = [
    {
        "question": "What does CPU stand for?",
        "options": ['A. Central Processing Unit', 'B. Computer Processing Unit', 'C. Control Programming Unit', 'D. Central Programming Unit'],
        "answer": "A"
    },
    {
        "question": "Which type of memory is volatile?",
        "options": ['A. ROM', 'B. SSD', 'C. RAM', 'D. Hard Drive'],
        "answer": "C"
    },
    {
        "question": "What does HTTP stand for?",
        "options": ['A. HyperText Transfer Program', 'B. HyperText Transfer Protocol', 'C. High-Transfer Text Protocol', 'D. HyperLink Transfer Protocol'],
        "answer": "B"
    }
]

score = 0

for q in questions:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("\n" + q["question"])
    
    for option in q["options"]:
        print(option)
    guess = input("Enter your answer: ").upper()   
    if guess == q["answer"]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
        print(f"The correct answer is {q['answer']}")

# Get only the current date (YYYY-MM-DD)
current_date = datetime.now().strftime("%Y-%m-%d")

print(f'Your final score is: {score}/{len(questions)}')

user_data[name].append((f"{score}/{len(questions)}", current_date)) 
save_user_data(user_data)
