def no_dups(s):
    # Your code here
    cache = {}
    result = ""
    # split string into an array of words
    words = s.split()
    # for each new word not in the cache add it to cache and result string
    for word in words:
        if word not in cache:
            cache[word] = word
            result += word + " " 
    print(result)    
    return result.rstrip() # removes trailing whitespace


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))