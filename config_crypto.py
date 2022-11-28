import os
import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

#debug = True
#loglevel = 'debug'
bind = "8.219.61.64:80"
#后台执行，为True
daemon = True
timeout = 300
errorlog = '-'
accesslog = '-'
# 启动的进程数
workers = multiprocessing.cpu_count()
x_forwarded_for_header = 'X-FORWARDED-FOR'

