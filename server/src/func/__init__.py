from requests import get, post
from qrcode import make
from pydantic import HttpUrl
from jose import jwt, JWTError
from fastapi import UploadFile, File, Request
from src.lib.aws import ses, s3
from src.lib.fql import Q
from src.conf import env


def get_api_token()->str:
    try:
        url = f"https://{env.AUTH0_DOMAIN}/oauth/token"
        payload = {
            "grant_type": "client_credentials",
            "client_id": env.AUTH0_CLIENT_ID,
            "client_secret": env.AUTH0_CLIENT_SECRET,
            "audience": env.AUTH0_AUDIENCE
        }
        headers = {
            "content-type": "application/json"
        }
        response = post(url, json=payload, headers=headers)
        return response.json()['access_token']
    except Exception as e:
        raise Exception(e)

def verify_api_token(access_token: str)->str:
    try:
        jwks = get(f"https://{env.AUTH0_DOMAIN}/.well-known/jwks.json").json()
        claims = jwt.decode(access_token, jwks, algorithms=['RS256'], audience=env.AUTH0_AUDIENCE)
        return claims['sub']
    except JWTError as e:
        raise Exception(e)

def get_account_id()->str:
    try:
        return verify_api_token(get_api_token())
    except Exception as e:
        raise Exception(e)

def get_client_token(req:Request)->str:
    try:
        return req.headers.get("Authorization").split(" ")[1]
    except Exception as e:
        raise Exception(e)

def verify_client_token(token: str)->str:
    try:
        auth_endpoint = f"https://{env.AUTH0_DOMAIN}/oauth/tokeninfo"
        headers = {
            "content-type": "application/json",
            "authorization": f"Bearer {token}"
        }
        return post(auth_endpoint, headers=headers).json()['sub']
    except Exception as e: 
        raise Exception(e)

def upload_file(key: str, file: UploadFile=File(...))->HttpUrl:
    try:
        s3.put_object(Bucket=env.AWS_S3_BUCKET, Key=key, Body=file.file.read(),
            ContentType=file.content_type, ACL='public-read')
        return {
            "url": f"https://{env.AWS_S3_BUCKET}.s3.amazonaws.com/{key}",
            "content_type": file.content_type,
            "name": file.filename

        }
    except Exception as e:
        raise Exception(e)

def send_email(to: str, subject: str, body: str):
    try:
        ses.send_email(
            Source=env.AWS_SES_SOURCE,
            Destination={
                'ToAddresses': [to]
            },
            Message={
                'Subject': {
                    'Data': subject
                },
                'Body': {
                    'Text': {
                        'Data': body
                    }
                }
            }
        )
    except Exception as e:
        raise Exception(e)


def make_qrcode(url: HttpUrl)->HttpUrl:
    try:
        qr_id = id()
        make(url).save(f"tmp/{qr_id}.png")
        upload_file(f"{qr_id}.png", file=File(f"tmp/{qr_id}.png"))
        return f"https://{env.AWS_S3_BUCKET}.s3.amazonaws.com/{qr_id}.png"
    except Exception as e:
        raise Exception(e)