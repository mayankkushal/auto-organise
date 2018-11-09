import json

class ConfigHandelingMixin(object):
    """docstring for ConfigHandelingMixin"""

    def get_config_file(self):
        try:
            config = open('../organise.config', "r")
            return config
        except:
            return False

    def generate_config_file(self):
        with open('../organise.config', 'w') as f1:
            for line in open('organise.config'):
                f1.write(line)
