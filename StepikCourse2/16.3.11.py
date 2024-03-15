number_of_ips = int(input())

ips = [input() for i in range(number_of_ips)]
decimal_sums = []

for ip in ips:
    splitted_ip = list(map(int, ip.split('.')))
    decimal_sum = splitted_ip[0]*256**3 + splitted_ip[1]*256**2 + splitted_ip[2]*256**1 + splitted_ip[3]
    decimal_sums.append(decimal_sum)

ips_and_its_decimal_sums = zip(decimal_sums, ips)

sorted_ips = sorted(ips_and_its_decimal_sums)

for ip in sorted_ips:
    print(ip[1])
