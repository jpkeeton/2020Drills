


## Run a ping
# #TODO make this a function?
# print('Pinging')
# import os
# os.system("start cmd /k ping 8.8.8.8 -t")

def ping_test():
    print('Is Googl\'s DNS up?')
    os.system("start cmd /k ping 8.8.8.8 -t")

# ping_test()




# run my device checks
import os
print('Starting Device Pings!')
# Sonos System = 192.168.1.128

# Den = 192.168.1.134
# Move = 192.168.1.159
# Garage = 192.168.1.118

# Kitchen = 192.168.1.156

# Beam = 192.168.1.196

# Jen's Room = 192.168.1.186

# CaveDesk(S) = 192.168.1.194
# CaveDesk(R) = 192.168.1.100
# CaveDesk(L) = 192.168.1.128

# Living Room TV Stand (L) = 192.168.1.158
# Living Room TV Stand (R) = 192.168.1.108

# IPs as of 3/20/21
ip_list = ['8.8.8.8', '192.168.1.1',
           '192.168.1.128',
            '192.168.1.196',
            '192.168.1.134',
            '192.168.1.118',
            '192.168.1.158',
            '192.168.1.159',
            '192.168.1.156',
            '192.168.1.186',
            '192.168.1.194',
            '192.168.1.100',
            '192.168.1.128',
            '192.168.1.108']
# ip_list = ['192.168.1.1', '192.168.73.1', '192.168.73.121', '192.168.73.186']
# ip_list = ['8.8.8.8', '192.168.1.1', '192.168.1.115', '192.168.1.217']
# new_ip_list = ['192.168.1.170', '192.168.1.121']

for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"{ip} Ping Successful")
    else:
        print(f"{ip} Ping Unsuccessful")


# print('Pinging')
# import os
# os.system("start cmd /k ping 8.8.8.8")


# Print a Finished Message
print('\nAll Done')