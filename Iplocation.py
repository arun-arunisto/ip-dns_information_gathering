import os
import urllib.request as urllib2
import json
import socket
import subprocess

subprocess.call('clear',shell = True)

banner = (
  """
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  I LOVE DOS!    |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------'
                                ©️®️arun_arunisto
                                                """

)

banner_1 = (
  """
  
._____________.__                        __          
|   \______   \  |   ____   ____ _____ _/  |_  ____  
|   ||     ___/  |  /  _ \_/ ___\.__  \.   __\/ __ \ 
|   ||    |   |  |_(  <_> )  \___ / __ \|  | \  ___/ 
|___||____|   |____/\____/ \___  >____  /__|  \___  >
                               \/     \/          \/ 
                                    Type IP to Locate
                                                         """
  
  
  )

banner_2 = (
  """
  
________                        .__              __   
\______ \   ____   _____ _____  |__| ____        \ \  
 |    |  \ /  _ \ /     \|__  \ |  |/    \        \ \ 
 |    `   (  <_> )  Y Y  \/ __ \|  |   |  \       / / 
/_______  /\____/|__|_|  (____  /__|___|  /_____ /_/  
        \/             \/     \/        \/_____/      
                                Type DOMAIN to Locate
                                                       """
  
  
  )

print(banner)
msg = "advanced information gathering tool"
print()
print(msg.upper())
print('-' * len(msg))
print()

print("\033[91m {}\033[00m" .format('\n 1. IP Location Finder \t2. DNS Location Finder \t3. Exit'))


while True:
  opt = int(input("\n Enter your Option to Proceed : "))
  if opt == 1:
    subprocess.call('clear', shell = True)
    print(banner_1)
    msg = "advanced information gathering tool"
    print()
    print(msg.upper())
    print('-' * len(msg))
    print()
    ip = input("\n Enter IP : ")
    url = "http://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)
    sts = (" Status : " +values['status'])
    coun = ("\tCountry \t: \t" +values['country'])
    state = ("\tState \t\t: \t" +values['regionName'])
    city = ("\tCity \t\t: \t" +values['city'])
    zip_code = ("\tZip Code \t: \t" +values['zip'])
    tz = ("\tTime Zone \t: \t" +values['timezone'])
    isp = ("\tISP \t\t: \t" +values['isp'])
    print("\n")
    print("\033[92m {}\033[00m" .format(sts))
    print()
    print(coun)
    print(state)
    print(city)
    print(zip_code)
    print("\tLattitude \t: \t" ,values['lat'])
    print("\tLongtitude \t: \t" ,values['lon'])
    print(tz)
    print(isp)
    
  elif opt == 2:
    subprocess.call('clear', shell = True)
    print(banner_2)
    msg = "advanced information gathering tool"
    print()
    print(msg.upper())
    print('-' * len(msg))
    print()
    host = input("\n Enter URL : ")
    ip = socket.gethostbyname(host)
    print("\n Website : " +host)
    print("\n IP address : " +ip)
    url = "http://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)
    sts = (" Status : " +values['status'])
    coun = ("\tCountry \t: \t" +values['country'])
    state = ("\tState \t\t: \t" +values['regionName'])
    city = ("\tCity \t\t: \t" +values['city'])
    zip_code = ("\tZip Code \t: \t" +values['zip'])
    tz = ("\tTime Zone \t: \t" +values['timezone'])
    isp = ("\tISP \t\t: \t" +values['isp'])
    print("\n")
    print("\033[92m {}\033[00m" .format(sts))
    print()
    print(coun)
    print(state)
    print(city)
    print(zip_code)
    print("\tLattitude \t: \t" ,values['lat'])
    print("\tLongtitude \t: \t" ,values['lon'])
    print(tz)
    print(isp)
    
  else:
    break
  
    
    
