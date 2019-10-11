import socket

def gen_rgb_msg(channel, red, green, blue):
    msg_arr = [ord('R'), channel, red, green, blue]
    return bytes(msg_arr)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(gen_rgb_msg(1, 255, 255, 255), ("192.168.0.1"), 8888)
