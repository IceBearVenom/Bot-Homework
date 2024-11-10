import pickle, re
from datetime import datetime, date

# Month Data
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
    "December": 12
}

# Classes
class Date_Timer():
    def __init__(self) -> None:
        self.now = datetime.now().date()

    def timer(self, date_):
        # Var
        day = None
        month = None
        year = None

        # Checker
        for i in date_:
            if i.isdigit():
                if int(i) <= 31:
                    day = int(i)
                elif len(i) >= 4:
                    year = int(i)
            elif i in list(MONTH_DATA.keys()):
                month = int(MONTH_DATA[i])

        # Timer
        deadline = date(year, month, day)
        return str((deadline - self.now).days)

class Data_Attribute():
    def __init__(self) -> None:
        pass

    def _add_(self, data, msg=str):
        # Var
        message = msg.split()

        # Format
        title = message[0]
        desc = " ".join(message[1:-3])
        deadline = message[-3:]

        # Pick Timer
        date_timer = Date_Timer().timer(deadline)
        
        # Appending
        data.append({"Title": title, "Description": desc, "Deadline": deadline, "Timer": date_timer})
        self._save_(data)

    def _clear_(self, data):
        data.clear()
        self._save_(data)

    def _remove_(self):
        pass

    def _sort_(self, data):
        # Checking list
        if not data:
            # Return None
            return []
        else:
            # Sorting
            sorted_data = sorted(data, key=lambda x: int(x["Timer"]))
            return sorted_data

    def _display_(self, data):
        message = ""
        
        for i in range(len(data)):
            deadline = " ".join(data[i]["Deadline"])
            message += f"{i+1}. *{data[i]["Title"]}* >> {data[i]["Description"]} >> {deadline} >> {data[i]["Timer"]} Day/s"

        return message

    def _save_(self, data):
        with open("data.pkl", "wb") as file:
            pickle.dump(data, file)

    def _load_(self):
        with open("data.pkl", "rb") as file:
            load = pickle.load(file)
            sort = self._sort_(load)
            return sort

class Command():
    def __init__(self, message=str) -> None:
        msg = message.title()

        # Adding Command
        if msg.startswith("/Add"):
            msg = msg[len("/Add"):].lstrip()
            return msg
        # Remove Command
        elif msg.startswith("/Remove"):
            msg = msg[len("/Remove"):].lstrip()
            return msg
        else:
            return "Error! Message Invalid!"

