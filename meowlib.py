constlibrary = 'qwerty\nuiop[]\\asdfghjkl;\'zxcvbnm,./\":<>?{}|`1234567 890-=~!@#$%^&*()_+ QWERTYUIOP[]ASDFGHJKL;ZXCVBNM，。/；‘【】、《》？：“{}|~！@#￥%……&*（）——+'





def meow(filename: str):
    def go_meowline(line='', constlibrary=constlibrary):
        meowline = ''
        for i in line:
            if i in constlibrary:
                meowline = meowline + i
                pass
            else:
                if i != '/n':
                    meowline = meowline + '喵'
                    pass
                pass
            pass
        return meowline
    if filename == None:
        return None
    filename.replace('\\', '\\\\')
    meow_filename = filename.split('.')
    meow_filename.insert(-1,'喵.')
    MeowFilename = ''
    for i in meow_filename:
        MeowFilename = MeowFilename + i
        pass
    try:
        file = open(filename, 'r')
        file = file.readlines()
    except UnicodeDecodeError:
        try:
            file = open(filename, 'r', encoding='gbk')
            file = file.readlines()
        except UnicodeDecodeError:
            file = open(filename, 'r', encoding='UTF-8')
            file = file.readlines()
    meow_file = open(MeowFilename, 'w')
    meow_content = []
    for line in file:
        meow_content.append(go_meowline(line))
    meow_file.writelines(meow_content)
    return




