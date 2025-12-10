## Script start

def convert_slash_notation(slash_notation):
    """
    Takes an IP address in slash notation, and returns it in dotted decimal + subnet mask.
    e.g. 10.0.0.1/24 -> 10.0.0.1 255.255.255.0
    """

    # strip whitespace and separate address + subnet mask
    slash_notation = slash_notation.strip()
    position_slash = slash_notation.find('/')
    ip_add = slash_notation[:position_slash]
    prefix_length = int(slash_notation[position_slash+1:])

    # convert prefix length to dotted decimal notation
    subnet_mask = prefix_to_mask(prefix_length)

    return ip_add + ' ' + subnet_mask


def prefix_to_mask(prefix_length):
    """
    Takes a prefix length as input and transforms it into the corresponding subnet mask.
    e.g. /24 -> 255.255.255.0
    """

    if prefix_length == 32:
        return "255.255.255.255"

    octets = []
    # add '255' octets
    num_of_255 = prefix_length // 8
    for i in range(num_of_255):
        octets.append("255")   

    # add next octet
    num_bits_eq_one = prefix_length - num_of_255*8
    value_octet = 256 - 2**(8 - num_bits_eq_one)
    octets.append(str(value_octet))

    while len(octets) < 4:
        octets.append('0')

    return ".".join(octets)

#TODO: add docstring to router function

def router(num_router):
    # hostname configuration (if empty will be skipped)
    hostname = input("What hostname for the router? ")
    file_path = f"./files/config_router_{hostname}.txt"
    
    # write en + conf t (always)
    with open(file_path, 'w') as writer:
        writer.write("en\nconf t\n")

    if hostname:
        with open(file_path, 'a') as writer:
            writer.write('ho ' + hostname + '\n')

    # interfaces
    int_number = int(input("How many interfaces to set up? "))
    for i in range(int_number):
        # which interface to configure
        int_name = input(f"What's the name of interface {i+1}? ")
        # int ip address + subnet mask
        int_address = input("What's its IP address? ")
        int_subnet = input("What's the subnet? ")
        # full text of interface configuration
        int_conf_lines = '\nint ' + int_name + '\nip add ' + int_address + ' ' + int_subnet + '\nno shutdown\n'
        # append interface conf to file
        with open(file_path, 'a') as writer:
            writer.write(int_conf_lines)

    # show int brief + copy to start
    with open(file_path, 'a') as writer:
        writer.write('\nend' + '\nsh ip int b' + '\ncopy run start\n')


# num_routers = int(input("How many routers to set up? "))
# for i in range(num_routers):
#     router(i)
