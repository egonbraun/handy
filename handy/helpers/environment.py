from ..core.constants import Env


def env_short(env: Env) -> str:
    if env is Env.NONE:
        raise LookupError()

    return str(env)[0]
