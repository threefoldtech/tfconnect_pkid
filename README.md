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


# Using PKID in combination with the Threefold Connect app - derived key scope

You can let the user login using TF-Connect on your own 3rd party app, get a unique key (unique for the user and your application) and use that to write data to PKID.

Flow:
## 1. Make the user log in using TF-Connect 
Use the example to find out how to make the user log in and get a derived seed. 
URL for staging: https://example.staging.jimber.org/ (use 'Authenticate & get emailaddress and derived seed.' button)
URL of example code repository: https://github.com/threefoldtech/threefold_connect/tree/master/example
         
## 2. Get the key from the scope
See callback.js @ https://github.com/threefoldtech/threefold_connect/blob/master/example/src/views/callback/callback.js

## 3. Write data to PKID
Get the derived seed from the decrypted data in step 2, use the "Set document" section to write to PKID.



