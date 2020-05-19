import datetime

from django.core.mail import send_mail
from django_cron import CronJobBase, Schedule

from api_v1.models import Event


class Mailer(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'spa.mailer_job'

    def do(self):
        dataset = Event.objects.filter(
            date__range=[datetime.datetime.now() - datetime.timedelta(minutes=1), datetime.datetime.now()])
        for item in dataset:
            send_mail(
                'You have alert',
                'Your event'+item.title+' was started in 1h on '+item.date,
                'admin@admin.com',
                [item.email],
                fail_silently=False,
            )
