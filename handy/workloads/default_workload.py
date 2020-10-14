from ..commands import (
    MachineCredentialsSecretCommandOptions,
    ProvisionMachineCredentialsSecretCommand,
    DestroyMachineCredentialsSecretCommand,
)
from ..core.constants import Env
from ..services.secrets_manager import Secret, SecretsManagerService, VaultService
from .workload import Workload


class DefaultWorkload(Workload):
    _secret_manager: SecretsManagerService

    def __init__(self, name: str, number: int, environment: Env) -> None:
        super().__init__(name, number, environment)
        self._secret_manager = VaultService()

    def destroy(self):
        self.add_destroy_command(self._destroy_machine_credentials_secret())
        super().destroy()

    def provision(self):
        self.add_provision_command(self._provision_machine_credentials_secret())
        super().provision()

    def _provision_machine_credentials_secret(
        self,
    ) -> ProvisionMachineCredentialsSecretCommand:
        options = MachineCredentialsSecretCommandOptions()
        options.active_directory_enabled = True
        options.active_directory_username = (
            f"a_m{self.number}_{self.environment}@{self.environment_short}.{domain}"
        )
        options.okta_enabled = True
        options.okta_username = f"{self.slug}@{self.environment}.admin"
        options.secret_path = f"/workloads/{self.slug}/{self.environment}/managed"

        return ProvisionMachineCredentialsSecretCommand(options, self._vault)

    def _destroy_machine_credentials_secret(
        self,
    ) -> DestroyMachineCredentialsSecretCommand:
        options = MachineCredentialsSecretCommandOptions()
        options.secret_path = f"/workloads/{self.slug}/{self.environment}/managed"

        return DestroyMachineCredentialsSecretCommand(options, self._vault)
