import random
print("WELCOME TO THE GUESSING GAME")
score = 0
while True:
    low = int(input("\nLower Bound: "))
    hi = int(input("Upper Bound: "))

    if low > hi:
        print("\nLower Bound Must Be Less Than Upper Bound.\n")
        print("Please Try Aagin.\n")
        continue

    if abs(hi-low)<2:
        print("\nThe Range Is Too Small. Please Give A Larger Range.\n")
        continue

    ran_num = random.randrange(low, hi)
    print("\nAwesome! I've thought of a number between", low, "and", hi)
    print("Now you have 3 chances to guess it.\n\n")
    for i in range(3):
        guess = int(input("Your Guess: "))
        if guess == ran_num:
            print("\nCongrat's You guessed it! You win!\n+1 Added To Your Total Score\n")
            score += 1
            break
        elif guess < ran_num:
            print("Your Guess Was Too Low!")
        else:
            print("Your Guess Was Too High!")
        if i == 2:
            print("\nYou Lose! The Number Was", ran_num)
        else:
            print("Have One More Try")
    print("\nUp For Another Round? Or Exit? (Type Yes Or No)")
    response = input()
    if response.lower() == "yes":
        continue
    else:
        print("\n\nThanks For Playing! Your Total Score Is:", score)
        break
print("Press Any Key To Exit.")
input()
