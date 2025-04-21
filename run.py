import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x rvg')
    os.system('./rvg')
elif bit == '32bit':
    os.system('chmod +x rvg32')
    os.system('./rvg32')
else:
    print('device not supported')
