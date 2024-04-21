import my_classes
from datetime import datetime
import json

if __name__ == "__main__":
    
    print("---LeistungsanalyseApp---")

    supervisor_first_name = input("Enter supervisor first name: ")
    supervisor_last_name = input("Enter supervisor last name: ")
    supervisor_gender = input("Enter supervisor gender [male/female]: ")
    supervisor_age = int(input("Enter supervisor age: "))

    subject_first_name = input("Enter subject first name: ")
    subject_last_name = input("Enter subject last name: ")
    subject_gender = input("Enter subject gender [male/female]: ")
    subject_age = int(input("Enter subject age: "))

    experiment_name = input("Enter experiment name: ")

    supervisior = my_classes.Person(supervisor_first_name , supervisor_last_name, supervisor_gender, supervisor_age)
    subject = my_classes.Person(subject_first_name , subject_last_name, subject_gender, subject_age)
    experiment = my_classes.Experiment(experiment_name, datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), supervisior, subject)
    
    print("\nSaving inputed data to file...")
    supervisior.save("data")
    subject.save("data")
    experiment.save("data")
    print("File succesfully saved")
    print("------------------------\n")