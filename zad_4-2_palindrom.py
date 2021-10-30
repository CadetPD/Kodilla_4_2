print("Hej, chcesz wiedzieć czy dane słowo jest palindromem?")

def palindrome():

    word = input("No to wpisz dowolne słowo ;): ")

    if list(word) == list(reversed(word)):
        #print("To słowo jest palindromem!") Optional
        return True
    else:
        #print("To słowo nie jest palindromem!") Optional
        return False      

print(bool(palindrome()))