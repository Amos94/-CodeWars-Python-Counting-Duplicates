def duplicate_count(text):
    # Your code goes here
    new_text = text.lower()

    count = 0
    dictionary = {}

    for i in range(0,len(new_text)):
        dictionary[new_text[i]] = 0

    for key in dictionary:
        for i in range(0,len(new_text)):
            if(key == new_text[i]):
                dictionary[key] = dictionary[key] + 1

    for key in dictionary:
        if(dictionary[key] > 1):
            count = count + 1

    print(dictionary)
    return count
