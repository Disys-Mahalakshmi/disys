class phonecontacts:

    def __init__ (self,name,ph_num,email,groups):
        self.name=name
        self.phnum=ph_num
        self.emailid=email
        self.groups=groups

    def phcontacts(self):
        print("phcontacts:")

    def name_verification(self):
        name=input("Enter the username:")
        print("username is:"+name)
        if type(self.name)==str:
            if len(self.name)<= 20:                                                                                #LEN FUNCTION
                print("name verified")
            else:
                raise ValueError("The name should contain only lesser than or equal to 20 letters")
        else:
            raise TypeError("The name should contain letters only")

    def num_verification(self):

       phnum=input("Enter the phone number:")
       print("The Phone number is:"+phnum)
       if (len(phnum)==10) :
           if type(phnum) == int:                                                                            #TYPE VALIDATION
                print("phone-number verified")
       else:
           raise ValueError("The phone-number should not be greater than or lesser than 10")

    def email_verification(self):
        emailid=input("Enter the email id:")
        print("The email id is:"+emailid)
        if type(emailid) == str:
            if len(emailid) <= 30:                                                                              
                print("email_id is verified")
            else:
                raise ValueError("The Email-id should not contain more than 30 values")
        else:
            raise TypeError("Invalid email-id")

maha=phonecontacts("indira",9865003067,"indirasiva26@gmail.com","emergency contacts")
maha.phcontacts()
maha.name_verification()
maha.num_verification()
maha.email_verification()
       
