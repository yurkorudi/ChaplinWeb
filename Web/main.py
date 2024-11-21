from flask import *
from user_agents import *
from flask_sqlalchemy import SQLAlchemy



from extensions import db
from models import Image, User, Cinema, Session, Film, Seat, Ticket
from modules import *



app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://zulu:zuludf345@64.225.100.209:3306/chaplin"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)



with app.app_context():
    add_user(phone_number='34', first_name="Yura", last_name="Walker", email="Walker@gmail.com", login="Walker", password="4fvh38d",bought_tickets_summary=149)
    print(get_user())




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
    return 



@app.route('/home')
def homepage():
    global user_location
    global cities
    global user_device


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
    


@app.route('/movie')
def movie():
    global user_location
    global user_device
    global json
    film_name = request.args.get('movie_name')
    my_file = JSN(json=json, filepath='Web/mdb.json', type="0")
    movie = Film(filmname=film_name, json_file=my_file.dirty_data, city='lviv')


    if user_location == []:
        a = location()

    return render_template('Movie.html', city = "", cities = cities, movie_info = movie.ret_filmfile())
        


@app.route('/About.html')
def about():
    return render_template('About.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)