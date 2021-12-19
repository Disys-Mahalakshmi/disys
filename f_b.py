

Facebook=[{"groupfriends":[{"name":"maha","fbid":"mahamajeo2","grpname":"dosthana","grpcount":10},{"name":"sara","fbid":"sara_irish","grpname":"dosthana","grpcount":10},{"name":"vishnupriya","fbid":"vishnu_jumoer27","grpname":"dosthana","grpcount":10},{"name":"sowmiya","fbid":"meow_so01","grpname":"dosthana","grpcount":10},{"name":"udhaya","fbid":"udhu_love00","grpname":"dosthana","grpcount":10},{"name":"yesudas","fbid":"d_lover_20","grpname":"dosthana","grpcount":10},{"name":"rajesh","fbid":"Raju_Ias05","grpname":"dosthana","grpcount":10},{"name":"boopalan","fbid":"boo_jesus_child17","grpname":"dosthana","grpcount":10},{"name":"sathish","fbid":"satz_rs200","grpname":"dosthana","grpcount":10},{"name":"prejesh","fbid":"k_chocolate_boy_official_","grpname":"dosthana","grpcount":10}]},
           {"commonfriends":[{"name":"kavi","friendof":"aadhi","relation":"sister","no_of_mutualfrnds":10},{"name":"naveen","friendof":"jayanthi","relation":"brother","no_of_mutualfrnds":14},{"name":"priya","friendof":"sara","relation":"friend","no_of_mutualfrnds":2},{"name":"vishwa","friendof":"vishnu","relation":"friends","no_of_mutualfrnds":7},{"name":"sivan","friendof":"melkis","relation":"friend","no_of_mutualfrnds":11},{"name":"leena","friendof":"riyaz","relation":"friend","no_of_mutualfrnds":4},{"name":"balaji","friendof":"sara","relation":"closefriend","no_of_mutualfrnds":11},{"name":"sakthi","friendof":"arunpriya","relation":"brother","no_of_mutualfrnds":10},{"name":"thilak","friendof":"shalini","relation":"brother","no_of_mutualfrnds":12},{"name":"mathan","friendof":"jayanthi","relation":"friend","no_of_mutualfrnds":15}]}]


#list & dict

for i in Facebook:
    #print(i)
    print(i["groupfriends"][0]['grpname'])

    for j in i:
        print(j)
       
  
    if i["groupfriends"][0]["name"]=="maha":
        print("name exist")
    if i["commonfriends"][0]["name"]=="kavi":
        print("name exist")
    

for i in Facebook:
    for j,k in i.values():
        for k in j:
            print(j,k)

#validation syntax

for i in Facebook:
    if isinstance("name",str):
        continue
    else:
        raise TypeError("InvalidName")

    if isinstance("Groupcount",int):
        continue
    else:
        raise TypeError ("InvalidNumber")
    for j,k in i.items():
        print(j,k)
