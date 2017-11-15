# aws-scale
A quick script for users to encrypt and decrypt values using kms.

# Requirements
- python
- boto3

# Usage
```shell
python aws-kms-util.py encrypt -k <kms key> -v <value to encrypt>
```
or
```shell
python aws-kms-util.py decrypt -v <value to decrypt>
```

It will then

```
$ python aws-kms-util.py encrypt -k wink -v foo
AQICAHi505hkmWJbt8eaPSQRTkdgmYozKHwplJneiRnExwaFXgE04f4eIrYJJA3QPEvFNyczAAAAYTBfBgkqhkiG9w0BBwagUjBQAgEAMEsGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMPNucH10vhydn3IiMAgEQgB5cGh3camHVSFrpuCTP0vr9OPDAzbnBmVntLsUbieM=

$ python aws-kms-util.py decrypt -v AQICAHi505hkmWJbt8eaPSQRTkdgmYozKHwplJneiRnExwaFXgE04f4eIrYJJA3QPEvFNyczAAAAYTBfBgkqhkiG9w0BBwagUjBQAgEAMEsGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMPNucH10vhydn3IiMAgEQgB5cGh3camHVSFrpuCTP0vr9OPDAzbnBmVntLsUbieM=
foo
```
