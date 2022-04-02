
#import section
import os
from flask import Flask
from flask import render_template
from flask import request, redirect, session, url_for
from flask_pymongo import PyMongo
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
#intialize database and collection variable
#db = client.database
# mongo.db.create_collection("organizations_info")
# mongo.db.create_collection("user_info")


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
        return render_template("addorg.html")
    else:
        first_name = request.form['FirstName']
        last_name = request.form['LastName']
        organization_name = request.form['OrganizationName']    
        org_type = request.form['types_of_org']    
        go_fund_link= request.form['gofundme']
        mission_state = request.form['mission-statement']
    collection = mongo.db.organizations_info
    collection.insert_one({"firstName":first_name, "lastName":last_name, "organization_name":organization_name, "types_of_org":org_type, "gofundme": go_fund_link , "mission_statement":mission_state})
    return render_template('all_organizations.html')

@app.route('/all_organizations')
def all_organizations():
    collection = mongo.db.organizations_info
    # collection.insert_many(organizations_info)
    organizations = collection.find({})
    return render_template('all_organizations.html', organizations = organizations)

@app.route('/education')
def education():
    collection = mongo.db.organizations_info
    # collection.insert_many(organizations_info)
    organizations = collection.find({'types_of_org':'education'})
    return render_template('education.html', organizations = organizations)

@app.route('/finance')
def finance():
    collection = mongo.db.organizations_info
    # collection.insert_many(organizations_info)
    organizations = collection.find({'types_of_org':'finance'})
    return render_template('finance.html', organizations = organizations)

@app.route('/tech')
def tech():
    collection = mongo.db.organizations_info
    # collection.insert_many(organizations_info)
    organizations = collection.find({'types_of_org':'technology'})
    return render_template('tech.html', organizations = organizations)


