def read(filename):
	df_full = []
	with open(filename, 'r') as f:
		for line in f:
			df_full.append(line)
	return df_full

def dict_add(filename):
	wc = {}
	df_full = read(filename)
	for lines in df_full:
		words = lines.split()
		for word in words:
			if word in wc:
				wc[word] += 1
			else:
				wc[word] = 1
	return wc

read('reviews.txt')
wc = dict_add('reviews.txt')
for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])



