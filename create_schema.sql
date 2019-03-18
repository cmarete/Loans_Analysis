create database data_analysis_db;

use database data_analysis_db; 

create table members(
	member_id int not null auto_increment,
	first_name varchar(20),
    last_name varchar(20),
    address varchar(20), 
    zipcode varchar(20),
    state varchar(20),
    primary key(member_id)
);

create table loans(
	loan_id int not null auto_increment,
	loan_type varchar(20),
	term varchar(20),
	int_rate numeric,
	grade varchar(20),
	sub_grade varchar(20),
	primary key(loan_id)
); 

create table payment_plans(
    payment_plan_id int not null auto_increment,
    term varchar(20),
    primary key(payment_id)
); 

create table transactions(
	loan_id int not null,
	member_id int not null,
	payment_plan_id int,
	payment_amount bigint,
	initial_date date,
	closing_date date,
	is_active boolean,
    primary key(loan_id, member_id, payment_id)
);

create table payments(
	payment_id int not null,
	payment_plan_id int,
	transaction_id int not null,
	scheduled_date date,
	closing_date date,
    primary key(payment_id)
); 

