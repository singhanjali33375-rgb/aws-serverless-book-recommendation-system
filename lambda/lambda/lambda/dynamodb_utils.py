import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("BooksTable")

def get_recommended_books(keywords):
    response = table.scan()
    items = response.get("Items", [])

    result = []
    for book in items:
        for key in keywords:
            if key.lower() in book["summary"].lower():
                result.append(book["title"])
                break
    return result
