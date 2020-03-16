from Adapter.Adaptee import Adaptee
from Adapter.ClassAdapter import ClassAdapter
from Adapter.ObjectAdapter import ObjectAdapter
from Adapter.Target import Target

target = Target("John", 25, "37 Manhattan")
adaptee = Adaptee("Mary", 23, 37, "Chicago")

object_adapter = ObjectAdapter(adaptee)


def print_info(obj):
    print("{} {} {}".format(obj.name, obj.age, obj.address))


object_adapter = ObjectAdapter(adaptee)
class_adapter = ClassAdapter(adaptee.name, adaptee.age, adaptee.street_num, adaptee.street_name)

print_info(target)
print_info(object_adapter)
print_info(class_adapter)
