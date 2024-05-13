import json
from .coinmarketcap import CoinMarketCap
import logging
from typing import Dict, List

from django.core.cache import cache
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


channel_layer = get_channel_layer()
logger = logging.Logger(__name__)


def update_coin_data(coin_data: Dict) -> Dict:
    """Update the coin and return coin's data"""
    cache.set(coin_data['symbol'], coin_data)
    return coin_data


def send_data_to_websocket_coins_list_view(data: List[Dict]) -> None:
    """Send data to websocket coins list view """
    event = {
        'type':'send.message',
        'message': data
    }
    logger.info("send data to websocket")
    async_to_sync(channel_layer.group_send)('coins_list_group', event)
    