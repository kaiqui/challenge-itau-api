def test_token_with_invalid_seed(test_api, generate_token, generate_invalid_seed):
    claims = generate_invalid_seed
    token = generate_token(claims)
    response = test_api(token)
    assert response == False

def test_token_with_invalid_name(test_api, generate_token, generate_invalid_name):
    claims = generate_invalid_name
    token = generate_token(claims)
    response = test_api(token)
    assert response == False

def test_token_with_invalid_name_number(test_api, generate_token, generate_invalid_name_number):
    claims = generate_invalid_name_number
    token = generate_token(claims)
    response = test_api(token)
    assert response == False

def test_token_with_invalid_role(test_api, generate_token, generate_invalid_role):
    claims = generate_invalid_role
    token = generate_token(claims)
    response = test_api(token)
    assert response == False

def test_token_with_all_invalid_claims(test_api, generate_token, generate_invalid_claims):
    claims = generate_invalid_claims
    token = generate_token(claims)
    response = test_api(token)
    assert response == False

def test_token_with_invalid_claims(test_api, generate_token, generate_valid_claims):
    claims = generate_valid_claims
    claims['Itau'] = 'Challange'
    token = generate_token(claims)
    print(token)
    response = test_api(token)
    assert response == False

def test_token_with_all_valid_claims(test_api, generate_token, generate_valid_claims):
    claims = generate_valid_claims
    token = generate_token(claims)
    response = test_api(token)
    assert response == True
