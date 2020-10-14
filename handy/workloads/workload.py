from itertools import chain
from typing import Optional

from ..commands import Command
from ..core.constants import Env
from ..graph import Graph, Vertex


class Workload(object):
    _destroy_graph: Graph
    _provision_graph: Graph
    environment: Env
    name: str
    number: int

    def __init__(self, name: str, number: int, environment: Env) -> None:
        self._destroy_graph = Graph()
        self._provision_graph = Graph()
        self.environment = environment
        self.name = name
        self.number = number

    def destroy(self) -> None:
        for vertex in self._destroy_graph.walk():
            action = vertex.data
            action.execute()

    def provision(self) -> None:
        for vertex in self._provision_graph.walk():
            action = vertex.data
            action.execute()

    def add_provision_command(
        self, action: Command, source: Optional[Vertex] = None
    ) -> Vertex:
        if action is None:
            return None

        vertex = Vertex(action)
        self._provision_graph.add_vertex(vertex, source)
        return vertex

    def add_destroy_command(
        self, action: Command, source: Optional[Vertex] = None
    ) -> Vertex:
        if action is None:
            return None

        vertex = Vertex(action)
        self._destroy_graph.add_vertex(vertex, source)
        return vertex

    @property
    def environment(self) -> str:
        return str(self._environment.value).lower()

    @property
    def environment_short(self) -> str:
        return self.environment[0]

    @property
    def name(self) -> str:
        return self._name.lower()

    @property
    def number(self) -> str:
        return f"{self._number:03}"

    @property
    def slug(self) -> str:
        return "-".join(chain([str(self.number)], self.name.split())).lower()
