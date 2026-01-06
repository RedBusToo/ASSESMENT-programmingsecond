from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title = 'Home', description='This is the home page')

@app.route('/findUs')
def about():
    return render_template('findUs.html', title='Find_Us', description='This is the page to find our campus location.')

@app.route('/courses')
def course():
    return render_template('courses.html', title='Courses', description='This page shows our main courses!')

if __name__ == '__main__':
    app.run(debug=True)