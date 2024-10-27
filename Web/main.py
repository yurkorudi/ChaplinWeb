from flask import *

app = Flask(__name__)

cities = {
    "lviv":"Львів",
    "mor":"Моршин",
    "dol":"Долина",
    "oks":"Оксана",
}

@app.route('/')
def homepage():
    print("===", request.args)
    location = request.args.get('location')
    print ("LocatioN: " + str(location))

    return render_template('Homepage.html', city="", cities=cities)


@app.route('/home')
def location():
    print("===", request.args)
    location = request.args.get('location')
    city = ""
    if location:
        city = cities[location]
    print ("----- LocatioN: " + str(location))

    return render_template('Homepage.html', city=city, cities=cities)







@app.route('/Movies.html')
def movies():
    return render_template('Movies.html')

@app.route('/About.html')
def about():
    return render_template('About.html')


if __name__ == '__main__':
    app.run(debug=True)     