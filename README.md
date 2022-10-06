# 0x00. AirBnB clone - The console #

## Made by Connor Hostler and Caleb House ##

### Description of project: ###

The goal of this project is to create a command interpreter (the console) in order to manage the objects of the AirBnB project.

In order to accomplish this, several tasks must be completed:
* Put in place a parent class called BaseModel to take care of initialization, serialization, and deserialization of future instances.
* Create a simple flow of serialization/deserialization:
    * Instance<->Dictionary<->JSON string<->file
* Create all classes used for AirBnB that inherit from BaseModel:
    * User, State, City, Place, Amenity, Review
* Create the first abstracted storage engine of the project called file storage.
* Create all unittests to validate all our classes and storage engine.

### Description of command interpreter ###

The command interpreter contains several commands that allow the user to manage the objects of the project:
* Create a new object
* Retrieve an object from a file, database etc.
* Do operations on objects
* Update attributes of an object
* Destroy an object

__How to start the console:__
1. Clone the repository holbertonschool-AirBnB_clone into your terminal
2. Run the command `./console.py` and the command prompt `(hbnb) ` should appear

__How to use the console:__
1. Type the command help next to the prompt to be shown a list of documented commands
2. Type your desired command next to the `(hbnb) ` prompt and press `ENTER`
3. To exit the console, type the command `quit` or `EOF` which should return you to your terminal's command line

### Console Examples ###
