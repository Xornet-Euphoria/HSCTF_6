from Crypto.Hash import MD4


def is_zero_e_num(hash):
    if hash[0:2] == '0e' and hash[2:].isdigit():
        return True
    return False


if __name__ == '__main__':
    count = 0
    while True:
        password = '0e' + str(count)
        h = MD4.new()
        h.update(password.encode())

        if is_zero_e_num(h.hexdigest()):
            print('answer is {}: hash is {}'.format(password, h.hexdigest()))
            break

        if count % 1000000 == 0:
            print('current password is {}: hash is {}'.format(password, h.hexdigest()))

        count += 1
