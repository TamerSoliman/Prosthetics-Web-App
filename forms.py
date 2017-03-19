from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SubmitField
from wtforms.validators import InputRequired, DataRequired, NumberRange, Length

class LowerLimbData(FlaskForm):
	"""
	Render the necessary field types in the Jinja template when 	instantiated
	"""

	shoulder_height=DecimalField("Shoulder Height", validators=	[DataRequired()])
	chest_height=DecimalField("Chest Height", validators=[DataRequired()])
	waist_length=DecimalField("Waist Length", validators=[DataRequired()])
	gender=IntegerField("Gender", validators=[InputRequired(), NumberRange(min=0, max=1)])
	age=DecimalField("age", validators=[DataRequired()])
	hand1=DecimalField("Hand Length", validators=[DataRequired()])
	hand2=DecimalField("Hand Circumference", validators=[DataRequired()])
	forearm1=DecimalField("Forearm Length", validators=[DataRequired()])
	forearm2=DecimalField("Forearm Circumference", validators=[DataRequired()])
	arm1=DecimalField("Arm Length", validators=[DataRequired()])
	arm2=DecimalField("Arm Circumference", validators=[DataRequired()])
	submit=SubmitField("Submit")


class UpperLimbData(FlaskForm):
	"""
	Render the necessary field types in the Jinja template when 	instantiated
	"""
	shoulder_height=DecimalField("Shoulder Height", validators=[DataRequired()])
	chest_height=DecimalField("Chest Height", validators=[DataRequired()])
	waist_length=DecimalField("Waist Length", validators=[DataRequired()])
	gender=DecimalField("Gender", validators=[InputRequired()])
	age=DecimalField("age", validators=[DataRequired()])
	foot1=DecimalField("Foot Length", validators=[DataRequired()])
	foot2=DecimalField("Foot Circumference", validators=[DataRequired()])
	foreleg1=DecimalField("Foreleg Length", validators=[DataRequired()])
	foreleg2=DecimalField("Foreleg Circumference", validators=[DataRequired()])
	thigh1=DecimalField("Thigh Length", validators=[DataRequired()])
	thigh2=DecimalField("Thigh Circumference", validators=[DataRequired()])
	submit = SubmitField("Submit")
