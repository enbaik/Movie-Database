DROP DATABASE CSS498_Project;

CREATE DATABASE CSS498_Project;

USE CSS498_Project;

CREATE TABLE Movies
(
MovieId INT NOT NULL UNIQUE,
Title VARCHAR(20) NOT NULL,
Genre VARCHAR(80) NOT NULL,
MovieYear INT,
NoGenre INT,
ActionF INT,
Adventure INT,
Animation INT,
Children INT,
Comedy INT,
Crime INT,
Document INT,
Drama INT,
Fantasy INT,
FilmNoir INT,
Horror INT,
IMAX INT,
Musical INT,
Mystery INT,
Romance INT,
SciFi INT,
Thriller INT,
War INT,
Western INT,
PRIMARY KEY(MovieId)
);



CREATE TABLE Clients
(
ClientId INT NOT NULL UNIQUE,
FirstName VARCHAR(20) NOT NULL,
LastName VARCHAR(20) NOT NULL,
PrimaryPhone BIGINT NOT NULL UNIQUE,
PRIMARY KEY(ClientId),
CONSTRAINT Phone_range CHECK (PrimaryPhone BETWEEN 1000000000 and 9999999999)
);

CREATE TABLE Rentals 
(
ClientId INT NOT NULL,
MovieId INT NOT NULL,
Rental_Date DATE NOT NULL,
PRIMARY KEY(ClientId,MovieId),
FOREIGN KEY(MovieId) REFERENCES Movies(MovieId),
FOREIGN KEY(ClientId) REFERENCES Clients(ClientId)
);