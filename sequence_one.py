import os

list_of_names = ['www.jdsports.com', 'www.etsy.com', 'www.pinterest.com', 'www.yelp.com', 'www.nytimes.com', 'www.cnn.com', 'www.mayoclinic.org', 'www.webmd.com', 'www.state.gov', 'www.whitehouse.gov']
list_of_websites = ['184.87.67.199', '104.105.41.236', '104.77.220.247', '104.16.57.23', '151.101.1.164', '151.101.1.67', '184.87.61.168', '104.16.159.5', '184.87.67.64', '104.78.191.105']

for i in range(len(list_of_websites)):
    website = list_of_websites[i]
    
    os.system('echo ' + list_of_names[i])

    os.system('echo [$(date +"%b %d %H:%M:%S")]')

    os.system('sudo traceroute -I ' + website)

    os.system('echo [$(date +"%b %d %H:%M:%S")]')

    os.system('ping -w 10 ' + website)

    os.system('echo [$(date +"%b %d %H:%M:%S")]')

    os.system('sudo traceroute -I ' + website)

    os.system('echo [$(date +"%b %d %H:%M:%S")]')

    os.system('ping -w 10 ' + website)
    
