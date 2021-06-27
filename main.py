from tkinter import *
from tkinter import ttk
import tweepy
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from pandas import DataFrame
import tkinter as tk
from tkinter.filedialog import asksaveasfile

consumer_key = "Ut5tsE9sIeXoT7PA7FbvyLX6h"
consumer_secret = "4jlV39gBav73fLGgCruOTFhEK0HmHZL0TNNQBsipcQhZ4Lwivv"
access_key = "1404113094373122049-pm11zKMnQEboQAXEEWOOTwaoyCpeLh"
access_secret = "BzE1ic9FUnHi0Jh1Uwg1yngUHp7poNMhMWG9MDy3HLyAc"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

ws = Tk()
ws.title("Twitter Data Analysis")
ws.geometry('400x600') #width x length
ws['bg'] = '#ffbf00'


def printValue():
    global a
    global minLikes
    global maxLikes
    global minRetweet
    global maxRetweet
    global minDate
    global maxDate

    pname = player_name.get()
    min1 = min_likes.get()
    max2 = max_likes.get()
    min3 = min_retweet.get()
    max4 = max_retweet.get()
    min5 = min_Date.get()
    max6 = max_Date.get()

    Label(ws, text=f'{pname}, Registered!', pady=20, bg='#ffbf00').pack()
    a = pname
    minLikes = int(min1)
    maxLikes = int(max2)
    minRetweet = int(min3)
    maxRetweet = int(max4)
    minDate = min5
    maxDate = max6

tk.Label(ws, text="Twitter Username:").pack()
player_name = Entry(ws)
player_name.pack(pady=5)

tk.Label(ws, text="Min Likes:").pack()
min_likes = Entry(ws)
min_likes.pack(pady=5)

tk.Label(ws, text="Max Likes:").pack()
max_likes = Entry(ws)
max_likes.pack(pady=5)

tk.Label(ws, text="Min Retweet: ").pack()
min_retweet = Entry(ws)
min_retweet.pack(pady=5)

tk.Label(ws, text="Max Retweet: ").pack()
max_retweet = Entry(ws)
max_retweet.pack(pady=5)

tk.Label(ws, text="Min Date (yyyymmdd): ").pack()
min_Date = Entry(ws)
min_Date.pack(pady=5)

tk.Label(ws, text="Max Date (yyyymmdd): ").pack()
max_Date = Entry(ws)
max_Date.pack(pady=5)

Button(
    ws,
    text="Submit", 
    padx=15, 
    pady=5,
    command=printValue
    ).pack()

Label(ws, text=("\n"), pady=15, justify=LEFT, bg = '#ffbf00').pack()

def graph_data():
    twitter_tweets = api.user_timeline(screen_name= a, 
                            count=20,
                            include_rts = False,
                            tweet_mode = 'extended'
                            )

    tweets_all_time = []
    tweets_all_time.extend(twitter_tweets)
    oldest_id = twitter_tweets[-1].id

    while True:
        twitter_tweets = api.user_timeline(screen_name= a, 
                                # 200 is the maximum allowed count
                                count=200,
                                include_rts = False,
                                max_id = oldest_id - 1,
                                # Necessary to keep full_text 
                                # otherwise only the first 140 words are extracted
                                tweet_mode = 'extended'
                                )
        if len(twitter_tweets) == 0:
            break
        oldest_id = twitter_tweets[-1].id
        tweets_all_time.extend(twitter_tweets)

    
    outtweets = [[tweet.id_str, 
                #datetime.datetime.strptime(tweet.created_at, '%Y-%m-%d %H:%M:%S'),
                tweet.created_at,
                tweet.favorite_count, 
                tweet.retweet_count, 
                tweet.full_text.encode("utf-8").decode("utf-8")] 
                for idx,tweet in enumerate(tweets_all_time)]
    df = DataFrame(outtweets,columns=["id","date_made","likes","retweets", "text"])
    df.to_csv('%s_tweets.csv' % a,index=False)
    df.head(-1)
    df.nlargest(4,["likes"])
    df.min(0,["likes"])
    df["likes"].min()

    ylabels = ["likes","retweets"]

    fig = plt.figure(figsize=(13,3))
    fig.subplots_adjust(hspace=0.01,wspace=0.01)

    n_row = len(ylabels)
    n_col = 1
    for count, ylabel in enumerate(ylabels):
        ax = fig.add_subplot(n_row,n_col,count+1)
        ax.plot(df["date_made"],df[ylabel])
        ax.set_ylabel(ylabel)
    plt.show()

my_button = Button(ws, text="Graph (Likes & Retweets)!", padx=10, command=graph_data)
my_button.pack()
    
def min_and_max():
    twitter_tweets = api.user_timeline(screen_name= a, 
                            count=20,
                            include_rts = False,
                            tweet_mode = 'extended'
                            )

    tweets_all_time = []
    tweets_all_time.extend(twitter_tweets)
    oldest_id = twitter_tweets[-1].id

    while True:
        twitter_tweets = api.user_timeline(screen_name= a, 
                                # 200 is the maximum allowed count
                                count=200,
                                include_rts = False,
                                max_id = oldest_id - 1,
                                # Necessary to keep full_text 
                                # otherwise only the first 140 words are extracted
                                tweet_mode = 'extended'
                                )
        if len(twitter_tweets) == 0:
            break
        oldest_id = twitter_tweets[-1].id
        tweets_all_time.extend(twitter_tweets)

    
    outtweets = [[tweet.id_str, 
                #datetime.datetime.strptime(tweet.created_at, '%Y-%m-%d %H:%M:%S'),
                tweet.created_at,
                tweet.favorite_count, 
                tweet.retweet_count, 
                tweet.full_text.encode("utf-8").decode("utf-8")] 
                for idx,tweet in enumerate(tweets_all_time)]
    df = DataFrame(outtweets,columns=["id","date_made","likes","retweets", "text"])
    df.to_csv('%s_tweets.csv' % a,index=False)
    df.head(-1)
    df.nlargest(4,["likes"])
    df.min(0,["likes"])
    df["likes"].min()

    ylabels = ["likes","retweets"]

    fig = plt.figure(figsize=(13,3))
    fig.subplots_adjust(hspace=0.01,wspace=0.01)

    n_row = len(ylabels)
    n_col = 1

    
    df_sub = df.loc[(df["likes"] < maxLikes ) & (df["likes"] > minLikes ),:]

    ms = Tk()

    ms.title("Sorted Likes")
    ms.geometry("1555x790")

    main_frame = Frame(ms)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    for irow in range(df_sub.shape[0]):
        df_row = df_sub.iloc[irow,:]
        Label(second_frame, text=(df_row["date_made"]), pady=15, justify=LEFT).pack()
        Label(second_frame, text=("likes={:6}".format(df_row["likes"])), pady=15, justify=LEFT).pack()
        Label(second_frame, text=(df_row["text"]), pady=15, justify=LEFT).pack()
        Label(second_frame, text=("---------------------------------------------------------------------------------------"), pady=15, justify=LEFT).pack()

def min_and_max1():
    twitter_tweets = api.user_timeline(screen_name= a, 
                            count=20,
                            include_rts = False,
                            tweet_mode = 'extended'
                            )

    tweets_all_time = []
    tweets_all_time.extend(twitter_tweets)
    oldest_id = twitter_tweets[-1].id

    while True:
        twitter_tweets = api.user_timeline(screen_name= a, 
                                # 200 is the maximum allowed count
                                count=200,
                                include_rts = False,
                                max_id = oldest_id - 1,
                                # Necessary to keep full_text 
                                # otherwise only the first 140 words are extracted
                                tweet_mode = 'extended'
                                )
        if len(twitter_tweets) == 0:
            break
        oldest_id = twitter_tweets[-1].id
        tweets_all_time.extend(twitter_tweets)

    
    outtweets = [[tweet.id_str, 
                #datetime.datetime.strptime(tweet.created_at, '%Y-%m-%d %H:%M:%S'),
                tweet.created_at,
                tweet.favorite_count, 
                tweet.retweet_count, 
                tweet.full_text.encode("utf-8").decode("utf-8")] 
                for idx,tweet in enumerate(tweets_all_time)]
    df = DataFrame(outtweets,columns=["id","date_made","likes","retweets", "text"])
    df.to_csv('%s_tweets.csv' % a,index=False)
    df.head(-1)
    df.nlargest(4,["likes"])
    df.min(0,["likes"])
    df["likes"].min()

    ylabels = ["likes","retweets"]

    fig = plt.figure(figsize=(13,3))
    fig.subplots_adjust(hspace=0.01,wspace=0.01)

    n_row = len(ylabels)
    n_col = 1

    
    df_sub = df.loc[(df["retweets"] < maxRetweet) & (df["retweets"] > minRetweet),:]

    mk = Tk()

    mk.title("Sorted Retweets")
    mk.geometry("1555x790")

    main_frame = Frame(mk)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")


    for irow in range(df_sub.shape[0]):
        df_row = df_sub.iloc[irow,:]
        Label(second_frame, text=(df_row["date_made"]), pady=15, justify=LEFT).pack()
        Label(second_frame, text=("retweets={:6}".format(df_row["retweets"])), justify=LEFT).pack()
        Label(second_frame, text=(df_row["text"]), pady = 15, justify=LEFT).pack()
        Label(second_frame, text=("---------------------------------------------------------------------------------------"), pady=15, justify=LEFT).pack()

def min_and_max2():
    twitter_tweets = api.user_timeline(screen_name= a, 
                            count=20,
                            include_rts = False,
                            tweet_mode = 'extended'
                            )

    tweets_all_time = []
    tweets_all_time.extend(twitter_tweets)
    oldest_id = twitter_tweets[-1].id

    while True:
        twitter_tweets = api.user_timeline(screen_name= a, 
                                # 200 is the maximum allowed count
                                count=200,
                                include_rts = False,
                                max_id = oldest_id - 1,
                                # Necessary to keep full_text 
                                # otherwise only the first 140 words are extracted
                                tweet_mode = 'extended'
                                )
        if len(twitter_tweets) == 0:
            break
        oldest_id = twitter_tweets[-1].id
        tweets_all_time.extend(twitter_tweets)

    
    outtweets = [[tweet.id_str, 
                #datetime.datetime.strptime(tweet.created_at, '%Y-%m-%d %H:%M:%S'),
                tweet.created_at,
                tweet.favorite_count, 
                tweet.retweet_count, 
                tweet.full_text.encode("utf-8").decode("utf-8")] 
                for idx,tweet in enumerate(tweets_all_time)]
    df = DataFrame(outtweets,columns=["id","date_made","likes","retweets", "text"])
    df.to_csv('%s_tweets.csv' % a,index=False)
    df.head(-1)
    df.nlargest(4,["likes"])
    df.min(0,["likes"])
    df["likes"].min()

    ylabels = ["likes","retweets"]

    fig = plt.figure(figsize=(13,3))
    fig.subplots_adjust(hspace=0.01,wspace=0.01)

    n_row = len(ylabels)
    n_col = 1
 
    ab = Tk()

    ab.title("Sorted Date")
    ab.geometry("1555x790")

    main_frame = Frame(ab)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    max_Date1 = datetime.datetime(int(maxDate[0:4]),int(maxDate[4:6]),int(maxDate[6:8]))
    min_Date1 = datetime.datetime(int(minDate[0:4]),int(minDate[4:6]),int(minDate[6:8]))

    df_sub = df.loc[(df["date_made"] < max_Date1) & (df["date_made"] > min_Date1),:]

    for irow in range(df_sub.shape[0]):
        df_row = df_sub.iloc[irow,:]

        Label(second_frame, text=(df_row["date_made"]), pady=15, justify=LEFT).pack()
        Label(second_frame, text=("likes={:6} retweets={:6}".format(df_row["likes"],df_row["retweets"])), pady=15, justify=LEFT).pack()
        Label(second_frame, text=(df_row["text"]), pady=15, justify=LEFT).pack()
        Label(second_frame, text=("---------------------------------------------------------------------------------------"), pady=15, justify=LEFT).pack()

def getSheet():
    twitter_tweets = api.user_timeline(screen_name= a, 
                            count=20,
                            include_rts = False,
                            tweet_mode = 'extended'
                            )

    tweets_all_time = []
    tweets_all_time.extend(twitter_tweets)
    oldest_id = twitter_tweets[-1].id

    while True:
        twitter_tweets = api.user_timeline(screen_name= a, 
                                # 200 is the maximum allowed count
                                count=200,
                                include_rts = False,
                                max_id = oldest_id - 1,
                                # Necessary to keep full_text 
                                # otherwise only the first 140 words are extracted
                                tweet_mode = 'extended'
                                )
        if len(twitter_tweets) == 0:
            break
        oldest_id = twitter_tweets[-1].id
        tweets_all_time.extend(twitter_tweets)

    
    outtweets = [[tweet.id_str, 
                #datetime.datetime.strptime(tweet.created_at, '%Y-%m-%d %H:%M:%S'),
                tweet.created_at,
                tweet.favorite_count, 
                tweet.retweet_count, 
                tweet.full_text.encode("utf-8").decode("utf-8")] 
                for idx,tweet in enumerate(tweets_all_time)]
    df = DataFrame(outtweets,columns=["id","date_made","likes","retweets", "text"])
    df.to_csv('%s_tweets.csv' % a,index=False)
    df.head(-1)
    df.nlargest(4,["likes"])
    df.min(0,["likes"])
    df["likes"].min()

    ylabels = ["likes","retweets"]

    fig = plt.figure(figsize=(13,3))
    fig.subplots_adjust(hspace=0.01,wspace=0.01)

    n_row = len(ylabels)
    n_col = 1

    outtweets = [[tweet.id_str, 
              #datetime.datetime.strptime(tweet.created_at, '%Y-%m-%d %H:%M:%S'),
              tweet.created_at,
              tweet.favorite_count, 
              tweet.retweet_count, 
              tweet.full_text.encode("utf-8").decode("utf-8")] 
             for idx,tweet in enumerate(tweets_all_time)]
    df = DataFrame(outtweets,columns=["id","date_made","likes","retweets", "text"])
    df.to_csv('%s_tweets.csv' % a,index=False)
    df.head(-1)

button1 = Button(ws, text="Find Tweets (Likes)!", padx = 10, command=min_and_max)
button1.pack()

button2 = Button(ws, text="Find Tweets (Retweets)!", padx = 10, command=min_and_max1)
button2.pack()

button3 = Button(ws, text="Find Tweets (Date)!", padx = 10, command=min_and_max2)
button3.pack()

button4 = Button(ws, text="Save Tweets (CSV)", padx = 10, command=getSheet)
button4.pack()

ws.mainloop()