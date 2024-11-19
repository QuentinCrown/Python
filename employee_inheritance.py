# employee class
class Employee:
    def __init__(self, name, number):
        self._name = name
        self._number = number

    # name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # number
    def get_number(self):
        return self._number

    def set_number(self, number):
        self._number = number


# subclass
class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)  # Call parent class constructor
        self._shift_number = shift_number
        self._hourly_pay_rate = hourly_pay_rate

    # shift number
    def get_shift_number(self):
        return self._shift_number

    def set_shift_number(self, shift_number):
        self._shift_number = shift_number

    # hourly rate
    def get_hourly_pay_rate(self):
        return self._hourly_pay_rate

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self._hourly_pay_rate = hourly_pay_rate


# test time
def main():
    # worker details
    name = input("Enter the employee's name: ")
    number = input("Enter the employee's number: ")
    
    while True:
        try:
            shift_number = int(input("Enter the shift number (1 for day, 2 for night): "))
            if shift_number not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Shift number must be 1 (day) or 2 (night).")

    while True:
        try:
            hourly_pay_rate = float(input("Enter the hourly pay rate: "))
            if hourly_pay_rate < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Hourly pay rate must be a positive number.")

    # worker instance
    worker = ProductionWorker(name, number, shift_number, hourly_pay_rate)

    # details with objects
    print("\n--- Employee Details ---")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_number()}")
    print(f"Shift Number: {worker.get_shift_number()} ({'Day' if worker.get_shift_number() == 1 else 'Night'})")
    print(f"Hourly Pay Rate: ${worker.get_hourly_pay_rate():.2f}")


if __name__ == "__main__":
    main()
