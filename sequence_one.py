import os

list_of_websites = ['23.43.254.42', '151.101.1.224', '31.13.71.49', '31.13.71.36', '151.101.65.67', '151.101.65.164', '23.8.173.150', '104.18.24.142', '104.105.80.103', '104.78.191.105']

f = open("seq1_jliu08.txt", "a")

for website in list_of_websites:
    stream = os.popen(  'echo [$(date +"%b %d %H:%M:%S")]\n' + \
                        'sudo traceroute -I ' + website + "\n" + \
                        'echo [$(date +"%b %d %H:%M:%S")]\n' + \
                        'timeout 10 ping ' + website + "\n" + \
                        'echo [$(date +"%b %d %H:%M:%S")]\n' + \
                        'sudo traceroute -I ' + website + "\n" + \
                        'echo [$(date +"%b %d %H:%M:%S")]\n' + \
                        'timeout 10 ping ' + website)
    
    output = stream.read()
    
    f.write(output + "\n")
