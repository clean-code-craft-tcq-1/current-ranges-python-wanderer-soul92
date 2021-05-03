import unittest
import bms_monitor

class test_battery_ranges(unittest.TestCase):
  def test_to_check_empty_input_pass(self):
    self.assertTrue(bms_monitor.check_bms_range_input([]) == "Invalid Input")
    
  def test_passing_given_ranges(self):
    self.assertTrue(bms_monitor.check_bms_range_input([3, 3, 5, 4, 10, 11, 12]) == "Valid Input") 
    
   

  def test_failing_given_ranges(self):
    self.assertTrue(bms_monitor.check_bms_range_input([3,4,7,6,7,8]) == "Valid Input")    #no continuous range,should give invalid
    

if __name__ == '__main__':
  unittest.main()