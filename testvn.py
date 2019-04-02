from _lib._vitokenizer import *
from sklearn.model_selection import train_test_split
import pycrfsuite

tester = ViTokenizer.sqltokenize('Lực lượng chức năng Thừa Thiên Huế dùng dây thừng để tiếp cận, cứu hộ các nạn nhân trong vụ ôtô khách lao xuống vực.')
print(tester)

#tester = ViTokenizer.sylabelize('Lực lượng chức năng Thừa Thiên Huế dùng dây thừng để tiếp cận, cứu hộ các nạn nhân trong vụ ôtô khách lao xuống vực.')
#print(tester)

#X = ViTokenizer.sylabelize('MobiFone đầu tư hơn 2 tỉ đồng phát triển mạng')
#y = ['B_W','B_W','I_W','B_W','B_W','B_W','B_W','B_W','I_W','B_W']
#
#feat = ViTokenizer.sent2features(X, False)
#
#X_train, X_test, y_train, y_test = train_test_split(feat, y, test_size=0.2)
##print(X_train)
##print(y_train)
##print(zip(X_train, y_train))
#
#trainer = pycrfsuite.Trainer(verbose=True)
#
## Submit training data to the trainer
##for xseq, yseq in zip(X_train, y_train):
##	print(len(xseq))
##	print(len(yseq))
#trainer.append(X_train, y_train)
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
#
##labels = model.fit([ViTokenizer.sent2features(tester, False)],labs)

#feat = ViTokenizer.sent2features(tester, False)
#print(feat)

#feat = ViTokenizer.tolabels('Lực lượng chức năng Thừa Thiên Huế dùng dây thừng để tiếp cận, cứu hộ các nạn nhân trong vụ ôtô khách lao xuống vực.')
#print(feat)

#feat = ViTokenizer.tolabels('Con Là Con ')
#print(feat)

