# client
"""
client.py
"""
import socket
import json

if __name__ == '__main__':
    num = 10
    try:
        print('클라이언트 동작')
        # initialize Socket
        SERVER_ADDR = ('192.168.0.66', 3105)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(SERVER_ADDR)
            print('서버에 연결 되었습니다.')

            while True:
                input_tmp = input('전송할 데이터를 입력하세요:')
                # data = {'ctname': 'co2','con': str(input_tmp)}
                data = '{"ctname":"current position", "con": "%s"}'%(str(input_tmp)) + '<EOF>'
                # data = '{"ctname":"current position", "con": '+convert_str+'}' + '<EOF>'

                # print("send: ctname: {0}, contents: {1}".format(data['ctname'], data['con']))
                client.send(data.encode('utf-8'))
                print(data.encode('utf-8'))
                #data = client.recv(4096)
                #data = json.loads(data)
                #print("receive: ctname: {0}, contents: {1}".format(data['ctname'], data['con']))

                #num = int(data['num']) + 1

    except Exception as e:
        print(e)
