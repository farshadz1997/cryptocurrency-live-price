import logging
from django.core.cache import cache

from coins.coinmarketcap import CoinMarketCap
from coins.helpers import update_coin_data, send_data_to_websocket_coins_list_view
from core.celery import app


logger = logging.Logger(__name__)


@app.task(name='update-cryptocurrencies-data')
def update_cryptocurrencies_data() -> None:
    """Update the cryptocurrencies data
    and keep updated data in the cache"""

    # 1. requests to get data
    coin_market_cap = CoinMarketCap()
    active_coins = coin_market_cap.get_latest_coins()
    logger.info("The request for api is successfully done")
    if not active_coins or not active_coins.get('data'):
        logger.debug("The request for api is failed")
        return None
    active_coins = active_coins['data']
    
    # 2. detect updated coins and update the cache
    updated_coins = [
        update_coin_data(coin_data) for coin_data in active_coins
        if CoinMarketCap.is_updated_coin(coin_data, cache.get(coin_data['symbol']))
    ]

    # 3. send result to websocket channel
    send_data_to_websocket_coins_list_view(updated_coins)
    return None