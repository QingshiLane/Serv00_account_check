import sys,json,asyncio,random
from os import path
from telegram import Bot,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from datetime import datetime

with open('accounts.json', 'r') as file:
    '''
    {
	"TG_BOT_BAOHAO":"",
	"TG_USER_ID":"",
    }
    '''
    datas = json.load(file)
BOT_TOKEN=datas['TG_BOT_BAOHAO']
CHAT_ID=datas['TG_USER_ID']
QL_URL=datas['QL_URL']
ex_list=['😁','🌹','😆','😂','😄','😃','🤣','😅','😋','😍','🥳','💥','🌟','🌀','💫','🌈','🌙','🌞','🔥','🍀','🌻',
         '🌸','🍃','🌺','🌼','🦄','🦋','🐧','🐉','🦊','🦁','🐵','🐙','🦑','💡','📚','🎧','🛒','🎮','🚗','🚌','🚎',
         '🚕','🚲','🚜','🛴','🚂','✨','☠️','🔮','⚡','⚔️','🏴‍☠️','♛','♠️','❄️','➳','🌪️','🐍','🐢','🦉','🦧','🐯',
         '🧸','🍔','🍦','🍩','🕹️','🎥','📀','🧩','🎲','🎖️']
message = "🌟🌟🌟serv00&ct8保号🌟🌟🌟\n"
async def send_message(chat_id, message):
    bot = Bot(token=BOT_TOKEN)
    try:
        if QL_URL!='http://xxxxxx:xxxx/ #可选，你的青龙面板地址':
          # 创建键盘按钮
          keyboard = [
              [
                  InlineKeyboardButton('👉来自QL面板点此处直达面板👈', url=QL_URL)
              ]
          ]
          reply_markup = InlineKeyboardMarkup(keyboard)
          await bot.send_message(chat_id=chat_id, text=message,reply_markup=reply_markup,parse_mode=ParseMode.HTML)
        else:
          await bot.send_message(chat_id=chat_id, text=message,parse_mode=ParseMode.HTML)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")    

def main(login_results):
    global message
    suc,fai=0,0
    for result in login_results:
        username, panel, login_result = result.split(":")
        login_result = int(login_result)
        if panel=='panel.ct8.pl':ser='ct8'
        else:
            number = panel.split('panel')[1].split('.')[0]
            ser='s'+number
        if login_result == 1:
            suc+=1
            message += f"🟢{ser} 账号 <code>{username}</code> 登录成功\n"#parse_mode=ParseMode.HTML
        else:
            fai+=1
            message += f"🔴{ser} 账号 <code>{username}</code> 登录失败,请检查账号&密码是否正确\n"
    random_elements = random.sample(ex_list, 6)
    message+=f"{''.join(random_elements[:3])}脚本运行结束{''.join(random_elements[-3:])}\n"
    message+=f'登录成功(<code>{suc}</code>) 登陆失败(<code>{fai}</code>) 总计(<code>{suc+fai}</code>)\n'
    current_time = datetime.now()
    current_time_str=current_time.strftime('%Y-%m-%d %H:%M:%S')
    message+=f'📆{current_time_str}'
    asyncio.run(send_message(CHAT_ID, message))

if __name__ == "__main__":
    login_results = sys.argv[1:]
    main(login_results)
