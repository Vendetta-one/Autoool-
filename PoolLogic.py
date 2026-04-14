class RidePool:
    def __init__(self, base_fare, max_capacity=4):
        self.base_fare = base_fare
        self.max_capacity = max_capacity
        self.passengers = []

    def add_passenger(self, student_name):
        """Adds a student to the ride if there is space."""
        if len(self.passengers) < self.max_capacity:
            self.passengers.append(student_name)
            print(f"✅ {student_name} added to the ride.")
            return True
        else:
            print("❌ Auto is full! Capacity reached.")
            return False

    def calculate_split_fare(self):
        """Calculates how much each student owes."""
        num_passengers = len(self.passengers)
        if num_passengers == 0:
            return 0
        
        # Simple split logic: base fare divided by current occupants
        fare_per_person = self.base_fare / num_passengers
        return round(fare_per_person, 2)

    def get_ride_status(self):
        """Returns the current state of the ride."""
        return {
            "current_passengers": self.passengers,
            "count": len(self.passengers),
            "fare_per_person": self.calculate_split_fare(),
            "remaining_seats": self.max_capacity - len(self.passengers)
        }

# Example Usage:
# Suppose the auto ride from JUIT to the Station is 180 units.
juit_ride = RidePool(base_fare=180)

juit_ride.add_passenger("Rahul")
juit_ride.add_passenger("Sneha")

status = juit_ride.get_ride_status()
print(f"Current Fare: {status['fare_per_person']} per person.")
