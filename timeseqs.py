# Файл timeseqs.py
import sys, mytimer
# Импортирует функцию timer
reps = 10000
repslist = range(reps) # Вызов функции range вынесен за пределы цикла в 2.6

def forLoop():
res = []
for x in repslist:
res.append(abs(x))
return res

def listComp():
return [abs(x) for x in repslist]

def mapCall():
return list(map(abs, repslist))

# Вызов list необходим только в 3.0
def genExpr():
return list(abs(x) for x in repslist) # Функция list вынуждает

# вернуть сразу все результаты
def genFunc():
	def gen():
		for x in repslist:
			yield abs(x)
		return list(gen())
		
print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
	elapsed, result = mytimer.timer(test)
	print (‘-’ * 33)
	print (‘%-9s: %.5f => [%s...%s]’ %
	(test.__name__, elapsed, result[0], result[-1]))
