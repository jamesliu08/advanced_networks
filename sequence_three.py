import os

list_of_websites = ['www.youtube.com', 'www.reddit.com', '23.205.209.132', '23.205.209.128', 'cnj.craigslist.org']

for website in list_of_websites:
     os.system('echo ' + website)
     os.system('echo [$(date +"%b %d %H:%M:%S")]')
     os.system('sudo traceroute -I ' + website)
     os.system('echo [$(date +"%b %d %H:%M:%S")]')
     os.system('ping -w 10 ' + website)
     os.system('echo [$(date +"%b %d %H:%M:%S")]')
     os.system('sudo pchar -c -R 4 -I 128 -p ipv4icmp ' + website)
     os.system('echo [$(date +"%b %d %H:%M:%S")]')
     os.system('sudo traceroute -I ' + website)
     os.system('echo [$(date +"%b %d %H:%M:%S")]')
     os.system('ping -w 10 ' + website)
