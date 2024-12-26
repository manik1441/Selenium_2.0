import configparser


def config_read (section, value):
    try:
        config = configparser.ConfigParser()
        config.read('../config/config.ini')
        return config[section][value]
    except Exception as e:
        print(e)
        return None



def base_url():
    try:
        config = configparser.ConfigParser()
        config.read(' ../config/config.ini')
        env = config['DEFAULT']['run_env']
        url = config['URL'][env.upper()]
        print (url + '---------')
        return url 
    except Exception as e:
        print(e)
        return None