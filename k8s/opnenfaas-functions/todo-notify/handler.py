import json

# Event-driven notification function
# Triggered when a new todo item is created

def handle(event, context):

    # Read incoming JSON data
    try:
        data = json.loads(event.body)

        # Extract todo title
        title = data.get("title", "unknown task")

    except Exception:
        title = event.body or "unknown task"

    # Return notification response
    return {
        "statusCode": 200,
        "body": f"New todo notification created for: {title}"
    }