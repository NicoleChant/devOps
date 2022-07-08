### Postgres WSL

We will follow the tutorial from Microsofts page <a href = "https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-database" title = "Microsoft Setup Postgres on WSL"> Microsoft Tutorial </a>

```
sudo apt update
sudo apt install postgresql postgresql-contrib
psql --version
```

<ul>
<li> Checking the status of the database

```
sudo service postgresql status
```
</li>

<li> Start running our database

```
sudo service postgresql start
```
</li>

<li> Restart our database

```
sudo service postgresql restart
```

</li>

<li>Stop running our database

```
sudo service postgresql stop
```
</li>
</ul>

The default admin user, postgres, needs a password assigned in order to connect to a database. To set up a password:
```
sudo passwd postgres
exec $SHELL
```

To run PostgreSQL with pqsl shell:

```
sudo service postgresql start
sudo -u postgres psql
```

Once you have successfully entered the psql shell, you will see your command line change to look like this: postgres=#

To exit postgres=# enter: \q or exit or use the shortcut key: Ctrl+D

#### List Users

```
sudo -u postgres psql          #or          CREATE USER librarian;
postgres=# \du                     #or
postgres=# SELECT usename FROM pg_user;
```

Let's locate pg_hba.conf file

```
SHOW hba_file;
```

Mine is located at /etc/postgresql/12/main/pg_hba.conf

#### See current user

```
SELECT current_user;
```

or for more information we can use

```
\conninfo
```

#### Create new (super!)user

```
sudo -u postgres createuser <user_name>
sudo -u postgres psql
postgres=# ALTER USER librarian WITH superuser
postgres=# ALTER USER librarian WITH NOSUPERUSER;
```

The console should response with "ALTER ROLE"

#### Change user

```
\c - <user_name>
```
Notice that - is just substitute for current database.

### See all databases

```
\l
```

### Select current database

```
SELECT current_database();
```

### Change database

```
\c <dbname>
```

For instance, if we are user Mint and write
```
\c books
```

we should see the follow message in our console:
You are now connected to database "books" as user "Mint".

<ul>
<li>
Create Database

```
CREATE DATABASE <dbname>;
```
</li>

<li>
Drop Database

```
DROP DATABASE <dbname>;
```
</li>

<li>
Create database owned by specific user

```
CREATE DATABASE <dbname> OWNER <owner>;
```
</li>

<li>
Show tables of the database

```
psql -U postgres -d <dbname>
```
or within the PostgreSQL command line
```
\dt
```
</li>
</ul>


### A possible error

If we try to connect to the current database as a different user, for instance
```
\c - nicole
```

the following error may occur:

<span style="color:red">
FATAL:  Peer authentication failed for user "nicole"
Previous connection kept
</span>

The following command lists all the databases with user "postgres"

```
sudo -u postgres psql -l
```

Let's reveal the content of the magic file pg_hba.conf

```
sudo cat /etc/postgresql/12/main/pg_hba.conf
```

Let's modify this file

```
sudo nano /etc/postgresql/12/main/pg_hba.conf
```

and change this line

```
local   all             all                                     peer
```

to

```
local   all             all                                     md5
```

PRESS Ctrl+X and don't forget to restart the shell!


### I forgot my password first-aid kit

As before lets reach out to the pg_hba configuration file and let's change this line

```
#Database administrative login by Unix domain socket
local   all             postgres                                md5
```

to <strong> trust </strong>.

Then after we save the file, simply we restart the shell and the postgres and enter the psql and write
```
 ALTER USER postgres WITH PASSWORD '<new_password>';
```

Then change the pg_hba to its initial state.


### PostgresSQL datatypes


### PostgresSQL from Python

```
import psycopg2

conn = psychopg2.connect(
          host =
)
