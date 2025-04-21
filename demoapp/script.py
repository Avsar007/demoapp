def get_web_pages_with_dynamic_routes():
    return [{
        "doctype": "Custom Web Page",  # Doctype for dynamic pages (must extend WebsiteGenerator)
        "route": "/profile/<name>",  # Dynamic route where <name> changes
        # "name": "profile-page"  # Name of the web view document to render
    }]
