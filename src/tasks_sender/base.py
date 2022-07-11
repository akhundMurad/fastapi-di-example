from abc import ABC, abstractmethod


class TasksSender(ABC):
    @abstractmethod
    def send_mail(self) -> None:
        pass
