"""Napisz program w języku Python, który będzie symulował działanie samochodu z silnikiem. Program powinien spełniać poniższe wymagania:

Stwórz klasę Engine reprezentującą silnik. Klasa powinna mieć:

Atrybuty:
+ is_running - informujący, czy silnik jest włączony (początkowo False).
+ speed - reprezentujący prędkość obrotową silnika (początkowo 0).
Metody:
- start() - włącza silnik i ustawia prędkość na 0.
- stop() - wyłącza silnik i resetuje prędkość.
- increase_speed(amount) - zwiększa prędkość obrotową o podaną wartość.
- decrease_speed(amount) - zmniejsza prędkość obrotową o podaną wartość, ale prędkość nie może spaść poniżej 0.

Stwórz klasę Car reprezentującą samochód. Klasa powinna:

Atrybuty
+ Zawierać obiekt klasy Engine jako swój atrybut.
Metody
- Włączania silnika (start_engine()).
- Wyłączania silnika (stop_engine()).
- Przyspieszania samochodu poprzez zwiększanie prędkości silnika (accelerate(amount)).
- Zwalniania samochodu poprzez zmniejszanie prędkości silnika (decelerate(amount)).

W głównej części programu:
- Stwórz obiekt klasy Car.
- Włącz silnik samochodu.
- Zwiększ prędkość silnika dwukrotnie różnymi wartościami.
- Zmniejsz prędkość silnika dwukrotnie różnymi wartościami.
- Wyłącz silnik.

Program powinien wyświetlać odpowiednie komunikaty informujące o działaniach (np. „Engine started.”, „Engine speed increased to 500 RPM.”, itp.)."""

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
