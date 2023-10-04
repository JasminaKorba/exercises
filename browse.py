import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("pl.wiktionary.org", 80))
cmd = "GET https://pl.wiktionary.org/w/index.php?title=text_hand&action=edit&redlink=1#en HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")
mysock.close()
