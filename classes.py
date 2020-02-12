class Person:
  def __init__(self, name, id ,email ,ssn , gender ,phone):
      self.name = name
      self.id = id
      self.email = email
      self.ssn = ssn
      self.gender = gender
      self.phone = phone



  def sigIn(self , name ,email ,ssn , gender ,phone , password):
    print("Hello my name is " + self.name)




  def logIn(self , userName , password):
      print("Hello my name is " + self.name)




  def manege_Account(self):
      print("Hello my name is " + self.name)






class Visitor (Person):


    def __init__(self,name, id ,email ,ssn , gender ,phone ,destination):
        Person.__init__(self,name, id ,email ,ssn , gender ,phone)



    def Rate(self):
        print("Hello my name is " + self.name)




class Owner(Person):


    def __init__(self, name, id, email, ssn, gender, phone, realState , approvedFamily):

        Person.__init__(self, name, id, email, ssn, gender, phone)

#test
object = Owner('mohamed', 12, 'ad@gmail.com', 1123, 'male', '011', 'mozlakan', 'elkalam' )
print(object.email)



class Security_Man (Person):


    def __init__(self,name, id ,email ,ssn , gender ,phone ,ActiveHours):

        Person.__init__(self,name, id ,email ,ssn , gender ,phone)


    def Add_Visitor(self):

        print("Hello my name is " + self.name)


    def Ban_Visitor(self):


        print("Hello my name is " + self.name)




class Request_To_Enter:

    def __init__(self,idOwner,approvalState):

        self.id = idOwner
        self.approval = approvalState
        self.visitorObject = Visitor  # composition with visitor
        ownerObject = Owner  # aggergation with Owner


    def send_Request(self):

        print("Hello my name is " + self.idOwner)

    def Response(self):

        print("Hello my name is " + self.idOwner)




class Path:

    def __init__(self,id,path_List):

        self.id = id
        self.approval = path_List
        self.request_Object = Request_To_Enter  # composition with request
        self.processing_Object= Processing      # composition with Processing


    def Generate_Path(self):

        print("Hello my name is " + self.id)


    def Track(self):

        print("Hello my name is " + self.id)




class Vehicle:

    def __init__(self, namber, id, color, model, qr):

        self.namber = namber
        self.id = id
        self.color = color
        self.model = model
        self.qr = qr
        person_Object = Person        # aggergation with person




class Processing:

    def __init__(self):
        self


    def Check_Path(self):
        print("Hello my name is ")



    def Send_Alert(self):
        print("Hello my name is ")



    def CheckQr(self):
        print("Hello my name is ")



    def Control_Barrier(self):
        print("Hello my name is ")


    Security_Man_Association = Security_Man   #Association with Security_Man




class camera:


    def __init__(self , id , position):

        self.id = id
        self.position = position
        self.processing = Processing



    def Scan(self):
        print('b7bk')
