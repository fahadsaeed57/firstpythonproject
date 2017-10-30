class Overloading:
    def __init__(self,width=0,height=0):
        self.width = width;
        self.height=height

    def __str__(self):
        return "width : {0} Height : {1}".format(self.width,self.height)
    def __add__(self, other):
        width = self.width + other.width
        height= self.height + other.height
        return Overloading(width,height)
    def __sub__(self, other):
        width = self.width - other.width
        height = self.height - other.height
        return Overloading(width, height)
    def __lt__(self, other):
        self_mag = (self.width)+ (self.height)
        other_mag = (other.width) + (other.height)
        return self_mag < other_mag
    def __eq__(self, other):
        self_mag = (self.width) + (self.height)
        other_mag = (other.width) + (other.height)
        return self_mag == other_mag


p1=Overloading(13,12)
p2=Overloading(13,12)

print(p1==p2)
