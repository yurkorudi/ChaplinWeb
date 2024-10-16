from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('Homepage.html')

@app.route('/Movies.html')
def movies():
    return render_template('Movies.html')

@app.route('/About.html')
def about():
    return render_template('About.html')

if __name__ == '__main__':
    app.run(debug=True)     