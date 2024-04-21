import json

class Person:
    def __init__(self, first_name , last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def estimate_max_hr(self) -> int:
        """
        See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
        """
        if self.gender == "male":
            max_hr_bpm =  223 - 0.9 * self.age
        elif self.gender == "female":
            max_hr_bpm = 226 - 1.0 *  self.age
        return int(max_hr_bpm)

    def save(self, path):
        with open(f"{path}/Person_{self.last_name}_{self.first_name}.json", "w") as f:
            json.dump(self.__dict__, f)
    

class Experiment:
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def save(self, path):
        with open(f"{path}/Experiment_{self.experiment_name}_{self.date[:10].replace("/", "_")}.json", "w") as f:
            json.dump(self.__dict__, f, default=vars)

