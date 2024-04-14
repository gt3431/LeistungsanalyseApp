import my_functions as my_functions
from datetime import datetime
import json

if __name__ == "__main__":
    
    print("---LeistungsanalyseApp---")

    experiment_name = input("Enter experiment name: ")
    supervisor_name = input("Enter supervisor name: ")
    first_name = input("Enter subject first name: ")
    last_name = input("Enter subject last name: ")
    gender = input("Enter subject gender [male/female]: ")
    age = int(input("Enter subject age: "))

    person = my_functions.build_person(first_name , last_name, gender, age)
    experiment = my_functions.build_experiment(experiment_name, datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), supervisor_name, person)
    
    print("\n---Experiment Summary---")
    print(f"Created person:\n{person}\n")
    print(f"Created experiment:\n{experiment}\n")
    print("Saving experiment to file...")
    with open("experiment.json", "w") as f:
        json.dump(experiment, f)
    print("------------------------\n")