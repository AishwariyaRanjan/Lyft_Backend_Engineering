from __future__ import annotations

from abc import ABC, abstractmethod


class EngineStrategy(ABC):
    @abstractmethod
    def needs_service():
        pass


class ConcreteStrategyCapulet(EngineStrategy):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        if self.current_mileage - self.last_service_mileage > 30000:
            return True
        return False


class ConcreteStrategyWilloughby(EngineStrategy):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        if self.current_mileage - self.last_service_mileage > 60000:
            return True
        return False


class ConcreteStrategySternman(EngineStrategy):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        if self.warning_light_on:
            return True
        return False

# --------------------------#


class EngineContext():
    def __init__(self, strategy: EngineStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> EngineStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: EngineStrategy) -> None:
        self._strategy = strategy

    def execute_strategy(self) -> None:
        self._strategy.needs_service()  # what about parameters for diff engines
