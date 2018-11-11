# Efail tools

Playground for [efail](https://efail.de) analysis  
Tools to craft signed/encrypted/signed-then-encrypted emails with S/MIME and to decrypt/verify them

## Structure

This repo contains 3 pairs of tools:

- Sign / Verify: to manipulate signed emails
- Encrypt / Decrypt: to manipulate encrypted emails
- Sign and encrypt / Decrypt and verify: to manipulate signed-then-encrypted emails

## Usage

To sign-then-encrypt a message:

```bash
vi message.txt # put here the message to encrypt
python3 sign_and_ecrypt.py
# Will output a signed-then-encrypted message in se.p7
```

To decrypt-then-verify a message:

```bash
# Provided the signed-then-encrypted message is stored in se.p7
python3 decrypt_and_verify.py # will output the message in dv_message.txt
```

## Install

`m2crypto` needs to build dependencies so it can be installed with:

```bash
pip install --global-option=build_ext m2crypto
```
