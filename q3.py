# a

qt = open("C:\Joey\Data Analytics Programming\hw1\quotes.txt","r")
lines = qt.readlines()

list_quo = []
list_speaker = []
list_quo_trimmed = []
list_speaker_trimmed = []
full_quotes = []

for i in lines:
    
    ind_a=lines.index(i)
    if ind_a % 2 == 0:
        list_quo.append(i)
    else:
        list_speaker.append(i)
    
for quo in list_quo:
    
    list_quo_trimmed.append(quo.rstrip("\n"))

for speaker in list_speaker:
    
    list_speaker_trimmed.append(speaker.rstrip("\n"))
    
for j in range(len(list_quo)):
    
    full_quotes.append(list_quo_trimmed[j]+ " - " + list_speaker_trimmed[j])

full_quotes
    


# b

import re 

def words_in_full_quotes(quotes):
    
    words = re.split('\W*',quotes.lower())
    return words
    


# c
    
posting_list = {}

for i in range(len(full_quotes)):
    
    wordcount = {}
    key = full_quotes[i]

    for word in words_in_full_quotes(key):
        if word not in wordcount :
            wordcount[word] = 1
        else:
            wordcount[word] += 1
        posting_list[key] = wordcount

posting_list.items()



# d

reverse_posting_list = {}

for i in range(len(full_quotes)):
    
    quote = full_quotes[i]
    
    for word in words_in_full_quotes(quote):
        
        if word not in reverse_posting_list.keys():
            reverse_posting_list[word]={}
            reverse_posting_list[word][quote] = 1
                
        else:
            if quote not in reverse_posting_list[word]:
                reverse_posting_list[word][quote] = 1
            else:
                reverse_posting_list[word][quote] += 1
