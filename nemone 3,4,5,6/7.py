words = ["hi","python","teens","code","awesome","fun"]
long_words = []
for w in words:
    if len(w) >= 5:
        long_words.append(w)
print(long_words)