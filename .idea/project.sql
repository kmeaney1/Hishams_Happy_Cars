
CREATE TABLE seller(
   employee_id integer PRIMARY KEY,
   password integer,
   name varchar(50),
   phone_number varchar(50),
   email_addr varchar(50)
);

CREATE TABLE sellment(
   seller_id integer,
   car_VIN integer,
   customer_id integer,
   date varchar(50),
   PRIMARY KEY (seller_id,car_VIN,customer_id)
);

CREATE TABLE customer(
   user_id integer PRIMARY KEY,
   password integer,
   name varchar(50),
   phone_number varchar(50),
   email_addr varchar(50)
);

CREATE TABLE wish_list(
   customer_id integer,
   car_vin integer,
   PRIMARY KEY (car_vin,customer_id)
);

CREATE TABLE car(
   VIN integer PRIMARY KEY,
   car_model varchar(50),
   price integer,
   year integer,
   car_body_style varchar(50),
   number_of_doors integer,
   drive_wheel varchar(50),
   car_length float,
   car_width float,
   car_height float,
   horse_power integer,
   recall_record integer
);

CREATE TABLE recall(
   car_VIN integer PRIMARY KEY,
   date varchar(50),
   is_fixed varchar(50)
);


--insert into car values(1,"alfa-romero giulia",13495,2022,"convertible",2,"rwd",168.8,64.1,48.8,111,0);