import os

from flask import Flask, render_template
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
if os.path.exists("env.py"):
    import env

MONGODB_URI = os.environ["MONGO_URI"]


# Connect to mongodb cluster
client = MongoClient(MONGODB_URI)

for db_info in client.list_database_names():
   print(db_info)

# List all the databases in the cluster:
# for slang_words in itscool():
# 	print(slang_words)



app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo =PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )

