import os, yaml

def api_yml_reader(file):
    try:
        with open(os.path.join(os.path.dirname(__file__), f'../data/api/{file}'),'r') as f:
            yml = yaml.safe_load(f)
        return yml
    except FileNotFoundError as e:
        raise e