
-- Stored Prcoedure Code
DELIMITER //
CREATE PROCEDURE deletion (IN car_vin integer)
	BEGIN
    delete from car where VIN = car;
    END //

DELIMITER ;



-- delete the specific car with car_vin when calling the stored procedure
-- call delete(@car_vin);

