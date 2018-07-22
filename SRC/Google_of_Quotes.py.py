## Python Assignment
## Problem No.3 : Google of Quotes

## (e)

## Defining function to get TF

## (a)

mylist = []
fp = open('quotes.txt', 'r')
l = fp.readline()
while l is not '':
    mylist.append(l)
    l = fp.readline()

#(b)
i = 0
while (i <= (len(mylist)-4)):
    #print i
    s = my_list[i] + "-" + my_list[i+1]
    fin_list.append(s)
    i = i+2

#(c)
re.split('[\.\s,-]*', s)

#(d)

def get_d2(quote):
    q = words_in_full_quotes(quote)
    d = {}
    for k in q:
        d[k] = q.count(k)
    return d

def posit_dictionary(corpus):
	pos_dict = {}
	for k in fin_list:
	    d2 = get_d2(k)
	    pos_dict[k] = d2
	return pos_dict

##(e)

def tf(word, quote, dict1):
    numr = dict1[quote][word]
    #print(numr)
    denom = max(dict1[quote].values())
    #print(denom)
    TF = (numr)/(denom*1.0)
    return TF

## Defining function to get IDF

import math
def IDF(word, dict1, dict2):
    numr = len(dict1.keys())
    #print(numr)
    denom = len(dict2[word].keys())
    #print(denom)
    IDF = math.log(numr/denom)
    return IDF

def TF_IDF(word, quote, dict1, dict2):
    tf_ = tf(word, quote, dict1)
    idf = IDF(word, dict1, dict2)
    tfidf = tf_*(idf*1.0)
    return tfidf

## (f)

def search_single_word(word):
    fin_dict = {}
    dict_key = reverse_postings_list_dictionary[word].keys()
    for key in dict_key:
        fin_dict[key] =  TF_IDF(word, key, posting_list_dictionary, reverse_postings_list_dictionary)
    return fin_dict

## (g)

def Quote_search_multiple_words(inp):
    res_d = {}
    for w in inp:
        #print("word here is: ",w)
        ky = reverse_postings_list_dictionary[w].keys()
        #res_d = {}
        for j in ky:
            if(j not in res_d.keys()):
                res_d[j] = TF_IDF(w, j, posting_list_dictionary, reverse_postings_list_dictionary)
            else: 
                #print(j)
                #print("first TFIDF is:",res_d[j])
                res_d[j] = res_d[j] + TF_IDF(w, j, posting_list_dictionary, reverse_postings_list_dictionary)

    return res_d
