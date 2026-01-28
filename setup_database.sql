CREATE TABLE flight_prices (
    City VARCHAR (255) NOT NULL,
    Month VARCHAR(255) NOT NULL,
    Avg_Price DECIMAL (10,2) NOT NULL,
    PRIMARY KEY (City, Month)
    );
