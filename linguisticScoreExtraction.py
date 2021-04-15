import pysentiment2 as sent
import os
import pandas as pd
import numpy as np
from tqdm import tqdm
from textstat import flesch_reading_ease, smog_index, gunning_fog
from textstat import dale_chall_readability_score


## INSERT DIRECTORY OF Raw&Cleaned

lm = sent.LM()
hiv4 = sent.HIV4()

for company in tqdm(sorted(os.listdir())):
    
    if company == '.DS_Store':
        continue
    
    lmpos = []
    lmneg = []
    lmpol = []
    lmsub = []
    gipos = []
    gineg = []
    gipol = []
    gisub = []
    flesch = []
    smog = []
    
    calls = pd.read_csv(company)
    dates = calls['Date'].tolist()
    rawtext = calls['Raw Text'].tolist()
    cleaned = calls['Cleaned'].tolist()
    
    for call in cleaned:
        # print(call)
        # break
        total = len(call)
        # tok = lm.tokenize(call) # raw text Can also be tokenized by the installed tokenizer
        lm_score = lm.get_score(call)
        gi_score = hiv4.get_score(call)
        lmpos.append((lm_score['Positive']/total)*100)
        lmneg.append((lm_score['Negative']/total)*100)
        lmpol.append(lm_score['Polarity'])
        lmsub.append(lm_score['Subjectivity'])
        gipos.append((gi_score['Positive']/total)*100)
        gineg.append((gi_score['Negative']/total)*100)
        gipol.append(gi_score['Polarity'])
        gisub.append(gi_score['Subjectivity'])
    
    for raw in rawtext:
        flesch.append(flesch_reading_ease(raw))
        smog.append(smog_index(raw))
        
    ds = {'Date': dates, 'LM_Positve': lmpos, 'LM_Negative': lmneg,
          'LM_Polarity': lmpol, 'LM_Subjectivity': lmsub, 
          'GI_Positive': gipos, 'GI_Negative': gineg,
          'GI_Polarity': gipol, 'GI_Subjectivity': gisub, 'Flesch': flesch,
          'SMOG': smog}
    datescore = pd.DataFrame(ds)
    
    merged = pd.merge(left=calls, right=datescore, how='left', left_on='Date', right_on='Date')

    name = company[:-4] + '_scores.csv'
    merged.to_csv(name, index=False, header=True)
    
        
        