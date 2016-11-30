SET FOREIGN_KEY_CHECKS =0;



#product feedback
INSERT INTO product_feedback (product_feedback_id,franchise_id,customer_id,product_id,ratings,comments) VALUES 
(1,3,10008,20003,2,"Cant find the right size of bag , too small or too big for me."),
(2,1,10005,20003,1,"quality of Pokemon bags not appealing"),
(3,5,10009,20001,2,"Jeans variant 511 doesnt have good fitting"),
(4,2,10004,20008,2,"not enough variety in jackets for ladies"),
(5,5,10006,20009,3,"please keep round hats in store"),
(6,3,10006,20001,2,"I was looking to buy jeans from your store, but the designs are just to plain, please let me know when there are new variants available"),
(7,5,10008,20002,4,"Belts for Indian functions not value for money. I love your store , but some prices on Belts are just outrageous."),
(8,5,10002,20000,4,"long wait period for custom tops order. Please try to make it before 17th of this month"),
(9,5,10005,20008,5,"Love your jackets, when do youll go on sale?"),
(10,2,10001,20009,5,"Hats Off!!!");

#1,2,3,4,6

#product
INSERT INTO product (product.product_id,product.product_name) VALUES (20000,"Tops"),(20001,"Jeans"),(20002,"Belts"),(20003,"Bags"),(20004,"bandanas"),(20005,"skirts"),(20006,"Kurtis"),(20007,"jewellery"),(20008,"jackets"),(20009,"hats");



#service
INSERT INTO service (service.service_id,service.service_name) VALUES (1,"Billing Desk"),(2,"Sales Representative"),(3,"Security Personal"),(4,"Designer"),(5,"Cleaner"),(6,"Rack Helpers");

#service feedback
INSERT INTO service_feedback (service_feedback.service_feedback_id,service_feedback.franchise_id,service_feedback.customer_id,service_feedback.service_id,service_feedback.ratings,service_feedback.comments) VALUES 
(1,4,10001,3,3,"Lack of security and scrutiny, just saw some spit in the corner in the store"),
(2,2,10007,3,1,"You do see some fishy people in store"),
(3,1,10004,2,3,"I found you sales representative to be not upto the mark. He could not find the design i was looking for , and was eventually found by the manager"),
(4,4,10007,3,4,"The billing desk lady was not ready to accept my 100 dollar bill."),
(5,4,10004,5,4,"The store had some fishy smell in one corner"),
(6,1,10007,4,5,"No enough designs available in belts"),
(7,4,10001,5,1,"I could smell a dead rat somewhere"),
(8,4,10007,2,1,"There is too long a wait at the billing counter. And then i have spent extra time, writing this review"),
(9,3,10007,5,5,"My baby puked, but the cleaner cleant the stop promptly. A word of appreciation to him from myside"),
(10,2,10007,2,3,"Too long a queue for a clothing store :( "),
(11,4,10001,3,3,"long queues and slow cashiers");


#action item
INSERT INTO action_items (action_items.action_item_id,action_items.start_date,action_items.end_date,action_items.action_status,action_items.created_by,action_items.assigned_to,action_items.comments,action_items.product_feedback_id,action_items.service_feedback_id) VALUES 
(1,"2015-12-13 ","2016-01-20",1,20001,20013,"Improve rating till next quarter",null,1),
(2,"2015-11-17 ","2016-03-27",1,20002,20018,"Improve rating till next quarter",2,null),
(3,"2016-12-25 ","2017-03-14",0,20004,20028,"Improve rating till next quarter",7,null),
(4,"2015-10-30 ","2016-02-21",1,20004,20026,"Improve rating till next quarter",8,null),
(5,"2015-12-18 ","2016-03-23",1,20000,20009,"Improve rating till next quarter",null,2),
(6,"2015-12-12 ","2016-02-19",1,20000,20007,"Improve rating till next quarter",null,3),
(7,"2015-11-29 ","2016-03-29",1,20000,20006,"Improve rating till next quarter",null,4),
(8,"2016-11-15 ","2017-02-16",0,20000,200010,"Improve rating till next quarter",null,6);





#sold by
INSERT INTO sold_by (sold_by.product_id,sold_by.franchise_id) VALUES (20008,1),(20008,4),(20009,1),(20004,5),(20001,2),(20001,4),(20005,1),(20002,2),(20003,1);

#service provided by
INSERT INTO service_provided_by (service_provided_by.service_id,service_provided_by.employee_id) VALUES (4,20014),(6,20010),(1,20013),(6,20018),(3,20017),(4,20019),(5,20017),(6,20010),(4,20010),(1,20013);
INSERT INTO service_provided_by (service_provided_by.service_id,service_provided_by.employee_id) VALUES (4,20008),(1,20008),(3,20008),(1,20016),(2,20007),(4,20008),(2,20013),(2,20008),(1,20016),(2,20010);

#customer
INSERT INTO customer (customer.customer_id,customer.f_name,customer.l_name) VALUES (10000,"Uriel","Riggs"),(10001,"Molly","Goff"),(10002,"Tana","Jimenez"),(10003,"Lacy","Blackburn"),(10004,"Abraham","Greer"),(10005,"Zachery","Mccoy"),(10006,"Tasha","Moon"),(10007,"Jackson","George"),(10008,"Christian","Vaughn"),(10009,"Lucius","Cook");




#franchise
INSERT INTO franchise
(franchise.name,franchise_id,franchise.address,franchise.st_address,franchise.city,franchise.state,franchise.zip,franchise.manager_id) VALUES 
("San Jose Downtown",1,"Ap #876","9811 Risus. Av.","San Jose","California","94555",20000),
("Sunnyvale Temple",2,"638","830 Lacinia. Av.","Sunnyvale","California","94734",20001),
("University Local",3,"173","661-4917 Nec, Rd.","Dallas","Texas","73301",20002),
("Lake Mall",4,"213"," 4771 Nisl Ave","Austin","Texas","73298",20003),
("Business District Shopee",5,"868"," 3256 Eure Road","San Fransisco","California","95061",20004);


#employee
INSERT INTO employee  (employee.employee_id,employee.f_name,employee.l_name,employee.franchise_id,employee.manager_id) VALUES 


(20000,"Madhur","Khandelwal",1,null),
(20001,"Keyur","Golani",2,null),
(20002,"Kaushik","Shingane",3,null),
(20003,"Gurnoor","Singh",4,null),
(20004,"Suraj","Khurana",5,null),
(20005,"jackie","coo",1,2000),
(20006,"Jerome","Carr",1,20000),
(20007,"Dawn","Hopper",1,20000),
(20008,"Christian","Haley",1,20000),
(20009,"Taylor","Larsen",1,20000),
(20010,"Christine","Conrad",1,20000),
(20011,"Maite","Compton",2,20001),
(20012,"Frances","Moody",2,20001),
(20013,"Fallon","Gilbert",2,20001),
(20014,"Evangeline","Kim",2	,20001),
(20015,"Ria","Colon",2,20001),
(20016,"Oren","Burt",3,20002),
(20017,"Hasad","Holland",3,20002),
(20018,"Charissa","Mooney",3,20002),
(20019,"Emma","Stephens",3,20002),
(20020,"Wilter","White",3,20002),
(20021,"Kareb","Brute",4,20003),
(20022,"Holland","Freeman",4,20003),
(20023,"Charlotte","Miney",4,20003),
(20024,"Barani","Win",4,20003),
(20025,"Chritina","lauren",4,20003),
(20026,"Bluebor","Benskey",5,20004),
(20027,"Janhavi","Thakkar",5,20004),
(20028,"Narendra","Modi",5,20004),
(20029,"Shin","Lucre",5,20004),
(20030,"Mclaughlin","Storyman",5,20004);



#logins
INSERT INTO logins VALUES  -- duty of application to check if given ID actually exists in the given entiy_type table
("employee", 20000, "mgrpass0"),
("employee", 20001, "mgrpass1"),
("employee", 20002, "mgrpass2"),
("employee", 20003, "mgrpass3"),
("employee", 20004, "mgrpass4"),
("employee", 20005, "mgrpass5");

SET FOREIGN_KEY_CHECKS=1;

INSERT INTO service_feedback (service_feedback.service_feedback_id,service_feedback.franchise_id,service_feedback.customer_id,service_feedback.service_id,service_feedback.ratings,service_feedback.comments) 
VALUES (14,4,10001,3,3,"long queues and slow cashiers");

INSERT INTO action_items (action_items.start_date,action_items.end_date,action_items.action_status,action_items.created_by,action_items.assigned_to,action_items.comments,action_items.product_feedback_id,action_items.service_feedback_id)
VALUES ("2015-12-13", "2016-01-20",1, 20001, 20013, "Improve rating till next quarter", 1, NULL );

INSERT INTO action_items (action_items.start_date,action_items.end_date,action_items.action_status,action_items.created_by,action_items.assigned_to,action_items.comments,action_items.product_feedback_id,action_items.service_feedback_id)
VALUES ("2014-12-13", "2015-01-15",0, 20001, 20013, "Improve rating till next year", 1, NULL );
