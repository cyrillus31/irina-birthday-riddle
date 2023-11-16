from logging import debug
import flask
from flask import Flask, render_template, url_for 
# from forms import RegistrationForm, LoginForm

from riddles import first_riddle_text, second_riddle_text

app = Flask(__name__)

app.config['SECRET_KEY'] = '9efc17d27f6b28690111ebc0e4cf7c2e'


@app.route("/amazing_first_riddle")
def first_riddle():
    return render_template("riddles.html", message=first_riddle_text)


@app.route("/supercool_second_riddle")
def second_riddle():
    return render_template("riddles.html", message=second_riddle_text)


if __name__ == "__main__":
    app.run(debug=True)
