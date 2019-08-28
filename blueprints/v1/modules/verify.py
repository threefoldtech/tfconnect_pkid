import base64
import nacl.encoding
import nacl.signing

def verifySignedData(pk, data):
    print('/n### --- data verification --- ###')
    print("Verifying data: ", data)

    decoded_data = base64.b64decode(data)
    print("Decoding data: ", decoded_data)

    print(data)

    verify_key = nacl.signing.VerifyKey(pk, encoder=nacl.encoding.HexEncoder)
    print('verify_key: ', verify_key)

    verified_signed_data = verify_key.verify(decoded_data)
    print('verified_signed_data: ', verified_signed_data)

    print('### --- END data verification --- ###/n')

    return verified_signed_data