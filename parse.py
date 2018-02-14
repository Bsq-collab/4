'''
All restaurants in a specified borough.
All restaurants in a specified zip code.
All restaurants in a specified zip code and with a specified grade.
All restaurants in a specified zip code with a score below a specified threshold.
Something more clever.
'''

from pymongo import MongoClient

c=MongoClient("localhost",27017);
mfDB=c['test']
collie=mfDB['restaurants']
def find_boroughs(borough):
   dictionary = collie.find({"borough":borough})
   for each in dictionary:
       print each
       

find_boroughs("Manhattan")
