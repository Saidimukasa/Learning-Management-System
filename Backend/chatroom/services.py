from tortoise import Tortoise
from django.conf import settings
from .tortoise_models import ChatMessage
from LMS.settings import TORTOISE_INIT

async def chat_save_message(username, room_id, message, message_type, image_caption):

    """ function to store chat message in sqlite """

    await Tortoise.init(**settings.TORTOISE_INIT)
   #  register_tortoise(TORTOISE_INIT)
    await Tortoise.generate_schemas()

    await ChatMessage.create(room_id=room_id,  
                            username=username,
                            message=message, 
                            message_type=message_type, 
                            image_caption=image_caption
                       )
    
    await Tortoise.close_connections()