import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--file')
args = parser.parse_args()

filename = args.file
opened_file = open("mumbo_jumbo.txt")
encoded_text = opened_file.read()  # read the file into a string
opened_file.close()  # always close the files you've opened


def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')

decode_Caesar_cipher(encoded_text, -13)


