<h1 align="center">
 Leoclimb.fr
</h1>

[![leoclimb](demo.png)](https://leoclimb.fr)

## Stacks
- Django
- Postgres
- Docker-compose

## Usefull commands

### Migrate dev db to db prod

export existing local database :
```
pg_dump -U username -h localhost databasename >> sqldump.sql 
```

### import db in container

Stop existing database 
```
docker exec -it leoclimb_db_1 psql -U paul -d postgres -c "SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'leoclimb';"
```

Drop current database
```
docker exec -it leoclimb_db_1 psql -U paul -d postgres -c "DROP DATABASE leoclimb;"
```

Import db
```
docker exec -it leoclimb-db bash
psql -U paul -d leoclimb -U paul -f db-export
```

### Static files for productions

```
python3 manage.py collectstatic
```
It will create static folder containing static app images and static admin css
then in you ngnix conf render static folder
```
 location /static {
                autoindex on;
                alias {path to manage.py}/static;
        }
```

### Launching for production
```
docker-compose up -d --build
```