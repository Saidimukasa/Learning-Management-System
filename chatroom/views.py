from re import T
from django.shortcuts import render
from .models import ChatGroup
from .tortoise_models import ChatMessage
from tortoise import Tortoise
from django.conf import settings
from asgiref.sync import sync_to_async
from django.http import JsonResponse
from LMS.settings import TORTOISE_INIT


def index(request):
    return render(request, 'chat/index.html', {})



def get_participants(group_id=None, group_obj=None, user=None):
    """ function to get all participants that belong the specific group """
    
    if group_id:
        chatgroup = ChatGroup.objects.get(id=id)
    else:
        chatgroup = group_obj

    temp_participants = []
    for participants in chatgroup.user_set.values_list('email', flat=True):
        if participants != user:
            temp_participants.append(participants.title())
    temp_participants.append('You')
    return ', '.join(temp_participants)

def room(request, group_id):
    chatgroup = ChatGroup.objects.get(id=group_id)
    #TODO: make sure user assigned to existing group
    assigned_groups = list(request.user.group.values_list('id', flat=True))
    groups_participated = ChatGroup.objects.filter(id__in=assigned_groups)
    return render(request, 'chat/room.html', {
            'chatgroup': chatgroup,
            'participants': get_participants(group_obj=chatgroup, user=request.user.email),
            'groups_participated': groups_participated
     })



    # return render(request, 'chat/room.html', {
    #     'room_name': room_name
    # })


async def history(request, room_id):

    await Tortoise.init(**settings.TORTOISE_INIT)
    chat_message = await ChatMessage.filter(room_id=room_id).order_by('date_created').values()
    await Tortoise.close_connections()

    return await sync_to_async(JsonResponse)(chat_message, safe=False)
