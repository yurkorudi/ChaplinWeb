from flask import * 

from models import db, User
from config import Config



app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy
db.init_app(app)

# Create the database tables
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# Route to add a new user
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    new_user = User(name=data["name"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully"}), 201

# Route to fetch all users
@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name, "email": user.email} for user in users])

# Route to fetch a single user by ID
@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({"id": user.id, "name": user.name, "email": user.email})

if __name__ == "__main__":
    app.run(debug=True)