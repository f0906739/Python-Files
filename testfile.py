from random import randint


def log(func):
    def wrapper(*args):
        print(func.__name__, args)
        return func(*args)

    return wrapper


class CarChoices():
    default_colors = ['red', 'green', 'blue', 'pink', 'white']
    default_makers = ['honda', 'toyota', 'chevrolet', 'porsche', 'tesla']
    default_car_types = ['suv', 'van', 'truck']

    def __init__(self,
                 colors=default_colors,
                 makers=default_makers,
                 car_types=default_car_types):
        self.colors = colors
        self.makers = makers
        self.car_types = car_types


class Car():
    def __init__(self, color, make, car_type):
        self.color = color
        self.make = make
        self.car_type = car_type

        self.is_bidded = False
        # stores current 'Bidders' object v
        self.top_bidder = None
        self.top_offer = 0

    def __repr__(self):
        return f"Color: {self.color}\nMake: {self.make}\nType: {self.car_type}\nIs bidded for: {self.is_bidded}\nTop Bidder: {self.top_bidder.name}\nTop Offer: ${self.top_offer}"


class Shop:
    choices = CarChoices()
    cars = {}
    bidders = []

    @log
    def append_multiple_cars(self, num):
        if self.cars == {}:
            for parking_num, car in enumerate(self.generate_cars(
                    self.choices, num),
                                              start=1):
                self.cars[parking_num] = car
        else:
            # below may be unnecessary but may prevent cases where the dictionary keys are out of order.
            highest_park_num = sorted(list(self.cars.keys()))[-1]
            for parking_num, car in enumerate(self.generate_cars(
                    self.choices, num),
                                              start=highest_park_num + 1):
                self.cars[parking_num] = car

    @staticmethod
    def get_data(car_objects):
        for car in car_objects:
            yield f"Color: {car.color} Maker: {car.make} Car_Type: {car.car_type}"

    def append_bidder(self, name):
        self.bidders.append(name)

    @classmethod
    def generate_cars(cls, CarChoices_object, num):
        for _ in range(num):
            color = cls.choices.colors[randint(0, len(cls.choices.colors) - 1)]
            make = cls.choices.makers[randint(0, len(cls.choices.makers) - 1)]
            car_type = cls.choices.car_types[randint(
                0,
                len(cls.choices.car_types) - 1)]
            yield Car(color, make, car_type)

    @classmethod
    def append_single_car(cls, self, color, make, car_type):
        car = Car(color, make, car_type)
        after_last_index = len(self.cars) + 1

        self.cars[after_last_index] = car


# only sells small cars with bright colors (no trucks). Anti-honda.
class CarNova(Shop):
    car = CarChoices(colors=['red', 'green', 'pink', 'white'],
                     car_types=['suv', 'van'],
                     makers=['toyota', 'chevrolet', 'porsche', 'tesla'])


# only sells porsches (i don't think they sell trucks)
class PorscheDealer(Shop):
    car = CarChoices(makers=['porsche'], car_types=['suv', 'van'])


# only sells non-hip cars (no teslas or porsches)
class Oldies(Shop):
    car = CarChoices(makers=['honda', 'toyota', 'chevrolet'])


class Bidders():
    def __init__(self, name, shop, color, make, car_type, offer):
        self.name = name
        self.shop = shop
        self.color = color
        self.make = make
        self.car_type = car_type
        self.offer = offer

        self.matched_car_spotted = False
        self.bidded_car = None
        self.bidded_matched_spots = []
        self.is_out = False

    @log
    def enter_shop(self):
        self.shop.append_bidder(self.shop, self.name)
        self.is_out = False

    @log
    def leave_shop(self):
        self.shop.bidders.remove(self.name)
        self.is_out = True

    def scan_cars(self):
        for parking_num, car in self.shop.cars.items():
            color_matches = car.color == self.color
            make_matches = car.make == self.make
            car_type_matches = car.car_type == self.car_type

            if color_matches and make_matches and car_type_matches:
                self.matched_car_spotted = True
                if car.is_bidded:
                    self.bidded_matched_spots.append(parking_num)
                    print('CAR TAKEN already')
                else:
                    print("FOUND IT!!")
                    self.take_car(parking_num)
                    break

            else:
                print("car is NOT FOUND IN THIS PARKING SPACE")

        if self.matched_car_spotted is False:
            self.is_out = True
            print("BIDDER IS OUT!!!")

    def fight_bid(self):
        # may need more if statements, this might be buggy currently.
        if self.is_out is False:
            if self.matched_car_spotted is True and self.bidded_car is None:
                for parking_num in self.bidded_matched_spots.copy():
                    car = self.shop.cars[parking_num]
                    if self.offer > car.top_offer:
                        print(
                            f"Your ({self.name}) offer {self.offer} is more than current top bidder, who is: {car.top_bidder.name} who has an offer of {car.top_offer}"
                        )
                        self.take_car(parking_num)
                    else:
                        self.offer = int(
                            input(
                                f"Your offer is too low, change it to be higher than ${car.top_offer}: "
                            ))
                        self.ask_to_bid()
                        return self.fight_bid()

    def check_if_current_bid(self):
        if self.offer < self.bidded_car.top_offer:
            self.bidded_car = None

    def take_car(self, parking_num):
        car = self.shop.cars[parking_num]

        self.bidded_matched_spots.append(parking_num)
        if car.top_bidder is not None:
            car.top_bidder.bidded_car = None

        car.is_bidded = True
        car.top_bidder = self
        car.top_offer = self.offer
        self.bidded_car = car

    # I made this because if the bidder doesn't see any available cars, he may not want to try for already bidded cars.
    def ask_to_bid(self):
        selection = ""
        while selection not in ('y', 'n'):
            selection = str(
                input("Do you want to bid for the car? ('y' or 'n')"))

        if selection == 'n':
            self.is_out = True


# different car results in same shops. Shouldn't be random for same shop.
# firstShop = CarNova
# #100 is placeholder
# firstShop.append_multiple_cars(firstShop, 100)
# # for car in firstShop.cars:
# #     print(car.color, car.make, car.car_type)
# for car in firstShop.cars.values():
#     print(car.color, car.make, car.car_type)
# firstShop.append_single_car(firstShop, "red", "honda", "truck")

# print("MICKEY------------------------------------------------------")
# Mickey = Bidders("Mickey", firstShop, "red", "porsche", "suv", 500)
# Mickey.enter_shop()
# Mickey.scan_cars()
# print('MINNIE------------------------------------------------------')
# Minnie = Bidders("Minnie", firstShop, "red", "porsche", "suv", 600)
# Minnie.enter_shop()
# Minnie.scan_cars()
# print("Minnie's car:", Minnie.bidded_car.__repr__())
# Minnie.fight_bid()
# print("Minnie's car:", Minnie.bidded_car.__repr__())
# print("Mickey's car:", Minnie.bidded_car.__repr__())
# # Mickey.offer = 700
# Mickey.fight_bid()
# print("Minnie's car after Mickey fights back:", Minnie.bidded_car.__repr__())
# print("Mickey's car after Mickey fights back:", Mickey.bidded_car.__repr__())
