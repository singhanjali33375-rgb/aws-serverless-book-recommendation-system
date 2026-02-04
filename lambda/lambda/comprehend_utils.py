import boto3

comprehend = boto3.client("comprehend")

def analyze_text(text):
    response = comprehend.detect_key_phrases(
        Text=text,
        LanguageCode="en"
    )
    return [item["Text"] for item in response["KeyPhrases"]]
