from pwn import *

io = remote("a2befdcc18c9fdd3.247ctf.com", 50441)

print(io.recvline())
print(io.recvline())

for i in range(500):
    data = io.recvline()

    num1 = int(data.split()[-1][0:-1])
    num2 = int(data.split()[-3])

    total = num1 + num2
    print(f"{num1}+{num2}")
    res = str(total).encode("utf-8")
    io.sendline(res)
    print(io.recvline())

print(io.recvline())
io.close()
