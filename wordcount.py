def word_count(sentence):
    words = sentence.split() 
    wordf = {}  

    for word in words:
        wordf[word] = wordf.get(word, 0) + 1

    return word_freq