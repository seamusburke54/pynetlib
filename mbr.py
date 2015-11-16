import sys
import os.path
import subprocess
import struct

class mbrrecord():
	def __init__(self, sector, partno):
	#first record is at offset 446, records are 15 bytes
	offset = 446 + partno * 16
	self.active = false
	
	#if 0x80 is first byte means it's bootable
	if sector[offset] == '\x80':
		self.active = true
	self.type = ord(sector[offset+4])
	self.empty = false

	# if the partiti type is 0 it means it's empty
	if self.type == 0
		self.empty = true
	

#values for each HD sector are 32 bits and little endian
self.start = struct.unpack('<I', sector[offset + 8: \ offset +12: \ offset + 16])[0]
self.sectors = struct.unpack('<I', sector[offset + 12: \ offset + 16])[0]
def printPart(self):
	if self.empty == true:
		print("<empty>")
	else:
		outstr = ""
		if self.active == true:
		outstr += "Bootable:"
		outstr += "Type " + str(self.type) + ":"
		outstr += "Start " + str(self.start) + ":"
		outstr += "Total Sectors " + str(self.sectors)
		print outstr
def usage():
	print("usage " + sys.argv[0] + " <image file>\nAttempts to mount partitions from an image file")
	exit(1)
def main():
	if len(sys.argv) < 2:
		usage()
	if not os.path.isfile(sys.argv[1]):
		print("File " + sys.argv[1] + "cannot be opened for analysis")
		exit(1)
	with open(sys.argv[1], 'rb') as f:
		sector = str(f.read(512))
	if (sector[510] == "\x55" and sector[511] == "\xaa"):
		print("Is MBR or VBR")
	if (sector[446] == "\x80" or sector[446] == "\x00") and \ (sector[462] == "\x80" or sector[462] == "\x00") and \ (sector[478] == "\x80" or sector[478] == "\x00") and \ (sector[494] == "\x80" or sector[494] == "\x00"):
		print("is a MBR")
		parts = [mbrrecord(sector, 0), mbrrecord(sector, 1), \ mbrrecord(sector, 2), mbrrecord(sector, 3)]
		for p in parts:
			p.printPart()
			if not p.empty:
				notsupParts = [0x05, 0x0f, 0x85, 0x91, 0x9b, 0xc5, 0xe4, 0xee]
			if p.type in notsupParts:
				print("sorry GPT and other partitions not currently supported")
			else:
			mountpath = '/media/part%s' % str(p.partno)
			if not os.path.isdir(mountpath):
				subprocess.call(['mkdir', mountpath])
					mountopts = 'loop, ro, noatime, offset=%s % \ str(p.start * 512)
				subprocess.call(['mount', '-o' \ mountopts, sys.argv[1], mountpath])
		else:
			print("Appears to be VBR\nAttempting to mount")
			if not os.path.isdir('/media/part1'):
				subprocess.call(['mkdir', '/media/part1'])
				subprocess.call(['mount', '-o'. 'loop,ro,noatime', \ sys.argv[1], '/media/part1'])
if __name__ == "__main__":
main()


					
