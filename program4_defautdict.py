from collections import defaultdict
word_counts = defaultdict(int)
for word in ["my","my","name","is","is","is","Hai"]:
    word_counts[word] += 1
print(word_counts)
