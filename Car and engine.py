class Engine:

    def __init__(self):
        self.is_running = False
        self.speed = 0

    def start(self):
        if not self.is_running:
            self.is_running = True
            print("Engine started")
        else:
            print("Engine already running")

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.speed = 0
            print("Engine stopped")
        else:
            print("Engine is already off")

    def increase_speed(self, amount: int):
        if self.is_running:
            self.speed += amount
            print(f"Engine speed increased to {self.speed} RPM")
        else:
            print("Cannot increase speed. Engine is off.")

    def decrease_speed(self, amount: int):
        if self.is_running:
            self.speed -= amount
            if self.speed < 0:
                self.speed = 0
            print(f"Engine speed decrease to {self.speed} RPM")
        else:
            print("Cannot decrease speed. Engine is off.")


class Car:
    
    def __init__(self):
        self.engine = Engine()

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()

    def accelerate(self, amount: int):
        self.engine.increase_speed(amount)

    def decelerate(self, amount: int):
        self.engine.decrease_speed(amount)


if __name__ == "__main__":

    volvo = Car()

    volvo.start_engine()

    volvo.accelerate(5)
    volvo.accelerate(7)

    volvo.decelerate(2)
    volvo.decelerate(4)

    volvo.stop_engine()
