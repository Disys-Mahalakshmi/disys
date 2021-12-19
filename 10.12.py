

'''approach 1'''
name="maha"

'''approach 2'''

class friday:
    
      __work="python"
      
      def __init__(self):
          self.__tea=3
          
      def display(self):
          print(self.__tea)

          
maha=friday()
maha.display()


'''approach 3'''

saturday=("sleep","eat","repaet")

print(saturday[2])


'''approach 4'''

sunday={"morning":"playing","afternoon":"briyani","evening":"movie","night":"worried"}
 
print(sunday["evening"])


'''approach 5'''



for i in saturday :

    print(i)

for i in sunday.values():

    print(i)

for i in sunday.keys():
    print(i)


'''approach 6'''


students=[{"id":23,"name":"maha","branch":"b.com"},{"id":24,"name":"karthi","branch":"bsc"},{"id":25,"name":"bathraa","branch":"b.com"}]

print (students[1],students[2])


for i in students:
    if i["name"]=="maha":
        print("maha is available")
    elif i["branch"]=="b.com":
        print("b.com")

    if i["name"]=="karthi":
        print("karthi is available")
    if i["branch"]=="bsc":
        print("bsc")

    if i["name"]=="praveen":
       print("praveen is available")
    elif i["branch"]=="ece":
        print("ece")


'''approach 7'''


organisation=[{"internship":[{"id":80,"name":"praveen","dept":"it","reprting":"ak"},{"id":81,"name":"ramesh","dept":"it","reprting":"ak"}]},
 {"fulltimejob":[{"id":70,"name":"gopi","dept":"cloud","reprting":"arthi"},{"id":71,"name":"bala","dept":"cloud","reprting":"arthi"}]},
 {"contractjob":[{"id":101,"name":"sneha","dept":"finance","reprting":"nirmal"},{"id":102,"name":"surya","dept":"finance","reprting":"nirmal"}]}]

'''
for i in organisation:
	print(i)
'''

for i in organisation:
    for j in i.values():
        for k in j:
            print(k)


'''
for i in organisation:
    if i["internship"][0]["id"]=="80":
        print("id exist")
    if i["fulltimejob"][0]["id"]=="71":
        print("fulltime id exist")
    if i["contractjob"][0]["id"]=="102":
        print("contractjob exist")

for i in organisation:
    for j in i.values():
        for k in j:
            print(k)
'''


events=[{"alien sarees": [{"silsarees":["A1","A2"]}]}]


for shopping in events:
    print(shopping)
    for i,v in shopping.items():
        print(i,v)
        if "silksarees" in v[0]:
            print("found it", v[0]["silksarees"])


class disys:
    def __init__(self,vacc):
        self.vac=[]
        self.vac.append(vacc)
        self.count=0
    def logic(self):
        for i in self.vac:
            if i["vacine"] == None:
                self.count=self.count+1
            else:
                continue
            
        print(self.vac)
    def __del__(self):
         print("de allocation")
         del self.vac
         del self.count

jb=disys({"name":"jamesbond","id":"007","vacine":None})
jv=disys({"name":"jayavaradhan","id":"008","vacine":"1stdose"})
jv.logic()
del jb

def ret(obj:str):
        obj1=input("enter a value")
        print(obj,obj1)
        return obj1

ref=ret(2)


import collections

dictob=collections.OrderedDict()

dictob.clear()

c=collections.Counter()












    

    






          

 
