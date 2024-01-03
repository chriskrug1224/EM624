"""
Author: Christopher Kruger
Description:
Get two articles about the same topic, clean up the text, calculate the sentiment,
calculate bigrams in a 'word1_word2' format with a frequency above 3 then merge into one, then create word clouds
"""
import re
import bs4 as bs
import nltk
import requests
from nltk import BigramAssocMeasures, BigramCollocationFinder
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def txt_clean(word_list, min_len, stopwords_list): # Source: https://sit.instructure.com/courses/68274/files/11937366?module_item_id=1923930
    clean_words = []
    for line in word_list:
        parts = line.strip().split()
        for word in parts:
            word_l = word.lower().strip()
            if word_l.isalpha():
                if len(word_l) > min_len:
                    if word_l not in stopwords_list:
                        clean_words.append(word_l)
                    else:
                        continue
    return clean_words

word_min_len = 3 # Minimum word count to be registered from the text files

stopwords = open("stopwords_en.txt", "r",encoding = "utf8")
stopword_file = stopwords.read()
StopwordsList = []
StopwordsList.extend(["adam", "johnson", "hockey"]) # Adding additional stop words that are common between the two articles

for word in stopword_file.strip().split():
    StopwordsList.append(word.lower())

# Setting up the two articles for beautiful soup
bbcUrl = "https://www.bbc.com/news/uk-england-nottinghamshire-67419951"
nprUrl = "https://www.npr.org/2023/11/14/1212945117/adam-johnson-hockey-death-arrest"

body1 = requests.get(bbcUrl)
soup1 = bs.BeautifulSoup(body1.content, "html.parser")

print("---- ORIGINAL ARTICLES ----\n")
# Article 1
article1 = []
print("The title of the first article is:\n", soup1.title.string, "\n")
for paragraph in soup1.find_all("p"):
    # Old method, keeping for testing. Originally had each entity in a list be entire sentences
    # print(paragraph.text)
    # article1.append(paragraph.get_text())
    words = re.findall(r'\b\w+\b', paragraph.get_text()) # Used chatgpt for help, was unsure how to have every word as a seperate entity in a list
    article1.extend(words)

print("Full text for article 1 (", len(article1), "words): \n")
print(article1, "\n")

# Article 2
body2 = requests.get(nprUrl)
soup2 = bs.BeautifulSoup(body2.content, "html.parser")

article2 = []
print("The title of the second article is: \n", soup2.title.string, "\n")
for paragraph in soup2.find_all("p"):
    # print(paragraph.text)
    # article1.append(paragraph.get_text())
    words = re.findall(r'\b\w+\b', paragraph.get_text()) # Same comments as earlier
    article2.extend(words)
print("Full text for article 2 (", len(article2), "words): \n")
print(article2), "\n"

print("\n---- CLEAN ARTICILES ----\n")
# Clean using the txt_clean function
print("Clean article 1: \n")
cleanArticle1 = txt_clean(article1, word_min_len, StopwordsList)

print(cleanArticle1, "\n")

print("Clean article 2: \n")
cleanArticle2 = txt_clean(article2, word_min_len, StopwordsList)

print(cleanArticle2, "\n")

# Create bigrams for article 1
bigram_measures = BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(cleanArticle1)

# Filter bigrams by only showing those that appeared more than 3 times
finder.apply_freq_filter(3)
bigrams_formatted1 = ["{}_{}".format(w1, w2) for (w1, w2), freq in finder.score_ngrams(bigram_measures.raw_freq)] # Used chatgpt for getting the bigrams to be in the format word1_word2

print("The bigrams used more than 3 times (and formatted to x_y) in article 1 are:\n", bigrams_formatted1)

# Create bigrams for article 2
# Same comments as earlier
bigram_measures2 = BigramAssocMeasures()
finder2 = BigramCollocationFinder.from_words(cleanArticle2)

finder2.apply_freq_filter(3)
bigrams_formatted2 = ["{}_{}".format(w1, w2) for (w1, w2), freq in finder2.score_ngrams(bigram_measures2.raw_freq)]

print("The bigrams used more than 3 times (and formatted to x_y) in article 2 are:\n", bigrams_formatted2)

# Combining the single words and bigrams for the articles in a total list
totalArticle1 = bigrams_formatted1 + cleanArticle1
totalArticle2 = bigrams_formatted2 + cleanArticle2

print("\nThe combined total article and bigrams for article 1 is:\n", totalArticle1)
print("\nThe combined total article and bigrams for article 2 is:\n", totalArticle2)

# Sentiment Calculation
# Analyzer Source: https://sit.instructure.com/courses/68274/files/11937366?module_item_id=1923930
analyzer = SentimentIntensityAnalyzer()
# Transforms list to string
article1_text_str = ' '.join(totalArticle1)
pro_vad_sentiment = analyzer.polarity_scores(article1_text_str)

pro_pos = pro_vad_sentiment ["pos"]
pro_neg = pro_vad_sentiment ["neg"]
pro_neu = pro_vad_sentiment ["neu"]

print ("\nThe following is the distribution of the sentiment for article 1:\n")
print ("\nIt is positive for", "{:.1%}".format(pro_pos))
print ("\nIt is negative for", "{:.1%}".format(pro_neg))
print ("\nIt is neutral for", "{:.1%}".format(pro_neu))

article2_text_str = ' '.join(totalArticle2)
pro_vad_sentiment = analyzer.polarity_scores(article2_text_str)

pro_pos = pro_vad_sentiment ["pos"]
pro_neg = pro_vad_sentiment ["neg"]
pro_neu = pro_vad_sentiment ["neu"]

print ("\nThe following is the distribution of the sentiment for article 2:\n")
print ("\nIt is positive for", "{:.1%}".format(pro_pos))
print ("\nIt is negative for", "{:.1%}".format(pro_neg))
print ("\nIt is neutral for", "{:.1%}".format(pro_neu))

# Wordcloud calculation
text1 = " ".join(totalArticle1)
wc1 = WordCloud(background_color = "white", max_words = 1000)
wc1.generate(text1)
plt.imshow(wc1)
plt.axis("off")
plt.show()
wc1.to_file("article1.png")

text2 = " ".join(totalArticle2)
wc2 = WordCloud(background_color = "white", max_words = 1000)
wc2.generate(text2)
plt.imshow(wc2)
plt.axis("off")
plt.show()
wc2.to_file("article2.png")