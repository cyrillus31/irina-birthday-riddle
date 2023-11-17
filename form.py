from flask_wtf import FlaskForm
from flask_wtf.csrf import ValidationError
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


from riddles import final_answer

def validate_answer(form, field):
    if field.data.lower() == final_answer:
            return
    else:   
        raise ValidationError("Ответик неправильный! :) Попробуй еще разок!")

        
class FinalAnswerForm(FlaskForm):
    answer = StringField("Главное слово",
                         validators=[DataRequired(), validate_answer])
    submit_button = SubmitField("ОТПРАВИТЬ")
