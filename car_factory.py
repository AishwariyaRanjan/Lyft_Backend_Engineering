from battery_nubbin import Nubbin
from battery_spindler import Spindler
from car import Car
from engine_capulet import Capulet
from engine_strenman import Sternman
from engine_willoughby import Willoughby


class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Capulet(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Willoughby(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        engine = Sternman(warning_light_is_on)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Willoughby(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Capulet(current_mileage, last_service_mileage)
        battery = Nubbin(current_date, last_service_date)
        car = Car(engine, battery)
        return car
