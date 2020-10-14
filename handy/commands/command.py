from ..core.constants import Env
from ..services import ServiceAction


class CommandOptions(object):
    def __init__(self):
        self.environment = Env.NONE
        self.workload_name = ""
        self.workload_number = ""

    @property
    def environment(self) -> Env:
        return self._environment

    @environment.setter
    def environment(self, value: Env) -> None:
        self._environment = value

    @property
    def workload_name(self) -> str:
        return self._workload_name

    @workload_name.setter
    def workload_name(self, value: str) -> None:
        self._workload_name = value

    @property
    def workload_number(self) -> str:
        return self._workload_number

    @workload_number.setter
    def workload_number(self, value: str) -> None:
        self._workload_number = value


class Command(object):
    _action: ServiceAction
    _options: CommandOptions

    def __init__(self, options: CommandOptions) -> None:
        self._action = None
        self._options = options

    def execute(self) -> None:
        try:
            return self.__dict__[f"execute_{self._options.environment}"]()
        except KeyError:
            return self.execute_all()

    def execute_all(self) -> None:
        if self._action:
            self._action.execute()
        else:
            raise ActionNotImplementedError()

    def execute_none(self) -> None:
        raise NotImplementedError()
