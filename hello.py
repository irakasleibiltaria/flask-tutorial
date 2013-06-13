from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'Username: %s' % username

@app.route('/postid/<int:postid>')
def show_user_profile(postid):
    return 'Post id: %d' % postid


if __name__ == '__main__':
    app.debug = True
    app.run()
    # app.run(host='0.0.0.0')