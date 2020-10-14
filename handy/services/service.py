import abc


class ServiceCredential(abc.ABC):
    def __init__(self) -> None:
        pass


class BasicServiceCredential(ServiceCredential):
    _username: str
    _password: str

    def __init__(self, username: str, password: str) -> None:
        self._username = username
        self._password = password


class TokenServiceCredential(ServiceCredential):
    _token: str

    def __init__(self, token: str) -> None:
        self._token = token


class ServiceConnection(abc.ABC):
    def __init__(self) -> None:
        pass


class ServiceSession(abc.ABC):
    _connection: ServiceConnection
    _credential: ServiceCredential

    def __init__(self, credential: ServiceCredential) -> None:
        self._credential = credential

    @abc.abstractmethod
    def connect(self) -> ServiceConnection:
        pass

    def get_connection(self) -> ServiceConnection:
        return self._connection


class Service(abc.ABC):
    _session: ServiceSession

    def __init__(self, session: ServiceSession) -> None:
        self._session = session


class ServiceAction(abc.ABC):
    _service: Service

    def __init__(self, service: Service) -> None:
        self._service = service

    @abc.abstractmethod
    def execute(self):
        pass
