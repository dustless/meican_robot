# coding: utf-8
from robot.models import Account


def create_or_update_account(username, password, likes, dislikes):
    account = Account.objects.get_or_create(username=username, password=password, likes=likes, dislikes=dislikes)
    return account
