'''
All restaurants in a specified borough. DONE
All restaurants in a specified zip code. DONE
All restaurants in a specified zip code and with a specified grade.
All restaurants in a specified zip code with a score below a specified threshold.
Something more clever.
'''

from pymongo import MongoClient

c=MongoClient("lisa.stuy.edu",27017);
collie=c.test.restaurants

#mfDB=c['test']
#collie=mfDB['restaurants']
def find_boroughs(borough):
   dictionary = collie.find({"borough":borough})
   for each in dictionary:
       print each["name"]
   return dictionary

def by_zip(code):
    dictionary_zip=collie.find({"zipcode":code})
    for each in dictionary_zip:
        print each["name"]
    return dictionary_zip

def by_zip_grade(zc,grade):
    dictionary=collie.find({"$and":[{"zipcode":zc},{"grade":grade}]})
    for each in dictionary:
        print each["name"]
    return dictionary

def by_zip_score(zc,threshold):
    dictionary=collie.find({"$and":[{"zipcode":zc},{"score":{"$lt":threshold}}]})
    for each in dictionary:
        print each["name"]
    return dictionary

for each in collie.find():
    print each

print "=====================BOROUGH==================\n"
#find_boroughs("Manhattan")
print "=====================ZIP==================\n"
by_zip('11218')
print "=====================ZG==================\n"
#by_zip_grade(11220,"A")
