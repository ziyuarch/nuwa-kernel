import sys, struct
k = open(sys.argv[1], 'rb').read()
h = bytearray(4096)
h[0:8] = b'ANDROID!'
struct.pack_into('<I', h, 8, len(k))
struct.pack_into('<I', h, 12, 0)
struct.pack_into('<I', h, 16, 0)
struct.pack_into('<I', h, 20, 1584)
struct.pack_into('<I', h, 40, 4)
cmd = b'console=tty0 androidboot.console=tty0'
h[44:44+len(cmd)] = cmd
pad = (-len(k)) % 4096
open(sys.argv[2], 'wb').write(bytes(h) + k + b'\x00' * pad)
print('kernel', len(k), 'total', 4096 + len(k) + pad)
