s = "  this is My First Python programming class\tand i am learNING\tpython string and its function "


import logging
logging.basicConfig(filename='string.log', level= logging.INFO ,format=  '%(levelname)s, %(asctime)s, %(name)s, %(message)s')

class string_fun:
        logging.info('Accessing string functions class')
        def __init__(self,str_var):
            self.str_var = str_var

        # 1 . Try to extract data from index one to index 300 with a jump of 3
        def slicing(self,lower, upper, jump):
            try:
                logging.info('Entering slicing function')
                a = self.str_var [lower:upper:jump]
                logging.info(a)
                return a

            except Exception as e:
                logging.exception(e)

        # 2. Try to reverse a string without using reverse function
        def reverse(self):
            try:
                logging.info('entering reverse function')
                rev = self.str_var[::-1]
                logging.info(rev)
                return rev
            except Exception as e:
                logging.exception(e)

        # 3.Try to split a string after conversion of entire string in uppercase
        def split(self,split_item):
            try:
                logging.info('entering converting to uppercase and split function')
                u = self.str_var.upper()
                sp = (u.split(split_item))
                logging.info(sp)
                return sp
            except Exception as e:
                logging.exception(e)

        # 4. try to convert the whole string into lower case

        def lower_case(self):
            try:
                logging.info('entering converting to lowercase function')
                lw = (self.str_var.lower())
                logging.info(lw)
                return lw
            except Exception as e:
                logging.exception(e)

        # 5 . Try to capitalize the whole string

        def capitalize(self):
            try:
                logging.info('this is capitalizing the whole string function')
                caps = self.str_var.title()
                logging.info(caps)
                return caps
            except Exception as e:
                logging.exception(e)

        # 6 . Write a diference between isalnum() and isalpha()
        def alpha(self):
            try:
                logging.info('entering a function which checks if the string is alpha or alpha numeric')
                al = self.str_var.isalpha()
                al_num = self.str_var.isalnum()
                logging.info(al)
                logging.info(al_num)
                return al , al_num
            except Exception as e:
                logging.exception(e)

        # 7. Try to give an example of expand tab

        def expand_tabs(self):
            try:
                logging.info('entering expand tabs function')
                exp_tab = self.str_var.expandtabs()
                logging.info(exp_tab)
                return exp_tab
            except Exception as e:
                logging.exception(e)

        # 8 . Give an example of strip , lstrip and rstrip

        def strip(self):
            try:
                logging.info('entering string strip function')
                ls = self.str_var.lstrip()
                rs = self.str_var.rstrip()
                strp = self.str_var.strip()
                logging.info('lstrip =%s',ls)
                logging.info('rstrip =%s',rs)
                logging.info('strip =%s',strp)
                return (ls,rs,strp)
            except Exception as e:
                logging.exception(e)

        # 9.  Replace a string charecter by another charector by taking your own example

        def replace(self,to_replace, replacement):
            try:
                logging.info('entering a function which replaces particular string with given string')
                new_s = self.str_var.replace(to_replace,replacement)
                logging.info(new_s)
                return new_s
            except Exception as e:
                logging.exception(e)

        # 10 . Try  to give a defination of string center function with and exmple

        def center(self,width,fill_char):
            try:
                logging.info('entering a function which centers the string')
                cntr = self.str_var.center(width,fill_char)
                logging.info(cntr)
                return cntr
            except Exception as e:
                logging.exception(e)


try:
    test = string_fun(s)
    print(test.slicing(0,300,3))
    print(test.reverse())
    print(test.split('T'))
    print(test.lower_case())
    print(test.capitalize())
    print(test.alpha())
    print(test.expand_tabs())
    print(test.strip())
    print(test.replace('First','not first'))
    print(test.center(120,'$'))

except Exception as e:
    logging.exception(e)

