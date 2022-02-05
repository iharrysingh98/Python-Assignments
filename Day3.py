# question: From a dict, how can we print the Key whose value is maximum ??


Tv = {'Netflix':100, 'AmazonPrime':12, 'Hotstar' : 88}
 
Keymax = max(Tv, key= lambda x: Tv[x])
print(Keymax)