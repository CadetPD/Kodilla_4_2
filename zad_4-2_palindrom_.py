def palindrome(word):

    """
    Palindrome(word) checks if a word is palindrome or not
    Parameter: word
    Argument: 'word'
    Sollution: compare lists for argument ([normal] vs [reversed])
    Func result: returns after func execution

    """

    if list(word.lower()) == list(reversed(word.lower())):
        return True
    else:
        return False

print(palindrome("Kajak"))