# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
from datetime import datetime, timedelta

from ciljesled.models import *

import mandrill

mandrill_client = mandrill.Mandrill('6g6u4ph9BB5KqWBOr0x0MQ')

def sendemails(request):
    today = datetime.today().date()
    
    reminders = Reminder.objects.all().filter(date=today)
    
    for reminder in reminders:
        email = reminder.goal.user.email 
        name = reminder.goal.user.name
        goal = reminder.goal.goal
        deadline = reminder.goal.deadline.strftime('%d. %m. %Y')
        html = '<p>Zdravo ' + name + '!</p><p>Svoj cilj <strong>' + goal + '</strong> morash dosechi do <strong>' + deadline + '</strong>.</p>'
        
        try:
            message = {
                'html': html,
                'from_email': 'filipdobranic@gmail.com',
                'from_name': 'Ciljesled',
                'headers': {'Reply-To': 'filipdobranic@gmail.com'},
                'to': [{'email': email, 'name': name, 'type': 'to'}],
                'subject': 'Ciljesled te opominja'
            }

            result = mandrill_client.messages.send(message=message, async=False)
        
        except e:
            print('A mandrill error occurred: %s - %s' % (e.__class__, e))
            raise
    
    reminders.delete()
    
    return HttpResponse(1)

def setreminders(goal):
    delta = goal.deadline.date() - goal.start
    delta = delta.days
    if delta < 4:
        # set reminders every day
        i = 1
        while i < delta:
            date = goal.start + timedelta(days=i)
            
            reminder1 = Reminder(goal=goal, date=date, text='')
            reminder1.save()
            
            i = i+1
        
        reminderend = Reminder(goal=goal, date=goal.deadline.date(), text='')
        reminderend.save()
            
    elif delta < 9:
        # set reminders 1 day 3 days
        reminder1 = Reminder(goal=goal, date=goal.start + timedelta(days=1), text='')
        reminder1.save()
        
        i = 1
        while i < delta:
            if i % 3 == 0:
                date = goal.start + timedelta(days=i)
                reminder3 = Reminder(goal=goal, date=date, text='')
                reminder3.save()
            
            i = i+1
        
        reminderend = Reminder(goal=goal, date=goal.deadline.date(), text='')
        reminderend.save()
        
    elif delta < 16:
        # set reminders 1 day 3 days 5 days
        reminder1 = Reminder(goal=goal, date=goal.start + timedelta(days=1), text='')
        reminder1.save()
        
        reminder3 = Reminder(goal=goal, date=goal.start + timedelta(days=3), text='')
        reminder3.save()
        
        i = 1
        while i < delta:
            if i % 5 == 0:
                date = goal.start + timedelta(days=i)
                reminder5 = Reminder(goal=goal, date=date, text='')
                reminder5.save()
            
            i = i+1
        
        reminderend = Reminder(goal=goal, date=goal.deadline.date(), text='')
        reminderend.save()
        
    elif delta < 30:
        # set reminders 1 day 3 days 5 days 7 days
        reminder1 = Reminder(goal=goal, date=goal.start + timedelta(days=1), text='')
        reminder1.save()
        
        reminder3 = Reminder(goal=goal, date=goal.start + timedelta(days=3), text='')
        reminder3.save()
        
        reminder5 = Reminder(goal=goal, date=goal.start + timedelta(days=5), text='')
        reminder5.save()
        
        i = 1
        while i < delta:
            if i % 7 == 0:
                date = goal.start + timedelta(days=i)
                reminder7 = Reminder(goal=goal, date=date, text='')
                reminder7.save()
            
            i = i+1
        
        reminderend = Reminder(goal=goal, date=goal.deadline.date(), text='')
        reminderend.save()
        
    elif delta < 55:
        # set reminders 1 day 3 days 5 days 7 days 14 days
        reminder1 = Reminder(goal=goal, date=goal.start + timedelta(days=1), text='')
        reminder1.save()
        
        reminder3 = Reminder(goal=goal, date=goal.start + timedelta(days=3), text='')
        reminder3.save()
        
        reminder5 = Reminder(goal=goal, date=goal.start + timedelta(days=5), text='')
        reminder5.save()
        
        reminder7 = Reminder(goal=goal, date=goal.start + timedelta(days=7), text='')
        reminder7.save()
        
        i = 1
        while i < delta:
            if i % 14 == 0:
                date = goal.start + timedelta(days=i)
                reminder14 = Reminder(goal=goal, date=date, text='')
                reminder14.save()
            i = i+1
        
        reminderend = Reminder(goal=goal, date=goal.deadline.date(), text='')
        reminderend.save()
        
    else:
        # set reminders 1 day 3 days 5 days 7 days 14 days 25 days
        reminder1 = Reminder(goal=goal, date=goal.start + timedelta(days=1), text='')
        reminder1.save()
        
        reminder3 = Reminder(goal=goal, date=goal.start + timedelta(days=3), text='')
        reminder3.save()
        
        reminder5 = Reminder(goal=goal, date=goal.start + timedelta(days=5), text='')
        reminder5.save()
        
        reminder7 = Reminder(goal=goal, date=goal.start + timedelta(days=7), text='')
        reminder7.save()
        
        reminder14 = Reminder(goal=goal, date=goal.start + timedelta(days=14), text='')
        reminder14.save()
        
        i = 1
        while i < delta:
            if i % 25 == 0:
                date = goal.start + timedelta(days=i)
                reminder25 = Reminder(goal=goal, date=date, text='')
                reminder25.save()
                
            i = i + 1
        
        reminderend = Reminder(goal=goal, date=goal.deadline.date(), text='')
        reminderend.save()
        
        

# Create your views here.
@csrf_exempt
def login(request):
    fbid = request.POST.get('fbid')
    
    if len(User.objects.filter(fbid=fbid)) > 0:
        return HttpResponse(1)
    else:
        return HttpResponse(0)

@csrf_exempt
def createuser(request):
    name = request.POST.get('name')
    fbid = request.POST.get('fbid')
    email = request.POST.get('email')
    
    user = User(name=name, fbid=fbid, email=email)
    user.save()
    
    return HttpResponse(1)

@csrf_exempt
def getgoals(request):
    fbid = request.GET.get('fbid')
    user = User.objects.get(fbid=fbid)
    
    goals = user.goal_set.all()
    
    response = []
    
    for goal in goals:
        response.append(goal.as_json())
    
    return HttpResponse(json.dumps(response), content_type="application/json")

@csrf_exempt
def addgoal(request):
    fbid = request.POST.get('fbid')
    user = User.objects.get(fbid=fbid)
    
    deadline = request.POST.get('deadline')
    goal = request.POST.get('goal')
    description = request.POST.get('description')
    
    goal = Goal(deadline=datetime.strptime(deadline, '%d.%m.%Y'), goal=goal, description=description, user=user)
    
    goal.save()
    
    setreminders(goal)
    
    return HttpResponse(1)

@csrf_exempt
def deletegoal(request):
    goaltitle = request.POST.get('goal')
    fbid = request.POST.get('fbid')
    
    goals = Goal.objects.filter(goal=goaltitle)
    
    for goal in goals:
        if goal.user.fbid == fbid:
            goal.delete()
        
            return HttpResponse(1)

@csrf_exempt
def getuserinfo(request):
    fbid = request.GET.get('fbid')
    
    user = User.objects.get(fbid=fbid)
    
    return HttpResponse(json.dumps(user.as_json()), content_type="application/json")
        
@csrf_exempt
def updateemail(request):
    fbid = request.POST.get('fbid')
    email = request.POST.get('email')
    
    user = User.objects.get(fbid=fbid)
    user.email = email
    user.save()
    
    return HttpResponse(1)

@csrf_exempt
def updatename(request):
    fbid = request.POST.get('fbid')
    name = request.POST.get('name')
    
    user = User.objects.get(fbid=fbid)
    user.name = name
    user.save()
    
    return HttpResponse(1)