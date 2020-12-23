### Migrate dev db to db prod

export existing local database :
```
pg_dump -U username -h localhost databasename >> sqlfile.sql 
```
pwd for postgres : paultapedes7a

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

