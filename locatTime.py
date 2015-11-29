#-*- coding:utf-8 -*- 

import time 
import random
import os
 
if __name__ == '__main__': 
	timeSpaces = 2
	
	while True:
		fp = open('random.txt', 'w')
		fp.write(str(random.randint(0, 20)))
		fp.close()
		os.system('git add .')
		os.system('git commit -m "commit"')
		
		time.sleep(timeSpaces)
		
	print 'finished'