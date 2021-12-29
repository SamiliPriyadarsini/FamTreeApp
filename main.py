# This is a sample Python script.
from FTree import FTree


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')

    ftree_obj = FTree()
    status_add = ftree_obj.add(given_name="Manikchand",
                  surname="EntoGutka",
                  gender="Trans",
                  date_of_birth="00000000",
                  father_name="Baap",
                  mother_name=None)
    if status_add:
        record = ftree_obj.search(given_name="Manikchand",
                  surname="EntoGutka",
                  date_of_birth="00000000")
        print(record)

    if ftree_obj.commit():
        print("Commit Successful")
    else:
        print("Commit failed")

    status_del = ftree_obj.delete(given_name="Manikchand",
                     surname="EntoGutka",
                     date_of_birth="00000000")

    if status_del:
        print("Delete Successful")
    else:
        print("Delete failed")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
