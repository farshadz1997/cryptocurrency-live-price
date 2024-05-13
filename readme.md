# Cryptocurrency price updater
A simple project using Django-channels and WebSocket along with celery and celery-beat to update Cryptocurrency price
through Coinmarketcap API.
![Screenshot_13-5-2024_1558_localhost](https://github.com/farshadz1997/cryptocurrency-live-price/assets/60227955/2118d800-9dda-4630-a0a1-4245268b8fca)

## Installation
- Create ```.env``` file in the project root folder and set these key value
pairs inside it:
```txt
COIN_MARKET_CAP_API_KEY= Your token from the coinmarketcap panel
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
