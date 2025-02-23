# Serv00_account_check
serv00&amp;ct8账户登录检测，青龙面板部署，向TG机器人推送结果
## 一、创建TG机器人，获取机器人`Token`，并设置机器人命令描述
### 1.打开Telegram搜索[@BotFather](https://t.me/BotFather)，或点击直达

![image](https://github.com/user-attachments/assets/c38accac-011d-4f78-9e54-c9e256493c14) 

⚠️带认证且用户名为[@BotFather](https://t.me/BotFather)，主页描述如下图，不要搞错了

![image](https://github.com/user-attachments/assets/f4fb358d-8449-4a05-aa70-be5c9b639d8d)

### 2.创建一个私聊机器人，并获取机器人`Token`

1）进入机器人输入命令`/newbot`或者选择菜单命令`/newbot`

2）输入机器人名称（名称即昵称，随便填，可以和任何人相同、重复，不唯一）

3）输入机器人的用户名（用户名唯一标识，必须以`“大写字母开头Bot结尾”`或者`“小写字母开头_bot结尾”`两种格式二选一。图中作者以`test_bot`为用户名提示被占用创建不了机器人，所以为了演示就随便起了一个用户名`scxsd_bot`。为防止带来误解特此说明）

4）获得机器人`TOKEN`，备用ℹ️ℹ️ℹ️

![image](https://github.com/user-attachments/assets/3f04b164-7bea-4697-85a6-8a003820e34e)

## 二、获取个人用户ID
### 1.打开Telegram搜索[@KinhRoBot](https://t.me/KinhRoBot)，或点击直达

![image](https://github.com/user-attachments/assets/d86ff2b6-d308-4cf6-8859-07545043f3be)

### 2.输入`/id`命令，得到个人`用户ID`，备用ℹ️ℹ️ℹ️

![image](https://github.com/user-attachments/assets/2f9727be-2e0e-44eb-912d-81951ca4a797)

## 三、青龙面板部署
### 1.青龙面板安装Linux依赖`sshpass`

![image](https://github.com/user-attachments/assets/2935406e-287d-4c37-a868-9e3a01bc4514)

### 2.更改accounts.json

（1）打开`accounts.json`，修改其中`TG_BOT_TOKEN`和`TG_USER_ID`的值，将机器人的`Token`填入文件对应`" "`中（注意将值填入双引号中，保留双引号）。你的`用户ID`同理。

（2）修改其中的`QL_URL`，这个可以改为你的青龙面板地址；也可以选择不用管，若更改填入自己的青龙面板地址话，可以在tg机器人消息推送中插一个快捷链接，方便你直接进入面板。

（3）修改`accounts`,将列表中的字典键值更改为你的账号用户名和密码，以及对应的面板网址

![image](https://github.com/user-attachments/assets/d225b5eb-0e76-4233-927d-e82176f27d01)

### 3.将`start.sh`、`serv00.py`、`accounts.json`放在青龙面板脚本管理下

![image](https://github.com/user-attachments/assets/5ebbd613-ebed-497c-acd3-6f8942cdab66)

### 4.创建定时任务

任务名：`serv00&ct8保活`

命令：`task start.sh`

定时：`0 8 3,17 * * `

#定时规则为每月3号和17号的8点，请自行修改

![image](https://github.com/user-attachments/assets/1d761141-2393-44f1-8249-7b8c1ea5e7d1)
