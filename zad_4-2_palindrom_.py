def palindrome(word):

    """
    Palindrome(word) checks if a word is palindrome or not
    Parameter: word
    Argument: 'word'
    Sollution: compare lists for argument ([normal] vs [reversed])
    Func result: returns after bool()

    """

    if list(word.lower()) == list(reversed(word.lower())):
        #print("To słowo jest palindromem!") Optional
        return True
    else:
        #print("To słowo nie jest palindromem!") Optional
        return False

print(bool(palindrome("Kajak")))