# Parking Lot Challenge

## Overview
The Parking Lot Challenge is a programming simulation that involves creating a `ParkingLot` class to manage parking spaces based on the square footage provided. Each parking spot is typically 8x12 feet (96 sq ft), but the program is designed to accommodate different sizes. This application demonstrates how to dynamically calculate and manage parking within a given area.

## Features

### ParkingLot Class
- **Initialization**: Takes in the total square footage as input.
- **Dynamic Spot Calculation**: Generates an array of parking spots based on the specified spot dimensions. For instance, a 2000 sq ft lot can fit 20 cars in standard spots but only 16 cars if spots are 10x12 ft.
- **Parking Management**: Provides methods to check spot availability and park cars.

### Car Class
- **License Plate Property**: Each car instance carries a unique 7-digit license plate number.
- **Methods**:
  1. **Magic Method**: Custom string representation that returns the car's license plate.
  2. **Park Method**: Takes a `ParkingLot` and a spot number to attempt parking. It returns success or failure based on spot availability.

### Simulation
- **Main Execution**: Initializes an array of `Car` objects with random license plates and attempts to park them in the `ParkingLot` at random but valid spots until all spots are filled or no more cars are left to park. Cars will attempt different spots if initially unsuccessful.
- **Output**: The program outputs the parking status of each car to the terminal, indicating whether the parking attempt was successful or not.

### Optional Features
- **JSON Mapping**: An additional method in the `ParkingLot` class to map parked cars to their spots in a JSON format. This can be saved to a file and uploaded to an S3 bucket for further processing or storage.

## Video Demo
Watch the demo of the Parking Lot Challenge in action [here](demo.webm); Output [logs](output).

## Usage
To run the simulation:
1. Initialize the parking lot with a specified square footage.
2. Create car objects.
3. Execute the parking process until the lot is full or no cars remain.

This challenge provides practical insights into object-oriented programming, focusing on dynamic data structure handling, class interactions, and basic file operations with optional cloud integration.