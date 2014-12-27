# -*- coding: utf-8 -*-

from models import *
from datetime import datetime

import mandrill

mandrill_client = mandrill.Mandrill('6g6u4ph9BB5KqWBOr0x0MQ')

def sendemails():
    today = datetime.today().date()
    
    reminders = Reminder.objects.all().filter(date=today)
    
    for reminder in reminders:
        email = reminder.goal.user.email 
        name = reminder.goal.user.name
        goal = reminder.goal.goal
        deadline = reminder.goal.deadline.strftime('%d. %m. %Y')
        html = '<p>Zdravo ' + name + '!</p><p>Svoj cilj <strong>' + goal + '</strong> morash dosechi do <strong>' + deadline + '</strong>.</p><br><br><p>Yo ' + name + '!</p><p>Your goal <strong>' + goal + '</strong> is due on <strong>' + deadline + '</strong>.</p>'
        
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
        
        except mandrill.Error, e:
            print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
            raise
    
    reminders.delete()

if __name__ == "__main__":
    sendemails()