"""
Parking Lot Challenge:

Create a parking lot class that takes in a square footage size as input and creates an array of empty values based on the input square footage size. Assume every parking spot is 8x12 (96 ft2) for this program, but have the algorithm that calculates the array size be able to account for different parking spot sizes. For example, a parking lot of size 2000ft2 can fit 20 cars, but if the parking spots were 10x12 (120 ft2), it could only fit 16 cars. The size of the array will determine how many cars can fit in the parking lot.
Create a car class that takes in a 7 digit license plate and sets it as a property. The car will have 2 methods:

1.A magic method to output the license plate when converting the class instance to a string.
2.A "park" method that will take a parking lot and spot # as input and fill in the selected spot in the parking lot. If another car is parked in that spot, return a status indicating the car was not parked successfully. If no car is parked in that spot, return a status indicating the car was successfully parked.

Have a main method take an array of cars with random license plates and have them park in a random spot in the parking lot array until the input array is empty or the parking lot is full. If a car tries to park in an occupied spot, have it try to park in a different spot instead until it successfully parks. Once the parking lot is full, exit the program.
Output when a car does or does not park successfully to the terminal (Ex. "Car with license plate [LICENSE_PLATE] parked successfully in spot [SPOT #]").
OPTIONAL/BONUS - Create a method for the parking lot class that maps vehicles to parked spots in a JSON object. Call this method at the end of the program, save the object to a file, and upload the file to an input S3 bucket.
"""

import json
import random

import boto3
from botocore.exceptions import NoCredentialsError


def upload_to_s3(file_name, bucket_name, object_name=None):
    s3_client = boto3.client("s3")
    try:
        s3_client.upload_file(file_name, bucket_name, object_name or file_name)
        print(
            f"File {file_name} uploaded to bucket {bucket_name} as {object_name or file_name}"
        )
    except FileNotFoundError:
        print(f"The file {file_name} was not found")
    except NoCredentialsError:
        print("Credentials not available")


class ParkingLot:
    def __init__(self, square_footage, spot_length, spot_width):
        self.spot_size = spot_length * spot_width
        self.capacity = square_footage // self.spot_size
        self.parking_spots = [None] * self.capacity

        print(f"Each parking spot size: {self.spot_size} ft²")
        print(f"Total Car parking spots available: {self.capacity}")
        print(f"Total square footage available for parking: {square_footage} ft²\n")

    def park_car(self, car, spot_number):
        if self.parking_spots[spot_number] is None:
            self.parking_spots[spot_number] = car
            return True
        else:
            return False

    def find_spot(self, car):
        attempted_spots = set()
        while len(attempted_spots) < self.capacity:
            spot_number = random.randint(0, self.capacity - 1)
            if spot_number not in attempted_spots:
                attempted_spots.add(spot_number)
                result = self.park_car(car, spot_number)
                if result:
                    print(
                        f"Car with license plate {car} parked successfully in spot {spot_number}."
                    )
                    return result
                else:
                    print(f"\tSpot {spot_number} is already occupied.")
        return f"Failed to park the car-{car} no spots available."

    def export_to_json(self):
        parking_map = {
            index: (car.license_plate if car else None)
            for index, car in enumerate(self.parking_spots)
        }
        with open("parking_lot.json", "w") as file:
            json.dump(parking_map, file)


class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return self.license_plate

    def park(self, parking_lot):
        return parking_lot.find_spot(self)


if __name__ == "__main__":
    try:
        square_footage = int(
            input("Enter Total square footage available for parking in ft²:")
        )
        spot_length = int(input("Enter spot length:"))
        spot_width = int(input("Enter spot width:"))

        cars_park = int(input("How many cars you want to park:"))
        if square_footage > 0 and spot_length > 0 and spot_width > 0 and cars_park > 0:
            lot = ParkingLot(square_footage, spot_length, spot_width)
            cars = [
                Car(f"{random.randint(1000000, 9999999)}") for _ in range(cars_park)
            ]

            for car in cars:
                car.park(lot)

            file_name = lot.export_to_json()

            # bucket_name = "s3-bucket-name"
            # upload_to_s3(file_name, bucket_name)
        else:
            print("Please enter value greater then '0'")
    except:
        print("enter valid inputs.")
