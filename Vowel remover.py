def shortcut(s):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for char in s:
        if char not in vowels:
            result += char
    return result