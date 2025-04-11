from abc import ABC, abstractmethod


class Provider(ABC):

    @abstractmethod
    def create_instance(self, model: str, **kwargs) -> int:
        pass

    @abstractmethod
    def get_instance_status(self, instance_id: int) -> str:
        pass

    @abstractmethod
    def terminate_instance(self, instance_id: int) -> None:
        pass
