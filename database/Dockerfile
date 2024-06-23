# Use the official MySQL image from Docker Hub
FROM mysql:5.7

# Set the root password for MySQL (change as needed)
ENV MYSQL_USER test
ENV MYSQL_PASSWORD 1234
ENV MYSQL_ROOT_PASSWORD 1234
ENV MYSQL_DATABASE test

# Create a new table 'testtable' with a column 'testok'
COPY ./scripts/ /docker-entrypoint-initdb.d/

# Expose the default MySQL port
