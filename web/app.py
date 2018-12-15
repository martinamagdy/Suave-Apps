from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, jsonify,render_template
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import mysql_conn
import numpy as np
import pymysql
pymysql.install_as_MySQLdb()

connection_string = (
    f"root:{mysql_conn.password}@localhost/apps_db")
engine = create_engine(f'mysql://{connection_string}')


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the table
Apps = Base.classes.apps
description = Base.classes.apple_description
print(Base.classes.keys())

# Create our connection object
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def apps():
    # Perform a query to retrieve all apps
    all_apps = session.query(Apps.name).limit(20).all()
    apps=[]
    for app in all_apps:
        s=str(app).split("'")
        apps.append(s[1])
    return render_template("index.html",apps=apps)


@app.route("/info/<name>")
def info(name):
    # Perform a query to retrieve all apps
    all_apps = session.query(Apps.name).limit(20).all()
    apps=[]
    for app in all_apps:
        s=str(app).split("'")
        apps.append(s[1])

    category = session.query(Apps.a_category).filter(Apps.name == name).all()
    c=str(category).split("'")
    category = c[1]
    apple = session.query(Apps.a_price, Apps.a_user_rating, Apps.a_size_mb, Apps.a_content_rating).\
                               filter(Apps.name == name).all()
    a=str(apple).split(",")
    apple_info=[]
    z=0
    n=0
    for aapp in a:
        apple_info.append(a[z])
        z=z+1

    google = session.query(Apps.g_price, Apps.g_user_rating, Apps.g_size_mb, Apps.g_content_rating).\
                               filter(Apps.name == name).all()   
    g=str(google).split(",")
    google_info=[]
    for gapp in g:
        google_info.append(g[n])
        n=n+1

    return render_template("Apps.html", name=name,apple_info=apple_info,google_info=google_info, category=category,apps=apps)

@app.route("/api/available")
def available():
    return (
        "<img src=\"https://img.etimg.com/thumb/msid-46065787,width-300,imgsize-83533,resizemode-4/7-things-mobile-app-developers-should-focus-on.jpg\" alt=\"apps\" width=\"800\" height=\"300\"/>"+
        "<br/>"+
        "<br/>"+
        "Available Routes:<br/>" +
        "<br/>"+
        "<a href=\"/api/routes\">/api/routes</a><br/>"+
        "Return a list of all apps<br/>"+
        "<br/>"+
        "/api/{app_name}<br/>"+
        "return apple and android info about certain app<br/>"+
        "<a href=\"/\">Return To Home page</a>"
          )

@app.route("/api/routes")
def routes():
    app_api = session.query(Apps.name,Apps.a_category,
                           Apps.a_price, Apps.a_user_rating, Apps.a_size_mb, Apps.a_content_rating,
                           Apps.g_price, Apps.g_user_rating, Apps.g_size_mb, Apps.g_content_rating).all() 
    return jsonify(app_api)

@app.route("/api/<name>")
def JSON_data(name):
    app_dict = {}
    app_dict["AppleInfo"] = {}
    app_dict["AndroidInfo"] = {}

    app_dict["name"] = name
    app_dict["category"] = (session.query(
        Apps.a_category).
        filter(Apps.name == name).all())

    apple_data = (session.query(
        Apps.a_price, 
        Apps.a_user_rating, 
        Apps.a_size_mb, 
        Apps.a_content_rating).
        filter(Apps.name == name).all())
    android_data = (session.query(
        Apps.g_price, 
        Apps.g_user_rating, 
        Apps.g_size_mb, 
        Apps.g_content_rating).
        filter(Apps.name == name).all())

    dirty_apples = list(np.ravel(apple_data))
    dirty_googles = list(np.ravel(android_data))

    apples = []
    googles = []

    for item in dirty_apples:
        apples.append(str(item))
    for item in dirty_googles:
        googles.append(str(item))
        
    app_dict = { 
        "name": name,
        "category": (session.query(Apps.a_category).filter(Apps.name == name).all()),
        'AppleInfo': {
            'Price': apples[0],
            'UserRating': apples[1],
            'FileSize': apples[2],
            'ContentRating': apples[3] 
                    },
        'AndroidInfo': {
            'Price': googles[0],
            'UserRating': googles[1],
            'FileSize': googles[2],
            'ContentRating': googles[3]
                    
                    }
    }
    return jsonify(app_dict)
#  Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
