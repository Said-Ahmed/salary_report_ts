from abc import ABC, abstractmethod
from typing import List, Dict

class BaseReport(ABC):
    def __init__(self, employees: List[Dict]):
        self.employees = employees

    @abstractmethod
    def generate(self) -> str:
        pass