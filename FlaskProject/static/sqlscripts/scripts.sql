create table users ('ID' integer primary key autoincrement , 'FirstName' varchar(50), 'MiddleName' varchar(50), 'LastName' varchar(50),'Email' varchar(50), Password varchar(50), 'Role' bit); 
create table bookings ('ID' integer primary key autoincrement ,'Email' varchar(50),'Place' varchar(100), 'Date' TimeStamp Default Current_Timestamp, 'Remarks' varchar(100));