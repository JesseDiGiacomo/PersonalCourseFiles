class Parent ():
    def __init__(self, last_name, eye_color):
        print ("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print ("Last name: "+self.last_name)
        print ("Eye color: "+self.eye_color)
        

class Child (Parent):   #inheritance
    def __init__(self, last_name, eye_color, numbers_of_toys):
        print ("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.numbers_of_toys = numbers_of_toys

    def show_info(self):    #method overwriting
        print ("Last name: "+self.last_name)
        print ("Eye color: "+self.eye_color)
        print ("Numbers of toys: "+str(self.numbers_of_toys))   #str para converter o numero em string para que possa ser exibido.

billy_cyrus = Parent ("Cyrus", "blue")
billy_cyrus.show_info ()
        
miley_cyrus = Child ("Cyrus", "Blue", 5)
miley_cyrus.show_info()
