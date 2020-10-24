from flask import Flask, render_template, url_for, request, session, redirect
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
app.secret_key = 'mysecret'

client = MongoClient('mongodb+srv://Sojin:technica@cluster0.e0mte.mongodb.net/<Technica>?ssl=true&ssl_cert_reqs=CERT_NONE')
db = client.Users

names = ['Alice','Brody','Cindy', 'Genie', 'Jack']
pw = [0,1,2,3,4]

# for x in range(0, 5):
#     user = {
#         'name' : names[x],
#         'pw' : pw[x]
#     }
#
#     result=db.Users.insert(user)
#
# print('finished creating 500 business reviews')


# index route
@app.route("/")
def index():
    # if 'username' in session:
    #     return 'You are logged in as ' + session['username']
    return render_template("index.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
    # if request.method == 'POST':
    #     users = db.Users
    #     existing_user = users.find_one({'name' : request.form['username']})
    #
    #     if existing_user is None:
    #         hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
    #         users.insert({'name' : request.form['username'], 'pw' : hashpass})
    #         session['username'] = request.form['username']
    #         return redirect(url_for('index'))
    #
    #     return 'That username already exists!'
    # return render_template("login.html")
    if request.method == 'POST':
        users = db.Users
        login_user = users.find_one({'name' : request.form['username']})

        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['pw']) == login_user['pw']:
                session['username'] = request.form['username']
                return redirect(url_for('index'))

        return 'Invalid username/password combination'
    return render_template("login.html")

@app.route("/convos", methods=["GET"])
def convos():
    return render_template("convos.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")

@app.route("/inspiration", methods=["GET"])
def inspiration():
    return render_template("inspo.html")

@app.route("/funding", methods=["GET"])
def funding():
    return render_template("funding.html")

if __name__ == "__main__":
    app.run()
