import os

list_of_websites = ['www.youtube.com', 'www.reddit.com', 'www.amazon.com', 'www.amazon.co.jp', 'cnj.craigslist.org']

for website in list_of_websites:
     os.system(  'echo [$(date +"%b %m %H:%M:%S")]\n' + \
                        'traceroute ' + website + "\n" + \
                        'echo [$(date +"%b %m %H:%M:%S")]\n' + \
                        'timeout 10 ping ' + website + "\n" + \
                        'echo [$(date +"%b %m %H:%M:%S")]\n' + \
                        'timeout 150 clink -s64 ' + website + "\n" + \
                        'echo [$(date +"%b %m %H:%M:%S")]\n' + \
                        'traceroute ' + website + "\n" + \
                        'echo [$(date +"%b %m %H:%M:%S")]\n' + \
                        'timeout 10 ping ' + website)
