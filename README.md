# Writeups of 247/CTF

## Beginner challenges

### tips and tricks  
`
	import socket  
	import re  

	HOST = 'a2befdcc18c9fdd3.247ctf.com'  
	PORT = 50441  
	templist = ['247', '500']  
	regexp = r'\d{1,4}'  
  
	con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
	con.connect((HOST, PORT))  

	while True:  
    	total = 0  
    	data = con.recv(1024)  
    	 match = re.findall(regexp, repr(data))  
    
    	for num in match:  
        	if num not in templist:  
            		total += int(num)  
    		print(repr(data))  
    		print("Sending %d" % total)  
    		bt = bytes(total)  
    		con.sendall(bt)  

`
