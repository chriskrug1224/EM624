import os
import re
import time

import bs4 as bs
import fastf1 as ff1
import fastf1.plotting
import matplotlib.pyplot as plt
import numpy as np
import requests
import seaborn as sns
from fastf1 import plotting
from fastf1 import utils
from nltk import BigramAssocMeasures, BigramCollocationFinder
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud

"""
Author: Christopher Kruger
Description:
The program gives a recap of the major event at the 2021 Abu Dhabi Grand Prix, being Max Verstappen first time taking the World Driver Championship
against the publicly favored Lewis Hamilton's 8th Championship to take the new record of most championships in the sport of Formula 1. 
The program begins by analyzing two articles of the event, one from a British POV (Hamilton favored) and one from a Dutch POV (Verstappen favored), to check
word usage (pro, neg, neutral) and a wordcloud of the two articles. 
Next, by using the FastF1 API with a Pandas dataframe, the program gives the map of the track, telematry data, pitstop strategy, laptime distribution, and speed comparison
"""
# Start of article processing
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
StopwordsList.extend(["max", "verstappen", "lewis", "hamilton", "abu", "dhabi", "2021", "chrome", "browser", "video", "player", "race", "red", "bull", "mercedes"]) # Adding additional stop words that are common between the two articles

for word in stopword_file.strip().split():
    StopwordsList.append(word.lower())

englishURL = "https://www.skysports.com/f1/news/15740/12493844/abu-dhabi-gp-max-verstappen-takes-f1-title-from-lewis-hamilton-on-final-lap-after-late-controversy"
dutchURL = "https://www.dutchnews.nl/2021/12/verstappen-wins-formula-one-title-with-dramatic-last-lap-pass-in-abu-dhabi/?"

body1 = requests.get(englishURL)
soup1 = bs.BeautifulSoup(body1.content, "html.parser")

print("---- ORIGINAL ARTICLES ----\n")
# Article 1
origArticle1 = []
print("The title of the first article is:\n", soup1.title.string, "\n")
for paragraph in soup1.find_all("p"):
    # Old method, keeping for testing. Originally had each entity in a list be entire sentences
    # print(paragraph.text)
    # article1.append(paragraph.get_text())
    words = re.findall(r'\b\w+\b', paragraph.get_text()) # Used chatgpt for help, was unsure how to have every word as a seperate entity in a list
    origArticle1.extend(words)

article1 = origArticle1[22:] # Removing the first 23 words as they were irrelevant

print("Full text for article 1 (", len(article1), "words): \n")
print(article1, "\n")

# Had to utilize a fake header, time delay, and try/except errors as the Dutch article would be originally denied for being a web scraper with a 403 Forbidden
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

try:
    body2 = requests.get(dutchURL, headers=headers)
    body2.raise_for_status()  # Raise an HTTPError for bad responses
except requests.exceptions.HTTPError as errh:
    print ("HTTP Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("Something went wrong:",err)

time.sleep(2)  # Added a delay to avoid making requests too fast

soup2 = bs.BeautifulSoup(body2.content, "html.parser")

# Article 2
article2 = []
print("The title of the second article is:\n", soup2.title.string, "\n")
for paragraph in soup2.find_all("p"):
    words = re.findall(r'\b\w+\b', paragraph.get_text())
    article2.extend(words)

print("Full text for article 2 (", len(article2), "words): \n")
print(article2)


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
# plt.show()
wc1.to_file("EnglishArticle.png")

text2 = " ".join(totalArticle2)
wc2 = WordCloud(background_color = "white", max_words = 1000)
wc2.generate(text2)
plt.imshow(wc2)
plt.axis("off")
#plt.show()
wc2.to_file("DutchArticle.png")

# -----
# Start of FastF1 Processing
# -----

# Makes cache directory if it doesn't exist. This is a requirement for FastF1
if not os.path.exists('cache'):
    os.makedirs('cache')
else:
    print('cache dir exist')

# -----
# Track Map - Source: https://docs.fastf1.dev/examples_gallery/plot_annotate_corners.html#sphx-glr-examples-gallery-plot-annotate-corners-py
# -----
session = fastf1.get_session(2021, 22, 5) # Loading the race session for use
session.load()

lap = session.laps.pick_fastest()
pos = lap.get_pos_data() # Map is generated using the position telemetry data from the fastest lap, it is not a static pre-generated image

circuit_info = session.get_circuit_info()

# From Source:
# This is utilized for ensuring proper placement of corner and corner #'s around the track
# Defining a helper function for rotating points around the origin of a coordinate system
# The matrix [[cos, sin], [-sin, cos]] is called a rotation matrix
# By matrix multiplication of the rotation matrix with a vector [x, y], a new rotated vector [x_rot, y_rot] is obtained. (See also: https://en.wikipedia.org/wiki/Rotation_matrix)
def rotate(xy, *, angle): # includes arbitrary input
    rot_mat = np.array([[np.cos(angle), np.sin(angle)], [-np.sin(angle), np.cos(angle)]])
    return np.matmul(xy, rot_mat)

# Gets an array of shape [n, 2] where n is the number of points and the second axis is x and y
track = pos.loc[:, ('X', 'Y')].to_numpy()
# Converts the rotation angle from degrees to radian
track_angle = circuit_info.rotation / 180 * np.pi
# Rotates and plots the map of the track
rotated_track = rotate(track, angle=track_angle)
plt.plot(rotated_track[:, 0], rotated_track[:, 1])
offset_vector = [500, 0]

# Iterates over all corners
for _, corner in circuit_info.corners.iterrows(): # "_" for an unknown number, dependent on how many corners in a map. Leaving it as unknown for future proofing
    # Creates a string from corner number and letter
    txt = f"{corner['Number']}{corner['Letter']}"
    # Converts the angle from degrees to radians
    offset_angle = corner['Angle'] / 180 * np.pi
    # Rotates the offset vector so that it points sideways
    offset_x, offset_y = rotate(offset_vector, angle=offset_angle)
    # Adds the offset to the position of the corner
    text_x = corner['X'] + offset_x
    text_y = corner['Y'] + offset_y
    # Rotates the text position
    text_x, text_y = rotate([text_x, text_y], angle=track_angle)
    # Rotates the center of the corner equivalently to the rest of the track map
    track_x, track_y = rotate([corner['X'], corner['Y']], angle=track_angle)
    # Draws a circle next to the track to improve readability
    plt.scatter(text_x, text_y, color='grey', s=140)
    # Draws a line from the track to the circle
    plt.plot([track_x, text_x], [track_y, text_y], color='grey')
    # Places the corner number inside the circle
    plt.text(text_x, text_y, txt, va='center_baseline', ha='center', size='small', color='white')

# Clean up the plot, add title, set equal axis ratio
plt.title("Yas Marina Circuit")
plt.xticks([])
plt.yticks([])
plt.axis('equal')
plt.savefig("2021AbuDhabiGrandPrix-Map.png")
plt.show()



# Telemetry Data - Source: https://medium.com/towards-formula-1-analysis/how-to-analyze-formula-1-telemetry-in-2022-a-python-tutorial-309ced4b8992
# Reloading each session for use to ensure no issues with cacheing the information for repeated use or for potention issues with the Pandas Dataframe
session2 = ff1.get_session(2021, 22, 5)
session2.load()
# Storing the information
driver_1, driver_2 = 'VER', 'HAM' # Selecting only Verstappen and Hamilton
laps_driver_1 = session2.laps.pick_driver(driver_1)
laps_driver_2 = session2.laps.pick_driver(driver_2)
# Selects the fastest lap for both drivers
fastest_driver_1 = laps_driver_1.pick_fastest()
fastest_driver_2 = laps_driver_2.pick_fastest()
# Adding distance as the x-axis in the plot
telemetry_driver_1 = fastest_driver_1.get_telemetry().add_distance()
telemetry_driver_2 = fastest_driver_2.get_telemetry().add_distance()
# Storing the team name for coloring purposes
team_driver_1 = fastest_driver_1['Team']
team_driver_2 = fastest_driver_2['Team']
# Estimation of delta between the two drivers (real delta time is not available publicly)
delta_time, ref_tel, compare_tel = utils.delta_time(fastest_driver_1, fastest_driver_2)

# Plotting the information
plot_title = "2021 Abu Dhabi Grand Prix - VER vs HAM Telemetry"
plot_ratios = [1, 3, 2, 1, 1, 2]
plt.rcParams['figure.figsize'] = [15, 15] # Increasing size of plot to be readable
# Creating subplots of different sizes
fig, ax = plt.subplots(6, gridspec_kw={'height_ratios': plot_ratios})
# Title
ax[0].title.set_text(plot_title)
# Delta Plot
ax[0].plot(ref_tel['Distance'], delta_time)
ax[0].axhline(0)
ax[0].set(ylabel=f"Gap to {driver_2} (s)")
# Speed Plot
ax[1].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Speed'], label=driver_1, color=ff1.plotting.team_color(team_driver_1))
ax[1].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Speed'], label=driver_2, color=ff1.plotting.team_color(team_driver_2))
ax[1].set(ylabel='Speed')
ax[1].legend(loc="lower right")
# Throttle Plot
ax[2].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Throttle'], label=driver_1, color=ff1.plotting.team_color(team_driver_1))
ax[2].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Throttle'], label=driver_2, color=ff1.plotting.team_color(team_driver_2))
ax[2].set(ylabel='Throttle')
# Brake Plot
ax[3].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Brake'], label=driver_1, color=ff1.plotting.team_color(team_driver_1))
ax[3].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Brake'], label=driver_2, color=ff1.plotting.team_color(team_driver_2))
ax[3].set(ylabel='Brake')
# Gear Plot
ax[4].plot(telemetry_driver_1['Distance'], telemetry_driver_1['nGear'], label=driver_1, color=ff1.plotting.team_color(team_driver_1))
ax[4].plot(telemetry_driver_2['Distance'], telemetry_driver_2['nGear'], label=driver_2, color=ff1.plotting.team_color(team_driver_2))
ax[4].set(ylabel='Gear')
# RPM Plot
ax[5].plot(telemetry_driver_1['Distance'], telemetry_driver_1['RPM'], label=driver_1, color=ff1.plotting.team_color(team_driver_1))
ax[5].plot(telemetry_driver_2['Distance'], telemetry_driver_2['RPM'], label=driver_2, color=ff1.plotting.team_color(team_driver_2))
ax[5].set(ylabel='RPM')

# Hiding labels on the subplots
for a in ax.flat:
    a.label_outer()

# Saving the plot
plot_filename = plot_title.replace(" ", "") + ".png" # Removing spacing to save as a png
plt.savefig(plot_filename, dpi=300)
plt.show()

# -----
# Tire/Pit Stop Strategy - Source: https://docs.fastf1.dev/examples_gallery/plot_strategy.html#sphx-glr-examples-gallery-plot-strategy-py
# -----
# Obtaining pit stop information
session3 = fastf1.get_session(2021, 22, 5)
session3.load()
laps = session3.laps
drivers = session3.drivers
drivers = [session3.get_driver(driver)["Abbreviation"] for driver in drivers] # Convert numbers to abreviations for the plot
# Groups the laps, stint number, and tire compound to then count the number of laps in each grouping
stints = laps[["Driver", "Stint", "Compound", "LapNumber"]]
stints = stints.groupby(["Driver", "Stint", "Compound"])
stints = stints.count().reset_index()
stints = stints.rename(columns={"LapNumber": "StintLength"})
# print(drivers) for debugging list of drivers
# print(stints) for debugging the stint table

# Plotting the pit stop information
fig, ax = plt.subplots(figsize=(5, 10))
for driver in drivers:
    driver_stints = stints.loc[stints["Driver"] == driver]
    previous_stint_end = 0
    for idx, row in driver_stints.iterrows():
        # Compound name used for coloring and stint length used for width of bars
        plt.barh(y=driver, width=row["StintLength"], left=previous_stint_end, color=fastf1.plotting.COMPOUND_COLORS[row["Compound"]], edgecolor="black", fill=True)
        previous_stint_end += row["StintLength"]

plot_title2 = "2021 Abu Dhabi Grand Prix - Tire Strategies"
plt.title(plot_title2)
plt.xlabel("Lap Number")
plt.grid(False)
# Inverting the y-axis to show drivers in order of finishing
ax.invert_yaxis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
plt.tight_layout()
# Save to file
plot_filename2 = plot_title2.replace(" ", "") + ".png" # Removing spacing to save as a png
plt.savefig(plot_filename2, dpi=300)
plt.show()

# ------
# Driver Laptime Distribution - Source: https://docs.fastf1.dev/examples_gallery/plot_laptimes_distribution.html#sphx-glr-examples-gallery-plot-laptimes-distribution-py
# ------
# Calculating the laptime distribution
session4 = fastf1.get_session(2021, 22, 5)
session4.load()
point_finishers = session4.drivers[:2] # Only the top two point finishers, being VER and HAM
driver_laps = session4.laps.pick_drivers(point_finishers).pick_quicklaps()
driver_laps = driver_laps.reset_index()
finishing_order = [session4.get_driver(i)["Abbreviation"] for i in point_finishers]
driver_colors = {abv: fastf1.plotting.DRIVER_COLORS[driver] for abv, driver in fastf1.plotting.DRIVER_TRANSLATE.items()}

# Plotting the lapttime distribution
fig, ax = plt.subplots(figsize=(10, 5))
# Seaborn does not have Pandas timedelta support
# Must convert timedelta to float
driver_laps["LapTime(s)"] = driver_laps["LapTime"].dt.total_seconds()
sns.violinplot(data=driver_laps, x="Driver", y="LapTime(s)", inner=None, scale="area", order=finishing_order, palette=driver_colors)
sns.swarmplot(data=driver_laps, x="Driver", y="LapTime(s)", order=finishing_order, hue="Compound", palette=fastf1.plotting.COMPOUND_COLORS, hue_order=["SOFT", "MEDIUM", "HARD"], linewidth=0, size=5,)
ax.set_xlabel("Driver")
ax.set_ylabel("Lap Time (s)")
plot_title3 = "2021 Abu Dhabi Grand Prix - Lap Time Distribution"
plt.suptitle(plot_title3)
sns.despine(left=True, bottom=True)
plt.tight_layout()

# Save to file
plot_filename3 = plot_title3.replace(" ", "") + ".png" # Removing spacing to save as a png
plt.savefig(plot_filename3, dpi=300)
plt.show()

# -----
# Speed Traces Against One Another - Source: https://docs.fastf1.dev/examples_gallery/plot_speed_traces.html#sphx-glr-examples-gallery-plot-speed-traces-py
# -----
fastf1.plotting.setup_mpl(misc_mpl_mods=False) # Enable matblotlib patch for plotting timedelta values and load
# Obtain the speed traces
session5 = fastf1.get_session(2021, 22, 5)
session5.load()
ver_lap = session5.laps.pick_driver('VER').pick_fastest()
ham_lap = session5.laps.pick_driver('HAM').pick_fastest()
ver_tel = ver_lap.get_car_data().add_distance()
ham_tel = ham_lap.get_car_data().add_distance()
rbr_color = fastf1.plotting.team_color('RBR')
mer_color = fastf1.plotting.team_color('MER')
# Plotting the speed traces
fig, ax = plt.subplots()
ax.plot(ver_tel['Distance'], ver_tel['Speed'], color=rbr_color, label='VER')
ax.plot(ham_tel['Distance'], ham_tel['Speed'], color=mer_color, label='HAM')
ax.set_xlabel('Distance in m')
ax.set_ylabel('Speed in km/h')
ax.legend()
plot_title4 = "2021 Abu Dhabi Grand Prix - VER vs HAM Fastest Lap"
plt.suptitle(plot_title4)

# Save to file
plot_filename4 = plot_title4.replace(" ", "") + ".png" # Removing spacing to save as a png
plt.savefig(plot_filename4, dpi=300)
plt.show()