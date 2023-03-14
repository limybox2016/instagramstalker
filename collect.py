import json
import os
import sys
import shutil
from time import sleep
import subprocess

from InstagramAPI import InstagramAPI


def collect_user_data(username):
    # Login to Instagram
    api = InstagramAPI("write username", "write password")
    api.login()
    api.searchUsername(username)
    user_id = api.LastJson['user']['pk']

    subscribers = []
    has_more_subscribers = True
    next_max_id = ''
    while has_more_subscribers:
        api.getUserFollowers(user_id, maxid=next_max_id)
        subscribers.extend(api.LastJson['users'])
        has_more_subscribers = api.LastJson['big_list']
        if has_more_subscribers:
            next_max_id = api.LastJson['next_max_id']
        sleep(3)

    user_data_dir = f'{username}_data'
    os.makedirs(user_data_dir, exist_ok=True)

    subscribers_file = os.path.join(user_data_dir, f'{username}_subscribers.txt')
    if os.path.exists(subscribers_file):
        subscribers_file = os.path.join(user_data_dir, f'{username}_subscribers_1.txt')
    with open(subscribers_file, 'w') as f:
        for subscribers in subscribers:
            f.write(subscribers['username'] + '\n')

    subscriptions = []
    has_more_subscriptions = True
    next_max_id = ''
    while has_more_subscriptions:
        api.getUserFollowings(user_id, maxid=next_max_id)
        subscriptions.extend(api.LastJson['users'])
        has_more_subscriptions = api.LastJson['big_list']
        if has_more_subscriptions:
            next_max_id = api.LastJson['next_max_id']
        sleep(3)

    subscriptions_file = os.path.join(user_data_dir, f'{username}_subscriptions.txt')
    if os.path.exists(subscriptions_file):
        subscriptions_file = os.path.join(user_data_dir, f'{username}_subscriptions_1.txt')
    with open(subscriptions_file, 'w') as f:
        for subscriptions in subscriptions:
            f.write(subscriptions['username'] + '\n')

    shutil.copy('Progress.py', user_data_dir)

    if any("_1" in file for file in os.listdir(user_data_dir)):
        subprocess.run(["python", "Progress.py", user_data_dir])

    print(f'Data written to {subscribers_file}, {subscriptions_file}')

if __name__ == '__main__':
    username = input("Enter Instagram username: ")
    collect_user_data(username)
