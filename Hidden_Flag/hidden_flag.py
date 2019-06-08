if __name__ == '__main__':
    key = [105, 110, 118, 105, 115, 105, 98, 108, 101]
    f = open('chall.png', 'rb')
    enc_bytes = f.read()
    f.close()

    f = open('dec.png', 'wb')
    for i, byte in enumerate(enc_bytes):
        f.write((int(byte) ^ key[i % len(key)]).to_bytes(1, 'big'))

    f.close()
