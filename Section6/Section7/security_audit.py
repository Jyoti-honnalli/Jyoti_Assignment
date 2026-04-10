import socket
from datetime import datetime

target = input("Enter target IP: ")
ports = [21, 22, 80, 443]

results = []

print(f"\nScanning {target}...\n")

start = datetime.now()

for port in ports:
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((target, port))
    
    if result == 0:
        service = ""
        
        if port == 21:
            service = "FTP"
        elif port == 22:
            service = "SSH"
        elif port == 80:
            service = "HTTP"
        elif port == 443:
            service = "HTTPS"
        
        print(f"Port {port}: OPEN ({service})")
        results.append((port, service))
    else:
        print(f"Port {port}: CLOSED")
    
    s.close()

end = datetime.now()
duration = end - start

# Create HTML report
file = open("report.html", "w")

file.write("<html><body>")
file.write(f"<h1>Security Report for {target}</h1>")
file.write(f"<p>Scan Duration: {duration}</p>")
file.write("<table border='1'><tr><th>Port</th><th>Service</th></tr>")

for port, service in results:
    file.write(f"<tr><td>{port}</td><td>{service}</td></tr>")

file.write("</table></body></html>")
file.close()

print("\nReport saved as report.html")