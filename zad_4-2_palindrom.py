print("Hej, chcesz wiedzieć czy dane słowo jest palindromem?")

def palindrome():

    """
    Palindrome() checks if a word is palindrome or not
    No defined parameter, external argument = input()
    Sollution: compare lists for argument ([normal] vs [reversed])
    Func result: returns after bool()

    """

    word = input("No to wpisz dowolne słowo ;): ")

    if list(word.lower()) == list(reversed(word.lower())):
        #print("To słowo jest palindromem!") Optional
        return True
    else:
        #print("To słowo nie jest palindromem!") Optional
        return False      

print(bool(palindrome()))