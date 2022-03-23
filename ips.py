import ipaddress

ip='192.168.0.0'
endereço = ipaddress.ip_address(ip)

rede = ipaddress.ip_network(ip)


print(endereço + 256)
print(f'REDE: {rede}')