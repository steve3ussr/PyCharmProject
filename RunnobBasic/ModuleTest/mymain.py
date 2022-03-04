# import mymodule as mm
from importlib import reload
import mymodule

print("test")
mymodule.print_fuck("Towy")

print(
    dir(mymodule)
)
reload(mymodule)
