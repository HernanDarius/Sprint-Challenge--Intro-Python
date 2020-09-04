import unittest
from oop1 import *

class Oop1Tests(unittest.TestCase):
  def setUp(self):
    self.vehicle = Vehicle('vehicle', 'yes')
    self.flight_vehicle = FlightVehicle('vehicle', 'yes', 'flys')
    self.ground_vehicle = GroundVehicle('vehicle', 'yes', 'drives')
    self.car = Car('vehicle', 'yes', 'drives', 4)
    self.motorcycle = Motorcycle('vehicle', 'yes', 'drives', 2)
    self.starship = Starship('vehicle', 'yes', 'flys', 'Space')
    self.airplane = Airplane('vehicle', 'yes', 'flys', 'Sky')

  def test_flight_vehicle(self):
    self.assertTrue(isinstance(self.flight_vehicle, FlightVehicle))
    self.assertTrue(isinstance(self.flight_vehicle, Vehicle))

  def test_ground_vehicle(self):
    self.assertTrue(isinstance(self.ground_vehicle, GroundVehicle))
    self.assertTrue(isinstance(self.ground_vehicle, Vehicle))

  def test_starship(self):
    self.assertTrue(isinstance(self.starship, Starship))
    self.assertTrue(isinstance(self.starship, FlightVehicle))
    self.assertTrue(isinstance(self.starship, Vehicle))

  def test_airplane(self):
    self.assertTrue(isinstance(self.airplane, Airplane))
    self.assertTrue(isinstance(self.airplane, FlightVehicle))
    self.assertTrue(isinstance(self.starship, Vehicle))

  def test_car(self):
    self.assertTrue(isinstance(self.car, Car))
    self.assertTrue(isinstance(self.car, GroundVehicle))
    self.assertTrue(isinstance(self.car, Vehicle)) 

  def test_motocycle(self):
    self.assertTrue(isinstance(self.motorcycle, Motorcycle))
    self.assertTrue(isinstance(self.motorcycle, GroundVehicle))
    self.assertTrue(isinstance(self.motorcycle, Vehicle)) 


if __name__ == '__main__':
  unittest.main()