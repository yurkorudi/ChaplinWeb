from flask import *
from user_agents import parse
import json
from modls import JSN


app = Flask(__name__)



cities = {
    "lviv":"Львів",
    "mor":"Моршин",
    "dol":"Долина",
    "oks":"Оксана",
}
user_location = []
user_device = 'None'


@app.route('/')
def early_start ():
    global user_device
    user_agent = parse(request.headers.get('User-Agent'))
    if user_agent.is_mobile:
        user_device = "android"
    else:
        user_device = "desktop"

    return redirect(url_for('homepage'))




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
            #user_location.append(city)
            #user_location.append(cities)

        print ("----- >>", user_location)
    return 





@app.route('/home')
def homepage():
    global user_location
    global cities
    global user_device
    if user_device == 'desktop':
        print ('desktop version')
        return render_template('Homepage.html', city = "", cities = cities)
    else:
        print ('mobile version')
        return render_template('Homepage.html', city = "", cities = cities)




@app.route('/movies')
def movies():
    global user_location
    global user_device
    if user_location == []:
        a = location()
    if user_device == 'desktop':
        print ('desktop version')
        return render_template('Movies.html', city = "", cities = cities)
    else: 
        print ('mobile version')
        return render_template('Movies.html', city = "", cities = cities)
    
@app.route('/transformers')
def transformers():
    global user_location
    global user_device
    global json
    minifile = JSN(json=json, filepath='../Web/mdb.json', type="list")
    films = minifile.city(cityname='lviv')
    film = minifile.film(str(films[1]))


    if user_location == []:
        a = location()
    if user_device == 'desktop':
        print ('desktop version')
        return render_template('Transformers.html', city = "", cities = cities)
    else: 
        print ('mobile version')
        return render_template('Transformers.html', city = "", cities = cities)
        



@app.route('/About.html')
def about():
    return render_template('About.html')


if __name__ == '__main__':
    app.run(debug=True, host= '127.0.0.1')     