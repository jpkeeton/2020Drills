









# Run ipconfig
import subprocess
proc = subprocess.check_output("ipconfig" ).decode('utf-8')
print("Here's the output: " + proc)

# Get HostName and Computer Address
import os
import socket    
myKomputer = socket.gethostname()    
myIP = socket.gethostbyname(myKomputer)    
print("Komputer is: " + myKomputer)    
print("Komputer IP is: " + myIP)   

# Ping some IPs
ip_list = ['8.8.8.8', '192.168.1.1']
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"UP {ip} Ping Successful")
    else:
        print(f"DOWN {ip} Ping Unsuccessful")






# https://github.com/jpkeeton/2020Drills/blob/baa1e7b904794a9f9864affd7cfead165834b55f/NetworkCheck.py
# https://github.com/jpkeeton/2020Drills/blob/baa1e7b904794a9f9864affd7cfead165834b55f/GettingIPs.ipynb




 # Get HostName and Computer Address
# import os
# import socket    

# hostname = socket.gethostname()    
# IPAddr = socket.gethostbyname(hostname)    
# print("Your Computer Name is: " + hostname)    
# print("Your Computer IP Address is: " + IPAddr)    


