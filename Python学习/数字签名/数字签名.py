from Crypto.PublicKey import RSA


def generate_key(bits):
    return RSA.generate(bits)


if __name__ == "__main__":
    key = generate_key(2048)

    # 生成私钥文件
    sk = key.export_key()
    with open('master-private.pem', 'wb') as f:
        f.write(sk)

    # 生成公钥文件
    pk = key.publickey().export_key()
    with open('master-public.pem', 'wb') as f:
        f.write(pk)

