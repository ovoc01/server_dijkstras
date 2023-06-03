import sys

class Server:
    
    def __init__(self, ip):
        self.__ip = ip
        self.__website = []
        self.__distance: int = sys.maxsize
        self.__seeable = True
        self.__parents = None
        self.__children = {}

    def add_website(self, website):
        self.__website.append(website)

    def add_connection(self, server, distance):
        self.__children[server] = distance

    def get_distance(self):
        return self.__distance

    def set_distance(self, distance):
        self.__distance = distance

    def get_ip(self):
        return self.__ip

    def get_website(self):
        return self.__website

    def get_children(self):
        return self.__children

    def get_seeable(self):
        return self.__seeable

    def set_seeable(self, seeable):
        self.__seeable = seeable

def dijkstra(servers, start, target_website):
    unvisited = set(servers)
    start.set_distance(0)
    closest_server = None

    while unvisited:
        current_server = min(unvisited, key=lambda server: server.get_distance())
        unvisited.remove(current_server)

        if target_website in current_server.get_website():
            if closest_server is None or current_server.get_distance() < closest_server.get_distance():
                closest_server = current_server

        for neighbor, distance in current_server.get_children().items():
            if neighbor.get_seeable():
                new_distance = current_server.get_distance() + distance
                if new_distance < neighbor.get_distance():
                    neighbor.set_distance(new_distance)

    return closest_server