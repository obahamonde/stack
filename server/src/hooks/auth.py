from fastapi import FastAPI, APIRouter, Request, Response, UploadFile, File, status, Depends, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from requests import get, post
from pydantic import HttpUrl, EmailStr
from typing import Callable, Optional, List, Dict, Union, Any
from src.func import upload_file, send_email, make_qrcode
from src.model.collections import User, Account
from src.lib.fql import Q, fql
from src.conf import env
from jose import jwt, JWTError

class Auth:    
    AUTH0_DOMAIN= env.AUTH0_DOMAIN
    AUTH0_CLIENT_ID= env.AUTH0_CLIENT_ID
    AUTH0_CLIENT_SECRET= env.AUTH0_CLIENT_SECRET 
    AUTH0_APP_CLIENT_ID= env.AUTH0_APP_CLIENT_ID
    AUTH0_APP_CLIENT_SECRET= env.AUTH0_APP_CLIENT_SECRET
    AUTH0_AUDIENCE= env.AUTH0_AUDIENCE
    AUTH0_GRANT_TYPE= env.AUTH0_GRANT_TYPE

    @classmethod
    def get_api_token(cls)->str:
        try:
            url = f"https://{cls.AUTH0_DOMAIN}/oauth/token"
            payload = {
                "grant_type": cls.AUTH0_GRANT_TYPE,
                "client_id": cls.AUTH0_CLIENT_ID,
                "client_secret": cls.AUTH0_CLIENT_SECRET,
                "audience": cls.AUTH0_AUDIENCE
            }
            headers = {
                "content-type": "application/json"
            }
            response = post(url, json=payload, headers=headers)
            return response.json()['access_token']
        except Exception as e:
            raise Exception(e)

    @classmethod
    def verify_api_token(cls, access_token: str)->str:
        try:
            jwks = get(f"https://{cls.AUTH0_DOMAIN}/.well-known/jwks.json").json()
            claims = jwt.decode(access_token, jwks, algorithms=['RS256'], audience=cls.AUTH0_AUDIENCE)
            return claims['sub']
        except JWTError as e:
            raise Exception(e)

    @classmethod
    def get_account_id(cls)->str:
        try:
            return cls.verify_api_token(cls.get_api_token())
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_client_token(cls, req:Request)->str:
        try:
            return req.headers.get('Authorization').split(' ')[1]
        except Exception as e:
            raise Exception(e)

    @classmethod
    def verify_client_token(cls, token: str)->str:
        try:
            auth_endpoint = f"https://{cls.AUTH0_DOMAIN}/userinfo"
            headers = {
                "content-type": "application/json",
                "authorization": f"Bearer {token}"
            }
            return post(auth_endpoint, headers=headers).json()
        except Exception as e: 
            raise Exception(e)
auth = Auth()

def useAuth(app:FastAPI)->FastAPI:
    @app.middleware("http")
    async def auth_middleware(request: Request, call_next: Callable)->Response:
        if request.url.path.startswith("/api"):
            try:
                access_token = auth.get_client_token(request)
                user_id = auth.verify_client_token(access_token)
                request.state.user = user_id
                return await call_next(request)
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e)
        else:
            return await call_next(request)
    return app
