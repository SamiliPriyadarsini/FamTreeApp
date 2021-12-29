# import os.path
import pandas as pd


class FTree:
    # def constructor
    def __init__(self):
        print("FTree object created")

        # TODO: Remove hard-coding of f_name
        self.f_name = r"data/ft_data.csv"

        try:
            self.df = pd.read_csv(self.f_name)

        except FileNotFoundError:
            print(" ft_data.csv file not found !! ")

    # Methods
    def add(self, given_name, surname, gender, date_of_birth, father_name, mother_name):
        found_rec = self.search(given_name, surname, date_of_birth)
        if not found_rec.empty:
            # TODO: No print in PROD
            print("Already added ")
            return 0

        record = {
            "given_name": given_name,
            "surname": surname,
            "gender": gender,
            "date_of_birth": date_of_birth,
            "father_name": father_name,
            "mother_name": mother_name
        }
        self.df = self.df.append(record, ignore_index=True)
        return 1

    def update(self, given_name, surname, date_of_birth, update_dict):
        found_rec = self.search(given_name, surname, date_of_birth)
        if found_rec.empty:
            # TODO: No print in PROD
            print("Record Not Found")
            return 0

        # TODO: Remember enumerate
        for idx, field in enumerate(update_dict[update_fields]):
            value = update_dict[update_values][idx]
            self.df.loc[
                (self.df.given_name == given_name) &
                (self.df.surname == surname) &
                (self.df.date_of_birth == date_of_birth), field] = value
        return 1

    def delete(self, given_name, surname, date_of_birth):
        found_rec = self.search(given_name, surname, date_of_birth)
        if found_rec.empty:
            # TODO: No print in PROD
            print("Record Not Found")
            return 0

        # TODO: Yet to test and confirm
        del_idx = self.df.iloc[
            (self.df.given_name == given_name) &
            (self.df.surname == surname) &
            (self.df.date_of_birth == date_of_birth)]

        self.df.drop(index=del_idx)
        return 1

    def view_ftree(self):
        pass

    def search(self, given_name, surname, date_of_birth):
        found_rec = self.df.loc[
            (self.df.given_name == given_name) &
            (self.df.surname == surname) &
            (self.df.date_of_birth == date_of_birth)]
        return found_rec

    def commit(self):
        try:
            self.df.to_csv(self.f_name)
            return True

        except OSError:
            print(" ft_data.csv file not written !! ")
            return False
