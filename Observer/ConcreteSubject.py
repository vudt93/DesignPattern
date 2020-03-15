from Observer.Subject import Subject


class ConcreteSubject(Subject):
    observer_list = []

    def __init__(self):
        pass

    def subcribe(self, observer):
        self.observer_list.append(observer)

    def unsubcribe(self, observer):
        self.observer_list.remove(observer)

    def notify_all(self, event):
        for o in self.observer_list:
            o.update(event)