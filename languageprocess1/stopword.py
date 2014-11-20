#!/usr/bin/env python3

import languageprocess1.tokenizer 
import languageprocess1.normalizer

'''
Stop word remover removes stop words from a list of words or stringand return strings
It can support multple languges.
Also removes numerical strings.
'''
stopwords = {}	# dictionary to strore stopwords of languages

#stopword specific to this project
stopwords['english'] = ['a', 'about', 'above', 'after', 'again', 'against', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'attribute','attributes','at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'column', 'columns','could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't" , 'dont','down', 'during', 'each', 'elements', 'element','few', 'for', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'named','no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such' ,'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'type','under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']


def stopwordremover(text):

    data = text
    data = languageprocess1.normalizer.normalize(data)
#######################################improve this for digits, removed for inser query#############################
    if 'select' not in data and 'from' not in data: #improve
        newdata = [newtext for newtext in data if newtext not in stopwords['english']] #and not newtext.isdigit()]###check this for digit##### 
        # to check stopword and numbers
    else: 
        # for cases where numbers are required for ex select statemenets
        newdata = [newtext for newtext in data if newtext not in stopwords['english']] # to check stopword
    
    return newdata


if __name__ == '__main__':
    
    string = 'CREATE a TABLE student with; ,(id primary key, name text)'
    s = stopwordremover(string)
    print(s)
