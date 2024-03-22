import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta

def main():

    
    #print(date(year= 2020, month=1, day= 31))
    input_fp = r'.\input_data\\'
    input_fn = r'Leave Sample.xlsx'

    #get and clean criteria data
    criteria = pd.read_excel(input_fp + input_fn, sheet_name='Criteria', skiprows=1)
    criteria = criteria.dropna(axis='columns', how='all')
    
    criteria.info()
    
    #get and clean input data
    new_starter_dates = pd.read_excel(input_fp + input_fn, sheet_name='Input')
    
    #add standard allowances
    new_starter_dates['Yr_1_allowance'] = 21.0
    new_starter_dates['Yr_2_allowance'] = 22.0
    new_starter_dates['Yr_3_allowance'] = 23.0
    new_starter_dates['Yr_4_allowance'] = 24.0
    new_starter_dates['Yr_5_allowance'] = 25.0
    

    
    new_starter_dates['end_of first year'] = new_starter_dates['Start Date'].apply(end_of_first_year)
    
    
    new_starter_dates['end_of_second_year'] = new_starter_dates['end_of first year'].apply(calc_year_end)
    print(new_starter_dates)
    
    
    
def end_of_first_year(date):
     date_minus_one_year = date + relativedelta(years=1) 
     date_minus_one_month = date_minus_one_year  - relativedelta(months=1)
     date_as_last_day = date_minus_one_month + pd.offsets.MonthEnd(0)
     
     return date_as_last_day  

def calc_year_end(date):
    
    year_end = date.replace(month=12,day=31)

    return year_end
if __name__ == '__main__':
    main()