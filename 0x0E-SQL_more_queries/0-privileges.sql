#!/bin/bash

# Script to list all privileges of MySQL users user_0d_1 and user_0d_2 on localhost

# MySQL credentials
MYSQL_USER="root"  # Change this to your MySQL username if it's different
MYSQL_PASSWORD="your_mysql_password"  # Change this to your MySQL password

# MySQL query to list privileges of user_0d_1
echo "Privileges for user_0d_1:"
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW GRANTS FOR 'user_0d_1'@'localhost';"

# MySQL query to list privileges of user_0d_2
echo "Privileges for user_0d_2:"
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW GRANTS FOR 'user_0d_2'@'localhost';"
