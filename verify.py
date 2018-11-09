from M2Crypto import SMIME, X509

s = SMIME.SMIME()

# load the signer's cert
x509 = X509.load_cert('sample_keys/signer.pem')
sk = X509.X509_Stack()
sk.push(x509)
s.set_x509_stack(sk)

# load the signer's ca cert (in this case, the signer's
# cert itself because it is self-signed)
st = X509.X509_Store()
st.load_info('sample_keys/signer.pem')
s.set_x509_store(st)

# Load the data and verify it
p7, data = SMIME.smime_load_pkcs7('sign.p7')
v = s.verify(p7, data)
print(v)
print(data)
print(data.read())
