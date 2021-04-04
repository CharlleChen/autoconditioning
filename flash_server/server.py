def sock():
    print("socks start!")
    import socket
    import sys
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = socket.gethostname()
    print("host", host)
    # bind port
    s.bind(('192.168.0.101', 6666))

    print('Bind UDP on 6666...')

    # count = 0
    # temp = 0
    # humi = 0

    # target_temp = 1
    # target_humi = 1

    # clean status text
    with open('status', 'w') as f:
        pass

    while True:
        # read from raspberry pi
        data, addr = s.recvfrom(1024)
        print('Got connected from', addr)

        data = data.decode('utf-8')
        
        if len(data.split('-')) == 3:
            print("[people count, temp, humi]:", data)
            with open('status', 'w') as f:
                f.write(data)

        # send to raspberry pi

        with open('target', 'r') as f:
            msg = f.read()
        # msg = "-".join([str(target_temp), str(target_humi)])
        if not msg:
            msg = "0-0" 
        s.sendto(msg.encode('utf-8'), addr)

        sys.stdout.flush()

if __name__ == "__main__":
    sock()