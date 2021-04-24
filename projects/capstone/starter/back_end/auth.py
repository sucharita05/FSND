import os
import json
from flask import request, _request_ctx_stack, abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen

AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
ALGORITHMS = os.environ.get('ALGORITHMS')
API_AUDIENCE = os.environ.get('API_AUDIENCE')

if not AUTH0_DOMAIN and not ALGORITHMS and not API_AUDIENCE:
    AUTH0_DOMAIN = 'starinmaking.us.auth0.com'
    ALGORITHMS = ['RS256']
    API_AUDIENCE = 'http://localhost:5000'

# AuthError Exception
'''
AuthError Exception
A standardized way to communicate auth failure modes
'''


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code
        abort(status_code)


# Auth Header


def get_token_auth_header():
    # Obtains the Access Token from the Authorization Header
    auth = request.headers.get('Authorization', None)
    # Raise AuthError if no header is present
    if not auth:
        raise AuthError({
            'code': 'authorization_header_missing',
            'description': 'Authorization header is expected.'
        }, 401)

    parts = auth.split()
    # Raise AuthError if no Bearer is present
    if parts[0].lower() != 'bearer':
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must start with "Bearer".'
        }, 401)

    # Raise AuthError if no Token is present
    elif len(parts) == 1:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Token not found.'
        }, 401)

    # Raise AuthError if more than two values are present
    elif len(parts) > 2:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must be bearer token.'
        }, 401)

    token = parts[1]
    # Return the token part of the header
    return token


def check_permissions(permission, payload):
    # Abort if permissions are not included in the payload
    if 'permissions' not in payload:
        abort(400)
    if permission not in payload['permissions']:
        abort(403)


def verify_decode_jwt(token):
    # Get The Public Key From AUTH0
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    # Get The Data in the Header
    unverified_header = jwt.get_unverified_header(token)
    # Choose key
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    # Finally, verify!!!
    if rsa_key:
        try:
            # Use The Key to Validate The JWT
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload
        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
    raise AuthError({
        'code': 'invalid_header',
                'description': 'Unable to find the appropriate key.'
    }, 400)


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # To get the token
            token = get_token_auth_header()
            # To decode the jwt
            payload = verify_decode_jwt(token)
            # Validate claims and check the requested permission
            check_permissions(permission, payload)
            # Return the decorator which passes the decoded payload to the
            # decorated method
            return f(payload, *args, **kwargs)
        return wrapper
    return requires_auth_decorator
