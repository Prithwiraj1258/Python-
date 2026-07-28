class singleton:
    __instance=None
    def __init__(self):
        if singleton. __instance==None:
           singleton. __instance=self
        else :
            raise Exception('This is Singleton. Already have an instance, use that one by calling get_instance method')
    @staticmethod
    def get_instance():
       if singleton.__instance is None:
          singleton()
       
       return singleton.__instance

first=singleton.get_instance()
second=singleton.get_instance()
print(first)
print(second)