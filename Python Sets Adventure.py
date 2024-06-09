# Define the sets of flight destinations
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Destinations that both airlines fly to
common_destinations = our_routes.intersection(competitor_routes)
print("Destinations both airlines fly to:", common_destinations)

# Destinations unique to your airline
unique_to_our_airline = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_to_our_airline)

# Destinations unique to the competitor airline
unique_to_competitor_airline = competitor_routes.difference(our_routes)
print("Destinations unique to the competitor airline:", unique_to_competitor_airline)

# Whether there are any destinations that neither airline shares
all_destinations = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK"}
neither_airline_destinations = all_destinations.difference(our_routes.union(competitor_routes))
print("Destinations that neither airline shares:", neither_airline_destinations)
