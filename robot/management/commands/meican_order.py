# coding: utf-8
import datetime

from django.core.management.base import BaseCommand
from robot.task import job


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("[%s] start job..." % datetime.datetime.now())
        job()
        self.stdout.write('[%s] Successfully done' % datetime.datetime.now())
