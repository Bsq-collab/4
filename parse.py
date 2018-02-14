'''
All restaurants in a specified borough.
All restaurants in a specified zip code.
All restaurants in a specified zip code and with a specified grade.
All restaurants in a specified zip code with a score below a specified threshold.
Something more clever.
'''
c=MongoClient("lisa.stuy.edu",27017);
mfDB=c['test']
collie=mfDB['restaurants']
def find_boroughs(borough):
    for each in collie.find({"borough":borough}):
        print each["name"]
