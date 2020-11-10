from flask import Flask, render_template
import requests
import config

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


# fetch cover img
# calling movie database
url = f"http://www.omdbapi.com/?t={movie['title']}/&apikey={config.api_key}"

# get the response
response = requests.request("GET", url)

# parse result into JSON and look for data if available
movie_data = response.json()
print(movie_data)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
