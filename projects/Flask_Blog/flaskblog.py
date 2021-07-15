from flask import Flask
### TO RUN THE APP:
    # export FLASK_APP=flaskblog.py
    # flask run
# Create instance flask. __name__ = name of the module
app = Flask(__name__)

@app.route("/") # Route of the browser to go to different pages. / is the route of the page of our website
@app.route("/home") # Two routes with the same page
def home(): 
    return "<h1>Hello World!<h1>"

# Create an about page
@app.route("/about") 
def about(): 
    return "<h1>About page :)<h1>"


# To run without start the server. Just call the .py file.
if __name__ == '__main__':
    app.run(debug=True)