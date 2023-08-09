from pymongo import MongoClient
import certifi

MONGO_URI='mongodb+srv://jmartinburgo:jmartinburgo@cluster0.qff17mp.mongodb.net/?retryWrites=true&w=majority'

ca=certifi.where()

def dbConnection():
    try:
        client = MongoClient.connect(MONGO_URI,tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print(  'Error de conexion con la bdd')
    return db