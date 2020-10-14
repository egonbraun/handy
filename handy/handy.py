#!/usr/bin/env python3

import fire
from typing import List

from .core.constants import Env, WorkloadType
from .workloads import Workload, DefaultWorkload


class Handy(object):
    workload: Workload
    workload_type: WorkloadType

    def __init__(self, workload_type: WorkloadType = WorkloadType.DEFAULT):
        self.workload = None
        self.workload_type = workload_type

    @property
    def workload_type(self) -> WorkloadType:
        return self._workload_type

    @workload_type.setter
    def workload_type(self, value: WorkloadType) -> None:
        self._workload_type = value

    def provision(self, number: int, name: str, environments: List[Env]) -> None:
        for environment in environments:
            if type == WorkloadType.DEFAULT:
                self.workload = DefaultWorkload(number, name, environment)

            self.workload.provision()

    def destroy(self, number: int, name: str, environments: List[Env]) -> None:
        for environment in environments:
            if type == WorkloadType.DEFAULT:
                self.workload = DefaultWorkload(number, name, environment)

            self.workload.destroy()


if __name__ == "__main__":
    fire.Fire(Handy)
