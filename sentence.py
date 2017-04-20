f = open("text.txt")
Point = Exclamation_point = Question_mark = sentence = 0
for s in f:
	i = s.find('.')
	if i > -1:
		Point += 1
	else:
		i = s.find('!')
		if i > -1:
			Exclamation_point += 1
		else:
			i = s.find('?')
			if i > -1:
				Question_mark += 1;
print(Point, '+', Exclamation_point, '+', Question_mark, '=', sentence)				
print('Предложений', sentence)
f.close()