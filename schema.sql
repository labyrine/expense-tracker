CREATE TABLE users (
   id SERIAL PRIMARY KEY,
   username TEXT UNIQUE,
   password TEXT
);
CREATE TABLE income_categories (
   id SERIAL PRIMARY KEY,
   income_name TEXT UNIQUE
);
CREATE TABLE income (
   id SERIAL PRIMARY KEY,
   user_id INTEGER REFERENCES users(id),
   date DATE,
   amount DECIMAL,
   income_category TEXT REFERENCES income_categories(income_name),
   description TEXT
);
CREATE TABLE expense_categories (
   id SERIAL PRIMARY KEY,
   expense_name TEXT UNIQUE
);
CREATE TABLE expenses (
   id SERIAL PRIMARY KEY,
   user_id INTEGER REFERENCES users(id),
   date DATE,
   amount DECIMAL,
   expense_category TEXT REFERENCES expense_categories(expense_name),
   description TEXT
);

INSERT INTO income_categories (income_name) 
VALUES ('Muu');
INSERT INTO income_categories (income_name) 
VALUES ('Asumistuki');
INSERT INTO income_categories (income_name) 
VALUES ('Opintotuki');
INSERT INTO income_categories (income_name) 
VALUES ('Palkka');

INSERT INTO expense_categories (expense_name) 
VALUES ('Muu');
INSERT INTO expense_categories (expense_name) 
VALUES ('Asuminen');
INSERT INTO expense_categories (expense_name) 
VALUES ('Elektroniikka');
INSERT INTO expense_categories (expense_name) 
VALUES ('Herkut');
INSERT INTO expense_categories (expense_name) 
VALUES ('Hygienia');
INSERT INTO expense_categories (expense_name) 
VALUES ('Kodintarvikkeet');
INSERT INTO expense_categories (expense_name) 
VALUES ('Lahjat');
INSERT INTO expense_categories (expense_name) 
VALUES ('Liikenne');
INSERT INTO expense_categories (expense_name) 
VALUES ('Matkustaminen');
INSERT INTO expense_categories (expense_name) 
VALUES ('Ruoka');
INSERT INTO expense_categories (expense_name) 
VALUES ('Terveys');
INSERT INTO expense_categories (expense_name) 
VALUES ('Ulkona syöminen');
INSERT INTO expense_categories (expense_name) 
VALUES ('UniCafe');
INSERT INTO expense_categories (expense_name) 
VALUES ('Vaatteet ja asusteet');
INSERT INTO expense_categories (expense_name) 
VALUES ('Viihde');
INSERT INTO expense_categories (expense_name) 
VALUES ('Yleiset ostokset');
