# docker-web-server
In the address bar, it is passed as the "count " parameter, the count is the amount of resources that you need to request from the source and save in the database. The server executes requests asynchronously and asynchronously writes responses to the database.
## Installation
- You must have a PostgreSQL.
- The name of the "postgres" base.
- Host:port - 127.0.0.1:5432.
- User/password - postgres/postgres.
- Table: "Products".
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

Use "docker run --network=host -p 8080:8080 docker-web-server" to start the container.
## Example
http :// localhost : 8080 / ? count = Any number
http://localhost:8080/?count=3