# Taylor Beckett
Princeton University 
Computer Science Senior Thesis 2020-2021




## About the data set

This dataset is a compilation of 804 Earnings Calls from 21 companies over a period of 10 years from the third quarter of 2010 through the third quarter of 2020. All raw earnings calls can be found in the Earnings Call folder in PDF form. They can be read into programs using PyPDF or another PDF reader.

FinDataAndLinScores holds CSV files for every company in the dataset. Each CSV file holds 10 years of stock price data (with additional stock price variables), earnings reports announcements, and linguistic scores from each earnings call pertaining to the company. This dataset can be used to predict stock price movement or to conduct a variety of different analysis. To isolate just the days with earnings calls, select samples where a linguistic score (LM_Positive, LM_Negative, etc.) is not equal to 0.

The folder "Raw&Cleaned" holds a CSV file for each company. In each CSV file, there are columns for the Date of the call, the name of the company, the raw text of the call, and then the 'cleaned' tokenized call that has stop words and punctuation removed in addition to lemmatized words. Opening the CSV files in something like Excel or Numbers will not be formatted correctly. Instead, read them into a pandas DataFrame.

linguisticScoreExtraction.py shows how to extract linguistic scores from the raw and cleaned text of the earnings calls.

callCleaning.py shows how to clean the raw text of an earnings call (removing punctuation, stop words, tokenizing, and lemmatizing)
