import os
import csv

dictionary = {}

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

def parse_API(f, current_site, current_date, current_time):
    line = f.readline()
    while '[' not in line:
        s = line.strip().split()
        dictionary[current_site].append([current_site, s[0], current_date, current_time, s[1]])
        line = f.readline()

def parse_service(f, current_site):
    if current_site not in dictionary:
        dictionary[current_site] = []
    line = f.readline()
    current_date = ''
    current_time = ''
    while line and 'www' != line[0:3]:
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
        elif 'API' in line:
            line = parse_API(f, current_site, current_date, current_time)
        line = f.readline()
    return line

with open('seq2_jliu08.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if 'www' == line[0:3]:
            line = parse_service(f, line)
        # print(line)
    for key in dictionary:
        with open("bonus/" + key + '_seq2.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for l in dictionary[key]:
                writer.writerow(l)
