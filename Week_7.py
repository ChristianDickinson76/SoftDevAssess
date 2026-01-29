import math

# String Methods Practice: trim spaces, replace characters, count letters, check prefixes/suffixes
def clean(text):
    return text.lower().strip()


_userInput = int(input("What task to run? "))
match _userInput:
    case 1:
        # Case conversion and basic operations
        _userInput = input("Please enter a word or phrase: ")
        print(_userInput.upper())
        print(_userInput.lower())
        print(_userInput.capitalize())
        print(_userInput.title())
        print(_userInput.swapcase())
        print(_userInput[::-1])
        print(len(_userInput))
        if 'a' in _userInput:
            print(f"The letter 'a' is in {_userInput}!")
        else:
            print(f"The letter 'a' is NOT in {_userInput}.")

        print("strip():", repr(_userInput.strip()))
        print("lstrip():", repr(_userInput.lstrip()))
        print("rstrip():", repr(_userInput.rstrip()))

        print("strip('-'):", repr(_userInput.strip('-')))

        print("Replace 'a' with 'X':", _userInput.replace('a', 'X'))
        print("Replace 'o' with '0':", _userInput.replace('o', '0'))
        
        print("Replace 'hello' with 'hi':", _userInput.replace('hello', 'hi'))

        print(f"Count of 'e': {_userInput.count('e')}")
        print(f"Count of 'a': {_userInput.count('a')}")
        print(f"Count of 'o': {_userInput.count('o')}")
    
        print(f"Starts with 'The': {_userInput.startswith('The')}")
        print(f"Ends with '!': {_userInput.endswith('!')}")
    
        
        print(f"Words: {_userInput.split()}")
        
        print(f"Split by lines: {_userInput.splitlines()}")
    
        numbers = [5, 42, 123, 7]
        for num in numbers:
            print(f"{num} -> zfill(4): {str(num).zfill(4)}")

        print(clean(_userInput))
    