import platform

def aw(arg, info): # i have no idea what i wrote here
    a.write(str(f'{arg} - {info}\n'))

def get_distro():
    infa = platform.freedesktop_os_release()
    ids = infa["ID"]
    return ids

with open('about.txt', 'w') as a:
    aw(platform.system(), 'system')
    if platform.system() == 'Linux':
        aw(get_distro(), 'distro')
    elif platform.system() == 'Windows':
        aw(platform.win32_ver(), 'windows version')
        aw(platform.win32_is_iot(), 'is interprice version')
    
    aw(platform.release(), 'release version')
    aw(platform.node(), 'username')
    aw(platform.machine(), 'architecture')