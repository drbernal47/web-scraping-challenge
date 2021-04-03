from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/app"
# mongo = PyMongo(app)



# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars_data
# produce = db.produce





@app.route("/")
def index():
    mars_data = db.mars_data.find_one()
    return render_template("index.html", listings=mars_data)


@app.route("/scrape")
def scraper():
    mars_data = db.mars_data
    mars_scraped = scrape_mars.scrape()
    mars_data.update({}, mars_scraped, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
