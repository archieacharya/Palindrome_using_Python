def palindrome():

    print ("Please enter the word you would like to check for example:")

    word = input()
    if word == word[::-1]:
        print("It is a palindrome")
    else:
        print ('Sorry this word is not a palindrome :(')

    print ('Have a nice day!')
    print("Want to play again y/n?")

    re_play =input()

    if re_play.lower().startswith("y"):
        palindrome()
    else:
        print ("Your Loss!")

palindrome()