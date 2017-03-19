#    Tell me the Story!  
##    What is it & what does it do?

Limb amputation is a common complication of some chronic diseases like diabetes and traumatic incidents like car accidents. Most amputees choose to fit in a prosthetic limb for aesthetic and functional purposes.  The web application in this repository may help the prosthetic bioengineers / practitioners estimate the length of the missing limb of a patient, using measurements of the patient's body structure,  intact limb segments, as well as age and gender. 

When the application is deployed (e.g., on an internal server in a hospital or workshop), 3 web pages will be available. You can point your web browser to an "instructions" page to learn about the necessary measurements you need to collect from your patient to use the application. You can then point your browser to one of 2 web forms, depending on whether your patient is an upper-limb or lower-limb amputee. Fill in the form fields for the requested data, then hit the "submit" button. If no data-entry errors are detected, a new web page will pop up. This will display an estimate of the length of your patient's missing limb. Yes, it is as simple as that!


## What's Behind the Scenes?

This application is composed of 3 modules. There is an input module that collects your data, and an output module that gives you back the computed length estimates of the limb. For the convenience of the user, both of these modules are rendered as html web pages using the Flask Python  Framework.


Sandwiched between these 2 modules is a conditional-probability module that estimates the most probable limb length given the values of the input variable. This is a "pickled" SciKitLearn model (one for the lower, and one for the upper, limbs).

Details of the model building process can be found in the enclosed Jupiter notebook.  Briefly, separately for the upper and lower limbs, I built a cross-validated, l2-regularized regression model that takes anthropometric and demographic variables as predictors and returns an estimate of the limb length.

This application  is just for demonstration purposes. The data I used to build the model can be found here(http://mreed.umtri.umich.edu/mreed/downloads.html#ansur). These are anthropometric measures that the US Army collected from its personnel’s decades ago, so it may not be representative of the current civilian population of the US or elsewhere. Although more representative and up-to-date data are available, I can not use them in a public repository given that participants were not consented for this kind of usage.

#    Get Me Fixed!
##    How Can I Deploy It?

On a Ubuntu 14.04 server, with a server-wide installation of Python 3.4, do the following:

1. create a new directory, "prosthetics". Move inside this directory. Generate a virtual python environment as shown here(https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). activate this virtual environment, then install the following python libraries:
pip install  Flask, Flask-WTF, numpy, scipy, sklearn, pandas

2.  Create a new directory, "app" inside the "prosthetics" directory. Move the following files from the current repository to the "app" directory:

	*  forms.py
	* views.py
	*  model_lower.pkl
	*  model_upper.pkl

3. Create a new directory, "templates", inside the "app" directory. Put the following html files inside this new directory:

	* base.html
	* instructions.html
	* lowerlimb.html
	* upperlimb.html
	* result.html

4. Now run the application as a python script. On your command line, type the following:
python3 views.py
Ideally, you should get a confirmation message declaring that your application is being served and can be requested by a web browser.

5. Now use a browser on the Ubuntu machine, or any other machine on the network, to visit the following 3 URL's:

	* http://localhost:5000/instructions
	* http://localhost:5000/lowerlimb
	* http://localhost:5000/upperlimb

6. Finally, try out filling in some values in the upper-limb or lower-limb form then submit the form. You should get an estimate of the length of the requested limb, returned on a simple web page.


Enjoy!

	#Whom Should You Blame?

Well, No one but yourself! I offer no warrantee, implied or explicit, for the code in any of my repositories. Use it at your own risk and discretion. I accept no liability, whatsoever, as a result of using it, or using a modified version of it!

Tamer Soliman, the author of this repository, has been immersed in data collection and statistical modeling since 2002. He holds a PhD in quantitative Experimental Psychology, where he designs experiments to understand and model human cognition, decision making, socio-cultural behavior, attitudes, and actions. He develops data-centered utilities and applications that subserve his data-science and machine-learning projects. While he approaches his projects with the mindset of a skeptic homo-academicus,  he understands the concept of "deadlines", and loves making money just as all other homo-sapiens!