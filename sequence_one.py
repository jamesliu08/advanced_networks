import os

list_of_websites = ['www.ebay.com', 'etsy.com', 'twitter.com', 'facebook.com', 'cnn.com', 'nytimes.com', 'www.mayoclinic.org', 'webmd.com', 'www.fda.gov', 'www.whitehouse.gov']

for website in list_of_websites:
    os.system('traceroute -I ' + website)
    os.system('timeout 10 ping ' + website)
    os.system('traceroute -I ' + website)
    os.system('timeout 10 ping ' + website)