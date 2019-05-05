import struct


def byte2int(b):
    if isinstance(b, int):
        return b
    else:
        # 网络序, unsigned char
        return struct.unpack("!B", b)[0]


def int2byte(i):
    return struct.pack("!B", i)

