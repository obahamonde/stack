import { type ViteSSGContext } from 'vite-ssg'

export type UserModule = (ctx: ViteSSGContext) => void

export type User = {
    nickname: string
    name: string
    picture: string
    updated_at: string
    email: string
    email_verified: boolean
    sub: string 
}

export type Message = {
    user: User
    content: string
}