import matplotlib.pyplot as plt
from Wikitest import linkgen, datagen, modelmaker, inforeport, articletester

#POVlinks = linkgen('POV')
#datagen('POV.csv',POVlinks,'Special:Random',dropstubs=True)
modelmaker('POV.csv','POV.pkl')

(flgrslt, unflgrslt) = inforeport('POV.csv')
print('flagged articles\n'+str(flgrslt))
print('unflagged articles\n'+str(unflgrslt))

plt.figure(1)
flgrslt.plot.bar(rot=0, figsize=(8,5))
plt.title('Top words flagged articles')

plt.figure(2)
unflgrslt.plot.bar(rot=0, figsize=(8,5))
plt.title('Top words unflagged articles')
plt.show(block=True)