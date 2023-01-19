from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):

 client = MongoClient(host='mongodb+srv://sharanblog:Sharan1071@sharanblog.clxxvzc.mongodb.net/?retryWrites=true&w=majority',
                      port=int(port),
                      username=username,
                      password=password
                     )
 db_handle = client['db_name']
 return db_handle, client