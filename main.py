import os

from logging import debug
from typing import Final
import flask
from flask import Flask, render_template, url_for

# from forms import RegistrationForm, LoginForm

from riddles import first_riddle_text, second_riddle_text, final_answer, opening
from form import FinalAnswerForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "9efc17d27f6b28690111ebc0e4cf7c2e"

# cwd = os.getcwd()
# root, folders, files = next(os.walk(os.path.join(cwd, "static")))
# filepaths = [os.path.join("static", file) for file in files if ".css" not in file]


@app.route("/amazing_first_riddle")
def first_riddle():
    picture = os.path.join("static", "pic_1.jpg")
    return render_template("riddles.html", message=first_riddle_text, picture=picture, w=500, opening=opening)



@app.route("/supercool_second_riddle")
def second_riddle():
    picture = os.path.join("static", "boat_together.jpg")
    return render_template("riddles.html", message=second_riddle_text, picture=picture, w=500)


@app.route("/crossword_answer", methods=["GET", "POST"])
def crossword():
    form = FinalAnswerForm()
    if form.validate_on_submit():
        flask.flash("Ответ верный!", category="success")
        return flask.redirect(url_for("present"))
    return render_template("final_answer.html", form=form)


@app.route("/present")
def present():
    title = "Кирилл тебя тоже поздравляет с Днем Рождения, Ира!"
    return render_template("certificate.html", title=title)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
