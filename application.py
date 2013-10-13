from flask import Flask
 
app = Flask(__name__)

#Set application.debug=true to enable tracebacks on Beanstalk log output. 
#Make sure to remove this line before deploying to production.
application.debug=True
 
@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/sub/<user>')
def sub_page(user):
    return ("This is a sub page for %s!" % user)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
