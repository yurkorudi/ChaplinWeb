from flask import *
from user_agents import *
from flask_sqlalchemy import SQLAlchemy



from extensions import db
from models import Image, User, Cinema, Session, Film, Seat, Ticket
from funcs import *



app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://zulu:zuludf345@64.225.100.209:3306/chaplin"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)



with app.app_context():
    print(list_to_dict(get_users()))

def create_sample_data():
    with app.app_context():
        add_image(type="Poster", path="/images/poster1.jpg")
        add_image(type="Poster", path="/images/poster2.jpg")
        add_image(type="Thumbnail", path="/images/thumb1.jpg")
        add_image(type="Thumbnail", path="/images/thumb2.jpg")


        add_user(phone_number="1234567890", first_name="John", last_name="Doe",
                email="john.doe@example.com", login="johndoe", password="password123", bought_tickets_summary=3)
        add_user(phone_number="0987654321", first_name="Jane", last_name="Smith",
                email="jane.smith@example.com", login="janesmith", password="password456", bought_tickets_summary=5)
        add_user(phone_number="1122334455", first_name="Alice", last_name="Brown",
                email="alice.brown@example.com", login="alicebrown", password="password789", bought_tickets_summary=1)
        add_user(phone_number="5566778899", first_name="Bob", last_name="Johnson",
                email="bob.johnson@example.com", login="bobjohnson", password="password101", bought_tickets_summary=2)


        add_cinema(name="Grand Cinema", location="123 Main St, Cityville",
                contact_phone_number="555-1234", work_schedule="10:00 AM - 11:00 PM", instagram_link="https://instagram.com/grandcinema")
        add_cinema(name="Elite Theaters", location="456 Broadway Ave, Metropolis",
                contact_phone_number="555-5678", work_schedule="9:00 AM - 12:00 AM", instagram_link="https://instagram.com/elitetheaters")
        add_cinema(name="Movie Palace", location="789 Oak Lane, Smalltown",
                contact_phone_number="555-9012", work_schedule="11:00 AM - 10:00 PM", instagram_link="https://instagram.com/moviepalace")
        add_cinema(name="Galaxy Screens", location="101 Star Rd, Universe City",
                contact_phone_number="555-3456", work_schedule="8:00 AM - 1:00 AM", instagram_link="https://instagram.com/galaxyscreens")


        add_film(name="Action Blast", genre="Action", description="An explosive action-packed adventure.",
                release_start_date=datetime(2023, 5, 1), release_end_date=datetime(2023, 7, 1), director="Michael Bay",
                actors="Actor A, Actor B", duration=120, image_id=1)
        add_film(name="Romantic Escape", genre="Romance", description="A heartfelt love story.",
                release_start_date=datetime(2023, 6, 1), release_end_date=datetime(2023, 8, 1), director="Nancy Meyers",
                actors="Actor C, Actor D", duration=110, image_id=2)
        add_film(name="Comedy Night", genre="Comedy", description="A laugh-out-loud comedy.",
                release_start_date=datetime(2023, 7, 1), release_end_date=datetime(2023, 9, 1), director="Judd Apatow",
                actors="Actor E, Actor F", duration=100, image_id=3)
        add_film(name="Thriller Time", genre="Thriller", description="An edge-of-your-seat thriller.",
                release_start_date=datetime(2023, 8, 1), release_end_date=datetime(2023, 10, 1), director="David Fincher",
                actors="Actor G, Actor H", duration=130, image_id=4)


        add_session(film_id=1, cinema_id=1, session_datetime=datetime(2023, 5, 10, 18, 0), session_duration=120)
        add_session(film_id=2, cinema_id=2, session_datetime=datetime(2023, 6, 15, 20, 0), session_duration=110)
        add_session(film_id=3, cinema_id=3, session_datetime=datetime(2023, 7, 20, 19, 0), session_duration=100)
        add_session(film_id=4, cinema_id=4, session_datetime=datetime(2023, 8, 25, 21, 0), session_duration=130)


        add_seat(session_id=1, row=1, busy=False)
        add_seat(session_id=1, row=2, busy=True)
        add_seat(session_id=2, row=1, busy=False)
        add_seat(session_id=2, row=2, busy=True)


        add_ticket(user_phone_number="1234567890", seat_id=1, session_id=1)
        add_ticket(user_phone_number="0987654321", seat_id=2, session_id=1)
        add_ticket(user_phone_number="1122334455", seat_id=3, session_id=2)
        add_ticket(user_phone_number="5566778899", seat_id=4, session_id=2)
    print("created!")


create_sample_data()




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
        


@app.route('/about')
def about():
    global user_location
    global cities
    global user_device
    return render_template('About.html', city = "", cities = cities)


@app.route('/book', methods=['POST'])
def book():
    global user_location
    global user_device
    global json
    film_name = request.args.get('movie_name')
    my_file = JSN(json=json, filepath='Web/mdb.json', type="0")
    movie = Film(filmname=film_name, json_file=my_file.dirty_data, city='lviv')


    if user_location == []:
        a = location()

    return render_template('Booking.html', city = "", cities = cities, movie_info = movie.ret_filmfile())


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)