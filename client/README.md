---
title: Blog
---

<div class="text-center">
  <!-- You can use Vue components inside markdown -->
  <div i-carbon-dicom-overlay class="text-4xl my-2 m-auto" />
  <h3 text-3xl underline font-script>Blog</h3>
</div>
<a href="https://github.com/obahamonde/cloudapi">
<div bg-black text-amber-300 px-2 py-1 rounded-lg shadow m-4 w-64 m-auto my-4 cursor-pointer animate-back-in-down >About this template</div>
</a>
---

**This template integrates several technologies, including the following sorted by category or concern:**

**Front-end**

  [Vue.js](https://vuejs.org/) --- [Vite.js](https://vitejs.dev/) --- [TypeScript](https://www.typescriptlang.org/)
--- [UnoCSS](https://uno.antfu.me/)

**Back end**

  [FastAPI](https://fastapi.tiangolo.com/) -- [PyDantic](https://pydantic-docs.helpmanual.io/) -- [Auth0](https://auth0.com/) -- [FaunaDB](https://fauna.com/)


**Dev Ops**

[Pulumi](https://pulumi.com/) -- [AWS](https://aws.amazon.com/) -- [Cloudflare](https://www.cloudflare.com/) -- [GitHub](https://github.com/)

**Some Cool Features Included**

  [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)

  [ViteSSG](https://github.com/antfu/vite-ssg)

  [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

  [OAuth2](https://oauth.net/)

  [OpenID Connect](https://openid.net/)

  [FQLModel](https://github.com/obahamonde/fqlmodel)

  [Pulumi Automation API](https://pulumi.com/docs/reference/pulumi/pulumi/automation/api/)

  [AWS Service Clients](https://docs.aws.amazon.com/boto3/latest/userguide/clients.html)

**On Active Development**

  [CloudAPI](https://github.com/obahamonde/cloudapi)
  
  Suggestions are welcome! Actually looking for a mentor.

**Minimal_Full_Stack_App_Code**

```python
from fastapi import FastAPI, HttpException
from os import environ
from boto3 import Session
from botocore.exceptions import ClientError
from pydantic import BaseModel, EmailStr
from fastapi.responses import RedirectResponse, JSONResponse

def useSES():
    try:
        ses = Session(**environ).client('ses')
    except ClientError as e:
        print(e)
        return None
    return ses

class Contact(BaseModel):
    name: str
    email: EmailStr
    message: str
    def __repr__(self):
        return f'{self.name} <{self.email}>'

@app.post('/contact')
async def contact(contact: Contact):
    ses = useSES()
    if ses is None:
        raise HttpException(status_code=500, detail='Unable to send email')
    try:
        ses.send_email(
            Source=environ['EMAIL_FROM'],
            Destination={'ToAddresses': [contact.email]},
            Message={
                'Subject': {'Data': f"{contact.name}<{contact.email}> sent you a message"},
                'Body': {'Text': {'Data': contact.message}}
            }
        )
    except ClientError as e:
        print(e)
        raise HttpException(status_code=500, detail='Unable to send email')
    return RedirectResponse(url=f"https://{environ['DOMAIN']}/contact?success=true")
```

```ts
<script setup lang="ts">
    import { useRoute } from '@vite/vite-router';

    const app = new Vue({
        el: '#app',
        setup() {
            const isSuccess = ref(useRoute().query.
            const contact = ref({
                name: '',
                email: '',
                message: ''
            })
            success === 'true');
            const sendEmail = async (contact: Contact) => {
                const res = await fetch('/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(contact)
                });
                if (res.status in [200, 201]) {
                    router.push({
                        path: '/contact',
                        query: {
                            success: 'true'
                        }
                    });
                } else {
                    router.push({
                        path: '/contact',
                        query: {
                            success: 'false'
                        }
                    });
                }
            }
            return {
                contact,
                isSuccess,
                sendEmail
            }
        }
    })
    export default app;
</script>
```

```html
<template>
  <div class="text-center">
    <div i-carbon-dicom-overlay class="text-4xl -mb-6 m-auto" />
    <h3>Contact</h3>
  </div>
  <label for="name">Name</label>
  <input type="text" id="name" v-model="contact.name" />
  <label for="email">Email</label>
  <input type="email" id="email" v-model="contact.email" />
  <label for="message">Message</label>
  <textarea id="message" v-model="contact.message"></textarea>
  <button @click="sendEmail(contact)">Send</button>
  <div v-if="isSuccess">
    <p>Message sent!</p>
  </div>
  <div v-else>
    <p>Message failed to send!</p>
  </div>
</template>
```

````scss
<style scoped lang="scss">
    .text-center {
        text-align: center;
    }
    .text-4xl {
        font-size: 4rem;
    }
    .-mb-6 {
        margin-bottom: 6rem;
    }
    .m-auto {
        margin: auto;
    }
    label {
        display: block;
    }
    input, textarea {
        width: 100%;
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 4px;
        margin-bottom: 1rem;
    }
    textarea {
        height: 10rem;
    }
    button {
        padding: 0.5rem 1rem;
        border: 1px solid #ccc;
        border-radius: 4px;
        background-color: #ccc;
        color: #fff;
        cursor: pointer;
    }
    button:hover {
        background-color: #fff;
        color: #000;
    }
    .success {
        color: #00ff00;
    }
    .failure {
        color: #ff0000;
    }
</style>
    ```
````
