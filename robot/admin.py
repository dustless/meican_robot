from django.contrib import admin

from robot.models import Account, Config


class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'likes', 'dislikes', 'online')


admin.site.register(Account, AccountAdmin)

admin.site.register(Config)
