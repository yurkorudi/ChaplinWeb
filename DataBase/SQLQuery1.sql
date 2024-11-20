use Chaplin

-- Create user's table -- 
create table Users(
first_name VARCHAR(100) NOT NULL,
last_name VARCHAR(100) NOT NULL,
phone_number VARCHAR(15) NOT NULL primary key,
email varchar(100) not null unique,
user_login varchar(100) not null unique,
user_password varchar(100),
avatar image,
CONSTRAINT valid_phone_number CHECK (phone_number NOT LIKE '%[^0-9]%')
);

drop table Users;

-- Create cinema's table
create table Cinema(
id int NOT NULL primary key,
name VARCHAR(100) NOT NULL,
location VARCHAR(100) NOT NULL,
contact_phone_number varchar(100) not null unique,
work_schedule varchar(100),
pictures BLOB,
CONSTRAINT valid_contact_phone_number CHECK (contact_phone_number NOT LIKE '%[^0-9]%')
);

drop table Cinema;

-- Create film's table
create table Films(
id int not null primary key,
name VARCHAR(100) NOT NULL,
extension VARCHAR(2),
ticket_price int NOT NULL,
release_start_date date,
release_end_date date,
ganre VARCHAR(100) NOT NULL,
director VARCHAR(50),
actors VARCHAR(100),
duration int NOT NULL,
description varchar(100),
license_key varchar(30),
pictures_path text
);

drop table Films;

-- Create activities's table
create table Activities(
user_email VARCHAR(100) foreign key(user_email) references Users(email),
date_of_account_creation date,
date_of_the_penultimate_login date,
date_of_the_last_login date,
visited_ganres varchar(100),
bought_tickets_number int,
cinema_id int foreign key(cinema_id) references Cinema(id)
);

drop table Activities;

-- Create schedule's table
create table Schedule_of_sessions(
id int primary key,
session_datetime datetime,
cinema_id int foreign key(cinema_id) references Cinema(id),
film_id int foreign key(film_id) references Films(id)
);

drop table Schedule_of_sessions;

-- Create seat's table
create table Seat(
seat_number int primary key,
book_datetime datetime,
cinema_id int foreign key(cinema_id) references Cinema(id)
);

drop table Seat;

-- Create ticket's table
create table Ticket(
id int primary key,
date_of_purchase date,
user_phone_number VARCHAR(15) foreign key(user_phone_number) references Users(phone_number),
session_id int foreign key(session_id) references Schedule_of_sessions(id),
seat int foreign key(seat) references Seat(seat_number),
CONSTRAINT valid_user_phone_number CHECK (user_phone_number NOT LIKE '%[^0-9]%')
);

drop table Ticket;
