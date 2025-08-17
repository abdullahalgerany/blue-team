ip_string = "192.168.1.1"
port = "443"
port = int(port)
is_secure = bool(port == 443)
# print(is_secure)

log_tokens = "Aug 12 10:02:11 web01 sshd[1234]: Failed password for " \
"root from 203.0.113.45 port 22 ssh2".split()
month, day, time, host, *message_ports = log_tokens

# print(f"[PARSED] Date: {month} {day} {time}, Host: {host}")
# print(f"[MESSAGE]: {' '.join(message_ports)}")

failed_attempts = [
 
]

# if failed_attempts:
#     alert_level = "HIGH"
#     print(f"[ALERT] {len(failed_attempts)} failed login attempts detected! Level: {alert_level}")
# else:
#     print("[OK]: No login attempts found")

log_lines = [
    "Aug 12 10:02:11 sshd[1234]: Failed password for root from 203.0.113.45 port 22 ssh2",
    "Aug 12 10:05:43 sshd[1234]: Accepted password for admin from 198.51.100.23 port 22 ssh2",
    "Aug 12 10:06:01 sshd[1234]: Failed password for guest from 192.0.2.15 port 22 ssh2"
]


# for line_num, line in enumerate(log_lines):
#     if "Failed password" in line:
#         print(f"[SECURITY]: Line Number{line_num} Unauthorized login attempt -> {line}")


def analyze_logs(log_file, thershold=2, **options):
    verbose = options.get('verbose', False)
    failed_count = 0

    with open(log_file, "r") as file:
        for line in file:
            if "Failed password" in line:
                failed_attempts += 1
                if verbose:
                    print(f"[DEBUG] Failed attempt: {line.strip()}")

    if failed_count >= thershold:
        print(f"[ALERT] {failed_count} failed login attempts detected (threshold={thershold})")
    else:
        print(f"[INFO] {failed_count} failed attempts — below threshold")