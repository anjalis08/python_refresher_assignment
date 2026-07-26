import string

def operations_on_string(text):
    #Remove punctuations
    for symbol in string.punctuation:
        text = text.replace(symbol,"")

    #Convert to Lowercase
    text = text.lower()

    #Split into words
    words =text.split()

    #Frequency of the words
    freq = {word:words.count(word) for word in set(words)}

    return freq

raw_text = "Data Science is amazing. Data science requires Python, and Python requires practice!"
ans = operations_on_string(raw_text)
print(ans)



