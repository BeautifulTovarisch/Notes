Amazon Cognito provides ODIC Identity Providers (IdP) in the form of Cognito User Pools.

```mermaid
graph LR
user((User))
cognito[[Cognito]]

oauth{Oauth}
oidc{OIDC}
saml{SAML}

user-- OIDC -->cognito

cognito-->oauth
cognito-->oidc
cognito-->saml
```

## Rate Limits

## User Pools

User pools act an an OIDC identity provider. Pools provide both federated and direct login access to users.

- Issues user attributes in a JWT
- Can be configured to handle interaction with 3rd party IdPs

### Authentication

Cognito provides several mechanisms for authentication. Generally these involve invoking specific APIs and/or responding to authentication challenges.

#### Normal Authentication

The following sequence is used for **client-side** authentication flows:

1. `InitiateAuth`
2. `RespondToAuthChallenge`

```mermaid
sequenceDiagram
User->>App: Credentials

App->>User Pool: InitiateAuth
User Pool->>App: Challenge
App->>User: Prompt
User->>App: Response

App->>User Pool: RespondToAuthChallenge
User Pool->>App: Tokens
App->>User: Access to Application
```

## Identity Pools

## Security

## Common Scenarios