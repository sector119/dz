import os.path

STORAGE = '/Users/sector119/PycharmProjects/dz/storage.csv'


class Department:
    def __init__(self, _id, title, director_name, phone_number, monthly_budget,
                 yearly_budget, website_url):
        self._id = self.set_id(_id)
        self._title = title
        self._director_name = self.set_director_name(director_name)
        self._phone_number = phone_number
        self._monthly_budget = monthly_budget
        self._yearly_budget = yearly_budget
        self._website_url = website_url

    def get_id(self):
        return self._id

    def set_id(self, value):
        if isinstance(value, str) and not value.isdigit():
            raise ValueError('Error. id field is not digit')

        return int(value)

    def get_director_name(self):
        return self._director_name

    def set_director_name(self, value):
        if not value.isalpha():
            raise ValueError('Error. director_name field is not alpha')

        return value

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

    def remove(self, _id):
        for i in range(len(self._departments)):
            if self._departments[i].get_id() == _id:
                del self._departments[i]
                break

    def find(self, query):
        for department in self._departments:
            if query in str(department):
                print(department)

    def show(self):
        for department in self._departments:
            print(department)

    def clear(self):
        self._departments = []

    def load(self, sep='\t'):
        self.clear()

        if not os.path.isfile(self.storage):
            raise FileNotFoundError('Error. Storage file not found')

        with open(self.storage, 'r') as f:
            for line in f.readlines():
                self.append(Department(*line.strip().split(sep)))

    def save(self):
        with open(self.storage, 'w') as f:
            for department in self._departments:
                f.write(str(department) + '\n')


d1 = Department(1, 'title1', 'directorone', 1, 1, 1, 'http://site1.com')
d2 = Department(2, 'title2', 'directortwo', 2, 2, 2, 'http://site2.com')
d3 = Department(3, 'title3', 'directorthree', 3, 3, 3, 'http://site3.com')

collection = DepartmentCollection([d1, d2])
collection.append(d3)
collection.save()

#

collection = DepartmentCollection()
collection.load()
collection.show()
collection.find('tle2')
collection.remove(2)
collection.show()
