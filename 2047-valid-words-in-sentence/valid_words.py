from collections import Counter
digits = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyz"
punct = "!.,"

def is_valid(word):
    if len(word) == 0:
        return False

    count = Counter(word)

    if any(count[d] > 0 for d in digits):
        return False

    if count["-"] > 0:
        if count["-"] > 1:
            return False
        hyphen_pos = word.find("-")
        if hyphen_pos == 0 or hyphen_pos == len(word) - 1:
            return False
        if word[hyphen_pos-1] not in letters or word[hyphen_pos+1] not in letters:
            return False

    punct_n = sum(count[p] for p in punct) 
    if punct_n > 0:
        if punct_n > 1: 
            return False 
        for p in punct:
            p_pos = word.find(p)
            if p_pos != -1 and p_pos != len(word) - 1:
                return False
    return True

def countValidWords(sentence):
    return sum(1 for w in sentence.split(" ") if is_valid(w))

                 
print(is_valid("cat"))
print(countValidWords("cat  and dog"))