# High Implied Volatility Stocks

App aims to parse and display stocks with high implied volatility (IV). High IV stocks are analyzed to enter some options constructions (e.g. Sell Credit Bull Put).

App launched in docker containers and consists of few parts:

1. Backend on FastApi + SqlAlchemy.
App backend part fetches stocks fundamental data from [Finviz](https://finviz.com/) and volatility info from [Barchart](https://www.barchart.com/). App parses fetched data, periodically saves to the database, and shares from the DB via Rest API.

2. Postgresql database.

3. Frontend on React ([create-react-app](https://create-react-app.dev/) template) + Material UI.
App frontend part fetches asynchronously stocks data from backend API endpoints and display it.

<img src="https://i.ibb.co/R9x8mF3/image.png" alt="image"/>

## Install

Docker-compose should be already installed.

1. Clone the repository:
```console
git clone https://github.com/balancy/high_volatility_stocks
```

2. Rename `.env.example` to `.env` and fill your proper values:
- `HOST` - hostname
- `PGADMIN_DEFAULT_EMAIL` - pgadmin email
- `PGADMIN_DEFAULT_PASSWORD` - pgadmin password
- `POSTGRES_DB` - name of postgres db
- `POSTGRES_PASSWORD` - postgres db password
- `POSTGRES_PORT` - postgres db port
- `POSTGRES_USER` - postgres db admin username
- `WEB_PORT` - host backend port

3. Go inside cloned repository, build docker containers:
```console
docker compose build
```

## Launch

Start docker containers:
```
docker compose run
```

Frontend part will be accessible via:
```
host:3000
```
where `host` is your hostname