import nmap3

Nmap_obj = nmap3.PortScanner()

Nmap_obj.scan('192.168.1.15', '1-1024')

Nmap_obj.command_line()

Nmap_obj.scaninfo()

Nmap_obj.all_hosts()

Nmap_obj['192.168.1.15'].hostnames()

Nmap_obj['192.168.1.15'].hostname()

Nmap_obj['192.168.1.15'].state()
Nmap_obj['192.168.1.15'].all_protocols()
Nmap_obj['192.168.1.15']['tcp'].keys()

Nmap_obj['192.168.1.15'].all_tcp()
Nmap_obj['192.168.1.15'].all_udp()
Nmap_obj['192.168.1.15'].all_ip()
Nmap_obj['192.168.1.15'].all_sctp()
Nmap_obj['192.168.1.15'].has_tcp(22)
Nmap_obj['192.168.1.15']['tcp'][22]
