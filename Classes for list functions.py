l = [3,4,5,6,7, [23,456,67,8,78,78] ,[345,56,87,8,98,9] ,(234,6657,6), {"key1" :"sudh" , 234:[23,45,656]}]

import logging
logging.basicConfig(filename= 'lists.log',level=logging.INFO, format='%(levelname)s, %(asctime)s,%(name)s,%(message)s')


class list_fun:
    logging.info('accessing list_fun class')
    def __init__(self,l):
        self.l = l

    # 1 . Try to reverse a list

    def reverse(self):
        try:
            logging.info('entering reverse list function')
            rev = self.l[::-1]
            logging.info(rev)
            return rev
        except Exception as e:
            logging.exception(e)

    # 2. try to access 234 out of this list
    # 3 . try to access 456

    def access_from_list_tuple(self,x):
        try:
            logging.info('entering a function which checks for given data in list/tuple/set/dict')
            for i in self.l:
                if type(i)!= list and type(i) != dict and type(i) != tuple and type(i) != set:
                    if i == x:
                        logging.info('from list')
                        logging.info(i)
            for i in self.l:
                if type(i)== list or type(i) == tuple or type(i) == set:
                    for n in i:
                        if n == x:
                            logging.info('from nested list/tuple/set')
                            logging.info(n)
            for i in self.l:
                if type(i) == dict:
                    for n in i.keys():
                        if n == x:
                            logging.info('from dict key')
                            logging.info(n)
                    for n in i.values():
                        if n == x:
                            logging.info('from dict value')
                            logging.info(n)
            else:
                logging.info('matching element returned if match is found')

        except Exception as e:
            logging.exception(e)

    # 4 . Try to extract only a list collection form list l

    def extract_list(self):
        try:
            logging.info('entering a function which extracts only list entities')
            l = []
            for i in self.l:
                if type(i) == list:
                    lst = l.append(i)
            logging.info(l)
            for i in self.l:
                if type(i)== list or type(i) == tuple or type(i) == set:
                    for n in i:
                        if type(n) == list:
                            logging.info('from nested list/tuple/set')
                            logging.info(n)
            for i in self.l:
                if type(i) == dict:
                    for n in i.keys():
                        if type(n) == list:
                            logging.info('from dict key')
                            logging.info(n)
                    for n in i.values():
                        if type(n) == list:
                            logging.info('from dict value')
                            logging.info(n)


        except Exception as e:
            logging.exception(e)

    # 5.5 . Try to extract "sudh"

    def extract_dict_val(self,to_extract):
        try:
            logging.info('entering a function which extracts a particular dictionary value')
            for i in self.l:
                if type(i) == dict:
                    for x in i.values():
                        if x == to_extract:
                            logging.info(to_extract)
                            return to_extract
                    else:
                        logging.info('value not present')
                        return ('value not present')

        except Exception as e:
            logging.exception(e)


    # 6 . Try to list all the key in dict element avaible in list

    def extract_dict_key(self):
        try:
            logging.info('entering a function which extracts dictionary keys')
            l = []
            for i in self.l:
                if type(i) == dict:
                    logging.info(i.keys())
            else:
                logging.info('dictionary type key element returned if present')

        except Exception as e:
            logging.exception(e)

    # 7 . Try to extract all the value element form dict available in list
    def extract_dict_all_val(self):
        try:
            logging.info('entering a function which extracts all dictionary values')
            l = []
            for i in self.l:
                if type(i) == dict:
                    logging.info(i.values())
            else:
                logging.info('dictionary type value element returned if present')

        except Exception as e:
            logging.exception(e)

try:

    test = list_fun(l)
    print(test.reverse())
    test.access_from_list_tuple(234)
    print(test.extract_list())
    print(test.extract_dict_val('check'))
    test.extract_dict_key()
    test.extract_dict_all_val()

except Exception as e:
    logging.exception(e)

