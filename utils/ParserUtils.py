import json


class ParserUtils:

    @staticmethod
    def parse_json(path):
        f = open(path)
        data = json.load(f)
        f.close()
        return data
