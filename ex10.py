from typing import List, Optional

STORAGE = 'storage.csv'


class Department:
    def __init__(self, _id, title, director_name, phone_number, monthly_budget, yearly_budget, website_url):
        self._id = _id
        self._title = title
        self._director_name = director_name
        self._phone_number = phone_number
        self._monthly_budget = monthly_budget
        self._yearly_budget = yearly_budget
        self._website_url = website_url

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not value.isdigit():
            raise ValueError('id field is not digit')

        self._id = value

    # And so on for all attributes...

    def __str__(self):
        return f'{self._id}\t{self._title}\t{self._director_name}\t{self._phone_number}\t{self._monthly_budget}\t{self._yearly_budget}\t{self._website_url}'


class DepartmentCollection:
    def __init__(self, departments: Optional[List[Department]] = None, storage=STORAGE):
        if departments is not None:
            self._departments = departments

            self.save()
        else:
            self._departments = []

        self.storage = storage

    def append(self, value: Department):
        self._departments.append(value)

    def remove(self, _id):
        for i in range(len(self._departments)):
            if self._departments[i].id == _id:
                del self._departments[i]
                break

    # And other methods...

    def save(self):
        with open(self.storage) as f:
            f.writelines(self._departments)
