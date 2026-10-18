print("Hello would u like to play my game? ")
playing = input()
marks = 0
if playing.lower()!='yes':
    quit()
print("Okay lets play !")

answer = input("what is 2+2")
if answer == "4":
    print("correct!")
    marks +=1

else:
    print("incorrect!")

answer =input("what does CPU stand for? ")
if answer.lower() == "central processing unit":    
        print("correct!")
        marks +=1
else:
    print("incorrect!")

print("You got " + str(marks) + " marks") 