year=int(input("Enter a year: "))

'''
A year is leap year if 
1) Year is multiple of 4 and not multiple of 100.
2) Year is multiple of 400
'''

if ((year%4==0 and year%100!=0) or (year%400==0)):        ## Main Logic
    print(str(year) + ' is a leap year!')
    print('366 days')
    print('''
          January   : 31
          February  : 29
          March     : 31
          April     : 30
          May       : 31
          June      : 30
          July      : 31
          August    : 31
          September : 30
          October   : 31
          November  : 30
          December  : 31    
    ''')
else:
    print(str(year) + ' is not a leap year.')
    print('365 Days')
    print('''
              January   : 31
              February  : 28
              March     : 31
              April     : 30
              May       : 31
              June      : 30
              July      : 31
              August    : 31
              September : 30
              October   : 31
              November  : 30
              December  : 31
        ''')

'''
------OUTPUT------

Enter a year: 2012
2012 is a leap year!
366 days

          January   : 31
          February  : 29
          March     : 31
          April     : 30
          May       : 31
          June      : 30
          July      : 31
          August    : 31
          September : 30
          October   : 31
          November  : 30
          December  : 31 

------------------
'''
