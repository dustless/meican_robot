# coding: utf-8
from meican import MeiCan, NoOrderAvailable, MeiCanLoginFail

from robot.models import Account, Config


def job():
    config = Config.objects.first()
    if config and not config.enable:
        return
    accounts = Account.objects.filter(online=True)

    def like_or_dislike_dish(dish, keys):
        """
        判断菜名是否为用户喜欢/不喜欢的
        :param dish:
        :param keys:
        :return: bool
        """
        for key in keys:
            if key in dish.name:
                return True
        return False

    for account in accounts:
        # login to meican and get dish list
        try:
            meican = MeiCan(account.username, account.password)
            dishes = meican.list_dishes()
        except NoOrderAvailable:
            print('今天没有开放点餐或已点过餐了')
            continue
        except MeiCanLoginFail:
            print('用户名(%s)或者密码不正确' % account.username)
            continue

        like_keys = account.likes.split("|")
        dislike_keys = account.dislikes.split("|")
        like_dishes = [dish for dish in dishes
                       if like_or_dislike_dish(dish, like_keys)]

        # 有喜欢的菜，直接预订第一个 TODO: 按喜好优先级预订
        order_dish = dishes[0]
        if like_dishes:
            order_dish = like_dishes[0]
        # 没有喜欢的菜，挑一个不讨厌的就行
        else:
            for dish in dishes:
                if not like_or_dislike_dish(dish, dislike_keys):
                    order_dish = dish
                    break

        meican.order(order_dish)
        print("order dish %s for user %s:" % (order_dish.name, account.username))
