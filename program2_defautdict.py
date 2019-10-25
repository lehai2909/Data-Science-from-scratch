word_counts = {}
for word in ["my","my","name","is","is","is","Hai"]:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
        
print(word_counts)
    
#for items in word_counts.items():
#   print(items[0],items[1])
    
