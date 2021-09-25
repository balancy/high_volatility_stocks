# High Implied Volatility Stocks

App aims to parse and display stocks with high implied volatility (IV). High IV stocks are analyzed to enter some options constructions (e.g. Sell Credit Bull Put). It uses stocks fundamentals from [Finviz](https://finviz.com/) and volatility info from [Barchart](https://www.barchart.com/).

App launched in docker and consists of few parts:
- Backend on FastApi + SqlAlchemy
- Postgresql database
- Frontend on React ([create-react-app](https://create-react-app.dev/) template) + Material UI

<img src="https://i.ibb.co/R9x8mF3/image.png" alt="image"/>

## Install

Docker-compose should be already installed.

1. Clone the repository:
```console
git clone https://github.com/balancy/high_volatility_stocks
```

2. Go inside cloned repository, build docker containers:
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
localhost:3000
```