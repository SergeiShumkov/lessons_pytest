
class BuilderBaseClass:

    def __init__(self):
        self.result = {}


    def update_inner_value(self, key, value):
        if not isinstance(key, list):
            self.result[key] = value
        else:
            temp = self.result
            for item in key[:-1]:
                if item not in temp.keys():
                    temp[item] = {}
                temp = temp[item]
            temp[key[-1]] = value
        return self   


    def build(self):
        return self.result

