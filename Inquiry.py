import Operations as op

def run():

	kOffset_a = 24
	kOffset_b = 8

	clk = 0
	arr = []

	isNextTrainA = True

	offset = kOffset_a

	for clk in range(0, 8192*4):
		if int(clk%(8192)) == 0:
			if isNextTrainA:
				offset = kOffset_a
				isNextTrainA = False
			else:
				offset = kOffset_b
				isNextTrainA = True
		
		
		

		#The Bluetooth clock is a 28-bit counter with a clock cycle of 312.5µs.
		# Bluetooth communication at the Baseband level is organised into time slots.
		# Each slot has a length of two clock cycles, i.e. 625µs.
		clk_bits = op.dec2bin(clk, 32) # change clock to 32 bits 
		
		#---------------------------
		# 			Find X

		# 0 index is right most one
		# 4-0 would actually mean -> indices 27, 28, 29 , 30, 31

		# Similarly take clock's 16-12
		# +1 because python does not include b if a:b
		clk_16_12 = op.bin2dec(clk_bits[31-16:31-12+1])
		clk_4_2_0 = op.bin2dec(clk_bits[31-4:31-2+1]+clk_bits[31-0])


		#################################################
		sub_clk = 0
		'''if clk_16_12 > clk_4_2_0:
			sub_clk = clk_16_12 - clk_4_2_0
		else:
			sub_clk = clk_4_2_0 - clk_16_12
		'''
		# clk_4_2_0 is always a pattern like 0101 2323 ... 12131213, 14151415. (32 tics)
		# clk_16_12 is 0 for 4096 tics and 1 for next 4096 then 2 so on
		# subtraction doesn't make sense
		sub_clk = (clk_4_2_0 - clk_16_12)		
		temp_clk = (sub_clk % 16) # in decimal
		
		Xi = op.dec2bin((clk_16_12 + offset + temp_clk) % 32, 32)
		X = Xi[31-4:31-0+1]
		#print(">>> " + X)
		#print("X: "+str(temp_clk))
		#---------------------------





		# 0000 1001 1110 1000 
		#address = [ 4-LSBs-of-DCI(0x00), GIAC LAP (0x9E8B33)]
		address = op.hex2bin('09E8B33') # this return 32 bits

		###########################
		## we can flip the address

		address = address[4:] # Get 28 bits

		#print("Address:" + address)

		A = address[27-27:27-23+1]
		B = address[27-22:27-19+1]
		C = ''.join((address[27-8],address[27-6],address[27-4],address[27-2],address[27-0]))
		D = address[27-18:27-10+1]
		E = ''.join((address[27-13],address[27-11],address[27-9],address[27-7],address[27-5],address[27-3],address[27-1]))
		F = '0'
		
		#print('clock [1]: ' + clk_bits[31-1])
		Y1 = clk_bits[31-1] * 5 # in binary
		#Y1 = clk_bits[31-2]

		if clk_bits[31-1] == '0':
			Y2 = '000000'
		else:
			Y2 = '100000'
		#Y2 will either be 100000 or 000000
		#Y2 = op.dec2bin(32 * op.bin2dec(clk_bits[31-1]), 32) # in binary

		#Y1 = '0'
		Y2 = '0'

		add_1 = '{0:05b}'.format((op.bin2dec(A) + op.bin2dec(X))%32)
		xor_1 = '{0:05b}'.format(op.bin2dec(add_1) ^ op.bin2dec(B))
		xor_2 = '{0:05b}'.format(op.bin2dec(C) ^ op.bin2dec(Y1))
		perm_1 = op.perm5(xor_1, xor_2, D)
		add_2 = op.bin_add(E,F,perm_1, Y2)
		freq = op.bin2dec(add_2) % 79
		arr.append(freq)
	return arr


