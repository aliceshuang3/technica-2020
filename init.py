from flask import Flask
from pymongo import MongoClient 

app = Flask(__name__)

client = MongoClient('mongodb+srv://Sojin:technica@cluster0.e0mte.mongodb.net/<Technica>?retryWrites=true&w=majority')
db = client.Users

names = ['Alice','Brody','Cindy', 'Genie', 'Jack']
pw = [0,1,2,3,4]

for x in range(0, 5):
    user = {
        'name' : names[x],
        'pw' : pw[x]
    }

    result=db.Users.insert(user)

print('finished creating 500 business reviews')


# index route
@app.route("/")

def index():
    
    return "!"


if __name__ == "__main__":
    app.run()