from dataclasses import dataclass

@dataclass
class Deteccion:
    x: float
    y: float
    width: float
    height: float
    class_name: str
    confidence: float