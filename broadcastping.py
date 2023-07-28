from ping3 import ping, verbose_ping
import ipaddress

def ping_to_network_hosts(ipv4):
    try:
        ip_obj = ipaddress.IPv4Address(ipv4)
        
        for i in range(255):    
            ip = ip_obj + i

            consulta_ping = ping(str(ip),timeout=2,ttl=2)

            if consulta_ping == None or consulta_ping == False:
                print(f"Ping {ip} - Fallido ")
                
            else:
                print(f"El host {ip}, es accesible y el tiempo de respuesta es : [{round(consulta_ping,4)} ms]")
                   
    except ipaddress.AddressValueError as e:
        print(f"Error {e}")        

    except Exception as e:
        print(f"Error: {e}")
    
    except KeyboardInterrupt as e:
        print("Interrupcion por teclado ")

if __name__ == "__main__":
    ip = input('Ingrese la ip de la red que desea consultar [formato 192.168.1.0] : \n')
    ping_to_network_hosts(ip)