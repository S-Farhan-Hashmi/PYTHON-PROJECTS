print("Hello,Welcom to quiz world")
a=input("Enter your name : ").title()
questions=questions = {
    "1. What is the capital of Australia?": [
        "A) Sydney", 
        "B) Melbourne", 
        "C) Perth", 
        "D) Canberra"
    ],
    "2. Who wrote the play Romeo and Juliet?": [
        "A) Charles Dickens", 
        "B) William Shakespeare", 
        "C) George Orwell", 
        "D) Jane Austen"
    ],
    "3. What is the chemical symbol for Gold?": [
        "A) Gd", 
        "B) Go", 
        "C) Au", 
        "D) Ag"
    ],
    "4. Which planet is known as the Red Planet?": [
        "A) Earth", 
        "B) Mars", 
        "C) Venus", 
        "D) Jupiter"
    ],
    "5. How many continents are there on Earth?": [
        "A) 5", 
        "B) 6", 
        "C) 7", 
        "D) 8"
    ],
    "6. Who was the first person to step on the Moon?": [
        "A) Neil Armstrong", 
        "B) Yuri Gagarin", 
        "C) Buzz Aldrin", 
        "D) Michael Collins"
    ],
    "7. What is the largest organ in the human body?": [
        "A) Brain", 
        "B) Liver", 
        "C) Skin", 
        "D) Heart"
    ],
    "8. In which year did World War II end?": [
        "A) 1942", 
        "B) 1945", 
        "C) 1947", 
        "D) 1950"
    ],
    "9. Which gas do plants absorb from the atmosphere?": [
        "A) Oxygen", 
        "B) Nitrogen", 
        "C) Carbon Monoxide", 
        "D) Carbon Dioxide"
    ],
    "10. Who is known as the father of the computer?": [
        "A) Alan Turing", 
        "B) Charles Babbage", 
        "C) Bill Gates", 
        "D) Steve Jobs"
    ]
}
answers=answers = {
    "1. What is the capital of Australia?": "D",
    "2. Who wrote the play Romeo and Juliet?": "B",
    "3. What is the chemical symbol for Gold?": "C",
    "4. Which planet is known as the Red Planet?": "B",
    "5. How many continents are there on Earth?": "C",
    "6. Who was the first person to step on the Moon?": "A",
    "7. What is the largest organ in the human body?": "C",
    "8. In which year did World War II end?": "B",
    "9. Which gas do plants absorb from the atmosphere?": "D",
    "10. Who is known as the father of the computer?": "B"
}
def main():
    while True:
        print(f"Hey {a}, enter start to start and enter exit to exit")
        b=input("Enter your desired task :  ").lower()
        if b=="start":
            

