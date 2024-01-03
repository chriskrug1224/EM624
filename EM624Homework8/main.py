"""
Author: Christopher Kruger

Source: https://www.procon.org/headlines/tiktok-bans-top-3-pros-and-cons/
Description:
Two files have been created that describe the pros and cons of banning TikTok.
The script takes in the two files (along with a stopwords_en.txt) and does the following:
Clean the texts by removing
o the stopwords, using the attached stopwords_en.txt file
o words shorter than 3 characters
o all the words that are obviously frequently used (like the name of the issue)
o the punctuation
o end-of-line (“/n”) and blank lines
Using the library "vader", calculate the sentiment for the 2 texts
Extract bigrams
Calculate the Lexical Diversity Ratio, that is the ratio between the number of unique words and
total number of words. The lexical diversity ratio provides insights into the richness of a text's
vocabulary. Higher ratios indicate greater diversity, suggesting a broader range of vocabulary and
potentially more complex or varied language usage.
Create word clouds for the 2 texts.
"""
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

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

# Opening the text files
pros_txt_file = open("pros_tiktok.txt", 'r',encoding='utf8')
cons_txt_file = open("cons_tiktok.txt", 'r',encoding='utf8')
stopwords_file = open("stopwords_en.txt", 'r',encoding='utf8')

# Initilizing lists
stopwords_list = []
pros_list = []
cons_list = []
punctuation_list = [".", ",", ":", ";", "?", "(", ")", "[", "]", "'", "!", "-", "/", "$"]

# Small clean up
for word in stopwords_file:
    stopwords_list.append(word.strip())
for word in pros_txt_file:
   pros_list.append(word.strip())
for word in cons_txt_file:
   cons_list.append(word.strip())

# Adding more words that are repeated for both
stopwords_list.extend(["tiktok", "china", "chinese", "government", "governments", "united", "states"])

# Cleans both lists and incorporates the minimum word length and removes the stop words
pro_clean_words = txt_clean(pros_list, word_min_len, stopwords_list)
con_clean_words = txt_clean(cons_list, word_min_len, stopwords_list)

# --- Sentiment Calculation ----
# Analyzer Source: https://sit.instructure.com/courses/68274/files/11937366?module_item_id=1923930
# Using vader library
analyzer = SentimentIntensityAnalyzer()
# Transforms list to string
pro_clean_text_str = ' '.join(pro_clean_words)
pro_vad_sentiment = analyzer.polarity_scores(pro_clean_text_str)

pro_pos = pro_vad_sentiment ["pos"]
pro_neg = pro_vad_sentiment ["neg"]
pro_neu = pro_vad_sentiment ["neu"]

print ("\nThe following is the distribution of the sentiment for being in favor of banning TikTok:")
print ("\nIt is positive for", "{:.1%}".format(pro_pos))
print ("\nIt is negative for", "{:.1%}".format(pro_neg))
print ("\nIt is neutral for", "{:.1%}".format(pro_neu))

# Transforms list to string
con_clean_text_str = ' '.join(con_clean_words)
con_vad_sentiment = analyzer.polarity_scores(con_clean_text_str)

con_pos = con_vad_sentiment ["pos"]
con_neg = con_vad_sentiment ["neg"]
con_neu = con_vad_sentiment ["neu"]

print ("\nThe following is the distribution of the sentiment for being opposed to banning TikTok:")
print ("\nIt is positive for", "{:.1%}".format(con_pos))
print ("\nIt is negative for", "{:.1%}".format(con_neg))
print ("\nIt is neutral for", "{:.1%}".format(con_neu))

# --- Bigram Calculation ---
pro_bigram = list(nltk.bigrams(pro_clean_words))
print("\nThe following are the bigrams extracted from the pro text:\n")
print(pro_bigram)
con_bigram = list(nltk.bigrams(con_clean_words))
print("\nThe following are the bigrams extracted from the con text:\n")
print(con_bigram)

# Used in the report, shows the top 5 bigrams for ease of viewing
freqdist_pro = nltk.FreqDist(pro_bigram).most_common(5)
freqdist_con = nltk.FreqDist(con_bigram).most_common(5)
print("\n The most frequent bigrams and their frequencies from the pro file are as follows: \n", freqdist_pro)
print("\n The most frequent bigrams and their frequencies from the con file are as follows: \n", freqdist_con)


# --- Lexical Diversity Ratio Calculation ---
pro_total_length = len(pros_list)
con_total_length = len(cons_list)

def totalWords(word_list): # Gets total words, not incorporating minimum length of word
    total_words = []
    for line in word_list:
        parts = line.strip().split()
        for word in parts:
            word_l = word.lower().strip()
            if word_l.isalpha():
                total_words.append(word_l)
            else:
                continue
    return total_words

def uniqueWords(word_list): # Gets all unique words, not incorporating minimum length of word
    unique_words = []
    for line in word_list:
        parts = line.strip().split()
        for word in parts:
            word_l = word.lower().strip()
            if word_l.isalpha():
                if word_l not in unique_words:
                    unique_words.append(word_l)
            else:
                continue
    return unique_words

pro_total_words = totalWords(pros_list)
con_total_words = totalWords(cons_list)

pro_unique_words = uniqueWords(pros_list)
con_unique_words = uniqueWords(cons_list)

pro_LDR = len(pro_unique_words)/len(pro_total_words)
con_LDR = len(con_unique_words)/len(con_total_words)

print ("\nThe Lexical Diversity Ratio for the Pro Text is", "{:.1%}".format(pro_LDR))
print ("\nThe Lexical Diversity Ratio for the Con Text is", "{:.1%}".format(con_LDR))

# --- Word Cloud Calculation ---
# Source: https://sit.instructure.com/courses/68274/files/11937229?module_item_id=1923929
pro_WC = WordCloud(background_color = "white", max_words = 2000)
con_WC = WordCloud(background_color = "white", max_words = 2000)

pro_WC.generate(pro_clean_text_str)
con_WC.generate(con_clean_text_str)

pro_WC.to_file("pro.png")
con_WC.to_file("con.png")

plt.imshow(pro_WC)
plt.axis("off")
plt.show()

plt.imshow(con_WC)
plt.axis("off")
plt.show()
