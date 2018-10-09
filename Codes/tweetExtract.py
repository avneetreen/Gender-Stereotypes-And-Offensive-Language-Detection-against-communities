"""
  @Avneet Kaur
  Getting tweets containing specific keywords out of a twitter

"""

# -*- coding: utf-8 -*-
import tweepy
from tweepy import OAuthHandler
import csv
import HTMLParser

consumerKey = "uCsPigNph7jucTr0JIGRdvD7Z"
consumerSecret = "WLSkdDpXUcUYOeU2puk3Q1uQKidURMd18kjNMGKWIVasnXLx1A"
accessKey = "1017803951431979009-mYwKyFpi0wrETuT21t28gmHtdaGAKf"
accessSecret = "JSBlFd4fVPAK7VfzIOvtVxeAl4HrF9FjZ8hOKFT3qb9D9"

auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)

tweetObjects = []

#get tweets
def getTweets(auth,query,language,limit):
  global tweetObjects
  api = tweepy.API(auth)
  for tweet in tweepy.Cursor(api.search, q=query, lang=language).items(limit):
    tweetObjects.append(tweet)

#clean the tweets by removing html characters like "&lt; &amp;" from tweets
def cleanText(tweet):
  parser = HTMLParser.HTMLParser()
  tweet = parser.unescape(tweet) 
  tweet = tweet.encode('ascii', 'ignore')
  return tweet

#parse the tweet object to extract text and id
def parseJSON(tweetObjects):
  tweetsCleaned = []
  counter = 1
  for tweet in tweetObjects:
    tweet_id = tweet.id_str
    tweet_text = cleanText(tweet.text)
    tweetsCleaned.append([counter,tweet.id_str,tweet_text])
    counter+=1
  return tweetsCleaned

#write the cleaned tweets to csv file
def writeToCSV(tweets,filename):
  with open(filename, 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for tweet in tweets:
      wr.writerow([tweet[0]] + [tweet[1]] + [tweet[2]])

#read file to get query terms
def readQueryTerms(filename):
  with open(filename) as f:
    lines = f.readlines()
  return lines

if __name__ == "__main__":
  limit = 750
  language = "en"
  query = ""
  
  filename1=""
  filename2=""
  filename3=""
  
  #get query from file
  words = readQueryTerms(filename1) 
  words = [x.lower().strip() for x in words]
  query1 = (" OR ").join(words)
  
  hateWords = readQueryTerms(filename2) 
  hateWords = [x.lower().strip() for x in hateWords]
  query2 = (" OR ").join(hateWords)
  
  #newQuery = query2
  newQuery = "(" + query1 + ")" + " AND " + "(" + query2 + ")"
  #newQuery = query1
  print(newQuery)
 
  getTweets(auth,newQuery,language,limit)
  cleanedTweets = parseJSON(tweetObjects)
  writeToCSV(cleanedTweets,filename3)
