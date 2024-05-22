class NumberTooSmall(Exception) :
  def init (self, num) :
     self.num = num
  def get_details(self) :
   return {'Number too small' : self.num}
class NumberTooBig(Exception) :
  def init (self, num) :
   self.num = num
  def get_details(self) :
   return {'Number too big' : self.num}
class Numbers :
  def init (self) :
   self.dct = { }
  def append(self, num, cube ) :
   self.dct[num] = cube
  def display(self) :
   for k, v in self.dct.items( ) :
     print(k, v)
   print( )
n = Numbers( )
print('Enter 10 numbers between 3 to 30 :')
try :
  for x in range(10) :
   num = int(input( ))
   if num > 30 :
     raise NumberTooBig(num)
   elif num < 3 :
      raise NumberTooSmall(num)
   else :
      cube = num * num *num
      n.append(num, cube)
except NumberTooBig as ntb :
   print(ntb.get_details( ))
except NumberTooSmall as nts :
   print(nts.get_details( ))
finally :
   n.display( )
