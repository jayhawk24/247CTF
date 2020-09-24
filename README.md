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
## Web

### Secured Session
Visiting the website shows this code.
`

    import os
    from flask import Flask, request, session
    from flag import flag
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    
    
    def secret_key_to_int(s):
        try:
            secret_key = int(s)
        except ValueError:
            secret_key = 0
        return secret_key
    
    
    @app.route("/flag")
    def index():
        secret_key = secret_key_to_int(
            request.args['secret_key']) if 'secret_key' in request.args else None
        session['flag'] = flag
        if secret_key == app.config['SECRET_KEY']:
            return session['flag']
        else:
            return "Incorrect secret key!"
    
    
    @app.route('/')
    def source():
        return "
    
    
    %s
    
    " % open(__file__).read()
    
    if __name__ == "__main__":
        app.run()
    
`
So a session is created always with this line.
`
	session['flag'] = flag
`
  
We can set our session by adding a get parameter called secret_key which will set our session and we will get our flag.  
so goto b12fa redacted .247ctf.com/flag?secret_key  
and you will get a cookie called   

session=eyJmbGFnIjp7Ii redacted ptPn6ECgKW2vT09o

decrypt it twice with base 64.
  
{"flag":{" b":"247CTF{da807 redacted 807b9a91}"fX0._lU-Q.LGd_µ4´~i´ùú(
[kÓ09o

### Trusted Client
Look into the source code and you will find a javascript function which runs on submiting.  
It is written in js fu*k so decrypt on this website https://enkhee-osiris.github.io/Decoder-JSFuck/ it get find the flag. 

