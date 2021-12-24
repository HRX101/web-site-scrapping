import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file="facebook.xlsx"
rd=pd.ExcelFile(file)
dfs=rd.parse(rd.sheet_names[0])
dfs=list(dfs['Facebook'])
print(dfs)
sd=SentimentIntensityAnalyzer()
val="Dec"
for data in dfs:
    a=data.find(val)
    if a==-1:
        ss=sd.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])

