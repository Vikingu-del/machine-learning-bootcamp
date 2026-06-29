import time
from random import randint
import os

def log(func):
    def myinner(*args, **kwargs):
        username = os.environ.get("USER", "user")
        title_name = func.__name__.replace('_', ' ').title()
        start_time = time.time()
        result = func(*args, **kwargs)
        exec_time = time.time() - start_time
        if exec_time < 1.0:
            time_str = f"{exec_time * 1000:.3f} ms"
        else:
            time_str = f"{exec_time:.3f} s"
        log_str = f" {title_name:<19}[ exec-time = {time_str}]\n"
        with open("machine.log", "a") as f:
            f.write(f"{username}(Running):{log_str}")
        return result
    return myinner

class CoffeeMachine():
    water_level = 100
    
    
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    
    
    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")


    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
