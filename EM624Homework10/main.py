"""

Author: Christopher Kruger

Description:
By parsing through the json file of 10 years worth of articles on the HuffingtonPost (2012 - 2022),
the code shows the top 20 words used in each article's short description,
the sentiment for each year (using the first 10,000 words because the program would run for over an hour with every word),
and the wordcloud for each year
"""

import json
import string
from collections import Counter

from matplotlib import pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from nltk.tokenize import RegexpTokenizer, word_tokenize
from wordcloud import WordCloud
import nltk
from collections import Counter

stopwords = open("stopwords_en.txt", "r",encoding = "utf8") # Take in stop words
stopword_file = stopwords.read()
StopwordsList = []
StopwordsList.extend(["s", "-"]) # Removing "s" because it gets accidently included when a word like Trump's gets turned into 'Trump' and 's'. Same with "-" for Covid-19. Didn't completely work for S though :\
def remove_punctuation(text): # Removes puncutation in short descriptions, like '.', ',', '!', etc.
    return text.translate(str.maketrans("", "", string.punctuation))

for word in stopword_file.strip().split():
    StopwordsList.append(word.lower())

df = pd.read_json("News_Category_Dataset_v3.json", lines=True)

# print(df.info())
# print(df.columns)
date_desc = df[["date", "short_description"]]
date_desc.groupby(["date", "short_description"])
# print(date_desc)

list_2012, list_2013, list_2014, list_2015, list_2016, list_2017, list_2018, list_2019, list_2020, list_2021, list_2022 = ([] for i in range(11))

# Takes the date_desc dataframe. Turns each year's articles into its own list. Then splits/seperates each sentence to just be a list of words seperated by commas

for index, row in date_desc.iterrows():
    if "2022" in str(row["date"]):
        # print(row["short_description"])
        list_2022.extend(remove_punctuation(row["short_description"]).split())
        # print("2022 List loaded\n")
    elif "2021" in str(row["date"]):
        # print(row["short_description"])
        list_2021.extend(remove_punctuation(row["short_description"]).split())
        # print("2021 List loaded\n")
    elif "2020" in str(row["date"]):
        # print(row["short_description"])
        list_2020.extend(remove_punctuation(row["short_description"]).split())
        # print("2020 List loaded\n")
    elif "2019" in str(row["date"]):
        # print(row["short_description"])
        list_2019.extend(remove_punctuation(row["short_description"]).split())
        # print("2019 List loaded\n")
    elif "2018" in str(row["date"]):
        # print(row["short_description"])
        list_2018.extend(remove_punctuation(row["short_description"]).split())
        # print("2018 List loaded\n")
    elif "2017" in str(row["date"]):
        # print(row["short_description"])
        list_2017.extend(remove_punctuation(row["short_description"]).split())
        # print("2017 List loaded\n")
    elif "2016" in str(row["date"]):
        # print(row["short_description"])
        list_2016.extend(remove_punctuation(row["short_description"]).split())
        # print("2016 List loaded\n")
    elif "2015" in str(row["date"]):
        # print(row["short_description"])
        list_2015.extend(remove_punctuation(row["short_description"]).split())
        # print("2015 List loaded\n")
    elif "2014" in str(row["date"]):
        # print(row["short_description"])
        list_2014.extend(remove_punctuation(row["short_description"]).split())
        # print("2014 List loaded\n")
    elif "2013" in str(row["date"]):
        # print(row["short_description"])
        list_2013.extend(remove_punctuation(row["short_description"]).split())
        # print("2013 List loaded\n")
    elif "2012" in str(row["date"]):
        # print(row["short_description"])
        list_2012.extend(remove_punctuation(row["short_description"]).split())
        # print("2012 List loaded\n")

"""print("The words for 2012: \n")
print(list_2012)"""

# Filtered words to not include stop words

list_2012_filtered = [word for word in list_2012 if word.lower() not in StopwordsList]
list_2013_filtered = [word for word in list_2013 if word.lower() not in StopwordsList]
list_2014_filtered = [word for word in list_2014 if word.lower() not in StopwordsList]
list_2015_filtered = [word for word in list_2015 if word.lower() not in StopwordsList]
list_2016_filtered = [word for word in list_2016 if word.lower() not in StopwordsList]
list_2017_filtered = [word for word in list_2017 if word.lower() not in StopwordsList]
list_2018_filtered = [word for word in list_2018 if word.lower() not in StopwordsList]
list_2019_filtered = [word for word in list_2019 if word.lower() not in StopwordsList]
list_2020_filtered = [word for word in list_2020 if word.lower() not in StopwordsList]
list_2021_filtered = [word for word in list_2021 if word.lower() not in StopwordsList]
list_2022_filtered = [word for word in list_2022 if word.lower() not in StopwordsList]

"""print("The filtered words for 2012: \n")
print(list_2012_filtered)"""

# Top 20 used words with counter
counter_2012 = Counter(list_2012_filtered)
counter_2013 = Counter(list_2013_filtered)
counter_2014 = Counter(list_2014_filtered)
counter_2015 = Counter(list_2015_filtered)
counter_2016 = Counter(list_2016_filtered)
counter_2017 = Counter(list_2017_filtered)
counter_2018 = Counter(list_2018_filtered)
counter_2019 = Counter(list_2019_filtered)
counter_2020 = Counter(list_2020_filtered)
counter_2021 = Counter(list_2021_filtered)
counter_2022 = Counter(list_2022_filtered)

# print(counter_2012)

# With the counter example, used for testing
# top_words_2012 = counter_2012.most_common(20)

# Takes just the top words, ignoring the counter
top_words_2012 = [word for word, count in counter_2012.most_common(20)]
top_words_2013 = [word for word, count in counter_2013.most_common(20)]
top_words_2014 = [word for word, count in counter_2014.most_common(20)]
top_words_2015 = [word for word, count in counter_2015.most_common(20)]
top_words_2016 = [word for word, count in counter_2016.most_common(20)]
top_words_2017 = [word for word, count in counter_2017.most_common(20)]
top_words_2018 = [word for word, count in counter_2018.most_common(20)]
top_words_2019 = [word for word, count in counter_2019.most_common(20)]
top_words_2020 = [word for word, count in counter_2020.most_common(20)]
top_words_2021 = [word for word, count in counter_2021.most_common(20)]
top_words_2022 = [word for word, count in counter_2022.most_common(20)]

print("The top 20 words in 2012:", top_words_2012)
print("The top 20 words in 2013:", top_words_2013)
print("The top 20 words in 2014:", top_words_2014)
print("The top 20 words in 2015:", top_words_2015)
print("The top 20 words in 2016:", top_words_2016)
print("The top 20 words in 2017:", top_words_2017)
print("The top 20 words in 2018:", top_words_2018)
print("The top 20 words in 2019:", top_words_2019)
print("The top 20 words in 2020:", top_words_2020)
print("The top 20 words in 2021:", top_words_2021)
print("The top 20 words in 2022:", top_words_2022)

# ----
# Sentiment Calculation - for the first 10,000 words. It takes way too long to do each year's entire list of words. Should be a good overview even with 10,000 words
# ----

# Analyzer Source: https://sit.instructure.com/courses/68274/files/11937366?module_item_id=1923930
analyzer = SentimentIntensityAnalyzer()
# Transforms list to string for year 2012
print("Calculating the sentiment for the first 10,000 words used in 2012 articles: \n")
year1_text_str = ' '.join(list_2012_filtered[:10000])
pro_vad_sentiment = analyzer.polarity_scores(year1_text_str)

pro_pos = pro_vad_sentiment ["pos"]
pro_neg = pro_vad_sentiment ["neg"]
pro_neu = pro_vad_sentiment ["neu"]

# print ("\nThe following is the distribution of the sentiment for each year:\n")
print ("\nIt is positive for", "{:.1%}".format(pro_pos))
print ("\nIt is negative for", "{:.1%}".format(pro_neg))
print ("\nIt is neutral for", "{:.1%}".format(pro_neu))

# Transforms list to string for year 2013
print("Calculating the sentiment for the first 10,000 words used in 2013 articles: \n")
year2_text_str = ' '.join(list_2013_filtered[:10000])
pro_vad_sentiment = analyzer.polarity_scores(year2_text_str)

pro_pos = pro_vad_sentiment ["pos"]
pro_neg = pro_vad_sentiment ["neg"]
pro_neu = pro_vad_sentiment ["neu"]

# print ("\nThe following is the distribution of the sentiment for each year:\n")
print ("\nIt is positive for", "{:.1%}".format(pro_pos))
print ("\nIt is negative for", "{:.1%}".format(pro_neg))
print ("\nIt is neutral for", "{:.1%}".format(pro_neu))

# Transforms list to string for year 2014
print("Calculating the sentiment for the first 10,000 words used in 2014 articles: \n")
year3_text_str = ' '.join(list_2014_filtered[:10000])
pro_vad_sentiment = analyzer.polarity_scores(year3_text_str)

pro_pos = pro_vad_sentiment ["pos"]
pro_neg = pro_vad_sentiment ["neg"]
pro_neu = pro_vad_sentiment ["neu"]

# print ("\nThe following is the distribution of the sentiment for each year:\n")
print ("\nIt is positive for", "{:.1%}".format(pro_pos))
print ("\nIt is negative for", "{:.1%}".format(pro_neg))
print ("\nIt is neutral for", "{:.1%}".format(pro_neu))

# Transforms list to string for year 2015
print("Calculating the sentiment for the first 10,000 words used in 2015 articles: \n")
year4_text_str = ' '.join(list_2015_filtered[:10000])
pro_vad_sentiment = analyzer.polarity_scores(year4_text_str)

pro_pos = pro_vad_sentiment ["pos"]
pro_neg = pro_vad_sentiment ["neg"]
pro_neu = pro_vad_sentiment ["neu"]

# print ("\nThe following is the distribution of the sentiment for each year:\n")
print ("\nIt is positive for", "{:.1%}".format(pro_pos))
print ("\nIt is negative for", "{:.1%}".format(pro_neg))
print ("\nIt is neutral for", "{:.1%}".format(pro_neu))

# Transforms list to string for year 2016
print("Calculating the sentiment for the first 10,000 words used in 2016 articles: \n")
year5_text_str = ' '.join(list_2016_filtered[:10000])
pro_vad_sentiment = analyzer.polarity_scores(year5_text_str)

pro_pos = pro_vad_sentiment ["pos"]
pro_neg = pro_vad_sentiment ["neg"]
pro_neu = pro_vad_sentiment ["neu"]

# print ("\nThe following is the distribution of the sentiment for each year:\n")
print ("\nIt is positive for", "{:.1%}".format(pro_pos))
print ("\nIt is negative for", "{:.1%}".format(pro_neg))
print ("\nIt is neutral for", "{:.1%}".format(pro_neu))

# Transforms list to string for year 2017
print("Calculating the sentiment for the first 10,000 words used in 2017 articles: \n")
year6_text_str = ' '.join(list_2017_filtered[:10000])
pro_vad_sentiment = analyzer.polarity_scores(year6_text_str)

pro_pos = pro_vad_sentiment ["pos"]
pro_neg = pro_vad_sentiment ["neg"]
pro_neu = pro_vad_sentiment ["neu"]

# print ("\nThe following is the distribution of the sentiment for each year:\n")
print ("\nIt is positive for", "{:.1%}".format(pro_pos))
print ("\nIt is negative for", "{:.1%}".format(pro_neg))
print ("\nIt is neutral for", "{:.1%}".format(pro_neu))

# Transforms list to string for year 2018
print("Calculating the sentiment for the first 10,000 words used in 2018 articles: \n")
year7_text_str = ' '.join(list_2018_filtered[:10000])
pro_vad_sentiment = analyzer.polarity_scores(year7_text_str)

pro_pos = pro_vad_sentiment ["pos"]
pro_neg = pro_vad_sentiment ["neg"]
pro_neu = pro_vad_sentiment ["neu"]

# print ("\nThe following is the distribution of the sentiment for each year:\n")
print ("\nIt is positive for", "{:.1%}".format(pro_pos))
print ("\nIt is negative for", "{:.1%}".format(pro_neg))
print ("\nIt is neutral for", "{:.1%}".format(pro_neu))

# Transforms list to string for year 2019
print("Calculating the sentiment for the first 10,000 words used in 2019 articles: \n")
year8_text_str = ' '.join(list_2019_filtered[:10000])
pro_vad_sentiment = analyzer.polarity_scores(year8_text_str)

pro_pos = pro_vad_sentiment ["pos"]
pro_neg = pro_vad_sentiment ["neg"]
pro_neu = pro_vad_sentiment ["neu"]

# print ("\nThe following is the distribution of the sentiment for each year:\n")
print ("\nIt is positive for", "{:.1%}".format(pro_pos))
print ("\nIt is negative for", "{:.1%}".format(pro_neg))
print ("\nIt is neutral for", "{:.1%}".format(pro_neu))

# Transforms list to string for year 2020
print("Calculating the sentiment for the first 10,000 words used in 2020 articles: \n")
year9_text_str = ' '.join(list_2020_filtered[:10000])
pro_vad_sentiment = analyzer.polarity_scores(year9_text_str)

pro_pos = pro_vad_sentiment ["pos"]
pro_neg = pro_vad_sentiment ["neg"]
pro_neu = pro_vad_sentiment ["neu"]

# print ("\nThe following is the distribution of the sentiment for each year:\n")
print ("\nIt is positive for", "{:.1%}".format(pro_pos))
print ("\nIt is negative for", "{:.1%}".format(pro_neg))
print ("\nIt is neutral for", "{:.1%}".format(pro_neu))

# Transforms list to string for year 2021
print("Calculating the sentiment for the first 10,000 words used in 2021 articles: \n")
year10_text_str = ' '.join(list_2021_filtered[:10000])
pro_vad_sentiment = analyzer.polarity_scores(year10_text_str)

pro_pos = pro_vad_sentiment ["pos"]
pro_neg = pro_vad_sentiment ["neg"]
pro_neu = pro_vad_sentiment ["neu"]

# print ("\nThe following is the distribution of the sentiment for each year:\n")
print ("\nIt is positive for", "{:.1%}".format(pro_pos))
print ("\nIt is negative for", "{:.1%}".format(pro_neg))
print ("\nIt is neutral for", "{:.1%}".format(pro_neu))

# Transforms list to string for year 2022
print("Calculating the sentiment for the first 10,000 words used in 2022 articles: \n")
year11_text_str = ' '.join(list_2022_filtered[:10000])
pro_vad_sentiment = analyzer.polarity_scores(year11_text_str)

pro_pos = pro_vad_sentiment ["pos"]
pro_neg = pro_vad_sentiment ["neg"]
pro_neu = pro_vad_sentiment ["neu"]

# print ("\nThe following is the distribution of the sentiment for each year:\n")
print ("\nIt is positive for", "{:.1%}".format(pro_pos))
print ("\nIt is negative for", "{:.1%}".format(pro_neg))
print ("\nIt is neutral for", "{:.1%}".format(pro_neu))

# ----
# Wordcloud calculation
# ----

# 2012 Wordcloud
wc2012 = " ".join(list_2012_filtered)
wc1 = WordCloud(background_color = "white", max_words = 1000)
wc1.generate(wc2012)
plt.imshow(wc1)
plt.axis("off")
# plt.show()
wc1.to_file("2012.png")

# 2013 Wordcloud
wc2013 = " ".join(list_2013_filtered)
wc2 = WordCloud(background_color = "white", max_words = 1000)
wc2.generate(wc2013)
plt.imshow(wc2)
plt.axis("off")
# plt.show()
wc2.to_file("2013.png")

# 2014 Wordcloud
wc2014 = " ".join(list_2014_filtered)
wc3 = WordCloud(background_color = "white", max_words = 1000)
wc3.generate(wc2013)
plt.imshow(wc3)
plt.axis("off")
# plt.show()
wc3.to_file("2014.png")

# 2015 Wordcloud
wc2015 = " ".join(list_2015_filtered)
wc4 = WordCloud(background_color = "white", max_words = 1000)
wc4.generate(wc2015)
plt.imshow(wc4)
plt.axis("off")
# plt.show()
wc4.to_file("2015.png")

# 2016 Wordcloud
wc2016 = " ".join(list_2016_filtered)
wc5 = WordCloud(background_color = "white", max_words = 1000)
wc5.generate(wc2015)
plt.imshow(wc5)
plt.axis("off")
# plt.show()
wc5.to_file("2016.png")

# 2017 Wordcloud
wc2017 = " ".join(list_2017_filtered)
wc6 = WordCloud(background_color = "white", max_words = 1000)
wc6.generate(wc2017)
plt.imshow(wc6)
plt.axis("off")
# plt.show()
wc6.to_file("2017.png")

# 2018 Wordcloud
wc2018 = " ".join(list_2018_filtered)
wc7 = WordCloud(background_color = "white", max_words = 1000)
wc7.generate(wc2018)
plt.imshow(wc7)
plt.axis("off")
# plt.show()
wc7.to_file("2018.png")

# 2019 Wordcloud
wc2019 = " ".join(list_2019_filtered)
wc8 = WordCloud(background_color = "white", max_words = 1000)
wc8.generate(wc2019)
plt.imshow(wc8)
plt.axis("off")
# plt.show()
wc8.to_file("2019.png")

# 2020 Wordcloud
wc2020 = " ".join(list_2020_filtered)
wc9 = WordCloud(background_color = "white", max_words = 1000)
wc9.generate(wc2020)
plt.imshow(wc9)
plt.axis("off")
# plt.show()
wc9.to_file("2020.png")

# 2021 Wordcloud
wc2021 = " ".join(list_2021_filtered)
wc10 = WordCloud(background_color = "white", max_words = 1000)
wc10.generate(wc2021)
plt.imshow(wc10)
plt.axis("off")
# plt.show()
wc10.to_file("2021.png")

# 2022 Wordcloud
wc2022 = " ".join(list_2022_filtered)
wc11 = WordCloud(background_color = "white", max_words = 1000)
wc11.generate(wc2022)
plt.imshow(wc11)
plt.axis("off")
# plt.show()
wc11.to_file("2022.png")

