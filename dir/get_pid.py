"""
获取进程的PID值
"""

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    sleep(1)
    print("Child PID:",os.getpid())
    print("Get Parent PID:",os.getppid())
else:
    print("Get Child PID:",pid)
    print("Parent PID:", os.getpid())

