
# Simple Ping
# import os
# ip_to_check = input("enter the ip you want to check:")
# os.system('ping -n 4 {}'.format(ip_to_check))
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# # Simple Ping 2
# import os
# ip_to_check = input("enter the ip you want to check:")
# # this is just adding a spacer
# print('---' * 3)
# os.system('ping -n 4 {}'.format(ip_to_check)) 

# Running ipconfig
# import subprocess
# proc = subprocess.check_output("ipconfig" ).decode('utf-8')
# print (proc)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# # # Ping Multiple IPs
import os
from datetime import datetime

print ('Starting Pings!')
startTime = datetime.now()
ip_list = ['8.8.8.8', '192.168.1.1']
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"{ip} Ping Successful")
    else:
        print(f"{ip} Ping Unsuccessful")
        
# TODO so how long did this take?

# print(datetime.now() - startTime)
# or more verbosely
print('This test took: ' + (str(datetime.now() - startTime)) + ' Seconds')

# TODO find out and if it takes > n time, kill it


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# run netstat
# import subprocess
# nStat = subprocess.check_output("netstat -r" ).decode('utf-8')
# print(nStat)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# neet to stick an IP into this
# import subprocess
# nStat = subprocess.check_output("tracrt"  ).decode('utf-8')
# print(nStat)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# import socket
# socket.socket().connect(("google.com",443))

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# # ping a host and see if it's up
# import os
# hostname = "google.com" #example
# response = os.system("ping " + hostname)
# #and then check the response...
# if response == 0:
#   print(hostname + ': is up!')
# else:
#   print(hostname + ': is down!')











