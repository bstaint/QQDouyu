import pprint

def load(msg_bytes : bytes) -> dict:
    msg : str = msg_bytes.decode('utf-8', 'ignore').strip('\x00/')
    dict_map = map(lambda s: tuple(s.split('@=')), msg.split('/'))
    return dict(dict_map)

if __name__ == "__main__":
    load(b1)
