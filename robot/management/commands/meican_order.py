# coding: utf-8
from django.core.management.base import BaseCommand
from robot.task import job


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("start job...")
        job()
        self.stdout.write('Successfully done')
