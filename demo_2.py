from Wikitest import linkgen, datagen, modelmaker, inforeport, articletester

#Autobiolinks = linkgen('Autobiography')
#datagen('datafile.csv',links,"Special:RandomInCategory/Living_people")
model = modelmaker('Autobio.csv','Autobio.pkl')
test_articles = ['Charles_III','Keira_Maameri','Camilo_Echevarría','Diana_Hess']
preds = articletester(test_articles,'Autobio.pkl')
print(test_articles)
print(preds)