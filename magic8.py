import random

name = str(input("What is your name? "))
question = str(input("What is your question? "))
answer = ""

random_number = random.randint(1, 13)

# commenting out after testing print(random_number)
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Maybe so"
elif random_number == 11:
  answer = "Anything is possible"
elif random_number == 12:
  answer = "Why should I tell you?"
elif random_number == 13:
  answer = "13 is your lucky number! wink wink"
else:
  answer = "Error"

if question == "":
  print ("Please ask me a question")
else:
  if name == "":
    print("Question: " + question)
  else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)
