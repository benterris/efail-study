from M2Crypto import BIO, Rand, SMIME, X509

# Make a memory buffer out of the message
with open('message.txt') as f:
    message = f.read()


def makebuf(text):
    return BIO.MemoryBuffer(bytes(text, 'utf-8'))

# ------------ SIGN


# Make a MemoryBuffer of the message.
buf = makebuf(message)

# Seed the PRNG.
Rand.load_file('randpool.dat', -1)

# Instantiate an SMIME object; set it up; sign the buffer.
s = SMIME.SMIME()
s.load_key('sample_keys/signer_key.pem', 'sample_keys/signer.pem')
p7 = s.sign(buf, SMIME.PKCS7_DETACHED)

# Recreate buf.
buf = makebuf(message)

# Output p7 in mail-friendly format.
out = BIO.MemoryBuffer()
s.write(out, p7, buf)

# ------------ ENCRYPT

# Load target cert to encrypt to.
x509 = X509.load_cert('sample_keys/recipient.pem')
sk = X509.X509_Stack()
sk.push(x509)
s.set_x509_stack(sk)

# Set cipher: 3-key triple-DES in CBC mode.
s.set_cipher(SMIME.Cipher('des_ede3_cbc'))

# Encrypt the buffer.
p7 = s.encrypt(out)

# Output p7 in mail-friendly format.
encOut = BIO.MemoryBuffer()
encOut.write('From: sender@example.dom\n')
encOut.write('To: recipient@example.dom\n')
encOut.write('Subject: M2Crypto S/MIME testing\n')
s.write(encOut, p7)


stringES = str(encOut.read(), 'utf-8')
print(stringES)

# Write the signed and encrypted email to se.p7
with open('se.p7', 'w') as outf:
    outf.write(stringES)

# Save the PRNG's state.
Rand.save_file('randpool.dat')
