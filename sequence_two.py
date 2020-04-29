import os
import requests

list_of_websites = [('www.youtube.com', 'www.youtube.com/results', {'search_query': 'networks'}),
                    ('www.walmart.com', 'www.walmart.com/search/', {'query': 'networks'}),
                    ('www.amazon.com', 'www.amazon.com/s', {'k': 'networks'}),
                    ('www.amazon.de', 'www.amazon.de/s', {'k': 'networks'}),
                    ('www.bbc.co.uk', 'www.bbc.co.uk/search', {'q': 'networks'})]

for website in list_of_websites:

    print(website[0])

    os.system('echo [$(date +"%b %d %H:%M:%S")]')
    os.system('sudo traceroute -I ' + website[0])
    os.system('echo [$(date +"%b %d %H:%M:%S")]')
    os.system('ping -w 10 ' + website[0])
    os.system('echo [$(date +"%b %d %H:%M:%S")]')

    print('API Response Time')

    for i in range(3):
        payload = website[2]
        r = requests.get('https://' + website[1], params = payload, headers={'User-Agent': 'James'})
        if r.status_code == requests.codes.ok:
            pass
        else:
            print(r.url)
        print(str(r.elapsed.total_seconds() * 1000.0))

    os.system('echo [$(date +"%b %d %H:%M:%S")]')
    os.system('sudo traceroute -I ' + website[0])
    os.system('echo [$(date +"%b %d %H:%M:%S")]')
    os.system('ping -w 10 ' + website[0])