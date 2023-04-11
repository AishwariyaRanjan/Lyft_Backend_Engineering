from servicable import Servicable


class Car(Servicable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()


# from abc import ABC, abstractmethod
# from engine import ConcreteStrategyCapulet, ConcreteStrategySternman, ConcreteStrategyWilloughby, EngineContext
# from battery import BatteryContext, ConcreteStrategyNubbin, ConcreteStrategySpindler

# # classes to define concrete products


# class Car(ABC):
#     # The Car interface declares the operations that all concrete products
#     # must implement
#     def __init__(self, engine, battery):
#         # self.last_service_date = last_service_date
#         self.engine = engine
#         self.battery = battery

#     @abstractmethod
#     def needs_service(self):
#         pass

# # Concrete Products provide various implementations of the Car interface.


# class ConcreteCarCalliope(Car):
#     def needs_service(self, current_date, last_service_date, current_mileage, last_service_mileage) -> bool:
#         engine_context = EngineContext(ConcreteStrategyCapulet(
#             last_service_mileage, current_mileage))
#         battery_context = BatteryContext(
#             ConcreteStrategySpindler(last_service_date, current_date))

#         if engine_context.execute_strategy() or battery_context.execute_strategy():
#             return True
#         return False


# class ConcreteCarGlissade(Car):
#     def needs_service(self, current_date, last_service_date, current_mileage, last_service_mileage) -> bool:
#         engine_context = EngineContext(ConcreteStrategyWilloughby(
#             last_service_mileage, current_mileage))
#         battery_context = BatteryContext(
#             ConcreteStrategySpindler(last_service_date, current_date))

#         if engine_context.execute_strategy() or battery_context.execute_strategy:
#             return True
#         return False


# class ConcreteCarPalindrome(Car):
#     def needs_service(self, current_date, last_service_date, warning_light_on) -> bool:
#         engine_context = EngineContext(
#             ConcreteStrategySternman(warning_light_on))
#         battery_context = BatteryContext(
#             ConcreteStrategySpindler(last_service_date, current_date))

#         if engine_context.execute_strategy() or battery_context.execute_strategy:
#             return True
#         return False


# class ConcreteCarRorschach(Car):
#     def needs_service(self, current_date, last_service_date, current_mileage, last_service_mileage) -> bool:
#         engine_context = EngineContext(ConcreteStrategyWilloughby(
#             last_service_mileage, current_mileage))
#         battery_context = BatteryContext(
#             ConcreteStrategyNubbin(last_service_date, current_date))

#         if engine_context.execute_strategy() or battery_context.execute_strategy:
#             return True
#         return False


# class ConcreteCarThovex(Car):
#     def needs_service(self, current_date, last_service_date, current_mileage, last_service_mileage) -> bool:
#         engine_context = EngineContext(ConcreteStrategyCapulet(
#             last_service_mileage, current_mileage))
#         battery_context = BatteryContext(
#             ConcreteStrategyNubbin(last_service_date, current_date))

#         if engine_context.execute_strategy() or battery_context.execute_strategy:
#             return True
#         return False

# # ----------------------------------------------------------------

# # creator class for factory method


# class CarFactory(ABC):
#     @abstractmethod
#     def createCar(self):
#         pass

#     def needs_service(self):
#         # Call the factory method to create a product object.
#         my_car = self.createCar()
#         result = my_car.needs_service()
#         return result

# # Concrete Creators to override the factory method in order to change the resulting
# # product's type.


# class ConcreteCreatorCalliope(CarFactory):
#     def createCar(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
#         return ConcreteCarCalliope(current_date, last_service_date, current_mileage, last_service_mileage)


# class ConcreteCreatorGlissade(CarFactory):
#     def createCar(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
#         return ConcreteCarGlissade(current_date, last_service_date, current_mileage, last_service_mileage)


# class ConcreteCreatorPalindrome(CarFactory):
#     def createCar(self, current_date, last_service_date, warning_light_on) -> Car:
#         return ConcreteCarPalindrome(current_date, last_service_date, warning_light_on)


# class ConcreteCreatorRorschach(CarFactory):
#     def createCar(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
#         return ConcreteCarRorschach(current_date, last_service_date, current_mileage, last_service_mileage)


# class ConcreteCreatorThovex(CarFactory):
#     def createCar(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
#         return ConcreteCarThovex(current_date, last_service_date, current_mileage, last_service_mileage)

# # ---------
