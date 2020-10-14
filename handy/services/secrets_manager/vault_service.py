from .secrets_manager_service import (
    Policy,
    Secret,
    Token,
    SecretsManagerService,
    CreateSecretAction,
    DeleteSecretAction,
    ReadSecretAction,
    CreatePolicyAction,
    DeletePolicyAction,
    ReadPolicyAction,
    CreateTokenAction,
    DeleteTokenAction,
    ReadTokenAction,
)


class VaultService(SecretsManagerService):
    def __init__(self) -> None:
        pass

    def create_secret(self, secret: Secret) -> None:
        print(f"create_secret: {secret.full_name}")

    def read_secret(self, secret: Secret) -> None:
        print("read_secret")

    def delete_secret(self, secret: Secret) -> None:
        print("delete_secret")

    def create_policy(self, policy: Policy) -> None:
        print(f"create_policy: {policy.path}")

    def read_policy(self, policy: Policy) -> None:
        print("read_policy")

    def delete_policy(self, policy: Policy) -> None:
        print("delete_policy")

    def create_token(self, token: Token) -> None:
        print("create_token")

    def read_token(self, token: Token) -> None:
        print("read_token")

    def delete_token(self, token: Token) -> None:
        print("delete_token")


class VaultCreateSecretAction(CreateSecretAction):
    def __init__(self, service: VaultService, secret: Secret) -> None:
        super().__init__(service, secret)


class VaultDeleteSecretAction(DeleteSecretAction):
    def __init__(self, service: VaultService, secret: Secret) -> None:
        super().__init__(service, secret)


class VaultReadSecretAction(ReadSecretAction):
    def __init__(self, service: VaultService, secret: Secret) -> None:
        super().__init__(service, service)


class VaultCreatePolicyAction(CreatePolicyAction):
    def __init__(self, service: VaultService, policy: Policy) -> None:
        super().__init__(service, policy)


class VaultDeletePolicyAction(DeletePolicyAction):
    def __init__(self, service: VaultService, policy: Policy) -> None:
        super().__init__(service, policy)


class VaultReadPolicyAction(ReadPolicyAction):
    def __init__(self, service: VaultService, policy: Policy) -> None:
        super().__init__(service, policy)


class VaultCreateTokenAction(CreateTokenAction):
    def __init__(self, service: VaultService, token: Token) -> None:
        super().__init__(service, token)


class VaultDeleteTokenAction(DeleteTokenAction):
    def __init__(self, service: VaultService, token: Token) -> None:
        super().__init__(service, token)


class VaultReadTokenAction(ReadTokenAction):
    def __init__(self, service: VaultService, token: Token) -> None:
        super().__init__(service, token)
