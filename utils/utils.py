import yaml

def api_yml_reader(file):
    with open(f'../../data/api/{file}','r') as f:
        yml = yaml.safe_load(f)
    return yml