import pymongo

class Database:
    
    def __init__(self,collection = "videoCollection",db = "videos"):
        self.db = db
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient[collection]
        self.collection = self.mydb[self.db]

    #modify to check if array else put into array
    def insert(self,items):
        if type(items) != list:
            items = [items]
        self.collection = self.mydb[self.db]
        return self.collection.insert_many(items)
        # return self.collection.insert(items)
    
    def find_one(self,search):
        self.collection = self.mydb[self.db]
        return self.collection.find_one(search)
    
    def find(self,search = {}):
        self.collection = self.mydb[self.db]
        return self.collection.find(search)

    def update(self,query,update):
        # update['upsert'] = True 
        self.collection = self.mydb[self.db]
        return self.collection.update(query,update)

    def delete(self,query):
        self.collection = self.mydb[self.db]
        return self.collection.remove(query)



    