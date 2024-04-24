import my_classes
from datetime import datetime
import json

if __name__ == "__main__":
    
    print("---LeistungsanalyseApp---")

    examiner_first_name = input("\nEnter examiner first name: ")
    examiner_last_name = input("Enter examiner last name: ")
    examiner_gender = input("Enter examiner gender [male/female]: ")

    subject_first_name = input("\nEnter subject first name: ")
    subject_last_name = input("Enter subject last name: ")
    subject_gender = input("Enter subject gender [male/female]: ")
    subject_birthyear = int(input("Enter subject birthyear: "))
    subject_birthmonth = int(input("Enter subject birthmonth: ")) 
    subject_birthday = int(input("Enter subject birthday: "))

    experiment_name = input("\nEnter experiment name: ")

    examiner = my_classes.Examiner(examiner_first_name , examiner_last_name, examiner_gender)
    subject = my_classes.Subject(subject_first_name , subject_last_name, subject_gender, datetime(subject_birthyear, subject_birthmonth, subject_birthday))
    experiment = my_classes.Experiment(experiment_name, datetime.now().strftime("%Y/%m/%m, %H:%M:%S"), examiner, subject)
    
    print("\nSaving inputed data to file...")
    examiner.save("data")
    subject.save("data")
    experiment.save("data")
    print("File succesfully saved")
    print("------------------------\n")