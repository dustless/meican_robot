## 使用说明

1. 安装要求: python3, pip, pipenv
2. 安装依赖包
    ```bash
    pipenv install
    ```
3. 初始化django环境
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
4. 跑后台服务
    ```
    python manage.py runserver
    ```
    然后可以通过访问 http://127.0.0.1/admin 进行后台数据管理，或者通过访问 http://127.0.0.1/account/add 进行账户添加
5. 定时订餐任务
    
    Ubuntu: 在ubuntu上可以执行
    ```
    python manage.py crontab add
    ```
    将定时任务添加到crontab里

