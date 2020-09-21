# test push gitlab

import yaml

from utils import Singleton


class Settings(object, metaclass=Singleton.Singleton):

    def __init__(self):
        self.configPath = "./settings/configfile.yml"
        self.config = yaml.safe_load(open(self.configPath))

    def getConfig(self):
        return self.config
