from abc import ABC, abstractmethod
from datetime import datetime

class BatteryStrategy(ABC):
    @abstractmethod
    def needs_service():
        pass

class ConcreteStrategySpindler(BatteryStrategy):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if self.current_date.year - self.last_service_date.year > 2:
            return True
        return False
        
class ConcreteStrategyNubbin(BatteryStrategy):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if self.current_date.year - self.last_service_date.year > 4:
            return True
        return False

    
#--------------------------#
class BatteryContext():
    def __init__(self, strategy: BatteryStrategy) -> None:
        self._strategy = strategy

    def strategy(self) -> BatteryStrategy:
       return self._strategy
    
    def strategy(self, strategy: BatteryStrategy) -> None:
        self._strategy = strategy

    def execute_strategy(self)->None:
        self._strategy.needs_service() #what about parameters for diff engines