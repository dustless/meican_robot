# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django import forms

from meican import MeiCan, MeiCanLoginFail

from robot.manager import create_or_update_account


def check_username_password(username, password):
    # Check username and password by trying to login meican.com
    try:
        meican = MeiCan(username, password)
        return True
    except MeiCanLoginFail:
        return False


class AccountAddForm(forms.Form):
    username = forms.CharField(required=True, label="用户名",
                               error_messages={'required': '用户名不能为空.'})
    password = forms.CharField(required=True, label="密码",
                               error_messages={'required': '密码不能为空.'})
    likes = forms.CharField(required=False, label="喜欢吃的菜关键字",
                            help_text="使用'|'分割，eg.宫保鸡丁|孜然肥牛")
    dislikes = forms.CharField(required=False, label="不喜欢吃的菜关键字",
                               help_text="使用'|'分割，eg.宫保鸡丁|孜然肥牛")

    def clean(self):
        cleaned_data = super(AccountAddForm, self).clean()
        username = cleaned_data['username']
        password = cleaned_data['password']
        if not check_username_password(username, password):
            msg = "用户名或密码错误"
            self.add_error('username', msg)
            self.add_error('password', msg)
        return cleaned_data


@csrf_exempt
def account_add_view(request):
    if request.method == "POST":
        form = AccountAddForm(request.POST)
        ret = form.is_valid()
        if ret:
            cleaned_data = form.clean()
            account = create_or_update_account(
                cleaned_data["username"], cleaned_data["password"],
                cleaned_data["likes"], cleaned_data["dislikes"])
            return HttpResponse("添加或更新成功")
        else:
            return render(request, 'account_add_form.html', {'form': form})
    return render(request, 'account_add_form.html', {'form': AccountAddForm()})

