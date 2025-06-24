import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x ali')
    os.system('./ali')
elif bit == '32bit':
    os.system('chmod +x ali32')
    os.system('./ali32')
else:
    print('device not supported')
