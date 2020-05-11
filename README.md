# alembic-migrate: Getting Started

## Running Locally

```sh
$ docker-compose up --build
$ docker exec app-server bash -c "alembic upgrade head"

$ docker exec app-server bash -c "alembic revision --autogenerate -m 'create table'"
$ docker exec app-server bash -c "alembic upgrade head"
```

## Add this to env.py to be able to migrate model

```
from model.product import Base as ProductBase
```

## Add database URL to alembic.ini
```
sqlalchemy.url = postgres://sandbox:sandbox@database/sandbox
```