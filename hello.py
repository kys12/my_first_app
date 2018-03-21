from flask import Flask, render_template

app = Flask ("MyApp")
# defining a Flask application called My App
# Now define roots for a web application
# NB For bbc/news and for bbc/sport - /sport and /news is the relative pad for the websites?
# import Flask, render_template - What this do?
# Use render_template method in order to log html

@app.route("/")
def hello ():
	return "Hello Kristi!"
# This is a decorator. It is 'hook' i.e. before you code this method, do this code and after the method is finished, do this code
# But you don't need 
# When the user goes and calls the slash root, call this method... - here the "hello" metthod
# The hello method will be called when the user calls the / url

@app.route("/idontexist")
def idontexist ():
	return "I do exist now!"

@app.route("/myname")
def myname ():
	return "Your name is Kristi"
# NB your route name does not have to be the same as your method name
# i.e. /myname could be /milktea and keep def myname and it would still work

app.run (debug=True)
# This will run the application
