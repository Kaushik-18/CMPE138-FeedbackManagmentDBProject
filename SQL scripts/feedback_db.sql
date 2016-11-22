DROP DATABASE IF EXISTS cmpe138_project_team3_feedback;
CREATE DATABASE cmpe138_project_team3_feedback;
USE cmpe138_project_team3_feedback;

CREATE TABLE customer
(
  customer_id INT(15) PRIMARY KEY AUTO_INCREMENT,
  f_name      VARCHAR(50) NOT NULL,
  l_name      VARCHAR(50) NOT NULL
);

CREATE TABLE product
(
  product_id   INT(15) PRIMARY KEY AUTO_INCREMENT,
  product_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE service
(
  service_id   INT(15) PRIMARY KEY AUTO_INCREMENT,
  service_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE service_feedback
(
  service_feedback_id INT(15) PRIMARY KEY AUTO_INCREMENT,
  ratings             INT(2),
  comments            VARCHAR(500),
  customer_id         INT(15),
  service_id          INT(15),
  franchise_id        INT(15),
  FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
    ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES service (service_id)
    ON DELETE CASCADE
);

CREATE TABLE product_feedback
(
  product_feedback_id INT(15) PRIMARY KEY AUTO_INCREMENT,
  ratings             INT(2),
  customer_id         INT(15),
  product_id          INT(15),
  comments            VARCHAR(500),
  franchise_id        INT(15),
  FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
    ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES product (product_id)
    ON DELETE CASCADE
);

CREATE TABLE employee
(
  employee_id  INT(15) PRIMARY KEY AUTO_INCREMENT,
  f_name       VARCHAR(50) NOT NULL,
  l_name       VARCHAR(50) NOT NULL,
  franchise_id INT(15)     NOT NULL,
  manager_id   INT(15)     NULL
);

CREATE TABLE franchise
(
  franchise_id INT(15) PRIMARY KEY AUTO_INCREMENT,
  name         VARCHAR(100) NOT NULL,
  st_address   VARCHAR(200) NOT NULL,
  address      VARCHAR(50)  NULL,
  city         VARCHAR(50)  NOT NULL,
  state        VARCHAR(50)  NOT NULL,
  zip          NUMERIC(5)   NOT NULL,
  manager_id   INT(15)      NULL,
  FOREIGN KEY (manager_id) REFERENCES employee (employee_id)
);

CREATE TABLE sold_by
(
  product_id   INT(15) NOT NULL,
  franchise_id INT(15) NOT NULL,
  FOREIGN KEY (product_id) REFERENCES product (product_id),
  FOREIGN KEY (franchise_id) REFERENCES franchise (franchise_id)
);

CREATE TABLE service_provided_by
(
  service_id  INT(15) NOT NULL,
  employee_id INT(15) NOT NULL,
  FOREIGN KEY (service_id) REFERENCES service (service_id)
    ON DELETE CASCADE,
  FOREIGN KEY (employee_id) REFERENCES employee (employee_id)
);

CREATE TABLE action_items
(
  action_item_id      INT(15) PRIMARY KEY AUTO_INCREMENT,
  start_date          DATETIME NOT NULL,
  end_date            DATETIME NOT NULL,
  action_status       INT(15)  NOT NULL   DEFAULT 0,
  created_by          INT(15)  NOT NULL,
  assigned_to         INT(15)  NOT NULL,
  comments            VARCHAR(300),
  service_feedback_id INT(15)  NULL ,
  product_feedback_id INT(15)  NULL ,
  FOREIGN KEY (service_feedback_id) REFERENCES service_feedback (service_feedback_id),
  FOREIGN KEY (product_feedback_id) REFERENCES product_feedback (product_feedback_id),
  FOREIGN KEY (created_by) REFERENCES employee (employee_id),
  FOREIGN KEY (assigned_to) REFERENCES employee (employee_id)
);

ALTER TABLE cmpe138_project_team3_feedback.employee
  ADD CONSTRAINT
FOREIGN KEY (franchise_id) REFERENCES franchise (franchise_id);