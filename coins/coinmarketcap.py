from django.conf import settings
import requests
import logging
from typing import Dict, Tuple, Any, Optional


URL_ACTIVE_COINS = (
    "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
)
URL_KEY_INFO = "https://pro-api.coinmarketcap.com/v1/key/info"

logger = logging.Logger(__name__)


class CoinMarketCap:
    def __init__(self):
        self.api_key = settings.COIN_MARKET_CAP_API_KEY
        self.headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": self.api_key,
        }

    def request(
        self,
        end_point: str = URL_ACTIVE_COINS,
        params: Dict = {},
        headers: Dict = {},
        method: str = "GET",
        expected_status_code: int = 200,
    ) -> Tuple[Optional[requests.Response], Optional[Dict]]:
        # combine headers
        final_headers = self.headers | headers
        
        try:
            if method == "GET":
                response = requests.get(end_point, params=params, headers=final_headers)
            if response.status_code == expected_status_code:
                logger.info(f'The request for api {end_point} is successfully done.')
                data = response.json()
                return (response, data)
            logger.error(f"something went wrong while requesting to: {end_point}")
            logger.error(f"{response.json()}")
            return (response, response.json())
        except Exception as e:
            logger.error(e)
            return None, None

    def is_authenticated(self) -> bool:
        response, _ = self.request(URL_KEY_INFO)
        return True if response and response.status_code == 200 else False
    
    def get_latest_coins(self, params: Dict = {}, headers: Dict = {}) -> Optional[Dict]:
        _, coins = self.request(params=params, headers=headers)
        return coins
    
    @staticmethod
    def is_updated_coin(coin: Dict, cached_coin: Dict) -> bool:
        """Check the coin is updated or not"""
        if not cached_coin:
            return True
        if coin['last_updated'] != cached_coin['last_updated']:
            logger.info(f'Coin {coin["symbol"]} has been updated.')
            return True
        return False