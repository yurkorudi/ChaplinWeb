from extensions import db
from models import *
from flask import jsonify, request




def get_user():
    users = User.query.all()
    result = [{"phone_number": u.phone_number, "name": f"{u.first_name} {u.last_name}", "tickets": u.bought_tickets_summary} for u in users]
    print(result)
    print("*******************************************************************************************")
    return result





    
def add_user(first_name, last_name, phone_number, email, login, password, bought_tickets_summary):
    try:
        new_user = User(
        phone_number=phone_number,
        first_name=first_name,
        last_name=last_name,
        email=email,
        login=login,
        password=password,
        bought_tickets_summary=bought_tickets_summary,
        date_of_creation=datetime.now()
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User added successfully"}), 201
    
    except Exception as e:
        db.session.rollback() 
        print(str(e))
        return jsonify({"error": str(e)}), 500




