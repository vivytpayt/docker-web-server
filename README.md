# docker-compose-web-server
In the address bar, passed the "count " parameter, the count is the amount of resources that you need to request from the source and save in the database. The server executes requests asynchronously and asynchronously writes responses to the database.\
Requests are sent to https://dummyjson.com/products/ . \
Responses are stored in the "products" table.
- Column in table: 
  - ('id', INT),
  - ('title', TEXT),
  - ('description', TEXT),
  - ('price', INT),
  - ('discountpercentage', FLOAT),
  - ('rating', FLOAT),
  - ('stock', INT),
  - ('brand', TEXT),
  - ('category', TEXT),
  - ('thumbnail', TEXT),
  - ('images', TEXT)
## Installation
Before starting, redefine the ports to the ones you need in the file "docker-compose.yaml".

Use "docker-compose up --build --force-recreate -d
" to start the containers.
## Example .env
DATABASE = 'postgres'\
DB_USER = 'postgres'\
PASSWORD = 'postgres'\
DB_HOST = 'database'\
DB_PORT = 5432\
WEB_HOST = '0.0.0.0'\
WEB_PORT = 8080\
TABLE = 'products'\
## Example request
http :// 0.0.0.0 : 8081 / ? count = Any number

http://0.0.0.0:8081/?count=3
