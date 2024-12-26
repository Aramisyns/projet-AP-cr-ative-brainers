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

score=0

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
            
# display the final score
print(f'your final score is : {score}/{len(questions)}')