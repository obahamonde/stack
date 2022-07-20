import { createAuth0, authGuard } from '@auth0/auth0-vue';
import { type UserModule } from '~/types'

const domain = "dev-tvhqmk7a.us.auth0.com"
const clientId = "53p0EBRRWxSYA3mSywbxhEeIlIexYWbs"
const calbackURL = "http://localhost:3000/"



export const install: UserModule = ({ isClient, initialState, app, router }) => {
  const auth0 = createAuth0({
    domain: domain,
    client_id: clientId,
    redirect_uri: calbackURL,
    audience: "https://oscarbahamonde.cloud/"
  })
 
  app.use(auth0)
}
