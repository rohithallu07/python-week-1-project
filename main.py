#Python quiz game

questions=("how many days are present in a week?:",
           "what is the largest landa animal in the world?:",
           "how many bones are there in human body?:")

options=(("A. 8", "B. 7", "C. 6", "D. 5"),
         ("A. Cheetah", "B. Tiger", "C. Lion", "D. Elephant"),
         ("A. 206", "B. 203", "C. 211", "D. 119"))

answers=("B","D","A")
guesses=[]
score=0
question_num=0
for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter(A, B, C, D): answer here ---> ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answera")

    question_num+=1

print("______________________________")
print("            RESULTS           ")
print("______________________________")

print("ansers: ",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score=(score/len(questions)*100)
print(f"your score in percentage is: {score}%")



