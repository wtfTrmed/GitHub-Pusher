# GitHub Pusher was proudly coded by wtfTrmed (https://github.com/wtfTrmed).
# Copyright (c) 2022 rodclip#7777

import os

def pushCommit(days: int):
    if days < 1:
        return os.system('git push')
    else:
        date = f'{days} day(s) ago'
        with open('days.txt', 'a') as file:
            file.write(f'{date}\n')

        os.system('git add days.txt')
        os.system('git commit --date="'+date+'" -m "github.com/wtfTrmed on top"')
        return days * pushCommit(days-1)

pushCommit(365)

# GitHub Pusher was proudly coded by wtfTrmed (https://github.com/wtfTrmed).
# Copyright (c) 2022 rodclip#7777



