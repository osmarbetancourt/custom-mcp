from typing import Any, Dict

class BackgroundWorkerDetails:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(**data)

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__
