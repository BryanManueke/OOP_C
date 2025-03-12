#create class
class Car(object):
  #variables
  car_color ='red';
  car_brand ='toyota';

  #method 1
  def carInfo(self):
    print('car color is {0}'.format(self.car_color));
    print('car brand is {0}'.format(self.car_brand));

  #method 2
  def carPark(self):
    print('Car park so to fast.')
    return 'Return car park.!!!';

  #method 3
  def carSpeed(self):
    print('Car speed so to fast.')
    return 'Return car speed.!!!';

  #main method
  def main(self):
    print('this is main function of class.')

    #call function
    self.carInfo();
    self.carPark();
    self.carSpeed();

if __name__ == '__main__':
    #create object of class
    obj_car = Car();
    obj_car.main();
    print(obj_car.car_color);
    print(obj_car.car_brand);
    print('{0}'.format(obj_car.carPark()));
    print('{0}'.format(obj_car.carSpeed()));

