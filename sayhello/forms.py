from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[DataRequired(), Length(1, 20)],
        render_kw={"autocomplete": "off"},
    )
    body = TextAreaField(
        "Message",
        validators=[DataRequired(), Length(1, 200)],
        render_kw={"autocomplete": "off"},
    )
    submit = SubmitField()
