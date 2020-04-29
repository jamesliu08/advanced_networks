import os

list_of_websites = ['www.youtube.com', 'www.reddit.com', 'www.amazon.com', 'www.amazon.co.jp', 'cnj.craigslist.org']

for website in list_of_websites:
     print(website)
     os.system('echo [$(date +"%b %m %H:%M:%S")]')
     os.system('sudo traceroute -I ' + website)
     os.system('echo [$(date +"%b %m %H:%M:%S")]')
     os.system('ping -w 10 ' + website)
     os.system('echo [$(date +"%b %m %H:%M:%S")]')
     os.system('sudo pchar -c -R 4 -I 128 -p ipv4icmp ' + website)
     os.system('echo [$(date +"%b %m %H:%M:%S")]')
     os.system('sudo traceroute -I ' + website)
     os.system('echo [$(date +"%b %m %H:%M:%S")]')
     os.system('ping -w 10 ' + website)
