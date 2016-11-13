create database cmpe138_project_team3_feedback;
use cmpe138_project_team3_feedback;

create table customer
	(customer_id	int(15) primary key AUTO_INCREMENT,
	 customer_name	varchar(100)
	);
    
create table product 
	( product_name  varchar(100),
	  product_id 	int(15) primary key AUTO_INCREMENT
 ); 
 
 create table service 
	( service_id 	 int(15) primary key AUTO_INCREMENT,
	  service_name   varchar(100)
);

create table service_feedback
(id numeric(15)  	primary key AUTO_INCREMENT,
 ratings 			int(2),
 comments 			varchar(500),
 customer_id 		int(15),
 service_id 		int(15),
 foreign key (customer_id) references customer(customer_id) on delete cascade,
 foreign key (service_id) references service(service_id) on delete cascade
 );
 
 create table product_feedback
 (id 			numeric(15) primary key AUTO_INCREMENT,
 ratings 		int(2),
 customer_id 	int(15),
 product_id 	int(15),
 foreign key   (customer_id) references customer(customer_id) on delete cascade,
 foreign key   (product_id) references product(product_id) on delete cascade
 );
 
 create table employee
 (id int(15)    primary key AUTO_INCREMENT,
  employee_name varchar(100) not null,
  franchise_id  int(15) not null,
  manager_id    int(15) null,
  foreign key (franchise_id) references franchise(id) 
 );
 
 create table franchise 
 ( id int(15)  primary key AUTO_INCREMENT,
   location    varchar(255) not null ,
   manager_id  int(15) null,
   foreign key (manager_id) references employee(id) 
 );
 
 create table sold_by
 (  product_id   int(15) not null,
    franchise_id int(15) not null,
    foreign key  (product_id) references product(product_id) on delete cascade,
	foreign key  (franchise_id) references franchise(id) 
 );
 
 create table service_provided_by
 ( service_id   int(15) not null,
   employee_id  int(15) not null,
   foreign key  (service_id) references service(service_id) on delete cascade, 
   foreign key  (employee_id) references employee(id)
 );
 
 create table action_items
 ( id                  int(15) primary key AUTO_INCREMENT,
   start_date          timestamp not null,
   end_date            timestamp not null ,
   action_status       varchar(15)not null,
   created_by          int(15) not null,
   assigned_to         int(15) not null,
   comments            varchar(300),
   service_feedback_id int(15),
   product_feedback_id int(15),
   foreign key (service_feedback_id) references service_feedback(id),
   foreign key (product_feedback_id) references product_feedback(id)
 )

