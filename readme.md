# Cryptocurrency price updater
Simple project using channels and websocket to update Cryptocurrency price
through Coinmarketcap API.

## Installation
- Create ```.env``` file in project root folder and set these key value
pairs inside it:
```txt
COIN_MARKET_CAP_API_KEY= Your token from coin market cap panel
ALLOWED_HOSTS=127.0.0.1 localhost 0.0.0.0
DEBUG=1 or 0
SECRET_KEY=some secret key
CELERY_BROKER=redis://redis:6379/2
CELERY_BACKEND=redis://redis:6379/2
POSTGRES_DB=postgres database name
POSTGRES_USER=postgres database username
POSTGRES_PASSWORD=postgres database password
```
- run it through docker-compose with the following command:
```bash
docker-compose up
```