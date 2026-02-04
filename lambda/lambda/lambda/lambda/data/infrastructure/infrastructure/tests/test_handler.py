from lambda.handler import lambda_handler

def test_lambda_handler():
    event = {"preference": "I like productivity books"}
    response = lambda_handler(event, None)
    assert response["statusCode"] == 200
