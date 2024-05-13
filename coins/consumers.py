import json
import logging

from channels.generic.websocket import AsyncWebsocketConsumer, SyncConsumer


logger = logging.Logger(__name__)


class CoinsListConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info("websocket connected")
        await self.channel_layer.group_add("coins_list_group", self.channel_name)
        self.groups.append("coins_list_group")
        await self.accept()

    async def disconnect(self, code):
        logger.warning(f"websocket disconnected with code: {code}")
        pass

    async def send_message(self, event):
        logger.info("sending message")
        if event["message"]:
            logger.info("some coins has been updated")
            await self.send(text_data=json.dumps(event))
            