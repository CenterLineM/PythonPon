class Human(object):
# 類屬性 此類共用
    species = "H. sapiens"

    def __init__(self,name):
        # Assign theargument to the instance's name attribute'
        self.name = name
    def say(self, msg):
        return "{name}: {message}".format(name=self.name, message=msg)

# 類方法