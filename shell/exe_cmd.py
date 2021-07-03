import subprocess

cmd = 'ls'

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

for line in p.stdout.readlines():
    print(line)

ret = p.wait()  # wait process