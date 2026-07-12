from abc import ABC
from abc import abstractmethod


class BaseIntelligence(ABC):

    @abstractmethod
    def analyze(
        self,
        normalized: dict,
    ) -> dict:
        pass