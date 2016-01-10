import array

def hex2bin(hex):
	return dec2bin(int(hex,16),32)

def dec2hex(n):
    """return the hexadecimal string representation of integer n"""
    return "%X" % n

def hex2dec(s):
    """return the integer value of a hexadecimal string s"""
    return int(s, 16)

def dec2bin(n, bits):
	frmt = '{0:0'+str(bits)+'b}'
	return frmt.format(n)

def bin2dec(n):
	return int(n,2)

def bin_add(*args): return '{0:b}'.format(sum(int(x, 2) for x in args))

def butterfly(p, z1, z2):
	if p==1:
		out = z2+z1;
	else:
		out = z1+z2;
	return out

# xor-1 : 5 bits
# xor_2 : 5 bits
# D : 9 bits
def perm5(arg_x, arg_c, arg_d):
	P = arg_c+arg_d

	Z = arg_x
	#Stage 1
	s1_03 = butterfly ( P[12], Z[0], Z[3] )
	s1_12 = butterfly ( P[13], Z[1], Z[2] )
	S1 = Z[4]+s1_03[1]+s1_12[1]+s1_12[0]+s1_03[0]

	# Stage 2
	s2_24 = butterfly ( P[10], S1[2], S1[4] )
	s2_13 = butterfly ( P[11], S1[1], S1[3] )
	S2 = s2_24[1]+s2_13[1]+s2_24[0]+s2_13[0]+S1[0]

	# Stage 3
	s3_14 = butterfly ( P[8], S2[1], S2[4] )
	s3_03 = butterfly ( P[9], S2[0], S2[3] )
	S3 =  s3_14[1]+s3_03[1]+S2[2]+s3_14[0]+s3_03[0]
	
	# Stage 4
	s4_02 = butterfly ( P[6], S3[0], S3[2] )
	s4_34 = butterfly ( P[7], S3[3], S3[4] )
	S4 = s4_34[1]+s4_34[0]+s4_02[1]+S3[1]+s4_02[0]

	# Stage 5
	s5_04 = butterfly ( P[4], S3[0], S3[4] )
	s5_13 = butterfly ( P[5], S3[1], S3[3] )
	S5 = s5_04[1]+s5_13[1]+S4[2]+s5_13[0]+s5_04[0]

	# Stage 6
	s6_12 = butterfly ( P[2], S3[1], S3[2] )
	s6_34 = butterfly ( P[3], S3[3], S3[4] )
	S6 = s6_34[1]+s6_34[0]+s6_12[1]+s6_12[0]+S5[0]

	# Stage 7
	s7_01 = butterfly ( P[0], S3[0], S3[1] )
	s7_23 = butterfly ( P[1], S3[2], S3[3] )
	S7 = S6[4]+s7_23[1]+s7_23[0]+s7_01[1]+s7_01[0]

	return S7

