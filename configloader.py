import json

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
            for key, value in input.items()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, bytes):
        return input.encode('utf-8')
    else:
        return input

def loadConfigs(filename):
    file = open(filename, "r")
    configs = byteify(json.load(file))
    file.close()
    return configs
