drop database if exists smarttbot;

create database smarttbot;

create table smarttbot.currencies (
id int auto_increment primary key,
currency varchar(30) unique not null
);

create table smarttbot.candles (
id int auto_increment primary key,
currency_id int not null,
frequency int not null,
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
open_value int not null,
low_value int not null,
high_value int not null,
close_value int not null,
foreign key (currency_id) references currencies(id)
);

insert into smarttbot.currencies values (default, 'bitcoin'), (default, 'monero');