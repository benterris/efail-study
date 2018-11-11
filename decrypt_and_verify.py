from M2Crypto import BIO, SMIME, X509

# Instantiate an SMIME object.
s = SMIME.SMIME()

# ------------ DECRYPT

# Load private key and cert.
s.load_key('sample_keys/recipient_key.pem', 'sample_keys/recipient.pem')

# Load the encrypted data.
p7, data = SMIME.smime_load_pkcs7('se.p7')

# Decrypt p7.
out = s.decrypt(p7)

# ------------ VERIFY

# load the signer's cert
x509 = X509.load_cert('sample_keys/signer.pem')
sk = X509.X509_Stack()
sk.push(x509)
s.set_x509_stack(sk)

# load the signer's CA cert (in this case, the signer's
# cert itself because it is self-signed)
st = X509.X509_Store()
st.load_info('sample_keys/signer.pem')
s.set_x509_store(st)


p7_bio = BIO.MemoryBuffer(out)
p7, data = SMIME.smime_load_pkcs7_bio(p7_bio)

# Raises an error if the data is not signed
verifiedData = s.verify(p7, data)

stringDecryptedVerified = str(verifiedData, 'utf-8')
print(stringDecryptedVerified)

# Write the decrypted message to dv_message.txt
with open('dv_message.txt', 'w') as outf:
    outf.write(stringDecryptedVerified)
