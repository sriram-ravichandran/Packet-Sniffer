import socket
Num = int(input("""Enter Your Choice
                   1. ICMP
                   2. TCP
                   3. UDP
"""))
my_ip = socket.gethostbyname(socket.gethostname())
if(Num==1):
    Source = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
    packet = "ICMP"
elif(Num==2):
    Source = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_TCP)
    packet = "TCP"
elif(Num==3):
    Source = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_UDP)
    packet = "UDP"

while True:
    S = Source.recvfrom(65535)
    source_ip = S[1][0]
    print("Protocol: "+packet+" Source: "+source_ip+" Destination: "+my_ip)


    