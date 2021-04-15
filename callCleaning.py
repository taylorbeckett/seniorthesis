import nltk
import string
import pandas as pd
import numpy as np
import os
import datetime
from tqdm import tqdm
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
nltk.download('wordnet')

os.chdir('..')
os.chdir(os.getcwd() + '/Data/Combined/_CSVScores/Raw&Cleaned')
print(os.getcwd())


def no_punc(call):
    if call != 0:
        punc_free = "".join([c for c in call if c not in string.punctuation])
        return punc_free


# Tokenizer
tokenizer = RegexpTokenizer(r'\w+')


def remove_stopwords(call):
    if call != 0:
        words = [w for w in call if w not in stopwords.words('english')]
        return words 
                            
                            
lemma = WordNetLemmatizer()
                            
                            
def word_lem(call):
    if call != 0:
        lem = [lemma.lemmatize(i) for i in call]
        return lem


# SET DIRECTORY TO Raw&Cleaned or wherever raw calls are located


for company in tqdm(sorted(os.listdir())):
    
    if company == '.DS_Store':
        continue
    
    cleaned = []
    
    calls = pd.read_csv(company)
    rawtext = calls['Raw Text'].tolist()
    
    for raw in rawtext:
        punc_free = no_punc(raw)
        tokenized = tokenizer.tokenize(punc_free.lower())
        no_stop = remove_stopwords(tokenized)
        clean = word_lem(no_stop)
        cleaned.append(clean)
    
    #cleaned is a list of cleaned calls that can be used to add to a DataFrame
    # example: call['Cleaned'] = cleaned
