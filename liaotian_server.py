from socket import *

sockfd = scoket(AF_INET,SOCK_DGRAM)
sockfd.bind('0.0.0.0',8888)

data,addr=sockfd.recvfrom(1024)

n=sockfd.sendto(data,addr)
sockfd.close()



































