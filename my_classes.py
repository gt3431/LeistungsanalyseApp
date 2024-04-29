import json
from datetime import datetime
import requests
import json

class Person:
    def __init__(self, first_name , last_name):
        self.first_name = first_name
        self.last_name = last_name

    def put(self,url):
        # Defines the data putted to the API
        data = {
            "name": self.first_name
        }
        data_json = json.dumps(data)
        response = requests.put(url, data=data_json)

        return(response.status_code)
        
    def save(self, path):
        with open(f"{path}/{type(self).__name__}_{self.last_name}_{self.first_name}.json", "w") as f:
            json.dump(self.__dict__, f)

class Subject(Person):
    def __init__(self, first_name , last_name, gender, birthdate : datetime, email):
        super().__init__(first_name, last_name)
        self.gender = gender
        self.__birthdate = {"year": birthdate.year, "month": birthdate.month, "day": birthdate.day}
        self.email = email

    def update_email(self, url):
        # Defines the data posted to the API
        data = {
            "name": self.first_name,
            "email": self.email
        }
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json)

        return(response.status_code)


    def estimate_max_hr(self) -> int:
        """
        See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
        """
        age = datetime.now().year - self.__birthdate["year"]
        if self.gender == "male":
            max_hr_bpm =  223 - 0.9 * age
        elif self.gender == "female":
            max_hr_bpm = 226 - 1.0 *  age
        return int(max_hr_bpm)

class Examiner(Person):
    def __init__(self, first_name , last_name, gender):
        super().__init__(first_name, last_name)
        self.gender = gender
    
class Experiment:
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def save(self, path):
        with open(f"{path}/Experiment_{self.experiment_name}_{self.date[:10].replace("/", "_")}.json", "w") as f:
            json.dump(self.__dict__, f, default=vars)

