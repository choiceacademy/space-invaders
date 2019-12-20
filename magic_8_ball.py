import random
print("Welcome to the online magic eight ball!\nAsk me any yes or no question and I will tell you what I forsee. If you want to stop, press 'q' to quit.")
question = input("What is your question?\n")
while (question != "q"):
	answers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitly", "You may rely on it.", "As I see it, yes", "Most likely", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again", "Ask again later.", "Better not tell you now.", "Cannot predict now", "Concentrate and ask again.", "Don't count on it", "My reply is no.", "My sources say no.", "Outlook is not very good.", "Very doubtful."]
	print("The answer to'", question.title(), "' is,", random.choice(answers))
	print ("If you want to stop, press 'q', if not, ask me another question.")
	question = input("What is your question?\n")
