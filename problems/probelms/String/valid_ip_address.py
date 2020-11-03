"""
Date: 1/22/2018
Inputs: decimal string such as 19216811
output: all possible ips

1-255.0-255.0-255,0-255


This is difficult question
"""

def get_available_ips(ip):
    ips = {i for i in generate_ip_addresses(ip)}
    ips = sorted(list(ips))
    print(ips)
    valid_ips = [_ip for _ip in ips if isValidIp(_ip)]
    return valid_ips

def isValidIp(ip):

    if ip.count(".") != 3:
        return False

    step =0
    for i in ip.split("."):
        if len(i) ==0:
            return False
        if step  == 0 and (int(i) <= 0 or int(i) > 255):
            return False
        if step  != 0 and (int(i) < 0 or int(i) > 255):
            return False
        step +=1
    return True

def generate_ip_addresses(ip):


    if len(ip) <= 0:
        return [""]  # Struggling point

    if len(ip) == 1:
        return [ip]

#    if len(ip) == 2:
#        return [ip]
#
#    if len(ip) == 3:
#        return [ip]


    ips1 = generate_ip_addresses(ip[1:])
    ips2 = generate_ip_addresses(ip[2:])
    ips3 = generate_ip_addresses(ip[3:])

    ip1 = ip[:1]
    ip2 = ip[:2]
    ip3 = ip[:3]

    results =[]

    for i in ips1:
        if len(i) != 0:           #Struggling point
            ip = ip1 + "." + i
        else:
            ip = ip1
        results.append(ip)
    for i in ips2:                 #Struggling point
        if len(i) != 0:
            ip = ip2 + "." + i
        else:                      #Struggling point
            ip = ip2
        results.append(ip)
    for i in ips3:
        if len(i) != 0:
            ip = ip3 + "." + i
        else:
            ip = ip3
        results.append(ip)
    return results

print(get_available_ips("1234445"))

#print(isValidIp("1.23.44.45"))