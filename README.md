# Taylor Beckett
Princeton University 
Computer Science Senior Thesis 2020-2021




## About the data set

The dataset consists of 860 earnings calls from 22 different companies spanning back 10 years. This equivalates to 40 earnings calls per company. Each pdf is labeled with the company name, the quarter the call took place in, and the year. 

The earnings calls were copied from SeekingAlpha and then converted to PDFs. After the earnings calls were converted to PDFS, they were uploaded to Python and cleaned using the nltk cleaning functions that were created. The cleaned earnings calls were then combined into a pandas data frame that is available to download in earningscalls.pkl. The data frame has three columns: Company Name, Date, and Earnings Calls (cleaned). 
