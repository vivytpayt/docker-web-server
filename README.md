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
Before starting, redefine the database, ports to the ones you need in the “docker-compose.yaml” file.

Use "docker-compose up --build --force-recreate -d
" to start the containers.
## Example request
http :// 0.0.0.0 : 8081 / ? count = Any number

http://0.0.0.0:8081/?count=3
