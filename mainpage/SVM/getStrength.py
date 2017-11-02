from sklearn import svm
import re

def testingSaala(enterpassword):
	with open('mainpage/SVM/test.txt','w') as test:
		testData = str(enterpassword)+'|'+str(2)
		test.write(testData)

def parseData(data):
	features=list()
	labels=list()
	passwords=list()

	with open(data) as f:
		for line in f:
			if line!='':
				current=line.replace('\n','').split('|')
				password=current[0]
				label=current[1]

				feature=[0,0,0,0,0]


				minlen= False
				specChar=False
				ucChar=False
				numChar=False


				if len(password)>8:
					minlen=True


				specialMatch=re.search(r'([^a-zA-Z0-9]+)', password, re.M)
				if specialMatch:
					specChar=True

				ucMatch = re.search(r'([A-Z])', password, re.M)
				if ucMatch:
					ucChar=True

				numMatch = re.search(r'([0-9])', password, re.M)
				if numMatch:
					numChar=True



				if minlen:
					feature[0]=1

				if specChar and ucChar and numChar:
					feature[1]=3

				if ucChar and numChar:
					feature[2]=1

				if specChar and numChar:
					feature[3]=2

				if specChar and ucChar:
					feature[4]=2


				features.append(feature)
				labels.append(int(label))
				passwords.append(password)

	return [features,labels,password]

def realGame():
	trainingData=parseData('mainpage/SVM/training.txt')
	testingData=parseData('mainpage/SVM/test.txt')


	clf=svm.SVC(kernel='linear',C=1.0)

	clf=clf.fit(trainingData[0],trainingData[1])


	prediction=clf.predict(testingData[0])
	# print ('prediction',prediction)
	# print (testingData[1])
	target=len(testingData[1])
	
	for index in range(target):
				if(prediction[index] == 0):
					predicted = "Very Weak Password"
				elif(prediction[index] == 1):
					predicted = "Weak Password"
				elif(prediction[index] == 2):
					predicted = "Strong Password"
				elif(prediction[index] == 3):
					predicted = "Very Strong Password"

	return (predicted,len(trainingData[1]))