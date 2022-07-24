import logging

l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]), {'k1' :"sudh" , "k2" : "ineuron","k3": "kumar",3: 6, 7: 8} , ["ineuron" , "data science "]]

import logging
logging.basicConfig(filename='list_dict.log', level=logging.INFO, format='%(levelname)s,%(asctime)s,%(name)s,%(message)s')

class non_premitive_fun():
    logging.info('accessing non_premitive_fun class')
    def __init__(self,l):
        self.l = l

    # Q1:

    def pattern(self,n):

        try:
            logging.info('entering a function to print given data in a particular pattern')
            self.n = n
            for i in range(n):
                for j in range(i + 1):
                    print('ineuron', end=' ')
                print('\n')

        except Exception as e:
            logging.exception(e)

    def rhombus_pattern(self,n):
        try:
            logging.info('entering a function to print given data in a particular pattern')
            self.n = n
            k = n
            m = n

            for i in range(n):
                k = k - 1
                print('   ' * k, end=' ')
                for j in range(i + 1):
                    print('ineuron', end=' ')
                print('\n')
            for i in range(n - 1, 0, -1):
                print(' ' * (m), end=' ')
                m = 2 * m
                for j in range(i):
                    print('ineuron', end=' ')
                print('\n')

        except Exception as e:
            logging.exception(e)

    # q3 : Try to extract all the list entity

    def extract_list(self):

        try:
            logging.info('entering a function to extract all list entities')
            for i in self.l:
                if type(i) == list:
                    logging.info(i)
            for i in self.l:
                if type(i) == tuple or type(i) == set:
                    for n in i:
                        if type(n) == list:
                            logging.info('from nested tuple/set')
                            logging.info(n)
            for i in self.l:
                if type(i)== dict:
                    for n in i.keys():
                        if type(n) == list:
                            logging.info('from nested dict keys')
                            logging.info(n)
            for i in self.l:
                if type(i)== dict:
                    for n in i.values():
                        if type(n) == list:
                            logging.info('from nested dict values')
                            logging.info(n)

        except Exception as e:
            logging.exception(e)

    # q4 : Try to extract all the dict enteties

    def extract_dict(self):

        try:
            logging.info('entering a function to extract all dictionary entities')
            for i in self.l:
                if type(i) == dict:
                    logging.info(i)
            for i in self.l:
                if type(i)== list or type(i) == tuple or type(i) == set:
                    for n in i:
                        if type(n) == dict:
                            logging.info('from nested list/tuple/set')
                            logging.info(n)

        except Exception as e:
            logging.exception(e)

    # q5 : Try to extract all the tuples entities

    def extract_tuple(self):

        try:
            logging.info('entering a function to extract all tuple entities')
            for i in self.l:
                if type(i) == tuple:
                    logging.info(i)
            for i in self.l:
                if type(i)== list or type(i) == set:
                    for n in i:
                        if type(n) == tuple:
                            logging.info('from nested list/set')
                            logging.info(n)
            for i in self.l:
                if type(i)== dict:
                    for n in i.keys():
                        if type(n) == tuple:
                            logging.info('from nested dict keys')
                            logging.info(n)
            for i in self.l:
                if type(i)== dict:
                    for n in i.values():
                        if type(n) == tuple:
                            logging.info('from nested dict values')
                            logging.info(n)

        except Exception as e:
            logging.exception(e)

    # q6 : Try to extract all the numerical data it may b a part of dict key and values

    def extract_numbers(self):

        try:
            logging.info('entering a function to extract all numerical values')
            l2 = []
            for i in self.l:
                if type(i) == int:
                    l2.append(i)
            for i in self.l:
                if type(i)== list or type(i) == set or type(i) == tuple:
                    for n in i:
                        if type(n) == int:
                            l2.append(n)
            for i in self.l:
                if type(i)== dict:
                    for n in i.keys():
                        if type(n) == int:
                            l2.append(n)
            for i in self.l:
                if type(i)== dict:
                    for n in i.values():
                        if type(n) == int:
                            l2.append(n)

            logging.info(l2)

        except Exception as e:
            logging.exception(e)

        # q7 : Try to give summation of all the numeric data

    def extract_numbers_sum(self):

        try:
            logging.info('entering a function to extract sum of all numerical values')
            l2 = []
            for i in self.l:
                if type(i) == int:
                    l2.append(i)
            for i in self.l:
                if type(i)== list or type(i) == set or type(i) == tuple:
                    for n in i:
                        if type(n) == int:
                            l2.append(n)
            for i in self.l:
                if type(i)== dict:
                    for n in i.keys():
                        if type(n) == int:
                            l2.append(n)
            for i in self.l:
                if type(i)== dict:
                    for n in i.values():
                        if type(n) == int:
                            l2.append(n)

            logging.info(sum(l2))

        except Exception as e:
            logging.exception(e)

    #q8 : Try to filter out all the odd values out all numeric data which is a part of a list

    def extract_odd_numbers(self):

        try:
            logging.info('entering a function to extract odd numbers')
            l2 = []
            for i in self.l:
                if type(i) == int:
                    if i %2 == 1:
                        l2.append(i)
            for i in self.l:
                if type(i)== list or type(i) == set or type(i) == tuple:
                    for n in i:
                        if type(n) == int:
                            if n % 2 == 1:
                                l2.append(n)
            for i in self.l:
                if type(i)== dict:
                    for n in i.keys():
                        if type(n) == int:
                            if n % 2 == 1:
                                l2.append(n)
            for i in self.l:
                if type(i)== dict:
                    for n in i.values():
                        if type(n) == int:
                            if n % 2 == 1:
                                l2.append(n)

            logging.info(l2)

        except Exception as e:
            logging.exception(e)

    # q9 : Try to extract "ineruon" out of this data

    def extract_particular_string(self):

        try:
            logging.info('entering a function to extract particular string')
            for i in self.l:
                if type(i) == str:
                    if i == 'ineuron':
                        logging.info(i)
            for i in self.l:
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for n in i:
                        if type(n) == str:
                            if n == 'ineuron':
                                logging.info('from nested tuple/set/list')
                                logging.info(n)
            for i in self.l:
                if type(i) == dict:
                    for n in i.keys():
                        if type(n) == str:
                            if n == 'ineuron':
                                logging.info('from nested dict keys')
                                logging.info(n)
            for i in self.l:
                if type(i) == dict:
                    for n in i.values():
                        if type(n) == str:
                            if n == 'ineuron':
                                logging.info('from nested dict values')
                                logging.info(n)

        except Exception as e:
            logging.exception(e)

    # q10 :Try to find out a number of occurances of all the data

    def number_of_occurences(self):

        try:
            logging.info('entering a function which finds out number of occurences of all data')
            l2 = []
            for i in self.l:
                if type(i) == int or type(i) == str or type(i) == float:
                    l2.append(i)
            for i in self.l:
                if type(i)== list or type(i) == set or type(i) == tuple:
                    for n in i:
                            l2.append(n)
            for i in self.l:
                if type(i)== dict:
                    for n in i.keys():
                            l2.append(n)
            for i in self.l:
                if type(i)== dict:
                    for n in i.values():
                            l2.append(n)
            logging.info(l2)

            for i in l2:
                logging.info("element is %s",i)
                logging.info('count of the element is %s',l2.count(i))

        except Exception as e:
            logging.exception(e)

    # q11 : Try to find out number of keys in dict element

    def number_of_dict_keys(self):
        try:
            logging.info('entering a function which finds out number of dictionary keys')
            l2 = []

            for i in self.l:
                if type(i) == dict:
                    for n in i.keys():
                        l2.append(n)

                for i in self.l:
                    if type(i)== list or type(i) == set or type(i) == tuple:
                        for n in i:
                            if type(n) == dict:
                                for n in i.keys():
                                    l2.append(n)

            logging.info ('dict keys: %s', l2)
            logging.info('count of keys:%s',len(l2))

        except Exception as e:
            logging.exception(e)

    # q12 : Try to filter out all the string data

    def extract_strings(self):

        try:
            logging.info('entering a function to extract all string data')
            l2 = []
            for i in self.l:
                if type(i) == str:
                        l2.append(i)
            for i in self.l:
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for n in i:
                        if type(n) == str:
                                l2.append(n)
            for i in self.l:
                if type(i) == dict:
                    for n in i.keys():
                        if type(n) == str:
                                l2.append(n)
            for i in self.l:
                if type(i) == dict:
                    for n in i.values():
                        if type(n) == str:
                                l2.append(n)

            logging.info(l2)

        except Exception as e:
            logging.exception(e)

    # q13 : Try to Find  out alphanum in data

    def extract_alphanum_strings(self):

        try:
            logging.info('entering a function to extract alphanumeric strings')
            l2 = []
            for i in self.l:
                if type(i) == str:
                    if i.isalnum() == True:
                        l2.append(i)
            for i in self.l:
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for n in i:
                        if type(n) == str:
                            if n.isalnum() == True:
                                l2.append(n)
            for i in self.l:
                if type(i) == dict:
                    for n in i.keys():
                        if type(n) == str:
                            if n.isalnum() == True:
                                l2.append(n)
            for i in self.l:
                if type(i) == dict:
                    for n in i.values():
                        if type(n) == str:
                            if n.isalnum() == True:
                                l2.append(n)

            logging.info(l2)

        except Exception as e:
            logging.exception(e)

    # q14 : Try to find out multiplication of all numeric value in  the individual collection inside dataset

    def multi_of_each_collection(self):

        try:
            logging.info('entering a fuction to find the multiplication of each collection like list/tuple/set/dict')
            for i in l:
                a = 1
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for b in i:
                        if type(b) != int:
                            a = 'no numbers present'
                    for b in i:
                        if type(b) == int:
                            a = a*b
                    logging.info(type(i))
                    logging.info(a)

                l2 = []
                if type(i) == dict:
                    for x in i.items():
                        for y in x:
                            if type(y) == int:
                                l2.append(y)

                    if len(l2) == 0:
                        a = 'no numbers present'
                    else:
                        for b in l2:
                            a = a * b

                    logging.info(l2)

                    logging.info(type(i))
                    logging.info(a)

        except Exception as e:
            logging.exception(e)

    # q15 : Try to unwrape all the collection inside collection and create a flat list

    def extract_all_to_list(self):

        try:
            logging.info('entering a function which unwaraps all entinties from list/tuple/set/dictionary collection')
            l2 = []
            for i in l:
                if type(i) == list:
                    l2.append(i)
                if type(i) == dict:
                    l2.append(list(i.keys()))
                    l2.append(list(i.values()))
                if type(i) != list and type(i) != dict:
                    i = list(i)
                    l2.append(i)
            l3 = []
            for i in l2:
                l3.extend(i)
            logging.info(l3)

        except Exception as e:
            logging.exception(e)


test = non_premitive_fun(l)
test.pattern(4)
test.rhombus_pattern(3)
test.extract_list()
test.extract_dict()
test.extract_tuple()
test.extract_numbers()
test.extract_numbers_sum()
test.extract_odd_numbers()
test.extract_particular_string()
test.number_of_occurences()
test.number_of_dict_keys()
test.extract_strings()
test.extract_alphanum_strings()
test.multi_of_each_collection()
test.extract_all_to_list()