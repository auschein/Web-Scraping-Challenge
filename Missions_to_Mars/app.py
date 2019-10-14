import sys
from flask import Flask, render_template, jsonify, redirect
import pymongo
import mars_scrape

sys.setrecursionlimit(2000)
app = Flask(__name__)


client = pymongo.MongoClient()
db = client.mars_db
collection = db.facts



@app.route('/scrape')
def scrape():
    red_planet = mars_scrape.scrape()
    print("\n\n\n")
    db.facts.insert_one(red_planet)
    return "Data"

@app.route("/")
def home():
    red_planet = list(db.facts.find())
    print(red_planet)
    return render_template("index.html", red_planet = red_planet)


if __name__ == "__main__":
    app.run(debug=True)