import subprocess
p = subprocess.Popen('ping 127.0.0.1').read()
# Linux Version p = subprocess.Popen(['ping','127.0.0.1','-c','1',"-W","2"])
# The -c means that the ping will stop afer 1 package is replied 
# and the -W 2 is the timelimit
p.wait()
print (p.poll())
