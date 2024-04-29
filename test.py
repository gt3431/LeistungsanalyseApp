import my_classes
from datetime import datetime

if __name__ == "__main__":
    
    print("---LeistungsanalyseApp---")
    print("->Running test file")
    print("->Generating sample objects")

    examiner = my_classes.Examiner("Tobias" , "Gasteiger", "male")
    subject = my_classes.Subject("Matti" , "Fletschinger", "male", datetime(2001, 5, 5), "matti.fletschinger@mail.com")
    experiment = my_classes.Experiment("Leistungstest", datetime.now().strftime("%Y/%m/%d, %H:%M:%S"), examiner, subject)
    
    print(f"Estimated max hartrate of subject: {subject.estimate_max_hr()}")

    print("->Saving sample objects to file")
    examiner.save("data")
    subject.save("data")
    experiment.save("data")
    print("Succesfully saved")
    print("->Uploading sample data to webserver...")
    url = "http://localhost:5000/"
    examiner.put(url)
    subject.put(url)
    subject.update_email(url)
    print("Succesfully uploaded")