class Person:
    def __init__(self, name, age, gender):
        # Initialize attributes
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        # Method to introduce the person
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Create an instance of the Person class with the name "Yazmin"
person_instance = Person(name="Yazmin", age=30, gender="Female")

# Call the introduce method to display the person's information
person_instance.introduce()
