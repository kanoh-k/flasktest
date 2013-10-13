import flask
 
application = flask.Flask(__name__)

#Set application.debug=true to enable tracebacks on Beanstalk log output. 
#Make sure to remove this line before deploying to production.
application.debug=True
 
@application.route('/')
def hello_world():
    return "Hello world!"

@application.route('/sub')
def sub_page():
    return "Sub page!"

@application.route('/user/<user>')
def user_page(user):
    return user
 
if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)

