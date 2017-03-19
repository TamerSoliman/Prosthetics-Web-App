from flask import Flask, render_template, redirect, flash, url_for
from forms import LowerLimbData,  UpperLimbData
from sklearn.externals import joblib

app=Flask(__name__)
app.secret_key="unguessable "

@app.route("/", methods=["GET"])
@app.route("/instructions", methods=["GET"])

def instructions():
	"""
	Renders the landing instructions page when the appropriate 	UrRL is requested by the browser
	"""	

	return render_template("instructions.html")


@app.route("/lowerlimb", methods=["GET", "POST"])

def lowerlimb():
	"""
	Renders the Lower Limb form upon a get request; runs the 	model and returns the populated results page upon a post 	request
	"""
	form=LowerLimbData()
	if form.validate_on_submit():
		patient_data =[form.shoulder_height.data, form.chest_height.data, form.waist_length.data, form.gender.data, form.age.data, form.hand1.data, form.hand2.data, form.forearm1.data, form.forearm2.data, form.arm1.data, form.arm2.data]
		estimate = lower_model.predict(patient_data)
		return render_template("result.html", estimate=estimate, which = "lower")
	return render_template("lowerlimb.html", form=form)

@app.route("/upperlimb", methods=["GET", "POST"])

def upperlimb():
	"""
	Renders the upper Limb form upon a get request; runs the 	model and returns the populated results page upon a post 	request
	"""

	form=UpperLimbData()
	if form.validate_on_submit():
		patient_data =[form.shoulder_height.data, form.chest_height.data, form.waist_length.data, form.gender.data, form.age.data, form.foot1.data, form.foot2.data, form.foreleg1.data, form.foreleg2.data, form.thigh1.data, form.thigh2.data]
		estimate = upper_model.predict(patient_data)
		return render_template("result.html", estimate=estimate, which = "upper")
	return render_template("upperlimb.html", form=form)

if __name__ == "__main__":
	lower_model=joblib.load("model_lower.pkl")
	upper_model=joblib.load("model_upper.pkl")
	app.run(host="0.0.0.0", port=5000)
