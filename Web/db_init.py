from datetime import date
from testmain import db, Employee, app


with app.app_context():
    db.drop_all()
    db.create_all()

e1 = Employee(firstname='John',
              lastname='Doe',
              email='jd@example.com',
              age=32,
              hire_date=date(2012, 3, 3),
              active=True
              )

e2 = Employee(firstname='Mary',
              lastname='Doe',
              email='md@example.com',
              age=38,
              hire_date=date(2016, 6, 7),
              active=True
              )

e3 = Employee(firstname='Jane',
              lastname='Tanaka',
              email='jt@example.com',
              age=32,
              hire_date=date(2015, 9, 12),
              active=False
              )

e4 = Employee(firstname='Alex',
              lastname='Brown',
              email='ab@example.com',
              age=29,
              hire_date=date(2019, 1, 3),
              active=True
              )

e5 = Employee(firstname='James',
              lastname='White',
              email='jw@example.com',
              age=24,
              hire_date=date(2021, 2, 4),
              active=True
              )

e6 = Employee(firstname='Harold',
              lastname='Ishida',
              email='hi@example.com',
              age=52,
              hire_date=date(2002, 3, 6),
              active=False
              )

e7 = Employee(firstname='Scarlett',
              lastname='Winter',
              email='sw@example.com',
              age=22,
              hire_date=date(2021, 4, 7),
              active=True
              )

e8 = Employee(firstname='Emily',
              lastname='Vill',
              email='ev@example.com',
              age=27,
              hire_date=date(2019, 6, 9),
              active=True
              )

e9 = Employee(firstname='Mary',
              lastname='Park',
              email='mp@example.com',
              age=30,
              hire_date=date(2021, 8, 11),
              active=True
              )


with app.app_context():
    db.session.add_all([e1, e2, e3, e4, e5, e6, e7, e8, e9])
    db.session.commit()