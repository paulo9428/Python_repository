class Test:                         
	def test(self):
		print("Puppy's test")
		self.__q()

	def __q(self):
		print("qqqqqqqqqqqq")

test = Test()

# error
test.__q() 

# 캡슐화된 메소드는 클래스 내에서만 사용가는