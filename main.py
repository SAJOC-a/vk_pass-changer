import random
import vk_api
import secrets
import string
from func import *
from requests import Session
from loguru import logger

alphabet = string.ascii_letters + string.digits
session = Session()

print('''
██╗░░░██╗██╗░░██╗  ░█████╗░██╗░░██╗░█████╗░███╗░░██╗░██████╗░███████╗██████╗░
██║░░░██║██║░██╔╝  ██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝░██╔════╝██╔══██╗
╚██╗░██╔╝█████═╝░  ██║░░╚═╝███████║███████║██╔██╗██║██║░░██╗░█████╗░░██████╔╝
░╚████╔╝░██╔═██╗░  ██║░░██╗██╔══██║██╔══██║██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗
░░╚██╔╝░░██║░╚██╗  ╚█████╔╝██║░░██║██║░░██║██║░╚███║╚██████╔╝███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝''')

file_path = input('\nВведи путь до txt/Enter the path to txt: ')
file = file_open(file_path, 'r').read()

use_proxy = input('[HTTP Only] Использовать proxy.txt?/Use proxy.txt? (y/n): ')
if use_proxy.lower() == 'y':
    proxy = file_open('proxy.txt', 'r').readlines()
    for i in range(len(proxy)):
        proxy[i] = proxy[i].replace("\n", "")

for account in file.split('\n'):
    try:
        data = {'number':account.split(':')[0],
                'password':account.split(':')[1]}

        if use_proxy.lower() == 'y':
            session.proxies = {'http': f'http://{random.choice(proxy)}'}

        vk_session = vk_api.VkApi(data['number'], data['password'], session=session)
        vk_session.auth()
        vk = vk_session.get_api()
        new_password = ''.join(secrets.choice(alphabet) for i in range(20))
        vk.account.changePassword(old_password=data['password'], new_password=new_password)
        with open('changed-accs.txt', 'a', encoding='utf-8') as f:
            f.write(f"{data['number']}:{new_password}\n")
        logger.info(f"Changed pass - {data['number']}")
    except Exception as error:
        if data['number']:
            logger.info(f"Not changed pass - {data['number']}")
        else:
            logger.info(f"Not changed pass")