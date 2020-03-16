from Builder.CarBuilder import CarBuilder
from Builder.Director import Director
from Builder.Form import Form
from Builder.FormBuilder import FormBuilder
from Builder.MotorbikeBuilder import MotorbikeBuilder

car_builder = CarBuilder()
motorbike_builder = MotorbikeBuilder()

car_director = Director(car_builder)
motorbike_director = Director(motorbike_builder)

car_director.build_car()
motorbike_director.build_motorbike()

car_builder.get_product().print()
motorbike_builder.get_product().print()


form_builder = FormBuilder("vudt", "123456", "abc123@gmail.com", "0907861123")
form_builder.set_city("Ho Chi Minh")
form_builder.set_birth_date("1993")
form = Form(form_builder)
form.print()
