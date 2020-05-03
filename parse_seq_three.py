import os
import csv

dictionary = {}

# pchar hop index, IP of hop, delay(rtt), package loss at hope
# pchar hop index, IP of bw per hop, queueing per hop
# pchar hop count

def parse_pchar(f, current_site, current_date, current_time):
    line = f.readline()
    while '[' not in line:
        if line[2] == ':':
            s = line.split()
            hop_index = s[0].strip(':')
            hop_ip = s[1]
            line = f.readline().strip()
            if 'Path length' in line:
                break
            s = line.split()
            package_loss = s[-1].strip('()')
            s = f.readline().split()
            delay = s[4]
            f.readline()
            f.readline()
            s = f.readline().split()
            bw = s[-2]
            s = f.readline().split()
            queueing = s[4]
            dictionary[current_site].append([current_site, current_date, current_time, hop_index, hop_ip, delay, package_loss])
            dictionary[current_site].append([current_site, current_date, current_time, hop_index, bw, queueing])
        else:
            pass
        line = f.readline()
    dictionary[current_site].append([current_site, current_date, current_time, hop_index])

def parse_traceroute(f, current_site, current_date, current_time):
    line = f.readline()
    while '[' not in line:
        s = line.split()
        hop_index = s[0]
        if s[1] != '*':
            i1 = 3
            i2 = 5
            i3 = 7
            hop_ip = s[2].strip('()')
            delay1 = s[i1]
            if '*' in delay1:
                i2 -= 1
                i3 -= 1
            delay2 = s[i2]
            if '*' in delay2:
                i3 -= 1
            delay3 = s[i3]
            avg_delay = 0.0
            num_items = 0
            for d in (delay1, delay2, delay3):
                if d != '*':
                    avg_delay += float(d)
                    num_items += 1
            avg_delay = avg_delay / num_items
            dictionary[current_site].append([current_site, current_date, current_time, hop_index, hop_ip, delay1, delay2, delay3, avg_delay])
        else:
            dictionary[current_site].append([current_site, current_date, current_time, hop_index, 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'])
        line = f.readline()
    dictionary[current_site].append([current_site, current_date, current_time, hop_index])
    return line

def parse_ping(f, current_site, current_date, current_time):
    list_of_times = []
    num_probes = 10
    for i in range(10):
        line = f.readline().strip()
        s = line.split('=')
        time = s[-1]
        try:
            list_of_times.append(float(time.split()[0]))
        except:
            num_probes -= 1
    avg = sum(list_of_times) / num_probes
    dictionary[current_site].append([current_site, current_date, current_time, list_of_times, avg])
    return line

def parse_service(f, current_site):
    if current_site not in dictionary:
        dictionary[current_site] = []
    line = f.readline()
    current_date = ''
    current_time = ''
    while line and line[0:3] not in ('www', '23.', 'cnj'):
        if '[' in line:
            line = line.strip('[]\n\t ')
            line = line.split()
            current_date = line[0] + ' ' + line[1]
            current_time = line[2]
        elif 'traceroute' in line:
            line = parse_traceroute(f, current_site, current_date, current_time)
            continue
        elif 'PING' in line:
            line = parse_ping(f, current_site, current_date, current_time)
            continue
        elif 'pchar' in line:
            line = parse_pchar(f, current_site, current_date, current_time)
        line = f.readline()
    return line

with open('seq3_jliu08.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line[0:3] in ('www', '23.', 'cnj'):
            if '23.205.209.128' in line:
                line = 'www.amazon.co.jp'
            elif '23.205.209.132' in line:
                line = 'www.amazon.com'
            elif 'cnj' in line:
                line = 'cnj.craigslist.com'
            line = parse_service(f, line)
    for key in dictionary:

        with open("bonus/" + key + '_seq3.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for l in dictionary[key]:
                writer.writerow(l)

