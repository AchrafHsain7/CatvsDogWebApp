from flask import Flask, request, render_template, session, redirect



app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

ANIMALS = ["dog", "cat"]


@app.route("/")
def index():
    return render_template("index.html", animals=ANIMALS)

@app.route("/process", methods=["POST"])
def process():
    animal = request.form.get("animal")
    image = request.form.get("image")
    if not image or not animal:
        return render_template("failure.html")
    
    return redirect("/")