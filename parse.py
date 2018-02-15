'''
Bayan Berri, Donia Tung
Team DataBases
SoftDev2 pd7
K04--Mi only nyam ital food, mon!
2018-02-15
'''
from pymongo import MongoClient
'''setting up interactions with the database'''
c=MongoClient("lisa.stuy.edu",27017);
collie=c.test.restaurants

def find_boroughs(borough):
   '''
   prints and returns all restaurants in a specified borough.
   '''
   dictionary = collie.find({"borough":borough})
   for each in dictionary:
      print each["name"]
   return dictionary

def by_zip(code):
   '''
   prints and returns all restaurants in a specified zip code.
   '''
   dictionary_zip=collie.find({"address.zipcode":code})
   for each in dictionary_zip:
      print each["name"]
   return dictionary_zip

def by_zip_grade(zc,grade):
   '''
   prints and returns all restaurants in a specified zipcode and with a specified grade.
   '''
   dictionary=collie.find({"$and":[{"address.zipcode":zc},{"grades.grade":grade}]})
   for each in dictionary:
      print each["name"]
   return dictionary

def by_zip_score(zc,threshold):
   '''
   prints and returns all restaurants in a specified zip code
   with a score below a specified threshold
   '''
   dictionary=collie.find({"$and":[{"address.zipcode":zc},{"grades.score":{"$lt":threshold}}]})
   for each in dictionary:
       print each["name"]
   return dictionary

def cleverness(borough, cuisine):
    '''
    based on the borough and cuisine inputted, returns a list of restaurants meeting the specs,
    shows their grade as well as their address, if you'd like to visit them! 
    '''
    dictionary=collie.find({"$and":[{"borough":borough},{"cuisine": cuisine}]})
    for each in dictionary:
        addressdict = each["address"]
        gradesdict = each["grades"]
        print each["name"] + " Grade: " + gradesdict[0]["grade"]
        print addressdict["building"]+ " " + addressdict["street"] + " " + addressdict["zipcode"]
    return dictionary




cleverness("Manhattan", "Chinese")

'''
print "=====================BOROUGH==================\n"
find_boroughs("Manhattan")
print "=====================ZIP==================\n"
by_zip('11218')
print "=====================ZG==================\n"
by_zip_grade("11218","A")
print "===================ZS===================\n"
by_zip_score("11218",4)
'''
