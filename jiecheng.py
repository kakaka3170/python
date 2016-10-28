

def chengfa99():
	'this is triangle 9X9 table';
	for i in range(1,10):
    		for j in range(1,i+1):
        		print ('%2d X %2d = %2d  '%(j,i,j*i),end='');
    		print('');
	pass;


if __name__ == '__main__' : 
	chengfa99();
	pass;



