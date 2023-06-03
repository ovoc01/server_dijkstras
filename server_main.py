from server_dijkstras.server import Server,dijkstra
# Create servers
server1 = Server("192.168.1.1")
server2 = Server("192.168.1.2")
server3 = Server("192.168.1.3")

# Add websites to servers
server1.add_website("example.com")
server2.add_website("example.org")
server3.add_website("example.net")
server3.add_website("spotify.com")

# Add connections between servers
server1.add_connection(server2, 10)
server2.add_connection(server3, 5)
server3.add_connection(server1, 20)

# Find the shortest path to a server with a specific website
target_website = "spotify.com"
closest_server = dijkstra([server1, server2, server3], server1, target_website)

if closest_server is not None:
    print(f"The shortest path to a server with {target_website} is {closest_server.get_ip()}")
else:
    print(f"No server found with {target_website}")