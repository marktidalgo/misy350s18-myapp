from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # return "hello friend"
    return render_template('index.html')


@app.route('/users/<string:username>')
def users(username):
    #return "<h1>hello %s</h1>" % username
    return render_template('users.html', uname=username)



@app.route('/form')
def form_basics():
        # return "hello friend"
    return render_template('form.html')

@app.route('/submit-form')
def form_submit():
        # return "hello friend"
    return render_template('submit-form.html')


if __name__ == '__main__':
    app.run()
