# client
"""
client.py
"""
import socket
import json

if __name__ == '__main__':
    num = 10
    try:
        print('start')
        # initialize Socket
        SERVER_ADDR = ('192.168.0.53', 3105)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(SERVER_ADDR)
            print('connection.')
            while True:
                input_tmp = input('send data input:')
                convert_str = '"'+input_tmp+'"'
                data2 = '{"ctname": "Sector_one", "con": '+convert_str+'}' + '<EOF>' 
                print("send : " + str(data2) )
                client.send(data2.encode('utf-8'))


    except Exception as e:
        print(e)