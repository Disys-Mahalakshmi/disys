
import json



Hotels = [1,2,3,4,5,6]
data=['''{"Hotels":"Sree Annapoorna","Type":"Veg","Food Recommended":"Idly(2 Nos)","Price":"Rs.42","Starters1":"Paneer Manchuriyan","st_Price1":"168","Starters2":"Veg Ball Manchurian","st_Price2":"168","Starters3":"Crispy Vegetables","st_Price3":"150","Ratings":"4.5"}''',
            '''{"Hotels":"Tiffin House","Type":"Veg","Food Recommended":"Butter Masala Appam","Price":"Rs.80","Starters1":"Kadai Panner","st_Price1":"90","Starters2":"Veg Kola","st_Price2":"110","Starters3":"sundal gravey","st_Price3":"130","Ratings":"4.1"}''',
     '''{"Hotels":"Shree Anandhaas","Type":"Veg","Food Recommended":"Poori(3 Nos)","Price":"Rs.74","Starters1":"Gobi Masala","st_Price1":"90","Starters2":"Kadai Veg","st_Price2":"90","Starters3":"Panner Tikka","st_Price3":"110","Ratings":"4.2"}''',
        '''{"Hotels":"Cock Ra Co","Type":"Non Veg","Food Recommended":"Chicken Fried Rice","Price":"Rs.230","Starters1":"Tandoori Chicken-Half","st_Price1":"194","Starters2":"Kalakki","st_Price2":"45","Starters3":"Tangdi Kabab","st_Price3":"70","Ratings":"4"}''',
      '''{"Hotels":"HMR","Type":"Non Veg","Food Recommended":"Chicken Biriyani","Price":"Rs.160","Starters1":"Chilli Chicken","st_Price1":"80","Starters2":"Pepper Chicken Boneless","st_Price2":"120","Starters3":"Pepper Mutton","st_Price3":"180","Ratings":"4"}''',
      '''{"Hotels":"Thalassery","Type":"Non Veg","Food Recommended":"Thalassery Chicken Dum Biriyani","Price":"Rs.185","Starters1":"Kasturi Kabab","st_Price1":"165","Starters2":"Fish Tikkka","st_Price2":"210","Starters3":"Mutton Mughalai","st_Price3":"220","Ratings":"3.1"}''']




Menu=['Veg Foods','Non Veg Foods']

def get_order():
       print("Veg Foods","\nNon Veg Foods")
       print('\n')
def list_hotels(get_order):
       order = input("")
       if Menu[0] == order: 
               print(loaded.loc[loaded['Type'] == 'Veg', 'Hotels'])
       elif Menu[1]== order:
               print(loaded.loc[loaded['Type'] == 'Non Veg', 'Hotels'])
       else:
               print("Sorry! We not have it")

def food_recommended(list_hotels):
    user =input("")
    for i in loaded['Hotels']:
        if i == user:
            print(loaded.loc[loaded['Hotels'] == 'Sree Annapoorna','Food Recommended'])
            print(loaded.loc[loaded['Hotels'] == 'Sree Annapoorna','Price'])
            print(loaded.loc[loaded['Hotels'] == 'Sree Annapoorna','Ratings'])
            break
        elif i == user:
            print(loaded.loc[loaded['Hotels'] == 'Tiffin House','Food Recommended'])
            print(loaded.loc[loaded['Hotels'] == 'Tiffin House','Price'])
            print(loaded.loc[loaded['Hotels'] == 'Tiffin House','Ratings'])
            break
        elif i == user:
            print(loaded.loc[loaded['Hotels'] == 'Shree Anandhaas','Food Recommended'])
            print(loaded.loc[loaded['Hotels'] == 'Shree Anandhaas','Price'])
            print(loaded.loc[loaded['Hotels'] == 'Shree Anandhaas','Ratings'])
            break
        elif i == user:
            print(loaded.loc[loaded['Hotels'] == 'Cock Ra Co','Food Recommended'])
            print(loaded.loc[loaded['Hotels'] == 'Cock Ra Co','Price'])
            print(loaded.loc[loaded['Hotels'] == 'Cock Ra Co','Ratings'])
            break
        elif i == user:
            print(loaded.loc[loaded['Hotels'] == 'Thalassery','Food Recommended'])
            print(loaded.loc[loaded['Hotels'] == 'Thalaseery','Price'])
            print(loaded.loc[loaded['Hotels'] == 'Thalaseery','Ratings'])
            break
        elif i == user:
            print(loaded.loc[loaded['Hotels'] == 'HMR','Food Recommended'])
            print(loaded.loc[loaded['Hotels'] == 'HMR','Price'])
            print(loaded.loc[loaded['Hotels'] == 'HMR','Ratings'])
            break
        else:
            print(loaded.loc[loaded['Hotels'] == 'Bhurma Bhai Hotel','Food Recommended'])
            print(loaded.loc[loaded['Hotels'] == 'Bhurma Bhai Hotel','Price'])
            print(loaded.loc[loaded['Hotels'] == 'Bhurma Bhai Hotel','Ratings'])
            break

get_order()
list_hotels(get_order)
food_recommended(list_hotels)
