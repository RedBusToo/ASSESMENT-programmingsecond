from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title = 'Home', description='This is the home page')

#@app.route('/about')
#def about():
#    return render_template('about.html', title='About', description='This is a simple Flask web app.')

if __name__ == '__main__':
    app.run(debug=True)