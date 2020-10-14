import abc

from ..service import Service, ServiceAction


DEFAULT_PATH_SEPARATOR = "/"


class Policy(object):
    _path: str
    _policy: str

    def __init__(self, path: str, policy: str) -> None:
        self._path = path
        self._policy = policy

    @property
    def path(self) -> str:
        return self._path

    @property
    def policy(self) -> str:
        return self._policy


class Secret(object):
    _data: str
    _name: str
    _path: str
    _sep: str

    def __init__(self, data: str, name: str, path: str) -> None:
        self._data = data
        self._name = name
        self._path = path
        self._sep = DEFAULT_PATH_SEPARATOR

    @property
    def data(self) -> str:
        return self._data

    @property
    def full_name(self) -> str:
        return self._sep.join([self.path, self.name])

    @property
    def name(self) -> str:
        return self._name

    @property
    def path(self) -> str:
        return self._path


class Token(object):
    def __init__(self) -> None:
        pass


class SecretsManagerService(Service):
    @abc.abstractmethod
    def create_secret(self, secret: Secret) -> None:
        pass

    @abc.abstractmethod
    def read_secret(self, secret: Secret) -> None:
        pass

    @abc.abstractmethod
    def delete_secret(self, secret: Secret) -> None:
        pass

    @abc.abstractmethod
    def create_policy(self, policy: Policy) -> None:
        pass

    @abc.abstractmethod
    def read_policy(self, policy: Policy) -> None:
        pass

    @abc.abstractmethod
    def delete_policy(self, policy: Policy) -> None:
        pass

    @abc.abstractmethod
    def create_token(self, token: Token) -> None:
        pass

    @abc.abstractmethod
    def read_token(self, token: Token) -> None:
        pass

    @abc.abstractmethod
    def delete_token(self, token: Token) -> None:
        pass


class SecretAction(ServiceAction):
    _secret: Secret

    def __init__(self, service: SecretsManagerService, secret: Secret) -> None:
        super().__init__(service)
        self._secret = secret


class CreateSecretAction(SecretAction):
    def __init__(self, service: SecretsManagerService, secret: Secret) -> None:
        super().__init__(service, secret)

    def execute(self) -> None:
        self._service.create_secret(self._secret)


class DeleteSecretAction(SecretAction):
    def __init__(self, service: SecretsManagerService, secret: Secret) -> None:
        super().__init__(service, secret)

    def execute(self) -> None:
        self._service.delete_secret(self._secret)


class ReadSecretAction(SecretAction):
    def __init__(self, service: SecretsManagerService, secret: Secret) -> None:
        super().__init__(service, secret)

    def execute(self) -> None:
        self._service.read_secret(self._secret)


class PolicyAction(ServiceAction):
    _policy: Policy

    def __init__(self, service: SecretsManagerService, policy: Policy) -> None:
        super().__init__(service)
        self._policy = policy


class CreatePolicyAction(PolicyAction):
    def __init__(self, service: SecretsManagerService, policy: Policy) -> None:
        super().__init__(service, policy)

    def execute(self) -> None:
        self._service.create_policy(self._policy)


class DeletePolicyAction(PolicyAction):
    def __init__(self, service: SecretsManagerService, policy: Policy) -> None:
        super().__init__(service, policy)

    def execute(self) -> None:
        self._service.delete_policy(self._policy)


class ReadPolicyAction(PolicyAction):
    def __init__(self, service: SecretsManagerService, policy: Policy) -> None:
        super().__init__(service, policy)

    def execute(self) -> None:
        self._service.read_policy(self._policy)


class TokenAction(ServiceAction):
    _token: Token

    def __init__(self, service: SecretsManagerService, token: Token) -> None:
        super().__init__(service)
        self._token = token


class CreateTokenAction(TokenAction):
    def __init__(self, service: SecretsManagerService, token: Token) -> None:
        super().__init__(service, token)

    def execute(self) -> None:
        self._service.create_token(self._token)


class DeleteTokenAction(TokenAction):
    def __init__(self, service: SecretsManagerService, token: Token) -> None:
        super().__init__(service, token)

    def execute(self) -> None:
        self._service.delete_token(self._token)


class ReadTokenAction(TokenAction):
    def __init__(self, service: SecretsManagerService, token: Token) -> None:
        super().__init__(service, token)

    def execute(self) -> None:
        self._service.read_token(self._token)
