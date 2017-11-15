#!/usr/bin/python -u

import argparse
import base64
import boto3

##########################################################################################################################################
### Grab the arguments
##########################################################################################################################################
parser = argparse.ArgumentParser(prog='Encrypt or decrypt values using kms.')
subparsers = parser.add_subparsers(help='sub-command help')

parser_encrypt = subparsers.add_parser('encrypt', help='Required values for encryption.')
parser_encrypt.add_argument('-k', '--kmskey', dest='kmskey', required=True, help='Enter the kms key to use to encrypt.')
parser_encrypt.add_argument('-v', '--value', dest='value', required=True, help='Enter the value to encrypt with the kms key.')

parser_decrypt = subparsers.add_parser('decrypt', help='Required values for decryption.')
parser_decrypt.add_argument('-v', '--value', dest='value', required=True, help='Enter the value to decrypt with the kms key.')

args = parser.parse_args()

##########################################################################################################################################
### Function to decrypt
##########################################################################################################################################
def dec():
    session = boto3.session.Session()

    kms = session.client('kms')

    encrypted_password = args.value
    binary_data = base64.b64decode(encrypted_password)
    meta = kms.decrypt(CiphertextBlob=binary_data)
    plaintext = meta[u'Plaintext']
    print(plaintext)

##########################################################################################################################################
### Function to encrypt
##########################################################################################################################################
def enc():
    session = boto3.session.Session()

    kms = session.client('kms')
    key_id = "alias/" + args.kmskey
    stuff = kms.encrypt(KeyId=key_id, Plaintext=args.value)
    binary_encrypted = stuff[u'CiphertextBlob']
    encrypted_password = base64.b64encode(binary_encrypted)
    print(encrypted_password)

try:
    args.kmskey
except:
    dec()
else:
    enc()
