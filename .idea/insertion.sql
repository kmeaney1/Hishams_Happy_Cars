-- Stored Prcoedure Code
DELIMITER //
CREATE PROCEDURE insertion (IN VIN integer, car_model varchar(50),
   price integer,
   year integer,
   car_body_style varchar(50),
   number_of_doors integer,
   drive_wheel varchar(50),
   car_length float,
   car_width float,
   car_height float,
   horse_power integer,
   recall_record integer)
    BEGIN
	insert into car values(VIN,car_model,price,year,
   car_body_style,
   number_of_doors,
   drive_wheel,
   car_length,
   car_width,
   car_height,
   horse_power,
   recall_record)
    END //
DELIMITER ; 

-- Calling insert
-- call insert(info_of_car);