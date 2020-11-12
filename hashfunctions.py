import hashlib
import bcrypt


def calc_md4(text, enc=True):
    if enc:
        text = text.encode('utf-8')
    return hashlib.new("md4", text).hexdigest()


def calc_md5(text, enc=True):
    if enc:
        text = text.encode('utf-8')
    return hashlib.md5(text).hexdigest()


def calc_sha1(text, enc=True):
    if enc:
        text = text.encode('utf-8')
    return hashlib.sha1(text).hexdigest()


def calc_sha224(text, enc=True):
    if enc:
        text = text.encode('utf-8')
    return hashlib.sha224(text).hexdigest()


def calc_sha256(text, enc=True):
    if enc:
        text = text.encode('utf-8')
    return hashlib.sha256(text).hexdigest()


def calc_sha384(text, enc=True):
    if enc:
        text = text.encode('utf-8')
    return hashlib.sha384(text).hexdigest()


def calc_sha512(text, enc=True):
    if enc:
        text = text.encode('utf-8')
    return hashlib.sha512(text).hexdigest()


def calc_sha3_224(text, enc=True):
    if enc:
        text = text.encode('utf-8')
    return hashlib.sha3_224(text).hexdigest()


def calc_sha3_256(text, enc=True):
    if enc:
        text = text.encode('utf-8')
    return hashlib.sha3_256(text).hexdigest()


def calc_sha3_384(text, enc=True):
    if enc:
        text = text.encode('utf-8')
    return hashlib.sha3_384(text).hexdigest()


def calc_sha3_512(text, enc=True):
    if enc:
        text = text.encode('utf-8')
    return hashlib.sha3_512(text).hexdigest()


def calc_blake2b(text, enc=True):
    if enc:
        text = text.encode('utf-8')
    return hashlib.blake2b(text).hexdigest()


def calc_blake2s(text, enc=True):
    if enc:
        text = text.encode('utf-8')
    return hashlib.blake2s(text).hexdigest()


def calc_ripemd160(text, enc=True):
    if enc:
        text = text.encode('utf-8')
    return hashlib.new("ripemd160", text).hexdigest()


def calc_whirlpool(text, enc=True):
    if enc:
        text = text.encode('utf-8')
    return hashlib.new("whirlpool", text).hexdigest()


def calc_bcrypt(text, enc=True, cost=10):
    if enc:
        text = text.encode('utf-8')
    return bcrypt.hashpw(text, bcrypt.gensalt(rounds=cost)).decode('utf-8')
