# PKID

## Concept
PKID is a public Key Indexed Datastore. You can save plain or encrypted data in a public key index; as long as you are the owner of the secret corresponding to that public key.


# Routes

## Document storage
### Set document

```
PUT /v1/documents/{pk}/{key}
```
Set the value of a document corresponding to {key} indexed by the public key {pk}. This is only possible when sending following header; signed by the secret key corresponding to {pk}.

pk is hex encoded;
request data is a base64 encoded and signed;
header is base64 encoded and signed;

```
{ 'intent' : 'pkid.store', timestamp: 'epochtime'}
```

### Get document

```
GET /v1/documents/{pk}/{key}
```
pk is hex encoded;
response data is base64 encoded;

Get the value of a document corresponding to {key} indexed by the public key {pk}. There is no requirement for a security header

# Run in dev mode

To run the backend in devmode simply execute following command

```
bin/dev.sh
```
or
```
docker-compose build
docker-compose up
```