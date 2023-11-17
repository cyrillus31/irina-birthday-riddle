import os

from logging import debug
from typing import Final
import flask
from flask import Flask, render_template, url_for 
# from forms import RegistrationForm, LoginForm

from riddles import first_riddle_text, second_riddle_text, final_answer
from form import FinalAnswerForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '9efc17d27f6b28690111ebc0e4cf7c2e'


@app.route("/amazing_first_riddle")
def first_riddle():
    return render_template("riddles.html", message=first_riddle_text)


@app.route("/supercool_second_riddle")
def second_riddle():
    return render_template("riddles.html", message=second_riddle_text)

@app.route("/crossword_answer", methods=["GET", "POST"])
def crossword():
    form = FinalAnswerForm()
    if form.validate_on_submit():
        flask.flash("Ответ верный!", category="success")
        return flask.redirect(url_for("present"))
    return render_template("final_answer.html", form=form)

@app.route("/present")
def present():
    filepath = os.path.join("static", "certificate.jpg")
    return render_template("certificate.html", filepath=filepath)

if __name__ == "__main__":
    app.run(debug=True)
