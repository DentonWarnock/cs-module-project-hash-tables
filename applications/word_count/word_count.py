def word_count(s):
    # Your code here
    words = {}
    ignore = ('"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&')
    
    for char in ignore:
        s = s.replace(char, "")
        
    s = s.split()
    
    for word in s:
        if word.lower() not in words:
            words[word.lower()] = 1
        else:
            words[word.lower()] += 1
    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))