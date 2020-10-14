from enum import Enum


class Enumerable(Enum):
    def __str__(self) -> str:
        return str(self.value)


class Env(Enumerable):
    ACCEPTANCE = "acceptance"
    COMMON = "common"
    DEVELOPMENT = "development"
    NONE = "none"
    PRODUCTION = "production"
    SERVICES = "services"
    TEST = "test"


class WorkloadType(Enumerable):
    DEFAULT = "default"
