from abc import ABC, abstractmethod 

class IModelYolo(ABC):
    @abstractmethod
    def load_model(self, model_path: str) -> None:
        pass

    @abstractmethod
    def predict(self, image) -> list:
        pass