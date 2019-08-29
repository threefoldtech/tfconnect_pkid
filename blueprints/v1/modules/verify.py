import base64
import nacl.encoding
import nacl.signing
import json
import time

def verifySignedData(pk, data):
    try:
        print('/n### --- data verification --- ###')
        print("Verifying data: ", data)

        # signature validation
        decoded_data = base64.b64decode(data)
        print("Decoding data: ", decoded_data)

        verify_key = nacl.signing.VerifyKey(pk, encoder=nacl.encoding.HexEncoder)
        print('verify_key: ', verify_key)

        verified_signed_data = verify_key.verify(decoded_data)
        print('verified_signed_data: ', verified_signed_data)

        print('### --- END data verification --- ###/n')
        return verified_signed_data
    except:
        return None


def verifySignedHeader(pk, header):
    try:
        print('/n### --- header verification --- ###')
        print("Verifying header: ", header)

        # signature validation
        decoded_header = base64.b64decode(header)
        print("Decoding header: ", decoded_header)

        verify_key = nacl.signing.VerifyKey(pk, encoder=nacl.encoding.HexEncoder)
        print('verify_key: ', verify_key)

        verified_signed_header = verify_key.verify(decoded_header)
        print('verified_signed_header: ', verified_signed_header)

        # timestamp validation 
        header = json.loads(verified_signed_header)

        milliseconds = time.time() * 1000
        diff = milliseconds - header['timestamp']
        print('timestamp difference', diff)

        print('### --- END header verification --- ###/n')

        # check if diff is less than 5s 
        # check if intent matches
        if diff < 5000 and header['intent'] == 'pkid.store':
            return header
        
        # raise exception in case validation fails
        raise 
    except:
        return None