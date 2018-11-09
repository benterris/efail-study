from M2Crypto import BIO, Rand, SMIME

# Make a memory buffer out of the message
with open('message.txt') as f:
    message = f.read()


def makebuf(text):
    return BIO.MemoryBuffer(bytes(text, 'utf-8'))


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
out.write('From: sender@example.dom\n')
out.write('To: recipient@example.dom\n')
out.write('Subject: M2Crypto S/MIME testing\n')
s.write(out, p7, buf)

stringResult = str(out.read(), 'utf-8')

print(stringResult)

# Save the PRNG's state.
Rand.save_file('randpool.dat')

with open('sign.p7', 'w') as outf:
    outf.write(stringResult)
