from flask import Flask

# Create an instance of this class. The first argument is the name of the application’s module or package.
#  __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.

app = Flask(__name__)

# route() decorator to tell Flask what URL should trigger our function.

@app.route('/')
def index():
    return 'Index Page'

if __name__=="__main__":
    app.run(debug=True)

