import socket
from time import sleep
import math

ip1 = "192.168.0.166"
ip2 = "192.168.0.202"

channels = [(ip1, 0), (ip1, 1), (ip2, 0), (ip2, 1)]

def gen_rgb_msg(channel, red, green, blue):
    msg_arr = [ord('R'), channel, red, green, blue]
    return bytes(msg_arr)

def gen_hsv_msg(channel, hue, sat, val):
    msg_arr = [ord('G'), channel, hue, sat, val]
    return bytes(msg_arr)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hueset = 0
valset = 0

while True:
  hueset = hueset + 1 
  valset = valset + 2
  for i in range(0, 4):
    chan = channels[i]
    chanhue = (hueset + 10*i) % 180
    chanval = 128 + 128 * math.pow(math.sin(valset/10 + 3.14159/4.0 * i), 11)
    sock.sendto(gen_hsv_msg(chan[1], int(hueset), 255, int(chanval)), (chan[0], 8888))

  if hueset >= 180:
    hueset = 0

  if valset >= 255:
    valset = 0

  sleep(0.1)
