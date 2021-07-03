"""
Problem: root can't create mode=777 dir
- https://blog.csdn.net/cuma2369/article/details/107665408
- https://stackoverflow.com/questions/5231901/permission-problems-when-creating-a-dir-with-os-makedirs-in-python
"""

import os

oldmask = os.umask(000)
os.makedirs('dir1', mode=0o777)
os.makedirs('dir2', mode=0o777)
os.umask(oldmask)
