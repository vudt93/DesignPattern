#!/usr/bin/env python

from Observer.ConcreteObserver import ConcreteObserver
from Observer.ConcreteSubject import ConcreteSubject

observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject = ConcreteSubject()
subject.subcribe(observer1)
subject.subcribe(observer2)
subject.notify_all("Event A")
subject.unsubcribe(observer1)
subject.notify_all("Event B")