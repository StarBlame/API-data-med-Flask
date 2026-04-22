from flask import Flask, render_template
import requests
app = Flask(__name__)
@app.route("/")
def hjem():
	url = "https://catfact.ninja/fact"
	response = requests.get(url)
	data = response.json()
	return render_template("index.html", fact=data["fact"], length=data["length"])
app.run(debug=True)
