import time, base64, struct

lat = float(input('широта: '))
lon = float(input('долгота: '))
alt = float(input('высота: '))
ts = int(time.time())
n = int(input('Количество видимых устройств '))
print("""
если 1 то 0x9812 

если 2 то 0x0a35

если 3 то 0x2939 

если 4 то 0xd396 

если 5 то 0xf741 

если 6 то 0x01dd 

если 7 то 0x08cd 

если 8 то 0x0e60""")

mac = [0x9812, 0x0a35, 0x2939, 0xd396, 0xf741, 0x01dd, 0x08cd, 0x0e60]
signals = dict()

for i in range(n):
    c = mac[int(input('Введите mac'))-1]
    rssi = int(input('Введите сигнал'))
    signals[c] = rssi


b = struct.pack('<f', lat)
b += struct.pack('<f', lon)
b += struct.pack('<f', alt)
b += struct.pack('<I', ts)
b += struct.pack('<B', n)
for key, item in signals.items():
    b += struct.pack('<H', key)
    b += struct.pack('<b', item)
print(str(b))
encoded = base64.b64encode(b)

print(encoded)
print(encoded.decode('utf-8'))
