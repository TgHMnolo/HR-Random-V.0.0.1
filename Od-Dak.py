#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import colorama
import random
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
work = [bcolors.OKBLUE + "'คุณอดแดกงานค่ะ'" + bcolors.BOLD,
       bcolors.OKGREEN + "'บริษัทเราไม่รับโจรค่ะ'" + bcolors.BOLD,
       bcolors.OKBLUE + "'อย่าทะลึ่งส่งใบสมัครมาอีกนะค่ะ'"  + bcolors.BOLD]
secure_random = random.SystemRandom()
print(bcolors.OKGREEN + " ผลการสุ่มคำตอบบของ HR V.0.0.0.1 " + bcolors.OKGREEN)
print(bcolors.FAIL + " สวัสดีค่ะ ดิฉันคือ HR(Humen Rampage) จากบริษัท ฯลฯ จะมาบอกคุณว่า --->   "      + bcolors.ENDC),(secure_random.choice(work))
print(bcolors.FAIL + " สวัสดีค่ะ ดิฉันคือ HR(Humen Rampage) จากบริษัท ฯลฯ จะมาบอกคุณว่า --->   "      + bcolors.ENDC),(secure_random.choice(work))
print(bcolors.FAIL + " สวัสดีค่ะ ดิฉันคือ HR(Humen Rampage) จากบริษัท ฯลฯ จะมาบอกคุณว่า --->   "      + bcolors.ENDC),(secure_random.choice(work))
print(bcolors.FAIL + " สวัสดีค่ะ ดิฉันคือ HR(Humen Rampage) จากบริษัท ฯลฯ จะมาบอกคุณว่า --->   "      + bcolors.ENDC),(secure_random.choice(work))
print(bcolors.FAIL + " สวัสดีค่ะ ดิฉันคือ HR(Humen Rampage) จากบริษัท ฯลฯ จะมาบอกคุณว่า --->   "      + bcolors.ENDC),(secure_random.choice(work))
