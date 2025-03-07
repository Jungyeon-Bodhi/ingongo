#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 09:07:52 2024

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please download following Python Libraries:
1. Pandas
2. Numpy
3. uuid
4. openpyxl
"""

import pandas as pd
import numpy as np
import uuid
from openpyxl import load_workbook

class Preprocessing:
    
    def __init__(self, name, file_path, file_path_others, list_del_cols, dates, miss_col, anon_col, anon_col2, identifiers, opened_cols, cols_new, 
                 anon_list, age_col = None, diss_cols = None, del_type = 0, file_type='xlsx'):
        """
        - Initialise the Performance Management Framework class

        name: str, Name of the project
        file_path: str, Directory of the raw dataset
        file_path_others: str, Directory of the opened-end questions' answers
        list_del_cols: list, Columns list for deleting
        dates: list, Dates on which the pilot test was conducted from the data
        miss_col: list, 
        anon_col: str, Column for anonymisation (Respondent Name)
        anon_col2: str, Column for anonymisation (Enumerator Name)
        identifiers: list, Columns for checking duplicates 
        opened_cols: list, Opened-end question columns
        cols_new: list, New names for the columns (for data analysis purpose)
        age_col: str, Column of age infromation (for age-grouping purpose)
        diss_cols: list, Column of WG-SS questions in the dataset (for disability-grouping purpose)
        del_type: int, [0 or 1]
        -> 0: Remove all missing values from the columns where missing values are detected
        -> 1: First, remove columns where missing values make up 10% or more of the total data points
              Then, remove all remaining missing values from the columns where they are detected
        file_type: str, filetype of the raw dataset
        """
        self.name = name
        self.file_path = file_path
        self.file_path_others = file_path_others
        self.file_type = file_type
        self.list_del_cols = list_del_cols
        self.dates = dates
        self.miss_col = miss_col
        self.anon_col = anon_col
        self.anon_col2 = anon_col2
        self.identifiers = identifiers
        self.opened_cols = opened_cols
        self.cols_new = cols_new
        self.anon_list = anon_list
        self.age_col = age_col
        self.diss_cols = diss_cols
        self.del_type = del_type
        self.df = None
    
    def data_load(self):
        """
        - To load a dataset
        """
        file_path = self.file_path
        file_type = self.file_type
        if file_type == 'xlsx' or file_type == 'xls':
            df = pd.read_excel(f"{file_path}.{file_type}")
            df = df.dropna(subset=['today'])
            condition = (df['A2-2. Province'] != 'Eastern Province') & (df['0. Which stakeholder is being interviewed?'] == 'Refugee youth')
            df = df.drop(df[condition].index)
            self.df = df
            return True
        elif file_type == 'csv':
            df = pd.read_csv(f"{file_path}.{file_type}")
            df = df.dropna(subset=['today'])
            condition = (df['A2-2. Province'] != 'Eastern Province') & (df['0. Which stakeholder is being interviewed?'] == 'Refugee youth')
            df = df.drop(df[condition].index)
            self.df = df
            return True
        else:
            print("Please use 'xlsx', 'xls' or 'csv' file")
            return False
        
    def delete_columns(self):
        """
        - To drop unnecessary columns
        """
        df = self.df
        list_cols = self.list_del_cols
        df = df.drop(columns = list_cols)
        print(f'Number of columns: {len(df.columns)} | After removing the columns that are not needed for the analysis')
        self.df = df
        return True

    def date_filter(self):
        """
        - To remove dates on which the pilot test was conducted from the dataset
        """
        df = self.df 
        dates = self.dates
        for date in dates:
            df = df[df['start'] != date]
        self.df = df
        return True
        
    def missing_value_clean(self):
        """
        - To detect and remove missing values
        """
        miss_col = self.miss_col
        df = self.df
        del_type = self.del_type
        initial_data_points = len(df)
        num_missing_cols = {}
        print("")
        for col in miss_col:
            missing_count = df[col].isnull().sum()
            num_missing_cols[col] = missing_count
            print(f'Column {col} has {missing_count} missing values')
    
        if del_type == 0: # Remove all missing values from the columns where missing values are detected
            df_cleaned = df.dropna(subset=miss_col)

        # First, remove columns where missing values make up 10% or more of the total data points
        # Then, remove all remaining missing values from the columns where they are detected
        elif del_type == 1:
            threshold = 0.1 * initial_data_points
            cols_to_drop = [col for col, missing_count in num_missing_cols.items() if missing_count > threshold]
            df_cleaned = df.drop(columns=cols_to_drop)
            print("")
            print(f'Number of columns: {len(df.columns)} | After removing the columns that contained missing values more than 10% of data points')
            print(f'Dropped columns = {cols_to_drop}')
            df_cleaned = df_cleaned.dropna(subset=miss_col)
        
        remaind_data_points = len(df_cleaned)
        print("")
        print(f'Number of deleted missing values: {initial_data_points - remaind_data_points}')
        print(f"Number of data points after missing value handling: {remaind_data_points}")
        print("")
        self.df = df_cleaned
        return True
    
    def save_data(self):
        """
        - To save the new dataframe
        """
        df = self.df
        file_path = self.file_path
        file_type = self.file_type
        if file_type == 'xlsx' or file_type == 'xls':
            df.reset_index(drop=True, inplace = True)
            df.to_excel(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        elif file_type == 'csv':
            df.reset_index(drop=True, inplace = True)
            df.to_csv(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        else: 
            print("Please use 'xlsx', 'xls' or 'csv' file")
            return False
        if file_type == 'xlsx':
            df.reset_index(drop=True, inplace = True)
            df.to_excel(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        elif file_type == 'csv':
            df.reset_index(drop=True, inplace = True)
            df.to_csv(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        else: 
            print("Please use 'xlsx' or 'csv' file")
            return False
        
    def data_anonymisation(self):
        """
        - To implement a dataframe anonymisation
        """
        df = self.df
        col1 = self.anon_col
        col2 = self.anon_col2
        file_path = self.file_path
        cols = self.anon_list
    
        def generate_unique_strings(prefix, series):
            unique_values = series.unique()
            key_mapping = {value: f"{prefix}{uuid.uuid4()}" for value in unique_values}
            return series.map(key_mapping), key_mapping
    
        df[col1], respondent_mapping = generate_unique_strings('respondent_', df[col1])
        df[col2], respondent_mapping = generate_unique_strings('enumerator_', df[col2])
        df.drop(columns = cols, inplace = True)
        original = self.file_path
        self.file_path = f'{file_path}_anonymised'
        self.save_data()
        self.file_path = original
        self.df = df
        print("The respondent name has been anonymised")
        return True
    
    def duplicates(self):
        """
        - To detect and remove duplicates
        """
        df = self.df
        col = self.identifiers
        duplicates = df[df.duplicated(subset=col, keep=False)]
        print("")
        print(f"Number of duplicate based on '{col}': {len(duplicates)}")

        if not duplicates.empty:
            print("Duplicate rows:")
            print(duplicates)
    
        df_cleaned = df.drop_duplicates(subset=col, keep='first')
    
        print(f"Number of data points: {len(df_cleaned)} | After removing duplicates")
        print("")
        self.df = df_cleaned
        return True

    def open_ended_cols(self):
        """
        - To save opened-ended columns and remove these from the dataset
        """
        df = self.df
        cols = self.opened_cols
        file_path = self.file_path_others
        empty_df = pd.DataFrame()
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            empty_df.to_excel(writer, sheet_name='basic', index=False)
        
            max_length = 0
            unique_data = {}

            for col in cols:
                unique_values = df[col].dropna().unique()
                unique_data[col] = unique_values
                max_length = max(max_length, len(unique_values))
        
            combined_df = pd.DataFrame({col: pd.Series(unique_data[col]) for col in cols})
            combined_df.to_excel(writer, sheet_name='open_ended', index=False)
        
        print(f"Open-ended columns have been saved to '{file_path}': {cols} ")
        df = df.drop(columns=cols)
        print(f'Number of columns: {len(df.columns)} | After removing the open-ended columns')
        self.df = df
        return True

    def columns_redefine(self):
        """
        - To change column names for smoother data analysis
        """
        df = self.df
        new_cols = self.cols_new
        file_path = f'{self.file_path}_columns_book.xlsx'
        original_cols = list(df.columns)
        df.columns = new_cols
    
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            empty_df = pd.DataFrame()
            empty_df.to_excel(writer, sheet_name='basic', index=False)

            columns_df = pd.DataFrame({'Column Names': new_cols,'Original Names': original_cols})
        
            columns_df.to_excel(writer, sheet_name='Column_Info', index=False)

            workbook = writer.book
            worksheet = workbook['Column_Info']
        
            for col in worksheet.columns:
                max_length = max(len(str(cell.value)) for cell in col)
                adjusted_width = max(max_length, 12)
                worksheet.column_dimensions[col[0].column_letter].width = adjusted_width

        print(f"Column information has been saved: {file_path}")
        self.df = df
        return True

    def age_group(self):
        """
        - To create new age group variable
        """
        df = self.df
        col = self.age_col
        bins = [0, 17, 24, 34, 44, 54, 64, float('inf')]
        labels = ['Below 18','18 - 24','25 - 34', '35 - 44', '45 - 54', '55 - 64', 'Above 65 years']
        df[col] = df[col].astype(int)
        df['Age Group'] = pd.cut(df[col], bins=bins, labels=labels, right=True)
        print('New age group variable (Age Group) has been created in this dataset')
        self.df = df
        return True
    
    def disability_wgss(self):
        """
        - To create disability group (based on the WG-SS)
        """
        df = self.df
        cols = self.diss_cols
        try:
            df['WG-Disability'] = ''
            
            def wg_ss(row, cols):
                values = row[cols]
                some_difficulty_count = (values == 'Some difficulty').sum()
                a_lot_of_difficulty = (values == 'A lot of difficulty').any() or (values == 'Cannot do at all').any()
                cannot_do_at_all = (values == 'Cannot do at all').any()
                if cannot_do_at_all:
                    return 'DISABILITY4'
                elif a_lot_of_difficulty:
                    return 'DISABILITY3'
                elif some_difficulty_count >= 2:
                    return 'DISABILITY2'
                elif some_difficulty_count >= 1:
                    return 'DISABILITY1'
                else:
                    return 'No_disability'
            df['WG-Disability'] = df.apply(lambda row: wg_ss(row, cols), axis=1)
            df['Disability'] = df['WG-Disability'].apply(lambda x: 'Disability' if x in ['DISABILITY4', 'DISABILITY3'] else 'No Disability')
            print('New disability variable (Disability) has been created in this dataset (Based on WG-SS)')
            self.df = df
            return True
        except Exception as e:
               print('New disability variable has not been created in this dataset')

    def grouping(self):
        df = self.df
        df['A3'] = df[['A3-1', 'A3-2', 'A3-3', 'A3-4', 'A3-5']].bfill(axis=1).iloc[:, 0]
        df['F9'] = df[['F9-1', 'F9-2']].bfill(axis=1).iloc[:, 0]
        df['F10'] = df[['F10-1', 'F10-2']].bfill(axis=1).iloc[:, 0]
        df['F11'] = df[['F11-1', 'F11-2']].bfill(axis=1).iloc[:, 0]
        df['F12'] = df[['F12-1', 'F12-2']].bfill(axis=1).iloc[:, 0]
        df['F13'] = df[['F13-1', 'F13-2']].bfill(axis=1).iloc[:, 0]
        df['F14'] = df[['F14-1', 'F14-2']].bfill(axis=1).iloc[:, 0]
        df['F15'] = df[['F15-1', 'F15-2']].bfill(axis=1).iloc[:, 0]
        self.df = df
        
    def L221(self):
        """
        - To calculate
        """
        df = self.df
        df['L221'] = pd.NA
        df.loc[df['0.Pathway'] == 'Young entrepreneurs', 'L221'] = 'Inadequate'
        try:
            df.loc[(df['0.Pathway'] == 'Young entrepreneurs') & (df['C9-b-10'] != 1), 'L221'] = 'Adequate'
            print('Indicator L2.1.1 variable has been created in this dataset')
            self.df = df
            return True
        except Exception as e:
               print('Indicator L2.1.1 variable has not been created in this dataset')
               
    def L311(self):
        """
        - To calculate
        """
        df = self.df
        df['L311'] = pd.NA
        df.loc[(df['0.Pathway'] == 'Recent university graduates') | (df['0.Pathway'] == 'NEET youths'), 'L311'] = 'Inadequate'
        try:
            df.loc[((df['0.Pathway'] == 'Recent university graduates') | (df['0.Pathway'] == 'NEET youths'))
                    & (df['D16'].isin(['Internships or apprenticeships', 
                            'Industrial attachments or workplace learning programs'])), 'L311'] = 'Adequate'
            print('Indicator L3.1.1 variable has been created in this dataset')
            self.df = df
            return True
        except Exception as e:
               print('Indicator L3.1.1 variable has not been created in this dataset')
               
    def L422(self):
        """
        - To calculate
        """
        df = self.df
        df['L422'] = 'Adequate'
        try:
            df.loc[(df['D16'].isin(['I have not accessed any of these services'])), 'L422'] = 'Inadequate'
            print('Indicator L4.2.2 variable has been created in this dataset')
            self.df = df
            return True
        except Exception as e:
               print('Indicator L4.2.2 variable has not been created in this dataset')
               
    def inclusion(self):
        """
        - To calculate
        """
        df = self.df
        
        df.loc[df['0.Pathway'] == 'Young entrepreneurs', 'gender_full'] = 'Not inclusive'
        df.loc[df['0.Pathway'] == 'Young entrepreneurs', 'youth_full'] = 'Not inclusive'
        df.loc[df['0.Pathway'] == 'Young entrepreneurs', 'youth_part'] = 'Not inclusive'
        df.loc[df['0.Pathway'] == 'Young entrepreneurs', 'gender_part'] = 'Not inclusive'
        df.loc[(df['0.Pathway'] == 'Young entrepreneurs') & (df['B16'] >= df['B15'] / 2), 'gender_full'] = 'Inclusive'
        df.loc[(df['0.Pathway'] == 'Young entrepreneurs') & (df['B20-b'] >= df['B20'] / 2), 'gender_part'] = 'Inclusive'
        df.loc[(df['0.Pathway'] == 'Young entrepreneurs') & (df['B17'] >= df['B15'] / 2), 'youth_full'] = 'Inclusive'
        df.loc[(df['0.Pathway'] == 'Young entrepreneurs') & (df['B20'] >= df['B19'] / 2), 'youth_part'] = 'Inclusive'
        self.df = df
        return True
 
    def scoring_ingongo(self):
        """
        - To calculate
        """
        df = self.df
        score_map1 = {'Strongly disagree': 1, 'Disagree': 2, 'Neither agree nor disagree': 3, 'Agree': 4, "Strongly agree":5}
        try:
            df['L321'] = pd.NA
            df['L353'] = pd.NA
            df['L221_soft'] = pd.NA
            df['L221_general'] = pd.NA
            df['L221_leadership'] = pd.NA
            df['L221_intermediate'] = pd.NA
            df['L221_advanced'] = pd.NA
            df['L221_business'] = pd.NA
            
            def scoring1(row):
                score = 0
                columns = ['C30', 'C31', 'C32', 'C33', 'C34', 'C35', 'C36', 'C37', 'C38', 'C39']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map1.get(row[col], 0)
                
                if score == 0:
                    return pd.NA
                else:
                    return score
                
            def scoring2(row):
                score = 0
                columns = ['F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'F24', 'F25']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map1.get(row[col], 0)
                if score == 0:
                    return pd.NA
                else:
                    return score
                
            def scoring3(row):
                score = 0
                columns = ['E1-1', 'E1-2', 'E1-3', 'E1-4', 'E1-5', 'E1-6', 'E1-7', 'E1-8']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map1.get(row[col], 0)
                if score == 0:
                    return pd.NA
                else:
                    return score 
                
            def scoring4(row):
                score = 0
                columns = ['E2-1', 'E2-2', 'E2-3', 'E2-4', 'E2-5', 'E2-6', 'E2-7', 'E2-8', 'E2-9',
                'E2-10', 'E2-11', 'E2-12', 'E2-13', 'E2-14', 'E2-15', 'E2-16', 'E2-17']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map1.get(row[col], 0)
                if score == 0:
                    return pd.NA
                else:
                    return score  
                
            def scoring5(row):
                score = 0
                columns = ['E3-1', 'E3-2', 'E3-3', 'E3-4', 'E3-5', 'E3-6', 'E3-7', 'E3-8']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map1.get(row[col], 0)
                if score == 0:
                    return pd.NA
                else:
                    return score  

            def scoring6(row):
                score = 0
                columns = ['E4-1', 'E4-2', 'E4-3', 'E4-4', 'E4-5', 'E4-6', 'E4-7', 'E4-8']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map1.get(row[col], 0)
                if score == 0:
                    return pd.NA
                else:
                    return score  

            def scoring7(row):
                score = 0
                columns = ['E5-1', 'E5-2', 'E5-3', 'E5-4', 'E5-5', 'E5-6', 'E5-7', 'E5-8', 'E5-9', 'E5-10']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map1.get(row[col], 0)
                if score == 0:
                    return pd.NA
                else:
                    return score 
                
            def scoring8(row):
                score = 0
                columns = ['E6-1', 'E6-2', 'E6-3', 'E6-4', 'E6-5', 'E6-6', 'E6-7']
                
                for col in columns:
                    if pd.notna(row[col]):
                        score += score_map1.get(row[col], 0)
                if score == 0:
                    return pd.NA
                else:
                    return score
            
            df['L321'] = df.apply(scoring1, axis=1)
            df['L353'] = df.apply(scoring2, axis=1)
            df['L221_soft'] = df.apply(scoring3, axis=1)
            df['L221_general'] = df.apply(scoring4, axis=1)
            df['L221_leadership'] = df.apply(scoring5, axis=1)
            df['L221_intermediate'] = df.apply(scoring6, axis=1)
            df['L221_advanced'] = df.apply(scoring7, axis=1)
            df['L221_business'] = df.apply(scoring8, axis=1)
            self.df = df
            return True
        except Exception as e:
               print('New variables has not been created in this dataset')

               
    def hired_youth(self):
        """
        - To calculate
        """
        df = self.df
        df['hired_youth'] = df['B17'].fillna(0) + df['B20'].fillna(0)
        self.df = df
        return True
    
    def foal(self):
        """
        - Feelings on aspects of life
        """
        df = self.df
        df['foal'] = df['F2'] + df['F3'] + df['F4'] + df['F6'] + df['F7'] + df['F8'] - round(df['F5']/2)
        self.df = df
        return True
    
    def industries(self):
        df = self.df
        industry_mapping = {
        'Agriculture forestry and fishing': 'Primary Industry',
        'Mining and quarrying': 'Primary Industry',
        'Manufacturing': 'Secondary Industry',
        'Electricity gas stream and air conditioning supply, water supply, gas and remediation services': 'Secondary Industry',
        'Construction': 'Secondary Industry',
        'Wholesale and retail trade; repair of motor vehicles and motorcycles': 'Wholesale, Retail, and Trade',
        'Transportation and storage': 'Transportation and Storage',
        'Accommodation and food services activities': 'Accommodation and Food Services',
        'Information and communication': 'Information and Communication',
        'Financial and insurance activities': 'Financial and Insurance Services',
        'Real estate activities': 'Real Estate and Business Services',
        'Professional, scientific and technical activities': 'Real Estate and Business Services',
        'Administrative and support activities': 'Real Estate and Business Services',
        'Public administration and defence; compulsory social security': 'Public Services and Social Care',
        'Education': 'Education',
        'Human health and social work activities': 'Public Services and Social Care',
        'Arts, entertainment and recreation': 'Culture, Arts, and Recreation',
        "Other" : 'Other',
        'Activities of households as employers': 'Other',
        'Activities of extraterritorial organizations and bodies': 'Other'}
        df['B4-2'] = df['B4'].map(industry_mapping)
        df['B7-2'] = df['B7'].map(industry_mapping)
        self.df = df
        return True
        
    def processing(self):
        """
        - To conduct data pre-processing
        1. Load the raw dataset
        2. Re-define variable names
        3. Handle duplicates
        4. Anonymise data (Respondents' names)
        5. Remove pilot test data points
        6. Drop unnecessary columns
        7. Handle missing values
        8. Extract answers from open-ended questions
        9. Create age and disability groups
        10. Save the cleaned dataset
        """
        self.data_load()
        self.columns_redefine()
        print(f'Initial data points: {len(self.df)}')
        self.duplicates()
        self.data_anonymisation()
        if len(self.dates) != 0:
            self.date_filter()
        print(f'Initial number of columns: {len(self.df.columns)}')
        self.delete_columns()
        self.missing_value_clean()
        self.open_ended_cols()
        if self.age_col != None:
            self.age_group()
        if self.diss_cols != None:
            self.disability_wgss()
        self.grouping()
        self.L221()
        self.L311()
        self.L422()
        self.scoring_ingongo()
        self.hired_youth()
        self.foal()
        self.inclusion()
        self.industries()
        original = self.file_path
        self.file_path = f'{self.file_path}_cleaned'
        self.save_data()
        self.file_path = original
        print("")
        print(f'Final number of data points: {len(self.df)}')
        print(f"Cleaned dataframe has been saved: {self.file_path}_cleaned.{self.file_type}")
        return True