import time
import socket
import struct
import STT
from PySide2 import QtCore
from PySide2 import QtWidgets
from typing import Tuple, Optional

socket.setdefaulttimeout(5)

def _pack(data : str):
    # 包含头信息前8个字节和结尾1个字节
    size = 8 + len(data) + 1
    bytes_ = struct.pack('<iih??', size, size, 689, 0, 0) \
        + data.encode('unicode-escape') \
        + b'\x00'
    return bytes_

def parse_recv_msg(bytes_ : bytes) -> Optional[tuple]:
    # 解析消息
    if len(bytes_) <= (4 + 8):
        return None

    size = struct.unpack('i', bytes_[0:4])[0]
    size_ = struct.unpack('i', bytes_[4:8])[0]
    if size != size_:
        return None

    if len(bytes_[12:]) < size:
        return None

    raw_message = bytes_[12:size+4]
    # print(raw_message)
    if raw_message.endswith(b"\x00"):
        return (size + 4, STT.load(raw_message))

    return None

class DouyuMessageSignal(QtCore.QObject):
    say = QtCore.Signal(str, str, str)
    gift = QtCore.Signal(str, str)

class DouyuMessageRunnable(QtCore.QThread):

    host = 'openbarrage.douyutv.com'
    port = 8601

    def __init__(self, rid: int):
        super(DouyuMessageRunnable, self).__init__()
        self.sock = None
        self.rid = rid
        self.lasttick = 0
        self.timeout = 0
        self.signals = DouyuMessageSignal()

    def __del__(self):
        if self.sock:
            print("close socket")
            self.sock.close()

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        print(f"connect {self.host}")
        self.sock.sendall(_pack("type@=loginreq/username@=/password@=/roomid@={}/".format(self.rid)))
        self.sock.sendall(_pack("type@=joingroup/rid@={}/gid@={}/".format(self.rid, -9999)))

    def parse(self, bytes_: bytes):
        while(not self.isInterruptionRequested()):
            msg = parse_recv_msg(bytes_)
            if not msg:
                return bytes_

            if msg[1].get('type', '') == 'chatmsg':
                self.signals.say.emit(msg[1]['level'], msg[1]['nn'], msg[1]['txt'])
            elif msg[1].get('type', '') == 'dgb':
                if msg[1]['rid'] == self.rid:
                    self.signals.gift.emit(msg[1]['nn'], msg[1]['gfid'])

            QtCore.QThread.msleep(150)
            bytes_ = bytes_[msg[0]:]

    def keepalive(self, timestamp):
        if (timestamp - self.lasttick) > 30:
            print("keepalive")
            self.sock.sendall(_pack(f"type@=keeplive/tick@={int(timestamp)}/"))
            self.lasttick = timestamp 

    def handle_timeout(self):
        self.timeout += 1
        if self.timeout >= 3:
            print("timeout")
            self.sock.close()
            self.connect()

    def run(self):
        self.connect()

        bytes_ = b''
        while(not self.isInterruptionRequested()):

            self.keepalive(time.time())

            try: bytes_ += self.sock.recv(1024)
            except socket.timeout: 
                bytes_ = b''
                self.handle_timeout()
                continue 
            finally: 
                QtCore.QThread.msleep(150)

            self.timeout = 0
            bytes_ = self.parse(bytes_)

