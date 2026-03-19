The Scenario: "SwiftRide" Platform
You are building the backend for a new ride-sharing app. You need to manage different types of users, a fleet of diverse vehicles, and a system to calculate fares dynamically.

1. The Architecture (Your Blueprints)
You need to design a system that handles the following components using OOP principles:

Users: Every user has a name, email, and rating. However, Drivers have a license_number and earnings, while Passengers have a preferred_payment_method.

Vehicles: There are different tiers: Economy, Luxury, and Electric.

Rides: A ride connects a Passenger, a Driver, and a Vehicle, and calculates the final cost based on distance.

2. The Requirements (Your Tasks)
Task A: Inheritance & Encapsulation
Create a base User class. Then, create Driver and Passenger classes that inherit from it.

Challenge: Make the driver’s earnings attribute private (e.g., __earnings). Create a method add_earnings(amount) to update it, ensuring no one can accidentally overwrite their bank balance.

Task B: Polymorphism in Fares
Each vehicle type charges differently per mile.

Economy: $1.00/mile.

Luxury: $3.00/mile + a $5.00 "Luxury Fee."

Electric: $1.20/mile (but gives a $2.00 "Green Discount" on the total).

Challenge: Create a calculate_fare(distance) method in each vehicle class. Use Polymorphism so that the Ride class can call .calculate_fare() without needing to know which type of car it is.

Task C: Composition
Create a Ride class. Instead of just using strings, the Ride object should take a Passenger object, a Driver object, and a Vehicle object as arguments.

Challenge: Create a start_ride() method that prints: "Driver [Name] is picking up [Passenger Name] in a [Vehicle Type]."