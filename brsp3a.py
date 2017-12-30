#!/usr/bin/python
import broadlink
import sys,getopt

def main(argv):
  opts,args=getopt.getopt(argv,"h")
  if(len(args)!=1):
    sys.exit(1)
  if(args[0]=='on'):
    fpower=True
  elif(args[0]=='off'):
    fpower=False
  else:
    sys.exit(1)


  type=0x947a
  host='192.168.0.XX'
  mac=bytearray.fromhex('47239dXXXXXX')

  print type,host,mac
  dev = broadlink.gendevice(type, (host, 80), mac)
  dev.auth()
  dev.set_power(fpower)



if __name__ == "__main__":
   main(sys.argv[1:])
