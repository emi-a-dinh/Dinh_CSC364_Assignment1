import socket

ex1 = "0.0.0.0"
ex2 = "10.0.0.200"
netmask = "255.255.255.192"

conversion1 = socket.inet_aton(ex1)
conversion2 = socket.inet_aton(ex2)
conversion3 = socket.inet_aton(netmask)

# print("ex1: ", type(int("".join(format(byte, "08b") for byte in conversion1))))
# print("ex2: ", "".join(format(byte, "08b") for byte in conversion2))
# print("netmask: ", "".join(format(byte, "08b") for byte in conversion3))

def ip_to_bin(ip):
    # 1. Split the IP into octets.
    ip_octets = ip.split(".")
    # 2. Create an empty string to store each binary octet.
    ip_bin_string = ""
    # 3. Traverse the IP, octet by octet,
    for octet in ip_octets:
        # 4. and convert the octet to an int,
        int_octet = int(octet)
        # 5. convert the decimal int to binary,
        bin_octet = bin(int_octet)
        # 6. convert the binary to string and remove the "0b" at the beginning of the string,
        bin_octet_string = bin_octet[2:]
        # 7. while the sting representation of the binary is not 8 chars long,
        # then add 0s to the beginning of the string until it is 8 chars long
        # (needs to be an octet because we're working with IP addresses).
        while len(bin_octet_string) != 8:
            bin_octet_string = "0" + bin_octet_string
        # 8. Finally, append the octet to ip_bin_string.
        ip_bin_string = ip_bin_string + bin_octet_string
    # 9. Once the entire string version of the binary IP is created, convert it into an actual binary int.
    ip_int = int(ip_bin_string, 2)
    # 10. Return the binary representation of this int.
    return bin(ip_int)


client : 1, 2, 4
server: 2, 3, 4, 5, 6