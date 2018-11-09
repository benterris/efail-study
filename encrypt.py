from M2Crypto import BIO, Rand, SMIME, X509

# Make a memory buffer out of the message
with open('message.txt') as f:
    message = f.read()


def makebuf(text):
    return BIO.MemoryBuffer(bytes(text, 'utf-8'))


# Make a MemoryBuffer of the message.
buf = makebuf(message)

# Seed the PRNG.
Rand.load_file('randpool.dat', -1)

# Instantiate an SMIME object.
s = SMIME.SMIME()

# Load target cert to encrypt to.
x509 = X509.load_cert('sample_keys/recipient.pem')
sk = X509.X509_Stack()
sk.push(x509)
s.set_x509_stack(sk)

# Set cipher: 3-key triple-DES in CBC mode.
s.set_cipher(SMIME.Cipher('des_ede3_cbc'))

# Encrypt the buffer.
p7 = s.encrypt(buf)

# Output p7 in mail-friendly format.
out = BIO.MemoryBuffer()
out.write('From: sender@example.dom\n')
out.write('To: recipient@example.dom\n')
out.write('Subject: M2Crypto S/MIME testing\n')
s.write(out, p7)

stringEncrypted = str(out.read(), 'utf-8')
print(stringEncrypted)

with open('encrypt.p7', 'w') as outf:
    outf.write(stringEncrypted)


# Save the PRNG's state.
Rand.save_file('randpool.dat')
