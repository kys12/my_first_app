from flask import Flask, render_template, request

app = Flask ("MyApp")
# defining a Flask application called My App
# Now define roots for a web application
# NB For bbc/news and for bbc/sport - /sport and /news is the relative pad for the websites?
# import Flask, render_template - What this do?
# Use render_template method in order to log html

@app.route("/")
def hello ():
	return "Hello World!"
# This is a decorator. It is 'hook' i.e. before you code this method, do this code and after the method is finished, do this code
# But you don't need 
# When the user goes and calls the slash root, call this method... - here the "hello" metthod
# The hello method will be called when the user calls the / url

@app.route("/<name>")
def hello_someone(name):
	return render_template("hello.html", name = name.title ())
# It will render our template which we have just defined as hello.html and pass it its name
# .title will make it a title name

@app.route ("/signup", methods = ["POST"])
def sign_up():
	form_data = request.form 
	print form_data ["email"]
	return "All OK"


# Previous examples...
# @app.route("/idontexist")
# def idontexist ():
# 	return "I do exist now!"

# @app.route("/myname")
# def myname ():
# 	return "Your name is Kristi"
# NB your route name does not have to be the same as your method name
# i.e. /myname could be /milktea and keep def myname and it would still work

# Print statement links back to the email entered into the form
# In the html file, you have an input field and give it the id of email
# In the python file, when you collect all the form data from the form
# form_data = request.form - this is what allows you to print out the form_Data
# access the email from the form_data
# it gives you the correct one as in html you have given id to email

# Method is specified as POST - why?
# GET vs POST 
# Everytime you hit an end point, you get a GET
# There are 2 maintypes of request GET and POST
# GET - say to the server "give me this webpage Im looking for"
# POST - give the server some information to do something with
# Form request for every html POST
# Make the method a POST in the python file - as it is receieving form data

# Form data that is sent along with it hi@hi.com is associated with the email property name
# square brackets to access the email property of the form data

app.run (debug=True)
# This will run the application
