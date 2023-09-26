from django.shortcuts import render
from django.http import HttpResponse

import json

from robots.models import Robot

EXISTING_MODELS = ('R2', '13', 'X5')


def new_robot_created(request):
    if request.method == 'POST':
        robot_info = json.loads(request.body)
        if 'model' in robot_info and robot_info['model'] in EXISTING_MODELS:
            Robot.objects.create(serial=f'{robot_info["model"]} {robot_info["version"]}',**robot_info)
            response = json.dumps({'response': 'New robot created!'})
            return HttpResponse(response)
    
        else: 
            return HttpResponse('Make sure your "model" is in existing models')