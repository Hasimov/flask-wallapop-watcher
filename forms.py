from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, Optional


class SearchForm(FlaskForm):
    name = StringField('Nombre', [Length(min=1, max=100, message='Es demasiado largo'), DataRequired(message='Campo obligatorio')])
    price_max = IntegerField('Precio', [NumberRange(1, message='No puede ser inferior a 1'), Optional()])