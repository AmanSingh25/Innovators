
#import section
import os
from flask import Flask
from flask import render_template
from flask import request, redirect, session, url_for
from flask_pymongo import PyMongo
import secrets
# import bcrypt
from organizations_info import organizations_info
#from templates import education

app = Flask(__name__)
# LG5-YwAi@eXncpV
#Name Of Database
app.config['MONGO_DBNAME'] = 'database'

#URI of database
app.config['MONGO_URI']= "mongodb+srv://innovators:ZOXFgRCwvlr34Nkl@cluster0.k8lte.mongodb.net/database?retryWrites=true&w=majority"

mongo = PyMongo(app)
#connect to MongoDB database


secret_key = os.environ.get('MONGO_URI')
# app.config['MONGO_URI'] = secret_key


# -- Session data --
app.secret_key = secrets.token_urlsafe(16)

#Initialize PyMongo
mongo = PyMongo(app)


#index route

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/addorg', methods=["GET", "POST"])
def new_organization():
    if request.method == "GET":
        #render the form to populate the required parameters
        return render_template("addorg.html")
    else:
        #assign from data to varaibles
        first_name = request.form['FirstName']
        last_name = request.form['LastName']
        organization_name = request.form['OrganizationName']    
        org_type = request.form['types_of_org'] 
        image = request.form['image'] 
        go_fund_link= request.form['gofundme']
        mission = request.form['mission']

    collection = mongo.db.organizations_info

     #insert an entry to the database using the variables declared above
    collection.insert_one({"firstName":first_name, "lastName":last_name, "organization_name":organization_name, "types_of_org":org_type, "gofundme": go_fund_link , "mission":mission, "image":image})
    return render_template('index.html')

@app.route('/all_organizations')
def all_organizations():
    collection = mongo.db.organizations_info
    # collection.insert_many(organizations_info)
    # sort the database alphabetically based on their name and render all the organizations name to the page in sorted manner
    organizations = collection.find().sort('organization_name')
    return render_template('all_organizations.html', organizations = organizations)
    
@app.route('/education')
def education():
    collection = mongo.db.organizations_info
    #sort the database alphabetically based on their name and render all the organizations name related to education in sorted manner
    organizations = collection.find({'types_of_org':'education'}).sort('organization_name')
    return render_template('education.html', organizations = organizations)

@app.route('/finance')
def finance():
    collection = mongo.db.organizations_info
    #sort the database alphabetically based on their name and render all the organizations name related to finance in sorted manner
    organizations = collection.find({'types_of_org':'finance'}).sort('organization_name')
    return render_template('finance.html', organizations = organizations)

@app.route('/tech')
def tech():
    collection = mongo.db.organizations_info
    #sort the database alphabetically based on their name and render all the organizations name related to tech in sorted manner
    organizations = collection.find({'types_of_org':'technology'}).sort('organization_name')
    return render_template('tech.html', organizations = organizations)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == "GET":
    #render the form to populate the required parameters
        return render_template("contact.html")
    else:
        #assign from data to varaibles
        first_name = request.form['FirstName']
        last_name = request.form['LastName']
        email = request.form['email']
        message = request.form['Message']

    collection = mongo.db.contact_info

     #insert an entry to the database using the variables declared above
    collection.insert_one({"firstName" : first_name, "lastName" : last_name, "email" : email, "Message": message})
    return render_template('index.html')

#SIGNUP Route
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == "POST":
#         users = mongo.db.users_info
#         #search for username in database
#         existing_user = users.find_one({'name': request.form['username']})

#         #if user not in database
#         if not existing_user:
#             username = request.form['username']
#             #encode password for hashing
#             password = request.form['password']
#             #hash password
#             # salt = bcrypt.gensalt()
#             # hashed = bcrypt.hashpw(password, salt)
#             #add new user to database
#             users.insert_one({'name': username, 'password': password})
#             #store username in session
#             session['username'] = request.form['username']
#             return redirect(url_for('signup'))

#         else:
#             return 'Username already registered.  Try logging in.'
    
#     else:
#         return render_template('signup.html')

# #LOGIN Route
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == "POST":
#         users = mongo.db.users_info
#         #search for username in database
#         login_user = users.find_one({'name': request.form['username']})

#         #if username in database
#         if login_user:
#             db_password = login_user['password']
#             #encode password
#             password = request.form['password']
#             # compare username in database to username submitted in form
#             if password == db_password:
#                 #store username in session
#                 session['username'] = request.form['username']
#                 return render_template('index.html')
#             else:
#                 return 'Invalid username/password combination.'
#         else:
#             return 'User not found.'
#     else:
#         return render_template('login.html')
    
# #LOGOUT Route
# @app.route('/logout')
# def logout():
#     #clear username from session data
#     session.clear()
#     return redirect('/')
