import sys


class Node:
    def __init__(self, _id):
        self.__distance = sys.maxsize
        self.__parents = None
        self.__children = {}
        self.__id = _id

    def add_child(self, another_node, distance):
        self.__children[another_node] = distance

    def get_id(self):
        return self.__id

    def get_distance(self):
        return self.__distance

    def get_parents(self):
        return self.__parents

    def get_children(self):
        return self.__children

    def set_distance(self, distance):
        self.__distance = distance

    def set_parents(self, parents):
        self.__parents = parents


def dijkstra(source: Node, graph):
    source.set_distance(0)
    none_visited_vertex = set(graph)

    while none_visited_vertex:
        vertex_with_min_dist = min(none_visited_vertex, key=lambda s: s.get_distance())

        none_visited_vertex.remove(vertex_with_min_dist)

        for child, distance in vertex_with_min_dist.get_children().items():
            temporary_dist = vertex_with_min_dist.get_distance() + distance

            if temporary_dist < child.get_distance():
                child.set_distance(temporary_dist)
                child.set_parents(vertex_with_min_dist)


def search_shortest_path(node_to_search):
    path = []
    node = node_to_search
    while node:
        path.append(node.get_id())
        node = node.get_parents()

    path.reverse()
    return path