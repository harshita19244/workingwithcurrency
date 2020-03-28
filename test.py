import unittest
from a1 import changeBase

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
	
	def test_change_base(self):
		
		# these are just sample values. You have to add testcases (and edit these) for various dates.
		# (don't use the current date as the json would keep changing every 4 minutes)
		# you have to hard-code the 2nd parameter of assertEquals by calculating it manually
		# on a particular date and checking whether your changeBase function returns the same
		# value or not.

		self.assertTrue(changeBase(240,"CAD","CAD","2010-10-25")==240.00000000000003)
		self.assertEquals(changeBase(100,"INR","USD","2018-08-13"),1.4282225186465516)
		self.assertAlmostEqual(changeBase(10,"KRW","EUR","2016-08-03"),12513.40,delta=0.1)
		self.assertAlmostEqual(changeBase(1, "SGD" , "HKD" , "2017-07-08" ), 5.656 , delta = 0.01)
		self.assertAlmostEqual(changeBase(1, "USD" , "AUD" , "2010-08-10" ), 1.102 , delta = 0.01)
		self.assertAlmostEqual(changeBase(1, "USD" , "CAD" , "2006-07-10" ), 1.124 , delta = 0.01)
		self.assertEquals(changeBase(120,"EUR","EUR","2000-10-26"),120.0)
		self.assertFalse(changeBase(140,"DKK","TRY","2013-08-19")==69.078)
		self.assertAlmostEqual(changeBase(100,"CAD","EUR","2003-06-26"),154.7,delta=0.05)
		self.assertAlmostEquals(changeBase(150,"EUR","PLN","2006-06-06"),37.895055958365965)



		print("DONE")


if __name__=='__main__':
	unittest.main()