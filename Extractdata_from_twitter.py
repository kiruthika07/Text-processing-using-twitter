from twitter import *
import csv

import sys
sys.path.append(".")
import config

twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))


results = twitter.trends.place(_id = 23424848)

print("Indian Trends")
trends=[]
for location in results:
    #print(location)
    for trend in location["trends"]:
        #print(" - %s" % trend["name"])
        trends.append([trend["name"]])
#print (trends)
with open('twitter_trends.csv', 'w',encoding="utf-8",newline='') as csvFile:
   csvwriter = csv.writer(csvFile)
   csvwriter.writerows(trends)
      
