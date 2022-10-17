# flask_boilerplate

this is a boilerplate of flask , PostgreSQL,  Docker 

## Requirements
For development we using [docker](https://www.docker.com/get-started)
You can also run directly without docker

## Installation with docker

clone [project](https://github.com/vipin733/flask_boilerplate)

```bash
git clone https://github.com/vipin733/flask_boilerplate
cd flask_boilerplate && cp .example.env .env
```
and update .env variable according to  your connivence 
also you can update docker-compose.yml file 

## run project


```bash
docker-compose up
```

## migrate tabel

```bash
 docker-compose exec web python manage.py create_db
```

## seed db tabel

```bash
 docker-compose exec web python manage.py seed_db
```

[http://localhost:5003/api/v1/home](http://localhost:5003/api/v1/home)
