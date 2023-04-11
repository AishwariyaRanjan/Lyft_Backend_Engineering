from tire import Tire


class Octoprime(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        wear_sum = 0
        for x in self.tire_wear:
            wear_sum += x

        if wear_sum >= 3:
            return True
        else:
            return False
