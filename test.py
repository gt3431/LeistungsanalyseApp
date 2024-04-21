import my_classes
from datetime import datetime
import json

if __name__ == "__main__":
    
    print("---LeistungsanalyseApp---")
    print("Running test file")
    print("Generating sample objects")
    supervisor = my_classes.Person("Tobias" , "Gasteiger", "male", 24)
    subject = my_classes.Person("Matti" , "Fletschinger", "male", 21)
    experiment = my_classes.Experiment("Leistungstest", datetime.now().strftime("%Y/%m/%d, %H:%M:%S"), supervisor, subject)
    
    print("Saving sample objects to file")
    supervisor.save("data")
    subject.save("data")
    experiment.save("data")
    print("Done!\n")