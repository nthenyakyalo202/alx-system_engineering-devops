#!/bin/bash

# Get the current date
now=$(date +"%d-%m-%Y")

# Set the MySQL root password
MYSQL_ROOT_PASSWORD="$1"

# Dump all databases into a single file
mysqldump -u root -p${MYSQL_ROOT_PASSWORD} --all-databases > backup.sql

# Compress the dump file
tar -czvf "${now}.tar.gz" backup.sql

# Remove the original dump file
rm backup.sql

