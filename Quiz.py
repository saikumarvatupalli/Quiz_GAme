print("Enter the game ")
print("Enter Ok! for the continue the Game :)")
Join = str(input())
if Join == "Ok":
    print("Thanks! Choose our game :)")
else:
    print("Ok! You can Quit the game :)")
print("Let's start the adventure!")
print(" Your Question : ")
Q_1 = "Which is the heavier metal of these two?(Gold or Silver)"
print(Q_1)
Answer = str(input())
if Answer == "Gold":
    print("Correct :) and got 1 point! Your next Question")
else:
    print("Not Correct! Ok your next question ")
Q_2 = "Who is invented the computer?"
print(Q_2)
Answer = str(input())
if Answer == "Charles Babbage":
    print("Correct :) and got 1 point! Your next Question")
else:
    print("Not Correct! Ok your next question ")
Q_3 = "1024 Kilobyte is equal to?"
print(Q_3)
Answer = str(input())
if Answer == "1Megabyte":
    print("Correct :) and got 1 point! Your next Question")
else:
    print("Not Correct! Ok your next question ")
Q_4 = "India lies in which continent"
print(Q_4)
Answer = str(input())
if Answer == "Asia":
    print("Correct :) and got 1 point! Your next Question")
else:
    print("Not Correct! Ok your next question ")
Q_5 = "which country are the Giza Pyramids in?"
print(Q_5)
Answer = str(input())
if Answer == "Egypt":
    print("Correct :) and got 1 point! Your next Question")
else:
    print("Not Correct! Ok your next question ")
Q_6 = "What city is the status of liberty in?"
print(Q_6)
Answer = str(input())
if Answer == "New York":
    print("Correct :) and got 1 point! Your next Question")
else:
    print("Not Correct! Ok your next question ")
Q_7 = "Gidda is the folk dance of?"
print(Q_7)
Answer = str(input())
if Answer == "Punjab":
    print("Correct :) and got 1 point! Your next Question")
else:
    print("Not Correct! Ok your next question ")
Q_8 = "Which is the most sensitive organ in our body?"
print(Q_8)
Answer = str(input())
print(Q_8)
if Answer == "Skin":
    print("Correct :) and got 1 point! Your next Question")
else:
    print("Not Correct! Ok your next question ")
Q_9 = "Who is known as Father of Indian Constitution?"
print(Q_9)
Answer = str(input())
if Answer == "Dr.B.R.Ambedkar":
    print("Correct :) and got 1 point! Your next Question")
else:
    print("Not Correct! Ok your next question ")
Q_10 = "Who is Father of our Nation?"
print(Q_10)
Answer = str(input())
if Answer == "Mahatma Gandhi":
    print("Correct :) and got 1 point! Your next Question")
else:
    print("Not Correct! Ok your next question ")
print("Enter the getting Points :)")
Points = int(input())
if Points >= 8:
    print("Great! you are good in GK")
elif Points >= 5 & Points <= 7:
    print("Pass!")
else:
    print("Fail! Next time prepare well")
