import pickle

class Advertising:
    def __init__(self, user, tel_number, date_of_publication, price):
        self.user = user
        self.tel_number = tel_number
        self.date_of_publication = date_of_publication
        self.price = price

    def check_data_base_user(self):
        user_data = {
            ('Mark', +380689124343, '150$'):'17.03.2023',
        }
        if self.tel_number not in user_data:
            user_data.setdefault((self.user, 
                                self.tel_number, 
                                self.price), self.date_of_publication)

            with open('/Users/danil/Documents/work_py/main/list_user.bin', 'wb') as file_upd:
                pickle.dump(user_data, file_upd)
            with open('/Users/danil/Documents/work_py/main/list_user.bin', 'rb') as file_r:
                show_file = pickle.load(file_r)

            for i, k in show_file.items():
                print('\n\t', *i, '-', k)

        else:
            print('This numbe is already taken')
            False


while True:
    user_advertisig = Advertising(input('Your name: '), input('Your tel-number: '), input('Date_of_publication: '), '50$')
    user_advertisig.check_data_base_user()