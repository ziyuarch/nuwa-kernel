import sys, struct
img, out = sys.argv[1], sys.argv[2]
k = open(img, 'rb').read()
hdr = bytearray(4096)
hdr[0:8] = b'ANDROID!'
struct.pack_into('<I', hdr, 8, len(k))
struct.pack_into('<I', hdr, 12, 0)
struct.pack_into('<I', hdr, 16, 0)
struct.pack_into('<I', hdr, 20, 1584)
struct.pack_into('<I', hdr, 40, 4)
pad = (-len(k)) % 4096
open(out, 'wb').write(bytes(hdr) + k + b'\x00' * pad)
print('kernel %d -> boot.img %d (pad %d)' % (len(k), 4096 + len(k) + pad, pad))
