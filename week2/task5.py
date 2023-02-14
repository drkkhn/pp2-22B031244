questions = {
    "What is the capital of the Kazakhstan?": {"astana"},
    "Which year Kazakhstan got independence": {"1991"},
    "What is the currency of Kazakhstan": {"tenge"},
    "Name the biggest lake in the world": {"caspian lake"}
}
points = 0
for question, answ in questions.items():
    user_answ = input(question + " ").lower()
    if answ.find(user_answ) > -1:
        points += 1

if points >= 3:
    print("Congrats")
else:
    print("You lose")
