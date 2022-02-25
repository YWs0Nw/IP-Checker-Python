import json ,requests ,os
me = """
                                            ,a8888a,                                    
                                          ,8P"'  `"Y8,                                  
                                         ,8P        Y8,                                 
8b       d8 8b      db      d8 ,adPPYba, 88          88 8b,dPPYba,  8b      db      d8  
`8b     d8' `8b    d88b    d8' I8[    "" 88          88 88P'   `"8a `8b    d88b    d8'  
 `8b   d8'   `8b  d8'`8b  d8'   `"Y8ba,  `8b        d8' 88       88  `8b  d8'`8b  d8'   
  `8b,d8'     `8bd8'  `8bd8'   aa    ]8I  `8ba,  ,ad8'  88       88   `8bd8'  `8bd8'    
    Y88'        YP      YP     `"YbbdP"'    "Y8888P"    88       88     YP      YP      
    d8'                                                                                 
   d8'
                                _                ___       _.--.
                                \`.|\..----...-'`   `-._.-'_.-'`
                                /  ' `         ,       __.--'
                                )/' _/     \   `-_,   /
                                `-'" `"\_  ,_.-;_.-\_ ',     2022/2047
                                    _.-'_./   {_.'   ; /
                                   {_.-``-'         {_/


    """
print(me)
IPfromUSER = input('* OPTION IP Address : ')
# Fatch Data From Url
r = requests.get('http://ip-api.com/json/'+IPfromUSER)
#Transfer text to json
json_str =  r.content
data = json.loads(json_str)
#
fail = 'fail'
IP = data['query']
Status = data['status']
if Status == fail:
    os.system('clear')
    print(me)
    print('Error')
else:
    CountryCode = data['countryCode']
    Timezone = data['timezone']
    ISP = data['isp']
    os.system('clear')
    print(me)
    print(f"IP     : {IP}")
    print(f"ISP    : {ISP}")
    print(f"CNTRC  : {CountryCode}")
    print(f"TIMEZ  : {Timezone}")
    print(f"STATUS : {Status}")
