## Script start

def convert_slash_notation(slash_notation):
    """
    Takes an IP address in slash notation, and returns it in dotted decimal + subnet mask.
    e.g. 10.0.0.1/24 -> 10.0.0.1 255.255.255.0
    """

    return


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


num_routers = int(input("How many routers to set up? "))
for i in range(num_routers):
    router(i)
