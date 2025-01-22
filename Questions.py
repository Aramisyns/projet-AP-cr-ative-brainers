import json
from datetime import datetime
import sys

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

def display_welcome():
    print("\n" + "="*50)
    print("       Welcome to the Computer Science QCM")
    print("="*50)

def display_menu():
    print("\n1. View History")
    print("2. Start the QCM")
    print("3. Exit")
    print("\n" + "="*50)

def show_history(user_data, name):
    if not user_data[name]['history']:
        print("\nNo history available.")
        return
    
    print("\nYour Game History:")
    print("="*80)
    for session in user_data[name]['history']:
        print(f"Date: {session['date']}")
        print(f"Category: {session['category']}")
        print(f"Score: {session['score']}/{session['total_questions']}")
        print("-"*40)

def display_question(question, options):
    print("\n" + "="*80)
    print(f"\n{question}\n")
    print(f"{options[0]:<40}{options[1]}")
    print(f"{options[2]:<40}{options[3]}")
    print("\n" + "="*80)

def display_categories(categories):
    print("\nAvailable categories:")
    print("="*80)
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category}")
    print("="*80)

def get_valid_category(quiz_content):
    while True:
        display_categories(quiz_content.keys())
        try:
            category_choice = int(input("\nSelect a category (number): "))
            if 1 <= category_choice <= len(quiz_content):
                return list(quiz_content.keys())[category_choice - 1]
            print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Please enter a valid number.")

def get_answer():
    while True:
        guess = input('\nEnter your answer (A/B/C/D): ').upper()
        if guess in ['A', 'B', 'C', 'D']:
            return guess
        print("Invalid input. Please enter A, B, C, or D.")

def run_quiz(name, user_data, quiz_content):
    selected_category = get_valid_category(quiz_content)
    print(f"\nYou have selected: {selected_category}")

    current_quiz = quiz_content[selected_category]
    questions = current_quiz["questions"]
    options = current_quiz["options"]
    answers = current_quiz["answers"]

    score = 0
    for qstnumber, question in enumerate(questions):
        display_question(question, options[qstnumber])
        guess = get_answer()
            
        if guess == answers[qstnumber]:
            score += 1
            print('\n✓ CORRECT!')
        else: 
            print('\n✗ INCORRECT!')   
            print(f'The correct answer is: {answers[qstnumber]}')

    save_session(name, user_data, selected_category, score, len(questions))
    display_results(selected_category, score, len(questions))

def save_session(name, user_data, category, score, total_questions):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_session = {
        "date": current_datetime,
        "category": category,
        "score": score,
        "total_questions": total_questions
    }
    user_data[name]['history'].append(new_session)
    save_user_data(user_data)

def display_results(category, score, total_questions):
    print('\n' + "="*80)
    print(f'\nCategory: {category}')
    print(f'Final score: {score}/{total_questions}')
    print(f'Session recorded on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print("\n" + "="*80)

def main():
    user_data = load_user_data()
    
    display_welcome()
    name = input('\nPlease enter your name: ')
    
    if name not in user_data:
        print(f"\nWelcome {name}! It's your first time.")
        user_data[name] = {'history': []}
    else:
        print(f"\nWelcome back {name}!")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            show_history(user_data, name)
        elif choice == "2":
            run_quiz(name, user_data, quiz_content)
        elif choice == "3":
            print("\nThank you for participating! Goodbye!")
            sys.exit()
        else:
            print("\nInvalid choice. Please try again.")

# Quiz content organized by categories
quiz_content = {
    "Computer Basics": {
        "questions": [
            "1- What does CPU stand for?",
            "2- Which type of memory is volatile?",
            "3- Which of the following is not an input device?",
            "4- What is the brain of the computer?",
            "5- What does GUI stand for?",
            "6- Which unit is used to measure computer memory?",
            "7- What type of storage device is an SSD?",
            "8- What does USB stand for?",
            "9- Which component is known as the computer's short-term memory?",
            "10- What is the purpose of a motherboard?"
        ],
        "options": [
            ('A. Central Processing Unit', 'B. Computer Processing Unit', 'C. Control Programming Unit', 'D. Central Programming Unit'),
            ('A. ROM', 'B. RAM', 'C. SSD', 'D. Hard Drive'),
            ('A. Keyboard', 'B. Mouse', 'C. Monitor', 'D. Microphone'),
            ('A. Monitor', 'B. CPU', 'C. RAM', 'D. Hard Drive'),
            ('A. General User Interface', 'B. Graphical User Interface', 'C. General Unity Interface', 'D. Graphical Unity Interface'),
            ('A. Hertz', 'B. Bytes', 'C. Pixels', 'D. Watts'),
            ('A. Optical Storage', 'B. Magnetic Storage', 'C. Solid State Storage', 'D. Cloud Storage'),
            ('A. Universal Serial Bus', 'B. United Serial Bus', 'C. Universal System Bus', 'D. United System Bus'),
            ('A. Hard Drive', 'B. ROM', 'C. RAM', 'D. CPU'),
            ('A. Process Data', 'B. Store Files', 'C. Display Images', 'D. Connect Components')
        ],
        "answers": ["A", "B", "C", "B", "B", "B", "C", "A", "C", "D"]
    },
    "Programming Fundamentals": {
        "questions": [
            "1- Which is not a programming paradigm?",
            "2- What is the purpose of a variable?",
            "3- What is a function in programming?",
            "4- What is an array?",
            "5- What does OOP stand for?",
            "6- What is a loop used for?",
            "7- What is debugging?",
            "8- What is a Boolean?",
            "9- What is a compiler?",
            "10- What is an algorithm?"
        ],
        "options": [
            ('A. Object-Oriented', 'B. Functional', 'C. Procedural', 'D. Mechanical'),
            ('A. Run Programs', 'B. Store Data', 'C. Display Output', 'D. Connect Devices'),
            ('A. Store Data', 'B. Reusable Code Block', 'C. Display Output', 'D. Format Text'),
            ('A. Single Value', 'B. Collection of Values', 'C. Text String', 'D. Boolean Value'),
            ('A. Object Oriented Programming', 'B. Order Of Processing', 'C. Object Oriented Protocol', 'D. Order Of Program'),
            ('A. Store Data', 'B. Display Output', 'C. Repeat Actions', 'D. Format Text'),
            ('A. Writing Code', 'B. Finding/Fixing Errors', 'C. Running Programs', 'D. Saving Files'),
            ('A. Number', 'B. Text', 'C. True/False Value', 'D. Array'),
            ('A. Code Writer', 'B. Code Translator', 'C. Code Runner', 'D. Code Storage'),
            ('A. Program', 'B. Code Block', 'C. Variable', 'D. Problem-Solving Steps')
        ],
        "answers": ["D", "B", "B", "B", "A", "C", "B", "C", "B", "D"]
    },
    "Networking": {
        "questions": [
            "1- What is an IP address?",
            "2- What does LAN stand for?",
            "3- What device connects networks?",
            "4- What is a firewall?",
            "5- What protocol is used for email?",
            "6- What is DNS used for?",
            "7- What does ISP stand for?",
            "8- What is a proxy server?",
            "9- What is bandwidth?",
            "10- What is a MAC address?"
        ],
        "options": [
            ('A. Network Name', 'B. Device Identifier', 'C. Website Address', 'D. Network Password'),
            ('A. Local Area Network', 'B. Large Area Network', 'C. Linear Access Node', 'D. Local Access Node'),
            ('A. Monitor', 'B. Router', 'C. Keyboard', 'D. Printer'),
            ('A. Antivirus', 'B. Security Barrier', 'C. Network Cable', 'D. File System'),
            ('A. FTP', 'B. HTTP', 'C. SMTP', 'D. TCP'),
            ('A. Network Security', 'B. Name Resolution', 'C. Data Storage', 'D. Email Transfer'),
            ('A. Internet Service Provider', 'B. Internal System Protocol', 'C. Internet Security Program', 'D. Internal Service Port'),
            ('A. File Server', 'B. Email Server', 'C. Intermediary Server', 'D. Database Server'),
            ('A. Network Speed', 'B. Cable Length', 'C. IP Address', 'D. Security Level'),
            ('A. IP Address', 'B. Hardware Address', 'C. Network Name', 'D. Domain Name')
        ],
        "answers": ["B", "A", "B", "B", "C", "B", "A", "C", "A", "B"]
    },
    "Cybersecurity": {
        "questions": [
            "1- What is malware?",
            "2- What is phishing?",
            "3- What is encryption?",
            "4- What is a VPN?",
            "5- What is two-factor authentication?",
            "6- What is a DDoS attack?",
            "7- What is a virus?",
            "8- What is a trojan horse?",
            "9- What is ransomware?",
            "10- What is a security patch?"
        ],
        "options": [
            ('A. Malicious Software', 'B. Hardware Error', 'C. Network Protocol', 'D. Operating System'),
            ('A. Network Attack', 'B. Identity Theft Attempt', 'C. Software Error', 'D. Hardware Failure'),
            ('A. Data Compression', 'B. Data Protection', 'C. Data Transfer', 'D. Data Storage'),
            ('A. Virtual Private Network', 'B. Virtual Protocol Node', 'C. Virtual Program Network', 'D. Virtual Private Node'),
            ('A. Double Password', 'B. Multiple Security', 'C. Two-Step Verification', 'D. Dual Login'),
            ('A. Virus Attack', 'B. Service Disruption', 'C. Data Theft', 'D. Password Breach'),
            ('A. Harmful Program', 'B. Network Error', 'C. Hardware Problem', 'D. System Update'),
            ('A. Security Tool', 'B. Antivirus', 'C. Malicious Program', 'D. Network Protocol'),
            ('A. Network Attack', 'B. Data Encryption', 'C. Malicious Software', 'D. System Error'),
            ('A. System Update', 'B. Security Update', 'C. Software Update', 'D. Network Update')
        ],
        "answers": ["A", "B", "B", "A", "C", "B", "A", "C", "C", "B"]
    },
    "Database Management": {
        "questions": [
            "1- What is a database?",
            "2- What is SQL?",
            "3- What is a primary key?",
            "4- What is DBMS?",
            "5- What is a query?",
            "6- What is normalization?",
            "7- What is a foreign key?",
            "8- What is data redundancy?",
            "9- What is a transaction?",
            "10- What is indexing?"
        ],
        "options": [
            ('A. File System', 'B. Data Collection', 'C. Programming Language', 'D. Network Protocol'),
            ('A. Programming Language', 'B. Query Language', 'C. Operating System', 'D. Network Protocol'),
            ('A. Main Password', 'B. Unique Identifier', 'C. Security Key', 'D. Access Code'),
            ('A. Database Management System', 'B. Data Memory System', 'C. Database Memory Storage', 'D. Data Management Storage'),
            ('A. Data Entry', 'B. Data Request', 'C. Data Storage', 'D. Data Transfer'),
            ('A. Data Compression', 'B. Data Organization', 'C. Data Encryption', 'D. Data Transfer'),
            ('A. Security Key', 'B. Reference Key', 'C. Main Key', 'D. Access Key'),
            ('A. Data Loss', 'B. Duplicate Data', 'C. Data Corruption', 'D. Data Transfer'),
            ('A. Data Transfer', 'B. Data Operation', 'C. Data Storage', 'D. Data Deletion'),
            ('A. Data Organization', 'B. Fast Data Access', 'C. Data Compression', 'D. Data Security')
        ],
        "answers": ["B", "B", "B", "A", "B", "B", "B", "B", "B", "B"]
    },
    "Web Development": {
        "questions": [
            "1- What is HTML?",
            "2- What is CSS?",
            "3- What is JavaScript?",
            "4- What is a web server?",
            "5- What is responsive design?",
            "6- What is a domain name?",
            "7- What is hosting?",
            "8- What is a cookie?",
            "9- What is HTTPS?",
            "10- What is API?"
        ],
        "options": [
            ('A. Programming Language', 'B. Markup Language', 'C. Query Language', 'D. Scripting Language'),
            ('A. Style Language', 'B. Programming Language', 'C. Query Language', 'D. Markup Language'),
            ('A. Markup Language', 'B. Style Language', 'C. Programming Language', 'D. Query Language'),
            ('A. Web Browser', 'B. Computer Host', 'C. Data Storage', 'D. Website Host'),
            ('A. Mobile Design', 'B. Adaptive Design', 'C. Web Design', 'D. Screen Design'),
            ('A. IP Address', 'B. Website Name', 'C. Server Name', 'D. Host Name'),
            ('A. Domain Service', 'B. Website Storage', 'C. Web Design', 'D. Database Service'),
            ('A. Web File', 'B. Data File', 'C. Tracking File', 'D. System File'),
            ('A. Secure Protocol', 'B. Web Protocol', 'C. Transfer Protocol', 'D. Network Protocol'),
            ('A. Program Interface', 'B. Application Interface', 'C. Programming Interface', 'D. Application Protocol')
        ],
        "answers": ["B", "A", "C", "D", "B", "B", "B", "C", "A", "A"]
    },
    "Operating Systems": {
        "questions": [
            "1- What is an operating system?",
            "2- What is multitasking?",
            "3- What is virtual memory?",
            "4- What is a process?",
            "5- What is a file system?",
            "6- What is a driver?",
            "7- What is a kernel?",
            "8- What is scheduling?",
            "9- What is deadlock?",
            "10- What is memory management?"
        ],
        "options": [
            ('A. Application Software', 'B. System Software', 'C. Utility Software', 'D. Web Software'),
            ('A. Multiple Programs', 'B. Multiple Users', 'C. Multiple Systems', 'D. Multiple Networks'),
            ('A. Extended Memory', 'B. Extra Memory', 'C. System Memory', 'D. Disk Memory'),
            ('A. Running Program', 'B. Stored Program', 'C. System Program', 'D. User Program'),
            ('A. Data Organization', 'B. Memory Organization', 'C. Program Organization', 'D. System Organization'),
            ('A. System Software', 'B. Hardware Interface', 'C. User Interface', 'D. Program Interface'),
            ('A. Core Program', 'B. System Core', 'C. OS Core', 'D. Program Core'),
            ('A. Task Management', 'B. Memory Management', 'C. File Management', 'D. User Management'),
            ('A. System Error', 'B. Resource Conflict', 'C. Program Error', 'D. Memory Error'),
            ('A. Memory Control', 'B. Memory Organization', 'C. Memory Allocation', 'D. Memory Interface')
        ],
        "answers": ["B", "A", "A", "A", "A", "B", "C", "A", "B", "C"]
    }
}
if __name__ == "__main__":
    main()

