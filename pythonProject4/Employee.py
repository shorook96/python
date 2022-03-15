from Person import Person


class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super(Employee, self).__init__(name, money, mood, healthRate)
        self.id = id
        self.email = email
        self.car = car
        self.__salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = Person.moods[0]
        elif hours < 8:
            self.mood = Person.moods[2]
        else:
            self.mood = Person.moods[1]

    def send_mail(self, to, subject, msg, receiver_name):
        mail_lines = ["\nFrom: " + self.email, "\nTo: " + to, "\n", "\nHi " + receiver_name, "\n" + msg, "\n" + subject]
        fl = open("mail.txt", 'a')
        for ln in mail_lines:
            fl.write(ln)
        fl.close()

    def drive(self):
        pass

    def refuel(self):
        pass

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, newsalary):
        if newsalary > 1000:
            self.__salary = newsalary
