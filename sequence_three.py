import os

list_of_websites = ['www.youtube.com']#, 'www.reddit.com', 'www.amazon.com', 'www.amazon.co.jp', 'cnj.craigslist.org']

f = open("seq3_jliu08.txt", "a")

output = ""

for website in list_of_websites:
    stream = os.popen(  'echo [$(date +"%b %m %H:%M:%S")]\n' + \
                        'sudo traceroute -I ' + website + "\n" + \
                        'echo [$(date +"%b %m %H:%M:%S")]\n' + \
                        'timeout 10 ping ' + website + "\n" + \
                        'echo [$(date +"%b %m %H:%M:%S")]\n' + \
                        'timeout 180 sudo ./clink.1.0/clink -s64 ' + website + "\n" + \
                        'echo [$(date +"%b %m %H:%M:%S")]\n' + \
                        'sudo traceroute -I ' + website + "\n" + \
                        'echo [$(date +"%b %m %H:%M:%S")]\n' + \
                        'timeout 10 ping ' + website)
    
    output += stream.read()
    output += "\n"
    
f.write(output)