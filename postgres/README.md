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

To exit postgres=# enter: \q or use the shortcut key: Ctrl+D
