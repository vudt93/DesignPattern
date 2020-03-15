from Observer.Observer import Observer


class ConcreteObserver(Observer):
    def __init__(self):
        pass

    def update(self, event):
        print("Receive " + event)