print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()

print("Okay! Lets play")
score = 0
answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect!")
    

answer = input("What does WRT stand for? ")

if answer.lower() == "wolf ridge trail":
    print("Correct")
    score += 1
else:
    print("Incorrect!")

    
    
answer = input("What does IBM stand for? ")

if answer.lower() == "Information business machine":
    print("Correct")
    score += 1
else:
    print("Incorrect!")



answer = input("What does GPU stand for? ")

if answer.lower() == "Graphical processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect!")

print("you got" + str(score) + " questions correct!")
print("you got" + str(score / 4 * 100) + "%.")









    
