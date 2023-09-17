import getopt
import sys
import time
import atexit
from scapy.all import IP, TCP, send, sniff

outfile = None

def process_packet(packet):
    char = chr(packet["IP"].id)
    print(char)
    outfile.write(char)

def exit_handler():
    if outfile is not None:
        outfile.close()

def main():
    atexit.register(exit_handler)
    server = False

    try:
        opts, args = getopt.getopt(sys.argv[1:],"",
            ["src=", "dst=", "src-port=", "dst-port=", "file=", "server"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    for o, a in opts:
        if o == "--src":
            src = a
        elif o == "--dst":
            dst = a
        elif o == "--src-port":
            src_port = int(a)
        elif o == "--dst-port":
            dst_port = int(a)
        elif o == "--file":
            file = a
        elif o == "--server":
            server = True
        else:
            print(o)
            assert False, "unhandled option"

    if server:
        global outfile
        outfile = open(file, "at")
        outfile.writelines(["\nCovert Tcp started...\n"])
        bpf = f"tcp and src host {src} and src port {src_port} and dst host {dst} and dst port {dst_port} and tcp[tcpflags] == tcp-syn"
        print(f"Listening with BPF filter:\n{bpf}")
        sniff(filter=bpf, prn=process_packet, store=0)
    else:
        with open(file, "rt") as infile:
            while True:
                char = infile.read(1)
                if not char:
                    break
                print(char)
                packet = IP(src=src, dst=dst, id=ord(char)) / TCP(
                    sport=src_port, dport=dst_port, flags="S"
                )
                send(packet)
                time.sleep(1)


if __name__ == "__main__":
    main()
