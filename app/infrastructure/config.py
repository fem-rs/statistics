import yaml

def read_config():
    try:
        with open("Config.yaml", "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except Exception as err:
        raise err   