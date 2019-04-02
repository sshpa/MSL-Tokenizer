from _lib._vitokenizer import *
from sklearn.model_selection import train_test_split
import pyodbc
import pickle
import os
import codecs
import json
import re
import pycrfsuite
import sklearn_crfsuite

class ViSQL:
#d = json.loads("{}")

#cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='utf8')
#cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf8')
#cnxn.setencoding(encoding='utf8')

	@staticmethod
	def trainSQLModel():
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=aisdl;UID=sa;PWD=123456')
		cursor = cnxn.cursor()
		
		test_size = 0.33
		seed = 7
		trainer = pycrfsuite.Trainer(verbose=True)

		model = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    #c1=0.1,
    #c2=0.1,
    max_iterations=100,
    all_possible_transitions=True)

		X_train = []
		y_train = []
		cursor.execute("SELECT * FROM datTrainData WHERE Feature<>'' and StatusId=0")		
		for row in cursor.fetchall():
			X = json.loads(row.Feature)
			Y = json.loads(row.Label)

			if len(X) == len(Y):
				X_train.append(X)
				y_train.append(Y)

		model.fit(X_train, y_train)
					
		#X_test = json.loads('[{"bias": 1.0,"word.lower":"mobifone","word_m1.lower":"bos1","word_p1.lower":"đầu","word.islower":false,"word.isupper":false,"word.istitle":false,"word.ispunct":0,"word.isfour_m3":false,"word.isfour_m2":false,"word.isfour_m1":false,"word.isfour":false,"word.istri_m2":false,"word.istri_m1":false,"word.istri":false,"word.isbi_m1":false,"word.isbi":false},{"bias": 1.0,"word.lower":"đầu","word_m1.lower":"mobifone","word_p1.lower":"tư","word.islower":true,"word.isupper":false,"word.istitle":false,"word.ispunct":0,"word.isfour_m3":false,"word.isfour_m2":false,"word.isfour_m1":false,"word.isfour":false,"word.istri_m2":false,"word.istri_m1":false,"word.istri":false,"word.isbi_m1":false,"word.isbi":true},{"bias": 1.0,"word.lower":"tư","word_m1.lower":"đầu","word_p1.lower":"hơn","word.islower":true,"word.isupper":false,"word.istitle":false,"word.ispunct":0,"word.isfour_m3":false,"word.isfour_m2":false,"word.isfour_m1":false,"word.isfour":false,"word.istri_m2":false,"word.istri_m1":false,"word.istri":false,"word.isbi_m1":true,"word.isbi":false},{"bias": 1.0,"word.lower":"hơn","word_m1.lower":"tư","word_p1.lower":"2","word.islower":true,"word.isupper":false,"word.istitle":false,"word.ispunct":0,"word.isfour_m3":false,"word.isfour_m2":false,"word.isfour_m1":false,"word.isfour":false,"word.istri_m2":false,"word.istri_m1":false,"word.istri":false,"word.isbi_m1":false,"word.isbi":false},{"bias": 1.0,"word.lower":"2","word_m1.lower":"hơn","word_p1.lower":"tỉ","word.islower":true,"word.isupper":true,"word.istitle":false,"word.ispunct":1,"word.isfour_m3":false,"word.isfour_m2":false,"word.isfour_m1":false,"word.isfour":false,"word.istri_m2":false,"word.istri_m1":false,"word.istri":false,"word.isbi_m1":false,"word.isbi":false},{"bias": 1.0,"word.lower":"tỉ","word_m1.lower":"2","word_p1.lower":"đồng","word.islower":true,"word.isupper":false,"word.istitle":false,"word.ispunct":0,"word.isfour_m3":false,"word.isfour_m2":false,"word.isfour_m1":false,"word.isfour":false,"word.istri_m2":false,"word.istri_m1":false,"word.istri":false,"word.isbi_m1":false,"word.isbi":false},{"bias": 1.0,"word.lower":"đồng","word_m1.lower":"tỉ","word_p1.lower":"phát","word.islower":true,"word.isupper":false,"word.istitle":false,"word.ispunct":0,"word.isfour_m3":false,"word.isfour_m2":false,"word.isfour_m1":false,"word.isfour":false,"word.istri_m2":false,"word.istri_m1":false,"word.istri":false,"word.isbi_m1":false,"word.isbi":false},{"bias": 1.0,"word.lower":"phát","word_m1.lower":"đồng","word_p1.lower":"triển","word.islower":true,"word.isupper":false,"word.istitle":false,"word.ispunct":0,"word.isfour_m3":false,"word.isfour_m2":false,"word.isfour_m1":false,"word.isfour":false,"word.istri_m2":false,"word.istri_m1":false,"word.istri":false,"word.isbi_m1":false,"word.isbi":true},{"bias": 1.0,"word.lower":"triển","word_m1.lower":"phát","word_p1.lower":"mạng","word.islower":true,"word.isupper":false,"word.istitle":false,"word.ispunct":0,"word.isfour_m3":false,"word.isfour_m2":false,"word.isfour_m1":false,"word.isfour":false,"word.istri_m2":false,"word.istri_m1":false,"word.istri":false,"word.isbi_m1":true,"word.isbi":false},{"bias": 1.0,"word.lower":"mạng","word_m1.lower":"triển","word_p1.lower":"eos1","word.islower":true,"word.isupper":false,"word.istitle":false,"word.ispunct":0,"word.isfour_m3":false,"word.isfour_m2":false,"word.isfour_m1":false,"word.isfour":false,"word.istri_m2":false,"word.istri_m1":false,"word.istri":false,"word.isbi_m1":false,"word.isbi":false}]')
		#labels = model.predict(X_test)
		
		# Save necessary files.
		f = open('./model.crf.pkl', 'wb')
		pickle.dump(model,f)
		f.close()
		
	@staticmethod
	def trainModel():
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=aisdl;UID=sa;PWD=123456')
		cursor = cnxn.cursor()
		
		test_size = 0.33
		seed = 7
		#trainer = pycrfsuite.Trainer(verbose=True)

		#cursor.execute("SELECT * FROM datTrainData WHERE Feature<>''")
		#for row in cursor.fetchall():
		#	X = json.loads(row.Feature)
		#	Y = json.loads(row.Label)
		#	X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
		#	trainer.append(X_train, y_train)
    #
		## Set the parameters of the model
		#trainer.set_params({
		#    # coefficient for L1 penalty
		#    'c1': 0.1,
		#
		#    # coefficient for L2 penalty
		#    'c2': 0.01,  
		#
		#    # maximum number of iterations
		#    'max_iterations': 200,
		#
		#    # whether to include transitions that
		#    # are possible, but not observed
		#    'feature.possible_transitions': True
		#})
		#
		## Provide a file name as a parameter to the train function, such that
		## the model will be saved to the file when training is finished
		#trainer.train('crf.model')

		model = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
    max_iterations=1000,
    all_possible_transitions=True)

		X_train = []
		y_train = []
		cursor.execute("SELECT * FROM datTrainData WHERE Feature<>''")		
		for row in cursor.fetchall():
			X_train.append(json.loads(row.Feature))
			y_train.append(json.loads(row.Label))
			
		model.fit(X_train, y_train)
		
		# Save necessary files.
		f = open('./model.crf.pkl', 'wb')
		pickle.dump(model,f)
		f.close()

	@staticmethod
	def loadBigrams():
		bi_grams = set()
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=aisdl;UID=sa;PWD=123456')
		cursor = cnxn.cursor()
		
		cursor.execute("SELECT * FROM datVietWord WHERE WordCount = 2")		
		for row in cursor.fetchall():
			bi_grams.add(row.Words)
	    
		return(bi_grams)

	@staticmethod
	def sql2feature(sent):
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=aisdl;UID=sa;PWD=123456')
		cursor = cnxn.cursor()
		
		sql = "select dbo.json2features(dbo.Sylabelize(?)) as Feature"
		cursor.execute(sql, (sent))
		row = cursor.fetchone()
		if row == None:
			return []
			
		return(json.loads(row.Feature))

	@staticmethod
	def sql2sylabelize(sent):
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=aisdl;UID=sa;PWD=123456')
		cursor = cnxn.cursor()
		
		sql = "select dbo.Sylabelize(?) as Sylabel"
		cursor.execute(sql, (sent))
		row = cursor.fetchone()
		if row == None:
			return []
			
		return(json.loads(row.Sylabel))

	@staticmethod
	def loadTrigrams():
		tri_grams = set()
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=aisdl;UID=sa;PWD=123456')
		cursor = cnxn.cursor()
		
		cursor.execute("SELECT * FROM datVietWord WHERE WordCount = 3")		
		for row in cursor.fetchall():
			tri_grams.add(row.Words)
	    
		return(tri_grams)

	@staticmethod
	def appendWord():
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=aisdl;UID=sa;PWD=123456')
		cursor = cnxn.cursor()
		with codecs.open(os.path.join(os.path.dirname(__file__), '_lib/models/words.txt'), 'r', encoding='utf-8') as fin:
			for token in fin.read().split('\n'):
				tmp = token.split(' ')
				sql = "insert into datVietWord(Words, WordCount) values(N'" + token + "'," + str(len(tmp)) + ")"
				cursor = cnxn.cursor()
				cursor.execute(sql)
				cnxn.commit()
				print(token)

	def appendName():
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=aisdl;UID=sa;PWD=123456')
		cursor = cnxn.cursor()
		with codecs.open(os.path.join(os.path.dirname(__file__), 'data/vnpernames.txt'), 'r', encoding='utf-8') as fin:
			for token in fin.read().split('\n'):
				token = token.strip()
				token = re.sub('\'', '\'\'', token)
				tmp = token.split(' ')
				sql = "insert into datVietName(Words, WordCount, Sex) select N'" + token + "'," + str(len(tmp)) + ",'' where not exists (select 1 from datVietName where Words=N'" + token + "')"
				cursor = cnxn.cursor()
				cursor.execute(sql)
				cnxn.commit()
				#print(token)

	@staticmethod
	def appendWordUtf8():
		print ("STEP : Preparing dictionary.")
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=aisdl;UID=sa;PWD=123456')
		cursor = cnxn.cursor()
		with codecs.open(os.path.join(os.path.dirname(__file__), 'data/VNDic_UTF-8.txt'), 'r', encoding='utf-8') as fin:
			words_ = []
			for token in fin.read().split('\n'):
				if re.search('##', token):
					word = re.sub('##', '', token)
					#word = '_'.join(word.split()) # Note: join by '_' to match CRFSuite format.
					words_.append(word)
				if re.search('@@', token):
					token = re.sub('@@', '', token)
					if token in ['Proverb', 'Idiom']:
						del words_[-1] # Remove last item added if it is a proverb or idiom.
		words_ = set(words_) # IMPORTANT NOTE: set is much faster to search than list.
		for word in words_:
			tmp = word.split(' ')
			word = re.sub('\'', '\'\'', word)			
			sql = "insert into datVietWord(Words, WordCount) select N'" + word + "'," + str(len(tmp)) + " where not exists (select 1 from datVietWord where Words=N'" + word + "')"
			#print(sql)
			cursor = cnxn.cursor()
			cursor.execute(sql)
			cnxn.commit()

	@staticmethod
	def appendLocation():
		with codecs.open(os.path.join(os.path.dirname(__file__), '_lib/data/vnlocations.txt'), 'r', encoding='utf-8') as fin:
			for token in fin.read().split('\n'):
				tmp = token.split(' ')
				#print(token)
				sql = "insert into datVietLocation(Words, WordCount) values(N'" + re.sub('\'', '\'\'', token) + "'," + str(len(tmp)) + ")"
				cursor = cnxn.cursor()
				cursor.execute(sql)
				cnxn.commit()

	@staticmethod
	def updateFeature():
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=aisdl;UID=sa;PWD=123456')
		cursor = cnxn.cursor()
		
		cursor.execute("SELECT * FROM datTrainData WHERE Feature=''")
		for row in cursor.fetchall():
			#print(row)
			syls = json.loads(row.Syls)
			feat = ViTokenizer.sent2features(syls, False)
			feat = re.sub('\'', '\'\'', json.dumps(feat, ensure_ascii=False))			
			#print(feat)
			
			sql = "UPDATE [dbo].[datTrainData] SET [Feature] = ? WHERE Id = ?"
			#print(sql)
			cursorUdp = cnxn.cursor()
			cursorUdp.execute(sql, (feat, row.Id))
			cnxn.commit()
    
	@staticmethod
	def appendTrain():
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=aisdl;UID=sa;PWD=123456')

		nRuns = 5
		for RUN in range(nRuns): 
		
			print ("Run# " + str(RUN))
			
			# Read in raw train file in JVnSeg format,
			# i.e. each line: "syllable \t label", label = {B_W, I_W, O}.
			# Empty line to mark end of sentences.
			if 1:
				fname = '_lib/data/train' + str(RUN+1) + '.iob2'
				fin = codecs.open(os.path.join(os.path.dirname(__file__), fname), mode = 'r', encoding='utf-8', errors = 'ignore') 
				seqs = [] # List of sentences.
				seq = {}
				seq['labels'] = [] # label = {B_W, I_W, O}.
				seq['syls'] = [] # Vietnamese syllables.
				sent = ''
			
				for line in fin:
					line_ = line.split()
					if len(line_) == 0: # End of sentence. 
		
						syls = re.sub('\'', '\'\'', json.dumps(seq['syls'], ensure_ascii=False))
						labs = re.sub('\'', '\'\'', json.dumps(seq['labels'], ensure_ascii=False))
						sent = re.sub('\'', '\'\'', sent)
						#print (syls)
						
						#sql = "INSERT INTO [dbo].[datTrainData]([DatasetId] ,[Sent] ,[Syls] ,[Label] ,[Feature] ,[StatusId]) VALUES (" + str(RUN) + ", '', N'" + re.sub('\'', '\'\'', json.dumps(seq['syls'], ensure_ascii=False).encode('utf8')) + "', N'" + re.sub('\'', '\'\'', json.dumps(seq['labels'], ensure_ascii=False).encode('utf8')) + "', '', 0)"
						
						sql = "INSERT INTO [dbo].[datTrainData]([DatasetId] ,[Sent] ,[Syls] ,[Label] ,[Feature] ,[StatusId]) VALUES (" + str(RUN+1) + ", ?, ?, ?, '', 0)"
						#print(sql)
						cursor = cnxn.cursor()
						cursor.execute(sql, (sent, syls, labs))
						cnxn.commit()
				
						seqs.append(seq)
						seq = {}
						seq['labels'] = []
						seq['syls'] = []
						sent = ''
						#input("Press Enter to continue...")
						continue
			
					seq['syls'].append(re.sub(":", "\:", line_[0])) # Must escape ':' -> specific to CRFSuite.
					seq['labels'].append(line_[1])
					if len(sent) > 0:
						sent = sent + ' '
					sent = sent + line_[0]
					#print seq
		
				# Last sentence.
				if len(seq['labels']) > 0:
					syls = re.sub('\'', '\'\'', json.dumps(seq['syls'], ensure_ascii=False))
					labs = re.sub('\'', '\'\'', json.dumps(seq['labels'], ensure_ascii=False))
					sent = re.sub('\'', '\'\'', sent)
					#print (syls)
					
					#sql = "INSERT INTO [dbo].[datTrainData]([DatasetId] ,[Sent] ,[Syls] ,[Label] ,[Feature] ,[StatusId]) VALUES (" + str(RUN) + ", '', N'" + re.sub('\'', '\'\'', json.dumps(seq['syls'], ensure_ascii=False).encode('utf8')) + "', N'" + re.sub('\'', '\'\'', json.dumps(seq['labels'], ensure_ascii=False).encode('utf8')) + "', '', 0)"
					
					sql = "INSERT INTO [dbo].[datTrainData]([DatasetId] ,[Sent] ,[Syls] ,[Label] ,[Feature] ,[StatusId]) VALUES (" + str(RUN+1) + ", ?, ?, ?, '', 0)"
					#print(sql)
					cursor = cnxn.cursor()
					cursor.execute(sql, (sent, syls, labs))
					cnxn.commit()
		
					seqs.append(seq)
					seq['labels'] = []
					seq['syls'] = []
					sent = ''
				fin.close()
