def context_404(context):
    # Modify the 404 page context
    context.custom_message = "Oops! This page is lost in space."
    context.suggested_link = "/"
    context.image_url = "/assets/demoapp/images/404-image.svg"