INSERT INTO customer(customer.f_name,customer.l_name) VALUES 
("first","customer"),
("second","customer");

INSERT INTO product(product.product_name) VALUES 
("pr1"),
("pr2");

INSERT INTO service(service.service_name) VALUES
("serv1"),
("serv2");


INSERT INTO franchise(franchise.name,st_address,address,city,state,zip) VALUES
("f1","s1","ad1","san jose","ca","222"),
("f2","s2","ad2","san jose","ca","223");


INSERT INTO employee(employee.f_name,employee.l_name,employee.franchise_id,employee.manager_id) VALUES
("e1","fir",1,4),
("e2","sec",2,5),
("e3","third",2,5),
("m1","m1",2,null),
("m2","m2",2,null);


INSERT INTO service_provided_by(service_provided_by.service_id,service_provided_by.employee_id) VALUES
(1,1),
(1,2),
(2,3);














