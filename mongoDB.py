import pymongo


class mongoDB:


    def readDataBase(self):
        username = "connectr"
        password = "Co3Ksdj868DF67HklqcFCgR"
        dbName = "appyconnect"
        host = "52.1.138.177"
        port = 27017
        myclient=pymongo.MongoClient("mongodb://"+username+":"+password+"@"+host+":"+port+"/?authSource="+dbName+"&authMechanism=SCRAM-SHA-1")
        print(myclient.list_database_names())
