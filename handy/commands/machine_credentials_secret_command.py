from ..commands import Command, CommandOptions
from ..core.constants import Env
from ..helpers.security import generate_password
from ..services.secrets_manager import (
    SecretsManagerService,
    CreateSecretAction,
    DeleteSecretAction,
)


class MachineCredentialsSecretCommandOptions(CommandOptions):
    def __init__(self):
        super().__init__()
        self.active_directory_enabled = False
        self.active_directory_username = ""
        self.okta_enabled = False
        self.okta_username = ""
        self.password = generate_password()
        self.secret_name = "machine"
        self.temp_password = generate_password()

    @property
    def active_directory_enabled(self) -> bool:
        return self._active_directory_enabled

    @active_directory_enabled.setter
    def active_directory_enabled(self, value: bool) -> None:
        self._active_directory_enabled = value

    @property
    def active_directory_username(self) -> str:
        return self._active_directory_username

    @active_directory_username.setter
    def active_directory_username(self, value: str) -> None:
        self._active_directory_username = value

    @property
    def okta_enabled(self) -> bool:
        return self._okta_enabled

    @okta_enabled.setter
    def okta_enabled(self, value: bool) -> None:
        self._okta_enabled = value

    @property
    def okta_username(self) -> str:
        return self._okta_username

    @okta_username.setter
    def okta_username(self, value: str) -> None:
        self._okta_username = value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        self._password = value

    @property
    def secret_name(self) -> str:
        return self._secret_name

    @secret_name.setter
    def secret_name(self, value: str) -> None:
        self._secret_name = value

    @property
    def secret_path(self) -> str:
        path = ""

        if self.workload_number and self.workload_name:
            path += f"/{self.workload_number}-{self.workload_name}"

        if self.environment is not Env.NONE:
            path += f"/{self.environment}"

        return path

    @property
    def temp_password(self) -> str:
        return self._temp_password

    @temp_password.setter
    def temp_password(self, value: str) -> None:
        self._temp_password = value


class MachineCredentialsSecretCommand(Command):
    _secret_manager: SecretsManagerService

    def __init__(
        self,
        options: MachineCredentialsSecretCommandOptions,
        secret_manager: SecretsManagerService,
    ):
        super().__init__(options)
        self._secret_manager = secret_manager


class ProvisionMachineCredentialsSecretCommand(MachineCredentialsSecretCommand):
    def __init__(
        self,
        options: MachineCredentialsSecretCommandOptions,
        secret_manager: SecretsManagerService,
    ):
        super().__init__(options, secret_manager)
        self._action = self._build_action()

    def _build_action(self) -> CreateSecretAction:
        secret_data = {
            "password": self._options.password,
            "temporary_password": self._options.temp_password,
        }

        if self._options.active_directory_enabled:
            secret_data["ad_username"] = self._options.active_directory_username

        if self._options.okta_enabled:
            secret_data["okta_username"] = self._options.okta_username

        return CreateSecretAction(
            self._secret_manager,
            Secret(secret_data, self._options.secret_name, self._options.secret_path),
        )


class DestroyMachineCredentialsSecretCommand(MachineCredentialsSecretCommand):
    def __init__(
        self,
        options: MachineCredentialsSecretCommandOptions,
        secret_manager: SecretsManagerService,
    ):
        super().__init__(options, secret_manager)
        self._action = self._build_action()

    def _build_action(self) -> DeleteSecretAction:
        return DeleteSecretAction(
            self._secret_manager,
            Secret(None, self._options.secret_name, self._options.secret_path),
        )
