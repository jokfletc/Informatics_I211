CREATE TABLE Addresses
(AddressID int NOT NULL AUTO_INCREMENT,
Name varchar(50) NOT NULL,
Address1 varchar(50) NOT NULL,
Address2 varchar(50),
City varchar(20) NOT NULL,
State varchar(20) NOT NULL,
Zip varchar(10) NOT NULL,
PRIMARY KEY (AddressID)
);

INSERT INTO Addresses (Name, Address1, Address2, City, State, Zip)
VALUES('John Fletcher','5266 Brookhollow Dr','6710 Millersburgh Rd','Newburgh','IN','47630'),
('Kyler Wethler', '1610 Westward St', '210 Apt.B Colonial Dr','Greenville','IN','73125'),
('Kyler Wethler', '2400 Eastward St',NULL,'Smallville','NY','89110'),
('John Fletcher','1874 ViewPointe Ct',NULL,'Lawrenceburgh','IL','56320'),
('Cole Williams','498 Furshire Ct','3217 N Ocean Ln','Greenville','IL','6712'),
('Ellis Frame','5252 Fall Creek Rd',NULL,'Indianapolis','IN','46220')
;