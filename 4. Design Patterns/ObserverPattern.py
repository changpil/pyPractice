import abc
class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self, lon, lat):
        pass

class MobileApp(Observer):
    def update(self, lon=0.0, lat=0.0):
        print(f"{lon} : {lat}")

class MobilePhone:
    lon, lat = 0.0, 0.0
    observers = []

    def move(cls, lon, lat):
        if cls.lon == lon and cls.lat == lat:
            return
        cls.lon, cls.lat  = lon, lat
        cls.notify()

    def register(cls, o):
        cls.observers.append(o)

    def notify(cls):
        for observer in cls.observers:
            observer.update(cls.lon, cls.lat)

phone = MobilePhone()

phone.register(MobileApp())
phone.move(1.0, 1.2)
phone.move(1.1, 21.2)
phone.move(1.2, 93)
phone.move(333.0, 144.2)


class Sub:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print(f"Notification for {self.name} : {message}")

class Pub:
    def __init__(self):
        self.subs = set()

    def register(self,sub):
        self.subs.add(sub)

    def unregister(self, sub):
        self.subs.discard(sub)

    def notify(self, message):
        for sub in self.subs:
            sub.update(message)

sub_list = [Sub("changpil@gmail.com"), Sub("clee@suse.com"),Sub("chalee@microsoft.com")]
pub = Pub()
for sub in sub_list:
    pub.register(sub)

pub.notify("greeting")