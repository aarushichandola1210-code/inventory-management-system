CREATE DATABASE IF NOT EXISTS inventory_db;
USE inventory_db;

CREATE TABLE IF NOT EXISTS products (
    ProductID VARCHAR(10) PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Supplier VARCHAR(100),
    Price DECIMAL(10,2),
    Quantity INT,
    PurchaseDate DATE
);

INSERT INTO products VALUES 
('P001','Wireless Mouse','Accessories','GlobalTech',15.99,50,'2025-01-10'),
('P002','Keyboard','Accessories','GlobalTech',25.49,40,'2025-01-12'),
('P003','Monitor','Electronics','DisplayCorp',150.00,20,'2025-02-01'),
('P004','USB Cable','Accessories','CablePro',5.99,100,'2025-01-15'),
('P005','External HDD 1TB','Storage','DataKeep',40.00,35,'2025-03-01'),
('P006','128GB USB Drive','Storage','FlashStore',3.50,200,'2025-03-05'),
('P007','Laptop Backpack','Accessories','CarryAll',10.00,15,'2025-01-25'),
('P008','Webcam HD','Peripherals','VisionX',18.00,10,'2025-02-18'),
('P009','Office Chair','Furniture','ComfortCorp',45.00,12,'2025-02-28'),
('P010','Desk Lamp','Lighting','LightHouse',7.20,12,'2025-03-10'),
('P011','Router','Networking','NetWave',20.00,6,'2025-02-07'),
('P012','Switch 8-Port','Networking','NetWave',12.50,5,'2025-03-02'),
('P013','SSD 512GB','Storage','DataKeep',45.00,22,'2025-03-15'),
('P014','HDMI Cable','Cables','CableWorks',2.00,40,'2025-01-30'),
('P015','Graphic Tablet','Peripherals','DrawPro',30.00,8,'2025-03-20'),
('P016','Surge Protector','Accessories','PowerSafe',6.00,20,'2025-02-23'),
('P017','CPU Cooler','Components','CoolTech',10.00,10,'2025-03-18');




