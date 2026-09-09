##Defining the class boda and a constant variable business
class boda:
    business = "Safety First Boda Boda"
    def __init__(self, name, address, license_no):
        self.name = name
        self.address = address
        self.license_number = license_no
    def display_info(self):
        print(f"Business Name: {self.business}")
        print(f"Driver Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"License Number: {self.license_number}")


##Renewing boda license for a specific period of time
    def renew_license(self, amount, period, license_no):
        self.amount = amount
        self.period =period
        self.license_number = license_no
    def calculate_renewal_fee(self):
        if self.period == "1 year":
            fee = self.amount * 1
        elif self.period == "2 years":
            fee = self.amount * 2
        elif self.period == "3 years":
            fee = self.amount * 3
        else:
            fee = 0
        return fee
    def display_renewal_fee(self):
        fee = self.calculate_renewal_fee()
        print(f"{self.license_number} has renewed his license at a fee of {fee}UGX for {self.period}.")


##Calculation of boda fare based of certain parameters
    def calculate_fare(self, distance, time, jam, weather, number_of_persons):
        base_fare = 1000
        distance = distance * 100 #Distance in meters
        time = time * 60 #Time in seconds
        jam = base_fare * 0.5 if jam else 0
        weather = base_fare * 0.2 if weather == "rainy" else 0
        number_of_persons = number_of_persons * 200
        total_fare = base_fare + distance + time + jam + weather + number_of_persons
        return total_fare
    def display_fare(self, distance, time, jam, weather, number_of_persons):
        fare = self.calculate_fare(distance, time, jam, weather, number_of_persons)
        print(f"Total Fare: {fare}UGX")

##Update boda location  
    def update_location(self, new_address):
        self.address = new_address
    def display_location(self):
        print(f"Current Location: {self.address}")

##Number of trips completed by the boda driver
    def __init__(self, name, address, license_no, trips_completed=0):
        self.name = name
        self.address = address
        self.license_number = license_no
        self.trips_completed = trips_completed
    def increment_trips(self):
        self.trips_completed += 1
    def display_trips(self):
        print(f"Total Trips Completed: {self.trips_completed}")

##Cancel a trip and update the number of trips completed
    def cancel_trip(self):
        if self.trips_completed > 0:
            self.trips_completed -= 1
            print("Trip cancelled successfully.")
        else:
            print("No trips to cancel.")
    def display_cancelled_trips(self):
        print(f"Total Trips Cancelled: {self.trips_completed}")

##Boda Objects
##Boda Information
boda1 = boda("Alex Ogwang", "Mukono", "UA 1714")
boda2 = boda("Mark Richard", "Entebbe", "UA 1217")
boda3 = boda("John Philip", "Seeta", "UA 1321")
boda1 = boda1.display_info()
boda2 = boda2.display_info()
boda3 = boda3.display_info()

##License Renewal
license1 = boda.renew_license(50000, "2 years", "UA 1714")
license2 = boda.renew_license(50000, "1 year", "UA 1217")
license3 = boda.renew_license(50000, "3 years", "UA 1321")
license1 = license1.display_renewal_fee()
license2 = license2.display_renewal_fee()
license3 = license3.display_renewal_fee()