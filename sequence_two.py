import os
import requests

list_of_websites = [('www.youtube.com', 'www.youtube.com/results', {'search_query': 'keyword'}),
                    ('www.walmart.com', 'www.walmart.com/search/', {'query': 'keyword'}),
                    ('www.amazon.com', 'www.amazon.com/s', {'k': 'keyword'}),
                    ('www.amazon.de', 'www.amazon.de/s', {'k': 'keyword'}),
                    ('www.bbc.co.uk', 'www.bbc.co.uk/search', {'q': 'keyword'})]

f = open("seq2_jliu08.txt", "a")
for website in list_of_websites:
    stream = os.popen(  'echo [$(date +"%b %m %H:%M:%S")]\n' + \
                        'sudo traceroute -I ' + website[0] + "\n" + \
                        'echo [$(date +"%b %m %H:%M:%S")]\n' + \
                        'timeout 10 ping ' + website[0] + "\n" + \
                        'echo [$(date +"%b %m %H:%M:%S")]\n')
    output = stream.read()
    f.write(output + "\n")

    for i in range(3):
        payload = website[2]
        r = requests.get('http://' + website[1], params = payload)
        if r.status_code == requests.codes.ok:
            pass
        else:
            print(str(r.status_code) + website[0])
        f.write(str(r.elapsed.total_seconds() * 1000.0) + "\n")

    stream = os.popen(  '\necho [$(date +"%b %m %H:%M:%S")]\n' + \
                        'sudo traceroute -I ' + website[0] + "\n" + \
                        'echo [$(date +"%b %m %H:%M:%S")]\n' + \
                        'timeout 10 ping ' + website[0] + "\n")
    output = stream.read()
    f.write(output + "\n")