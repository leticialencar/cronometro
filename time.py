def cronometro (h, m, s):
	total = h * 3600 + m * 60 + s
	
	while total >= 0:
		h = total // 3600
		m = (total % 3600) // 60
		s = total % 60
		print(h, m, s)
		total -=1

cronometro(23, 59, 59)