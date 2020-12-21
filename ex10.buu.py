STORAGE = open("data.txt", "r")
f2 = open("result.txt", "w")


class Department:
    def __init__(self, _id, title, director_name, phone_number, monthly_budget,
             yearly_budget, website_url):
        self._id = self.set_id(_id)
        self._title = title
        self._director_name = self.set_director_name(director_name)
        self._phone_number = self.set_phone_number(phone_number)
        self._monthly_budget = self.set_monthly_budget(monthly_budget)
        self._yearly_budget = self.set_yearly_budget(yearly_budget)
        self._website_url = website_url

    def get_id(self):
        return self._id

    def set_id(self, value):
        while not value.isdigit():
            value = input('Error. ID field is not digit. Try one more time -> ')
        return int(value)

    def get_director_name(self):
        return self._director_name

    def set_director_name(self, value):
        while not value.isalpha():
            value = input('Error. director_name field is not alpha. Try one more time -> ')
        return value

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, value):
        while not value.isdigit():
            value = input('Error. Phone number field is not digit. Try one more time -> ')
        return int(value)

    def get_monthly_budget(self):
        return self._monthly_budget

    def set_monthly_budget(self, value):
        while not value.isdigit():
            value = input('Error. Monthly budget field is not digit. Try one more time -> ')
        return int(value)

    def get_yearly_budget(self):
        return self._yearly_budget

    def set_yearly_budget(self, value):
        while not value.isdigit():
            value = input('Error. Yearly budget field is not digit. Try one more time -> ')
        return int(value)

    def __str__(self):
        return f'{self._id}\t{self._title}\t{self._director_name}\t{self._phone_number}\t{self._monthly_budget}\t{self._yearly_budget}\t{self._website_url}'


class DepartmentCollection:
    def __init__(self, departments=None, storage=STORAGE):
        if departments is not None:
            self._departments = departments
        else:
            self._departments = []

        self.storage = storage

    def append(self, value: Department):
        self._departments.append(value)

    def remove(self, _id: int):
        for i in range(len(self._departments)):
            if self._departments[i].get_id() == _id:
                del self._departments[i]
                break

    def change(self, _id: int, value: Department):
        for i in range(len(self._departments)):
            if self._departments[i].get_id() == _id:
                self._departments[i] = value
                break
        else:
            print('No departments with such id')

    def find(self, value):
        for department in self._departments:
            if value in str(department):
                print(department)

    def show(self):
        for department in self._departments:
            print(department)

    def clear(self):
        self._departments = []

    def save_to_file(self):
        for department in self._departments:
            f2.write(str(department) + '\n')


collection = DepartmentCollection()

for line in STORAGE.readlines():
    collection.append(Department(*line.strip('\n').split(' ')))

idToChange = input('Enter id of department you want to change info about: ')

newTitle = input("Enter title: ")
newName = input("Enter director name: ")
newNumber = input("Enter phone number: ")
newMonthlyBudget = input("Enter monthly budget: ")
newYearlyBudget = input("Enter yearly budget: ")
newUrl = input("Enter URL: ")
newDepartment = Department(idToChange, newTitle, newName, newNumber, newMonthlyBudget, newYearlyBudget, newUrl)

collection.change(int(idToChange), newDepartment)
collection.show()
