
# print the largest word in the sentence
sent=str(input())
largest_word=""
max_l=0
split_sent=sent.split()

ls=len(split_sent)

def lar(word_check):
    z=0
    for i in word_check:
        z=z+1
    if (max_l<=z):
        largest_word=word_check
        max_l=z


# wap to reverse letters in a word in a sentance
for k in range(ls):
    lar(split_sent[k])

print(largest_word)