import socket
import time

# Input target and ports
target = input("Enter target IP: ")
ports = input("Enter ports (comma separated): ")

# Convert ports to list
port_list = [int(p) for p in ports.split(",")]

start_time = time.time()

print("\nScanning started...\n")

# Open file to save results
file = open("scan_results.txt", "w")

for port in port_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        status = "OPEN"
    else:
        status = "CLOSED"

    output = f"Port {port}: {status}"
    print(output)
    file.write(output + "\n")

    s.close()

file.close()

end_time = time.time()

print("\nScan completed!")
print("Time taken:", round(end_time - start_time, 2), "seconds")