import frappe

def custom_resolver(path):
    
    route_map = {
        "team-leader": "users/admin",  
        "developer": "users/developer",
        "project-manager": "users/manager"
    }
    
    # If path exists in route_map, return the new route
    return route_map.get(path, path)  # Default to same path if no match
