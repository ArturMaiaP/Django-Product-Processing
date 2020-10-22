# Django-Product-Processing
# URL Documentation (Endpoints).

## Engine
GET productApp/process - Process products based on the registered rules;

## Product
GET productApp/products - Return all products and their respective classifications;
GET productApp/products/new - Return a form to add a new product to the database;
POST productApp/products/new - reates a new product;

## RULES
GET productApp/rules - Return all rules;
GET productApp/rules/new - Return a form to add a new rule to the database;
POST productApp/rules/new - Creates a new rule;
GET productApp/rules/<id> - Return the rule by id;
POST productApp/rules/<id> - Update the specified rule;

If you add or modify a rule, you should process the products again.

