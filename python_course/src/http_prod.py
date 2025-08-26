log_token = "Aug 12 10:06:01 sshd[1234]: Failed password for guest from 192.0.2.15 port 22 ssh2".split()
#print(log_token)
month, day, time, host, *message_ports =log_token
ip=log_token[9]
#print(f"[parsed] date: {month} {day} {time}, host: {log_token[9]}")
#print(f"[message]: {' '.join(message_ports)}")

failed_attemots = [
    "203.0.113.45",
    

]

