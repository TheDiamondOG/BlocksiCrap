import json
import os

class CoolConfig:
    def __init__(self, config:str, default_conf:dict):
        if not os.path.exists(config):
            with open(config, "w+") as f:
                json.dump(default_conf, f)
        self.config = config
        self.default_conf = default_conf

    def read(self):
        with open(self.config, "r") as f:
            return json.load(f)

    def write(self, data:dict):
        with open(self.config, "w+") as f:
            return json.dump(data, f)

    def reset(self):
        with open(self.config, "w+") as f:
            return json.dump(self.default_conf, f)