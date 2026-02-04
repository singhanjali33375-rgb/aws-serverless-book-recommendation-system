import json
from comprehend_utils import analyze_text
from dynamodb_utils import get_recommended_books

def lambda_handler(event, context):
    preference = event.get("preference", "")

    keywords = analyze_text(preference)
    books = get_recommended_books(keywords)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "recommendedBooks": books
        })
    }
