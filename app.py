from flask import Flask, render_template, request

myapp = Flask(__name__)

@myapp.route("/")
def root():
    return render_template("template.html", username = request.args['text'], method = request.method)

@myapp.route("/form", methods = ['POST','GET'])
def form():
    return render_template("form.html")

if __name__ == '__main__':
    myapp.debug = True
    myapp.run()
