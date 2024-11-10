from datetime import datetime, date
import pickle, re

# Data
MONTH_DATA = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "Mei": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "Agustus": 8,
    "September": 9,
    "October": 10,
    "Oktober": 10,
    "November": 11,
    "Desember": 12,
}

# Save Data
def save_data(data):
    with open("data.pkl", "wb") as file:
        pickle.dump(data, file)

# Loading Data
def load_data():
    with open("data.pkl", "rb") as file:
        load = pickle.load(file)
        return load

# echo "# Bot-Homework" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/IceBearVenom/Bot-Homework.git
# git push -u origin main

# Removing Data
def remove_data(data):
    index = int(input("Remove Number?: "))
    index -= 1
    if index > len(data):
        print("Index Out Of Range")
    elif index <= len(data):
        del data[index]
        print("Removed Data Succesfully")
    else:
        pass

# Dsiplay Data
def display_data(data):
    for i in range(len(data)):
        return f"{i+1}. {list(data[i].keys())[0]}: {list(data[i].values())[0]}"

# Classes
class Date_Timer():
    def __init__(self, title, date) -> None:
        self.title = title
        self.date = date

    def month_to_num(self):
        word = self.date.split()
        for m in MONTH_DATA:
            m_upper = m.upper()
            if any(m_upper[:3] in w[:3].upper() for w in word):
                return MONTH_DATA[m]
            
    def date_picker(self):
        word = self.date.split()
        for w in word:
            if len(w) <= 2:
                return w

    def year_picker(self):
        word = self.date.split()
        for w in word:
            if len(w) == 4:
                return w

    def date_format(self):
        date = self.date_picker()
        month = next((key for key, value in MONTH_DATA.items() if value == self.month_to_num()), None)
        year = self.year_picker()

        return f"{date} {month} {year}"

    def saving(self):
        data = {self.title: self.date_format()}
        my_data.append(data)

class Timer():
    def __init__(self, deadline) -> None:
        self.now = datetime.now().date()
        self.deadline = deadline

    def start_timer(self, index):
        date_pattern = r'(\d{1,2} \w+ \d{4})$'
        my_dl = str(list(self.deadline[index].values())[0])
        match = re.search(date_pattern, my_dl)
        if match:
            dl = match.group(0).split()
            dt = int(dl[0])
            month = int(MONTH_DATA[dl[1]])
            year = int(dl[2])

            deadL = date(year, month, dt)
            return str((deadL - self.now).days)

def sort_data(data):
    new = []
    for i in range(len(data)):
        dat = {f'{list(data[i].keys())[0]}': f'{list(data[i].values())[0]}', 'Deadline': Timer(data).start_timer(i)}
        new.append(dat)

    for i in range(len(new)):
        sorted_ = sorted(new, key=lambda item: list(item.values())[1])

    return sorted_

# Data
my_data = sort_data(load_data())

if __name__ == "__main__":
    print("Choose Number:\n1. Input Homework\n2. See Homeweork\n3. Remove Homework\n4. Timeleft for the Homework")
    option = input("Choose?: ")
    print("===============================")
    # Choosing
    if option == "1":
        # Input
        title_input = input("Masukan Nama PR: ")
        date_input = input("Masukan Tenggat PR: ")
        # Saving
        Date_Timer(title_input, date_input).saving()
        print("===============================")
        # Display data
        print(display_data(my_data))
    elif option == "2":
        print(display_data(my_data))
        print(my_data)
    elif option == "3":
        print(display_data(my_data))
        print("===============================")
        remove_data(my_data)
        print("===============================")
        print(display_data(my_data))
    elif option == "4":
        print(display_data(my_data))
