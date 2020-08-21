import telnetlib

HOST = '52.49.91.111'
PORT = 2003

tn = telnetlib.Telnet(HOST, PORT)

z = tn.read_all()
print z
