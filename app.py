""" API for user recommendation system
"""
#import required libraries
import pandas as pd
import numpy as np
import mysql.connector
from sqlalchemy import create_engine
import turicreate as tc
from flask import Flask, jsonify

APP = Flask(__name__)

# The details for connecting to the sql database of lucid blog which was hosted remotely
MYDB = mysql.connector.connect(host="remotemysql.com", user="8SawWhnha4", passwd="zFvOBIqbIz", database="8SawWhnha4")# pylint: disable=line-too-long

# The mysql engine to be queried and read
ENGINE = create_engine('mysql+mysqlconnector://8SawWhnha4:zFvOBIqbIz@remotemysql.com/8SawWhnha4')

# Queried Tables
USERS = pd.read_sql_query("SELECT * FROM users", ENGINE)
ARTICLES = pd.read_sql_query("""SELECT id AS post_id,title,content,tags FROM posts""", ENGINE)

# Data cleaning on titles column of articles
ARTICLES['title'] = ARTICLES['title'].apply(lambda x: x.strip().lower())
ARTICLES['title'] = ARTICLES['title'].fillna('')

#Construct a reverse map of indices and post titles
INDEX = pd.Series(ARTICLES['post_id'].values, index=ARTICLES['title'].values)
INDEX2 = pd.Series(ARTICLES['title'].values, index=ARTICLES['post_id'].values)

# Create Dataframes
ALLUSERS = pd.DataFrame(USERS)
MAN = tc.SFrame(data=USERS)

# Load models
USER_MODEL = tc.load_model("user_model")
ARTICLE_MODEL = tc.load_model("article_model")

# Homepage html body
REPORT = "<h2>How to use the API:</h2><p>This is a recommendation system for users and articles. </p><h3>Using Flask</h3><p>To get a user recommendation use this url </p><code>http://127.0.0.1:5000/user/username</code><p> For example:</p><code>http://127.0.0.1:5000/user/eniayomi</code><br><br><p>To get an article recommendation use this url</p><code>http://127.0.0.1:5000/article/title</code><p> For example:</p><code>http://127.0.0.1:5000/article/html begins here</code><br><br><h3>Using Docker</h3><p>To get a user recommendation use this url </p><code>http://127.0.0.1:5000/user/username</code><p> For example:</p><code>http://127.0.0.1:5000/user/eniayomi</code><br><br><p>To get an article recommendation use this url</p><code>http://127.0.0.1:5000/article/title</code><p> For example:</p><code>http://127.0.0.1:5000/article/html begins here</code>" # pylint: disable=line-too-long

@APP.route('/', methods=['GET'])
def home():
    """
    GET Request for homepage
    """
    # Give message to user
    return REPORT


@APP.route('/user/<string:username>', methods=['GET'])
def prediction(username):
    """
    GET Request for user recommendation
    """
    if username in MAN.select_column('username'):
        _a = ALLUSERS[ALLUSERS['username'] == username]
        _b = _a['id'].values[0]
        _c = _a['name'].values[0]
        return jsonify(names=list(USER_MODEL.recommend(users=[_b], k=3)['name']))
    return jsonify(names=list(USER_MODEL.recommend(users=[4924], k=3)['name']))

@APP.route('/article/<string:title>', methods=['GET'])
def article(title):
    """
    GET Request for article recommendation
    """
    try:
        idx = INDEX[title.lower()]
        if not isinstance(idx, np.int64):
            idx = np.int64(list(idx)[0])

        # Get 5 recommendations based on similar post
        rec = list(ARTICLE_MODEL.recommend_from_interactions([idx], k=5))

        # Get post_id of recommended posts
        post_id = [rec[x]['post_id'] for x, i in enumerate(rec)]

        # Return the top 5 most similar posts
        return jsonify(articles=list(INDEX2.loc[post_id]))

    except KeyError:
        return jsonify(articles="We Have No Recommendations For You!")


if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0')
