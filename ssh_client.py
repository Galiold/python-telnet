import paramiko

client = None


def ssh_con(hostname, port, usr, passwd):
    global client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.load_system_host_keys()
    client.connect(hostname, port, usr, passwd)
    print ("Connected to host!")


def ssh_cmd(cmd):
    stdin, stdout, stderr = client.exec_command(cmd)
    out = stdout.read()
    print(str(out)[2:-3])


if __name__ == '__main__':
    ssh_con('104.248.251.41', 22, 'root', '123456789')

    ssh_cmd("cd /home/test")
    ssh_cmd("pwd")

    # while True:
    #     cmd = input()
    #     ssh_cmd(cmd)
    #     if cmd == "exit":
    #         ssh_cmd("exit")
    #         break
