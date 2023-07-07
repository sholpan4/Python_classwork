config = {}

cfg_file = open('config.ini', encoding='utf-8')
my_config = cfg_file.readlines()
cfg_file.close()

print(my_config)
current_section = ""

for x in my_config:  #желательно i для индекса
    my_config = x.split("=")
    key = my_config[0]
    my_config[0] = my_config[0].strip()
    if len(my_config) == 1:
        if my_config[0].startswith('[') and my_config[0].endswith(']'):
            current_section = my_config[0][1:-1]
            config[current_section] = {}
    else:
        value = my_config[1]
        my_config[1] = my_config[1].strip()

        if my_config[0].startswith('#') or my_config[0].startswith(';'):
            continue
        if my_config[1].lower() in ['true', 'yes', 'on']:
            my_config[1] = True
        elif my_config[1].lower() in ['false', 'no', 'off']:
            my_config[1] = False
        elif my_config[1].isdigit():
            my_config[1] = int(my_config[1])
        config[current_section][my_config[0]] = my_config[1]
    #print(config)  будет повторение, елка
print(config)

