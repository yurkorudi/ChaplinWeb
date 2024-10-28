from flask import *

app = Flask(__name__)

cities = {
    "lviv":"Львів",
    "mor":"Моршин",
    "dol":"Долина",
    "oks":"Оксана",
}
user_location = []


def location():
    global user_location
    global cities
    if user_location == []:
        print("===", request.args)
        location = request.args.get('location')
        city = ""
        if location:
            city = cities[location]
            print ("----- LocatioN: " + str(location))
            user_location.append(city)
            user_location.append(cities)

        print ("----- >>", user_location)
    return 



@app.route('/home')
def homepage():
    global user_location
    global cities
    if user_location == []:
        a = location()
        user_location.append(a[0])
        user_location.append(a[1])
        return render_template('Homepage.html', city=user_location[0], cities=user_location[1])
    else:
        return render_template('Homepage.html', city = "", cities = cities)




@app.route('/movies')
def movies():
    global user_location
    if user_location == []:
        a = location()
    return render_template('Movies.html', city=user_location[0], cities=user_location[1])




@app.route('/About.html')
def about():
    return render_template('About.html')


if __name__ == '__main__':
    app.run(debug=True)     