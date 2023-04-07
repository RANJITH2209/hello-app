#importing packages
import streamlit as st
#from IPython.display import HTML
import pandas as pd
import numpy as np
import time
import os
import enchant
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import re
import sys
import string
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import nltk
nltk.download('omw-1.4')
nltk.download('wordnet')
nltk.download('words')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import wordnet
from nltk import word_tokenize
from collections import Counter
from nltk.stem import PorterStemmer
ps = PorterStemmer()
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = stopwords.words("english")
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

import warnings
warnings.filterwarnings("ignore")


#CoreProcess

def my_dict():
    
    """ This function maps internet slang words and returns meaningful words """

# Creating our very own dictionary by collecting most used internet slang words through various resources

    dct = {
        'afaic': "as far as I'm concerned",
        'afaik': 'as far as I know',
        'afair': 'as far as I recall',
     'afk': 'away from keyboard',
     'asap': 'as soon as possible',
     'awsm': 'awesome',
     'abt': 'about',
     'bbl': 'be back later',
     'bbs': 'be back soon',
     'bfd': 'big fucking deal',
     'brb': 'be right back',
     'btw': 'by the way',
     'b2b': 'business to business',
     'bt': 'but',
     'c&v': 'chapter & verse',
     'cya': 'see you',
     'cu': 'see you',
     'cys': 'check your settings',
     'coz': 'because',
     'em': 'them',
     'faq': 'frequently asked question',
     'ffs': "for fuck's sake!",
     'foaf': 'friend of a friend',
     'fyi': 'for your information',
     'g2g': 'got to go',
     'gagf': 'go and get fucked',
     'gfy': 'good for you',
     'gg': 'good going',
     'gj': 'good job',
     "gr8" : "great",
     'hth': 'hope this helps',
     'hv': 'have',
     'hav': 'have',
     'ic': 'I see',
    'i' : 'I',
     'icydk': "in case you didn't know",
     'icydn': "in case you didn't know",
     'icudk': "in case you didn't know",
     'iirc': 'if I recall correctly',
     'imho': 'in my humble opinion',
     'imo': 'in my opinion',
     'imp': 'important',
     'irc': 'internet relay chat',
     'irl': 'in real life',
     'istr': 'I seem to recall',
     'iydmma': "if you don't mind me asking",
     'jj': 'just joking',
     'jk': 'just kidding',
     'jooc': 'just out of curiosity',
     'k': 'okay',
     'kk': 'okay',
     'kkk ': 'okay',
     'l8': 'late',
     'l8r': 'later',
     'liek': 'I like that website',
     'lmao': 'laughing my ass off',
     'lol': 'laughing out loud',
     'lv': 'love',
     'myob': 'mind your own business',
     'nm': 'never mind',
     'noyb': 'none of your business',
     'np': 'no problem',
     'nsfw': 'not safe for work',
     'nt': 'no text',
     'nyc': 'nice',
     'oic': 'oh, I see',
     'omg': 'Oh my God',
     'omfg': 'Oh my fucking God',
     'omfl': 'Oh my fucking lag',
     'ooc': 'out of curiosity',
     'ot': 'off topic',
     'otoh': 'on the other hand',
     'osm': 'awesome',
     'pfo': 'please fuck off',
     'pita': 'pain in the ass',
     'po': 'piss off',
     'prog': 'computer program',
     'prolly': 'probably',
     'plz': 'please',
     'pls': 'please',
     'p2p': 'person to person',
     'qoolz': 'cool',
     'que': 'question',
     'r': 'are',
     'rl': 'real life',
     'rofl': 'rolling on the floor laughing',
     'rotfl': 'rolling on the floor laughing',
     'roflmao': 'rolling on the floor laughing my ass off',
     'rotflmao': 'rolling on the floor laughing my ass off',
     'rtfa': 'read the fucking article',
     'rtfm': 'read the fucking manual',
     'ru': 'are you',
     'r8': 'right',
     'sfw': 'safe for work',
     'stfu': 'shut the fuck up',
     'sux0rs': 'sucks',
     'kthx': 'okay thanks',
     'plzkthx': 'please okay thanks',
     'kthxbye': 'okay thanks goodbye',
     'ttfn': 'ta ta for now',
     'tia': 'thanks in advance',
     'ttyl': 'talk to you later',
     'tbh': 'to be honest',
     'thankx': 'thanks',
     'thx': 'thanks',
     'thanku': 'thank you',
     'thanq': 'thank you',
     'tnx': 'thanks',
        'tx': 'thanks',
     'tnq': 'thank you',
     'ty': 'thank you',
     'u': 'you',
     'ur': 'your',
     'vs': 'versus',
     'w/e': 'whatever',
     'w/o': 'without',
     'wduwta': 'what do u wanna talk about?',
     'wtf': 'what the fuck?',
     'ymmv': 'your mileage may vary ',
     'yu': 'you',
     'w8': 'wait',
     '<3': 'love',
     '2b': 'to be',
     "ain't": 'am not',
     "aren't": 'are not',
     "can't": 'cannot',
     "can't've": 'cannot have',
     "could've": 'could have',
     "couldn't": 'could not',
     "couldn't've": 'could not have',
     "didn't": 'did not',
     "doesn't": 'does not',
     "don't": 'do not',
     "hadn't": 'had not',
     "hadn't've": 'had not have',
     "hasn't": 'has not',
     "haven't": 'have not',
     "he'd": 'he would',
     "he'd've": 'he would have',
     "he'll": 'he will',
     "he'll've": 'he will have',
     "he's": 'he is',
     "how'd": 'how did',
     "how'd'y": 'how do you',
     "how'll": 'how will',
     "how's": 'how is',
     "I'd": 'I would',
     "I'd've": 'I would have',
     "I'll": 'I will',
     "I'll've": 'I will have',
     "I'm": 'I am',
     "I've": 'I have',
     "isn't": 'is not',
     "it'd": 'it would',
     "it'd've": 'it would have',
     "it'll": 'it will',
     "it'll've": 'it will have',
     "it's": 'it is',
     "let's": 'let us',
     "ma'am": 'madam',
     "mayn't": 'may not',
     "might've": 'might have',
     "mightn't": 'might not',
     "mightn't've": 'might not have',
     "must've": 'must have',
     "mustn't": 'must not',
     "mustn't've": 'must not have',
     "needn't": 'need not',
     "needn't've": 'need not have',
     "o'clock": 'of the clock',
     "oughtn't": 'ought not',
     "oughtn't've": 'ought not have',
     "shan't": 'shall not',
     "sha'n't": 'shall not',
     "shan't've": 'shall not have',
     "she'd": 'she would',
     "she'd've": 'she would have',
     "she'll": 'she will',
     "she'll've": 'she will have',
     "she's": 'she is',
     "should've": 'should have',
     "shouldn't": 'should not',
     "shouldn't've": 'should not have',
     "so've": 'so have',
     "so's": 'so is',
     "that'd": 'that would',
     "that'd've": 'that would have',
     "that's": 'that is',
     "there'd": 'there would',
     "there'd've": 'there would have',
     "there's": 'there is',
     "that'll've": 'that will have',
     "they'd": 'they would',
     "they'd've": 'they would have',
     "they'll": 'they will',
     "they'll've": 'they will have',
     "they're": 'they are',
     "they've": 'they have',
     "to've": 'to have',
     "wasn't": 'was not',
     "we'd": 'we would',
     "we'd've": 'we would have',
     "we'll": 'we will',
     "we'll've": 'we will have',
     "we're": 'we are',
     "we've": 'we have',
     "weren't": 'were not',
     "what'll": 'what will',
     "what'll've": 'what will have',
     "what're": 'what are',
     "what's": 'what is',
     "what've": 'what have',
     "when's": 'when is',
     "when've": 'when have',
     "where'd": 'where did',
     "where's": 'where is',
     "where've": 'where have',
     "who'll": 'who will',
     "who'll've": 'who will have',
     "who's": 'who is',
     "who've": 'who have',
     "why's": 'why is',
     "why've": 'why have',
     "will've": 'will have',
     "won't": 'will not',
     "won't've": 'will not have',
     "would've": 'would have',
     "wouldn't": 'would not',
     "wouldn't've": 'would not have',
     "y'all": 'you all',
     "y'all'd": 'you all would',
     "y'all'd've": 'you all would have',
     "y'all're": 'you all are',
     "y'all've": 'you all have',
     "you'd": 'you would',
     "you'd've": 'you would have',
     "you'll": 'you will',
     "you'll've": 'you will have',
     "you're": 'you are',
     "you've": 'you have',
     'thankyou': 'thank you',
     'goodmorning': 'good morning',
     'goodnight': 'good night',
     'howareyou': 'how are you',
     'loveyou': 'love you',
     'iam': 'I am',
     'im': 'I am',
     "i'm": 'I am',
     'ill': 'I will',
     'dont': 'do not',
     'cant': 'can not',
     'shouldnt': 'should not',
     'couldnt': 'could not',
     'wouldnt': 'would not',
     'mustnt': 'must not',
     'didnt': 'did not',
     'wont': 'will not',
     'doesnt': 'does not',
     'hasnt': 'has not',
     'havent': 'have not',
     'shouldve': 'should have',
     'wouldve': 'would have',
     'couldve': 'could have',
     'mustve': 'must have',
     'mightve': 'might have',
     'wellrespect': 'well respect',
     'sir ji': 'Sir',
        "sirji" : "Sir",
     'siryou': 'Sir you',
        "ji" : "",                
     'mins': 'minutes',
     'soo': 'so',
     'heyy': 'hey',
     'datascience': 'data science',
     'tq': 'thank you',
     'tnxx': 'thanks',
     'plzz': 'please',
     'Pls': 'please',
     'luv': 'love',
     'thnks': 'thanks',
     'thanx': 'thanks',
     'vedio': 'video',
     '2morrow': 'tomorrow',
     '1minute': 'one minute',
     'eqn': 'equation',
     'dono': 'dont know',
     'youre': 'you are',
     'tysm': 'thank you so much',
     'thnkuu': 'thank you',
     'thakyou': 'thank you',
     'reallyy': 'really',
        'realy' : 'really',
     'youu': 'you',
     'vid': 'video',
     'vdo': 'video',
     'lov': 'love',
     'fav': 'favourite',
     'g8': 'great',
     'wrt': 'with respect to',
     'ppl': 'people',
     'thks': 'thanks',
     'owsome': 'awesome',
     'nuthin': 'nothing',
     'omgg': 'omg',
     'ppt': 'power point',
     'borring': 'boring',
     'diz': 'this',
     'knw': 'know',
     'grt': 'great',
     'awsome': 'awesome',
     'theyd': 'they would',
     'bcz': 'because',
     'mucch': 'much',
        "ive": "I have",
        "ss": "yes",
        "nys": "nice",
        "bcoz" : "because",
        "ok" : "okay",
        "awesom": "awesome",
        "idk": "I don't know",
        "hrs" : "hours",
        "lec" : "lecture",
        "horray" : "hurrah",
        "thku" : "thank you",
        "vdeo" : "video",
        "vedio" : "video",
        "tanks" : "thanks",
        "makin" : "making",
        "thnx" : "thanks",
        "thank's" : "thanks",
        "thankeu" : "thank you",
        "tku" : "thank you",
        "thnkeuu" : "thank you",
        "tqs" : "thanks",
        "sar" : "Sir",
        "thnkeww" : "thank you",
        "bruh" : "bro",
        "thk" : "thank",
        "thats" : "that is",
        "osum" : "awesome",
        "ryt" : "right",
        "havnt" : "have not",
        "vids" : "videos",
        "thnk" : "thank",
        "thnq" : "thank you",
        "thnku" : "thank you", 
        "gud" : "good",
        "tc" : "take care",
        "thnkful" : "thankful",
        "frnd" : "friend",
        "tym" : "time",
        "xam" : "exam",
        "thnkew" : "thank you",
        "hlo" : "hello",
        "thnkiu" : "thank you",
        "coz" : "because",
        "thnkyu" : "thank you",
        "thankiu" : "thank you",
        "bst" : "best",
        "osam" : "awesome",
        "cuz" : "because",
        "pl" : "please",
    }
    
    import contractions
    
    dct.update(contractions.contractions_dict)
    # Creating an empty dictionary to store upper case slang words ('TY':'THANK YOU')
    
    dct = {key.lower():value for key,value in dct.items()}
    
    DCT = {}
    for i in dct:
        DCT[i.upper()] = dct[i].upper()
    
    # Creating an empty dictionary to store capital letter start slang words ('Ty':'Thank you')
    
    Dct = {}
    for i in dct:
        Dct[i.capitalize()] = dct[i].capitalize()
        
    # Updating everything (lower case, upper case, Capital start) inside the above dictionary dct    
    dct.update(DCT)
    dct.update(Dct)
    
    return dct
def get_playlist_comments(api_key, search_query,no_of_playlist):


    '''
    This function collects comments of all the videos of specified number of playlists. Youtube API needs to be 
    created in Google cloud platform before. It ignore all the independent videos.

    '''


    # Set up the YouTube Data API client
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/credentials.json"
    api_service_name = "youtube"
    api_version = "v3"
    youtube = build(api_service_name, api_version, developerKey=api_key)


    # Search for playlists using the search query
    search_response = youtube.search().list(
        q=search_query,
        type="playlist",
        part="id",
        maxResults=no_of_playlist
    ).execute()



    # Retrieve the playlist IDs from the search results
    playlist_ids = [result["id"]["playlistId"] for result in search_response["items"]]
    count = 1
    while count < np.ceil(no_of_playlist/50):
        count += 1
        if "nextPageToken" in search_response:
            search_response = youtube.search().list(
            q=search_query,
            type="playlist",
            part="id",
            pageToken = search_response['nextPageToken'],
            maxResults=50
            ).execute()
            playlist_ids = playlist_ids + [result["id"]["playlistId"] for result in search_response["items"]]


    # Retrieve all comments for all videos in each playlist
    comments = []
    for playlist_id in playlist_ids:
        playlist_link = f"https://www.youtube.com/playlist?list={playlist_id}"
        playlist_items_response = youtube.playlistItems().list(
            playlistId=playlist_id,
            part="snippet",
            maxResults=50 # maximum number of results per request
        ).execute()

        video_ids = [item["snippet"]["resourceId"]["videoId"] for item in playlist_items_response["items"]]

        for video_id in video_ids:
            try:
                # Retrieve the video title and link
                video_response = youtube.videos().list(
                    id=video_id,
                    part='snippet'
                ).execute()

                video_title = video_response['items'][0]['snippet']['title']
                video_link = f'https://www.youtube.com/watch?v={video_id}'
                Channel_id = video_response["items"][0]["snippet"]["channelId"]

                # Retrieve the comments for the video
                results = youtube.commentThreads().list(
                    part='snippet',
                    videoId=video_id,
                    textFormat='plainText',
                    maxResults=100 #the max value of comments it can take
                    ).execute()

                while results:
                    for item in results['items']:
                        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                        author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
                        author_id = item['snippet']['topLevelComment']['snippet']['authorChannelId']['value']
                        comments.append({
                            "topic" : topic,
                            "Unique_Column" : playlist_link,
                            "playlist_id" : playlist_id,
                            "channel_id":Channel_id,
                            "video_id":video_id,
                            'video_link': video_link,
                            'video_title': video_title,
                            'username': author,
                            'user_id': author_id,
                            'Comment': comment
                        })

                    if 'nextPageToken' in results:
                        results = youtube.commentThreads().list(
                            part='snippet',
                            videoId=video_id,
                            textFormat='plainText',
                            pageToken=results['nextPageToken'],
                            maxResults=100
                            ).execute()
                    else:
                        break
            except:
                continue
    # Convert the data into a Pandas DataFrame
    comments_df1 = pd.DataFrame(comments)

    # Return the DataFrame
    return comments_df1


def extract_comments(api_key, search_keyword,no_of_videos):



    '''
    This function collects comments of specified number of videos it ignores all the playlists. 
    Youtube API needs to be created in Google cloud platform before. 

    '''


    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = []
    search_response = youtube.search().list(
        q=search_keyword,
        type='video',
        part='id',
        maxResults=no_of_videos
    ).execute()
    video_ids = [item['id']['videoId'] for item in search_response['items']]
    count = 1
    while count < np.ceil(no_of_videos/50):
        count += 1
        if "nextPageToken" in search_response:
            search_response = youtube.search().list(
            q=search_keyword,
            type='video',
            part='id,snippet',
            pageToken = search_response['nextPageToken'],
            maxResults=50
            ).execute()
            video_ids = video_ids +  [item['id']['videoId'] for item in search_response['items']]

    for video_id in video_ids:
        try:
            # Retrieve the video title and link
            video_response = youtube.videos().list(
                id=video_id,
                part='snippet'
            ).execute()

            video_title = video_response['items'][0]['snippet']['title']
            video_link = f'https://www.youtube.com/watch?v={video_id}'
            Channel_id = video_response["items"][0]["snippet"]["channelId"]

            # Retrieve the comments for the video
            results = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                textFormat='plainText',
                maxResults=100 #the max value of comments it can take
                ).execute()

            while results:
                for item in results['items']:
                    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                    author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
                    author_id = item['snippet']['topLevelComment']['snippet']['authorChannelId']['value']
                    comments.append({
                        "topic" : topic,
                        "Unique_Column" : video_link,
                        "playlist_id":"(Blank)",
                        "channel_id":Channel_id,
                        "video_id":video_id,
                        'video_link': video_link,
                        'video_title': video_title,
                        'username': author,
                        'user_id': author_id,
                        'Comment': comment
                    })

                if 'nextPageToken' in results:
                    results = youtube.commentThreads().list(
                        part='snippet',
                        videoId=video_id,
                        textFormat='plainText',
                        pageToken=results['nextPageToken'],
                        maxResults=100
                        ).execute()
                else:
                    break
        except:
            continue

    # Convert the comments to a Pandas DataFrame
    comments_df = pd.DataFrame(comments)
    return comments_df


def AllComments(api_key,search,no_of_playlist,no_of_videos):
    '''
    This function collects all the comments of both playlist and videos.
    '''
    playlists = get_playlist_comments(api_key=api_key, search_query = search,no_of_playlist = no_of_playlist)
    videos = extract_comments(api_key=api_key, search_keyword = search,no_of_videos = no_of_videos)
    
    Combined_comments = pd.concat([playlists,videos],ignore_index=True)

    return Combined_comments

st.set_page_config(layout="wide")
#st.title("Team 5")

st.markdown("<h1 style='font-family: cursive; text-align: center;'>Team Senti5</h1>", unsafe_allow_html=True)
st.markdown(
    "<h1 style='text-align: center;'><img src='https://icons.iconarchive.com/icons/dtafalonso/android-lollipop/512/Youtube-icon.png' height='50'/> Smart Youtube Results</h1>",
    unsafe_allow_html=True
)

#image='https://www.google.com/url?sa=i&url=https%3A%2F%2Fpngtree.com%2Ffreepng%2Fyoutube-icon_4199913.html&psig=AOvVaw1CnJvmEWh5KG0Vu_HUCl2I&ust=1680616000918000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCLiVydLsjf4CFQAAAAAdAAAAABAD'
#st.image(image)
#st.markdown("<h1 style='text-align: center; color: red;'>Smart Youtube Results</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: right; font-size: 20px;'> ~ From the students of Praxis Business School, Bangalore</h2>", unsafe_allow_html=True)

st.subheader("Search")
topic = st.text_input("")
if topic != "":
  st.markdown("Fetching results, Please wait...")

#num = int(st.text_input("No of Videos:"))
num=10
width = 350
height =200

if topic != "":
  all_comments = AllComments(api_key="AIzaSyAciD1h142q9IqAPyGg7l_2tx4eufDbZ1E",search = topic ,no_of_playlist=0,no_of_videos=num) #r API

sorted_results = pd.DataFrame()
sorted_results['YT_Order'] = all_comments[['Unique_Column','video_title']].drop_duplicates()['Unique_Column'].tolist()
sorted_results['YT_Title'] = all_comments[['Unique_Column','video_title']].drop_duplicates()['video_title'].tolist()

raw = all_comments

raw = raw[raw['channel_id'] != raw['user_id']]

raw.drop_duplicates(inplace=True)
raw.dropna(inplace=True)
raw.reset_index(inplace=True, drop=True)


# Define a function that removes URLs from a given string using regular expressions
def remove_urls(comment):
    """ Removes URLs from the given text using regular expressions """
    
    # Define a regular expression pattern to match URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    
    # Use the sub method of the regular expression object to replace URLs with an empty string
    result = url_pattern.sub('', comment)
    
    # Return the modified string with URLs removed
    return result


def remove_special_char(my_string):
    """This function takes comments and returns comments removing the words which are starting with @ and # i.e. user name"""
    
    # Split the input string into words and filter out words starting with "@" or "#"
    filtered_words = (word for word in my_string.split() if '@' not in word and not word.startswith('#'))
    
    # Join the filtered words back into a single string with a space delimiter
    result = " ".join(filtered_words)
    
    # Return the modified string
    return result


# Define a function that converts repetitive special characters in a given string
def convert_special_char(my_string):
    """This function takes comments and convert the repetitive special character into single character"""
    
    # Define a dictionary mapping of repetitive special characters to their single equivalents using regular expressions
    char_map = {r'\.+': '.', r'\ +': ' ', r'\,+': ',', r'\-': ' ', r'\_': ' '}
    
    # Iterate through the dictionary and use regular expressions to replace repetitive special characters with their single equivalents
    for before, after in char_map.items():
        my_string = re.sub(before, after, my_string)
        
    # Return the modified string with repetitive special characters replaced
    return my_string.strip()


ascii_list  = set([65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,78, 79, 80, 81, 82, 83,
                   84, 85, 86, 87, 88, 89, 90,97, 98, 99, 100, 101, 102, 103,104, 105, 106,
                   107, 108, 109, 110, 111, 112, 113, 114, 115, 116,117, 118, 119, 120, 121, 122])

# Define a function called ignore_emojipunc_new that takes in a single argument called comment
def ignore_emojipunc_new(comment):
    '''
    This function removes the emojis from the comments
    '''
    # Create an empty string called new_word to store the updated comment without emojis
    new_word = ''
    # Create an empty string called punc to store any punctuation found in the comment
    punc = ''
    # Iterate over each word in the comment by splitting it on whitespace
    for word in comment.split():
                                   # Iterate over each character in the word
        for i in word:
            # Check if the character is an ASCII character (i.e., not an emoji or non-ASCII character)
            if ord(i) in ascii_list:
                # If it is an ASCII character, add it to new_word
                new_word += i
            else:
                # If it is not an ASCII character, add it to punc
                punc += i
        # Add a whitespace after each word to separate them
        new_word += ' '
    # Return the updated comment without leading or trailing whitespace, along with any punctuation found
    return (new_word.strip(), punc)



dct = my_dict()

#os.chdir('/content/drive/MyDrive/Data')

def convert_slang(my_string):
    
    """ Converts slang words in the comment and returns meaningful words """
    
    # Creating an empty string
    string = ""
   
    # Looping through each word of the comments
    
    for i in [i for i in my_string.split()]:
        if i in dct:                             # to avoid cases like   'gr8', '<3' , etc
            wrd = i
            punc = ''
        else:
            wrd, punc = ignore_emojipunc_new(i)

        # Condition Checks if the word is in our dictionary if so it maps the words accordingly
        if wrd in dct:
            string += dct[wrd] + punc +' '  
        # if not present, then the word will remain as it is
        else:

            string += wrd  + punc + ' ' 
            
    # Returns stripped final string
    return (string.strip())


def shorten_continuous_letters(word):
    """This function will return the shortened words for the characters that are too repititive (more than 2)"""
    
    #finds the pattern of two or more occurance of a word
    pattern = re.compile(r'(\w)(\1{2,})')

    # Replace any sequence of characters that repeats more than 2 times with a shorter version
    #'sub() that performs the substitution operation. '
    #substitute the double that word
    shortened_word = pattern.sub(lambda x: x.group(1) * 2, word)
    return shortened_word


import enchant
d_us=enchant.Dict("en_US")
d_uk=enchant.Dict("en_UK")
d_in=enchant.Dict("en_IN")
nltk_dict = set([word.lower() for word in nltk.corpus.words.words()])

def isEnglish(word):  
    
    # this function will ignore the emoji's ,  puncs  and numbers. Empty string will be true
    new_word = ignore_emojipunc_new(word)[0]
    
#     if new_word.startswith("'"):
#         new_word = new_word[1:]
#     if new_word.endswith("'"):
#         new_word = new_word[:-1]

    if new_word == '':
        return True

    if d_us.check(new_word.lower()) or d_uk.check(new_word.lower()) or d_in.check(new_word.lower()) \
        or new_word.lower() in nltk_dict:
        return True
    else:
        return False
    

from nltk.corpus import wordnet
#nltk.download('omw-1.4')
#nltk.download('wordnet')

class RepeatReplacer(object):
    #initializes two variables
    def __init__(self):
        #finds pattern of two or more words repated
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        #Referencing to the three groups of pattern above
        self.repl = r'\1\2\3'
    def replace(self, word):
        '''
        This function converts the words with repeated unwanted letters into a proper word with meaning.
        
        '''
        #Returns the word if synsets(other form of the word with same meaning)
        if wordnet.synsets(word):
            return word
        #if not it replace repeated character of different groups into single instances
        #and check if its in synsets 
        #else return the modified word itself
        #it repeats until the all groups are substituted and checked.
        repl_word = self.repeat_regexp.sub(self.repl, word)
        if repl_word != word:
            return self.replace(repl_word)
        else:
            return repl_word
        
replacer = RepeatReplacer()


# !pip install wordfreq
from wordfreq import get_frequency_dict

#getting the word probability of this dictionary
word_prob = get_frequency_dict(lang='en', wordlist='large')

#------------
#it replace lower character to upper 
WORD_PROB = {}
for i in word_prob:
    WORD_PROB[i.upper()] = word_prob[i]

# Creating an empty dictionary to store capital letter start slang words ('Ty':'Thank you')

#capitalizing the words and then storing it in dict.
Word_prob = {}
for i in word_prob:
    Word_prob[i.capitalize()] = word_prob[i]

# Updating everything (lower case, upper case, Capital start) inside the above dictionary dct    
word_prob.update(WORD_PROB)
word_prob.update(Word_prob)
#------------


#finding the max length of the longest word
max_word_len = max(map(len, word_prob))  # 34

def viterbi_segment(text, debug=False):
    
    '''
    This function splits the combined words into words with proper meaning.
    
    '''
    
    #inintializing the variable
    #probs => prob of best segmentation
    #last => last position of the best segmentation
    probs, lasts = [1.0], [0]
    
    #iterates through each character of the text
    for i in range(1, len(text) + 1):
        #initialize the empty string
        new_probs = []
        #
        for j in range(max(0, i - max_word_len), i):
            substring = text[j:i]
            length_reward = np.exp(len(substring))
            freq = word_prob.get(substring, 0) * length_reward
            compounded_prob = probs[j] * freq
            new_probs.append((compounded_prob, j))
            
            if debug:
                print(f'[{j}:{i}] = "{text[lasts[j]:j]} & {substring}" = ({probs[j]:.8f} & {freq:.8f}) = {compounded_prob:.8f}')

        prob_k, k = max(new_probs)  # max of a touple is the max across the first elements, which is the max of the compounded probabilities
        probs.append(prob_k)
        lasts.append(k)

        if debug:
            print(f'i = {i}, prob_k = {prob_k:.8f}, k = {k}, ({text[k:i]})\n')


    # when text is a word that doesn't exist, the algorithm breaks it into individual letters.
    # in that case, return the original word instead
    if len(set(lasts)) == len(text):
        return text
    #initialize word
    words = []
    #calculate the len of the text
    k = len(text)
    #loop for len(text)
    while 0 < k:
        #substring the word
        word = text[lasts[k]:k]
        #append it to the word list
        words.append(word)
        
        k = lasts[k]
    words.reverse()
    return ' '.join(words)


def split_message(message):
    ''' This use the viterbi_segment function, it applies to all the words and combines into a sentence '''  
    
    new_message = ' '.join(viterbi_segment(wordmash, debug=False) for wordmash in message.split())
    return new_message

def split_message_checker(word):
    '''
    Check if the split is a proper split else return the original word
    '''
    count = 0
    split_words_list = split_message(word).split()
    for split in split_words_list:
        #checks if the splitted word is in dictionary
        if (split in dct) or (isEnglish(split) == True):
            count += 1        
    #if all splitted words have meaning return splitted word
    #else return the original word
    if count == len(split_message(word).split()):
        return split_message(word)
    else :
        return word
    
def process_comment(comment):
    
    comment = remove_special_char(comment)         # Remove special characters from the comment
    comment = remove_urls(comment)                 # Remove URLs from the comment
    comment = convert_special_char(comment)        # Convert repetitive special characters into single characters in the comment
    comment = convert_slang(comment)               # Convert slang words in the comment
    
    word = comment.split()
    my_string = ' '.join([split_message_checker(replacer.replace(shorten_continuous_letters(ele))) if isEnglish(ele)==False else ele for ele in word  ])
    return convert_slang(my_string.strip())
    

raw['Comment'] = raw['Comment'].apply(process_comment)

raw.drop_duplicates(inplace=True)
raw.dropna(inplace=True)
raw.reset_index(inplace=True, drop=True)

print("Finished preprocessing the comments")

df = raw

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.reset_index(inplace=True, drop=True)


def calculate_the_words(comment):
    '''
    Function to calculate the number of words in a comment after ignoring emojis and punctuations
    '''
    # Call the function ignore_emojipunc_new to remove emojis and punctuations from the comment
    comment = ignore_emojipunc_new(comment)[0]

    # Split the comment by spaces and count the number of words
    return len(comment.split())


# Check % of English words presence

def calc_threshold(comment):             # Extract only the text from the comment and split it into words
    sent = ignore_emojipunc_new(comment)[0]
    sent = str(sent).split()    #[f(x) for x in sequence if condition]
    sum_sent = sum([True for word in sent if isEnglish(word)==True ])
    # If there are words in the comment, return the percentage of English words
    if len(sent) != 0:
        return (sum_sent / len(sent) * 100)
    # If there are no words in the comment, return -1
    return -1

df['length'] = df['Comment'].apply(calculate_the_words)
df['perc_English'] = df['Comment'].apply(calc_threshold)

for i in range(len(df)):
    if df.length[i] == 2 and df.perc_English[i] < 50:
        df.drop(i, axis=0, inplace=True)
    elif (df.length[i] == 3 and df.perc_English[i]<60):
        df.drop(i, axis=0, inplace=True)
    elif df.length[i]>=4 and df.perc_English[i]<75:
        df.drop(i, axis=0, inplace=True)
    else:
        pass
df.reset_index(inplace=True, drop=True)


# Reset the index
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.reset_index(inplace=True, drop=True)

print("Starting BERT Scoring...")


# Load the pre-trained sentiment analysis model
classifier = pipeline('sentiment-analysis', model='cardiffnlp/twitter-roberta-base-sentiment', device=0, batch_size=100,max_length=512, truncation=True)

# Load the DataFrame of sentences
# df = pd.read_csv('sentences.csv')

# Apply the pre-trained sentiment analysis model to the DataFrame of sentences using batching
results = []
for i in range(0, len(df), classifier.model.config.max_position_embeddings):
    batch = list(df['Comment'][i:i+classifier.model.config.max_position_embeddings])
    batch_results = classifier(batch)
    results.extend(batch_results)

# Extract the sentiment scores from the results
sentiment_scores = [result['score'] for result in results]
labels = [ int(result["label"][-1]) for result in results]
# Add the sentiment scores as a new column in the DataFrame

df["TwitterBertClass"] = labels
df['TwitterBertScore'] = sentiment_scores


df = df[df['TwitterBertClass']!=1]           #excluding neutral class
df.reset_index(inplace=True, drop=True)

# Define a function to count the number of adjectives and adverbs in a comment

def count_adj_adv(comment):
    tokenized_comment = word_tokenize(comment)  # Creating tokens from each comments
    pos_tagged_comment = nltk.pos_tag(tokenized_comment)  # Creating a POS tagger
    
    # Count the number of adjectives and adverbs present in each comment
    count = sum(1 for word, tag in pos_tagged_comment if tag.startswith('JJ') or tag.startswith('RB'))
    return count

# Apply the count_adj_adv function to each comment in the dataframe
df['adj_adv_count'] = df['Comment'].apply(count_adj_adv)

df['adj_adv_count']=np.where(df['adj_adv_count']>=5,5,df['adj_adv_count'])

# Utility score = Adj_adv count * %Englishwords + no.of words in comment
df['utility_score'] = ((df['adj_adv_count']+0.01) * (df['perc_English'] * 0.01))

df['TwitterBertScore'] = (df['TwitterBertScore'])*100 + df['utility_score']

df['TwitterBertClass'] = np.where(df['TwitterBertClass']==0, -1, 1)

df['TwitterBertScore'] = df['TwitterBertClass']* df['TwitterBertScore']


#-------------

df_grouped = df.groupby(['Unique_Column','video_title']).mean()



sorted_df = df_grouped.sort_values(by='TwitterBertScore', ascending=0)
sorted_df.reset_index(inplace=True)

comment_list = []
for i in range(0, len(sorted_df)):
    comment_list.append(len(df[df['Unique_Column']==sorted_df['Unique_Column'][i]]))
    
sorted_df['comments_count'] = comment_list

#------------------
new = pd.DataFrame()

new['Team5_Order'] = sorted_df['Unique_Column'].tolist()
new['title'] = sorted_df['video_title'].tolist()
new['comments_count'] = sorted_df['comments_count'].tolist()
new['BERTScore'] = sorted_df['TwitterBertScore']

new['norm_comments_count'] = new['comments_count'] * 100 / np.max(new['comments_count'])

#new['value_multiply'] = np.where(new['norm_comments_count']>=75, 3, np.where(new['norm_comments_count']>=50, 2.5, \
                                                                                                    # np.where(new['norm_comments_count']>=25, 2, 1)))
#new['new_score'] = new['value_multiply'] * new['BERTScore']
#new['new_score'] =( 0.4 * new['norm_comments_count'] ) + ( 0.6 * new['BERTScore'])

new['value_multiply'] = np.where(new['norm_comments_count']>=91, 3, np.where(new['norm_comments_count']>=81, 2.8, 
          np.where(new['norm_comments_count']>=71, 2.6, np.where(new['norm_comments_count']>=61, 2.4, 
          np.where(new['norm_comments_count']>=51, 2.2, np.where(new['norm_comments_count']>=41, 2, 
          np.where(new['norm_comments_count']>=31, 1.8, np.where(new['norm_comments_count']>=21, 1.6, 
          np.where(new['norm_comments_count']>=11, 1.4, 1.2)))))))))


new['new_score'] = new['value_multiply'] * new['BERTScore']

new_sorted = new.sort_values(by='new_score', ascending=0)
new_sorted.reset_index(inplace=True, drop=True)

sorted_results['Team5_Order'] = new_sorted['Team5_Order']
sorted_results['title'] = new_sorted['title']


#------------------
#sorted_results.to_csv(f"sorted_results_{topic}.csv", index=False)
#df.to_csv(f"poc_{topic}.csv", index=False)

def make_clickable(link):
    return f'<a href="{link}" target="_blank">{link}</a>'
#final_df = sorted_results.style.format({'YT_Order': make_clickable,'Team5_Order':make_clickable})


st.write("Results fetched")
col1, empty,col2 = st.columns(3)
col1.header("FrameWork 1")
col2.header("FrameWork 2")


for i in range(3):
  col2, empty,col1 = st.columns(3)


  youtube_vd_id2 =sorted_results["Team5_Order"][i][sorted_results["Team5_Order"][i].find("=")+1:] 
  html_code2 = f'<iframe width="{width}" height={height}" src="https://www.youtube.com/embed/{youtube_vd_id2}" frameborder="1" allowfullscreen></iframe>'

  col2.markdown(html_code2, unsafe_allow_html=True)
  col2.subheader(sorted_results["title"][i])

  
  youtube_vd_id1 =sorted_results["YT_Order"][i][sorted_results["YT_Order"][i].find("=")+1:] 
  html_code1 = f'<iframe width="{width}" height={height}" src="https://www.youtube.com/embed/{youtube_vd_id1}" frameborder="1" allowfullscreen></iframe>'
  col1.markdown(html_code1, unsafe_allow_html=True)
  col1.subheader(sorted_results["YT_Title"][i])
  
