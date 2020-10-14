from typing import Any, Dict, List, Optional

from .exceptions import CycleDetectedError


class Edge(object):
    _source: object
    _target: object
    _data: Any

    def __init__(
        self,
        source: Optional[object] = None,
        target: Optional[object] = None,
        data: Optional[Any] = None,
    ) -> None:
        self._source = source
        self._target = target
        self._data = data

    @property
    def source(self) -> object:
        return self._source

    @property
    def target(self) -> object:
        return self._target

    @property
    def data(self) -> object:
        return self._data


class Vertex(object):
    _data: object

    def __init__(self, data: Optional[Any] = None) -> None:
        self._data = data

    @property
    def data(self) -> object:
        return self._data


class Graph(object):
    _graph: Dict[str, List[Edge]]
    _root: Vertex
    _vertices: Dict[str, Vertex]

    def __init__(self) -> None:
        self._graph = {}
        self._root = Vertex("root")
        self._vertices = {}
        self._vertices[id(self._root)] = self._root
        self._graph[id(self._root)] = []

    def _walker(self, vid: str, visited: List[str], rec: List[str]) -> Vertex:
        visited.append(vid)
        rec.append(vid)

        for edge in self._graph[vid]:
            next_vid = id(edge.target)

            if next_vid in visited:
                if next_vid in rec:
                    raise CycleDetectedError
                else:
                    continue
            else:
                yield from self._walker(next_vid, visited, rec)

        rec.remove(vid)
        vertex = self._vertices[vid]

        if not self.is_root(vertex):
            yield vertex

    def add_vertex(self, vertex: Vertex, source: Optional[Vertex] = None) -> None:
        if source is None:
            source = self._root

        vid = id(vertex)
        self._graph[vid] = []
        self._vertices[vid] = vertex
        self.add_edge(vertex, source)

    def add_edge(self, target: Vertex, source: Optional[Vertex] = None) -> None:
        if source is None:
            source = self._root

        edge = Edge(source, target)
        self._graph[id(source)].append(edge)

    def is_root(self, vertex: Vertex) -> bool:
        return id(vertex) == id(self._root)

    def walk(self) -> Vertex:
        visited = []
        rec = []

        yield from self._walker(id(self._root), visited, rec)
