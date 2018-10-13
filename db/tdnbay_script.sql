create database tdnbay;

use tdnbay;


create table mediafile (
id int primary key auto_increment,
filename varchar(500) unique,
filetitle varchar(100),
filethumb varchar(500) unique,
fileviews int
);


