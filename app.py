from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
#for local usage
app.secret_key = 'supersecretkey'

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/egg-hunt", methods=["GET", "POST"])
def egg_hunt():
    # if it's try again
    if request.args.get("reset") == "true":
        session.pop("winning_egg", None)

    # randomly choose a winning egg number and store in session
    if "winning_egg" not in session or "reset" in request.args:
            session["winning_egg"] = random.randint(1, 5)
    user_guess = None
    if request.method == "POST":
        #compare guess to winning egg
        user_guess = int(request.form["guess"])
        if user_guess == session["winning_egg"]:
            result = "You found the surprise egg!"
        else:
            result = "That egg was empty. Try again!"
        return render_template("egg_hunt.html", result=result, guessed=user_guess, winning_egg=session["winning_egg"])
    return render_template("egg_hunt.html")

if __name__ == "__main__":
    app.run(debug=True)
