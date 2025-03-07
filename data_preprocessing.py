#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thurs Jan 16 11:18:51 2025

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please define the parameters for data preprocessing pipeline
"""
import bodhi_data_preprocessing as dp

project_name = "DOT Rwanda - DSE Baseline"

file_type = 'xlsx' 
# Original data format: xlsx, xls, csv

file_path = "Data/raw"
# Original data location and name (excluding file extension): "Data/(name)"

file_path_others = "Data/24-DOT-RW-1 - Open-End.xlsx"
# Specify the path and name of the Excel sheet where the values from the open-ended columns will be saved (New file)
# For example: "Data/(project name) others.xlsx"

enumerator_name = 'Enumerator Name'
respondent_name = 'A1'
# Original column name for enumerators' names (for anonymisation and duplicate removal)

identifiers = ['Enumerator Name','A1', 'start', '_id', '_uuid']
# Identifiers for detecting duplicates (list, do not remove respondent_name)
# Recommendation: At least three identifiers

dates = []
# Remove the dates on which the pilot test was conducted from the data
# for example ['2024-07-18', '2024-07-22', '2024-07-23']

cols_new = ['start','end','start-geopoint','latitude', 'longitude', 'altitude', 'precision', 'today', 'deviceid',
 'Enumerator Name', 'Enumerator Code', 'Consent1','Consent2', 'Consent3', 'Consent4',
 '0.Pathway', 'A1', 'A2-1', 'A2-2', 'A3-1', 'A3-2', 'A3-3', 'A3-4', 'A3-5', 'Sector', 'Cell', 'Village', 'EA1', 'EA2',
 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A11-o', 'A12', 'A12-o',
 'A13', 'A14', 'A15', 'A16-1', 'A16-2', 'A16-3', 'A16-4', 'A16-5', 'A16-6',
 'A17-a', 'A17-b', 'A18', 'A18-o', 'A19', 'A20', 'A21-a',
 'A21-1', 'A21-2', 'A21-3', 'A21-4', 'A21-5', 'A21-6', 'A21-7', 'A21-8', 'A21-9', 'A22', 'A23', 'A23-o',
 'B1-a', 'B1-1', 'B1-2', 'B1-3', 'B1-4', 'B2', 'B2-o', 'B3', 'B3-1', 'B4', 'B4-o',
 'B5', 'B6', 'B6-1', 'B7', 'B7-o', 'B8', 'B9-1', 'B9-1o', 'B9-2', 'B10', 'B11', 'B12', 'B13',
 'B14-1', 'B14-2', 'B15', 'B16', 'B17', 'B17-a', 'B18', 'B19', 'B20', 'B20-a', 'B20-b',
 'B21', 'B22', 'B23', 'C1', 'C2-a', 'C2-1', 'C2-2', 'C2-3', 'C2-4', 'C2-5', 'C3', 'C4', 'C5',
 'C6-a', 'C6-b-a', 'C6-b-1', 'C6-b-2', 'C6-b-3', 'C6-b-4', 'C6-b-5', 'C7-1', 'C7-2', 'C7-3', 'C7-4', 'C7-5', 'C7-6',
 'C8a', 'C8-1', 'C8-2', 'C8-3', 'C8-4', 'C8-5', 'C8-6', 'C8-7','C8-8', 'C8-o', 'C9-a', 'C9-a-o',
 'C9-b-a', 'C9-b-1', 'C9-b-2', 'C9-b-3', 'C9-b-4', 'C9-b-5', 'C9-b-6', 'C9-b-7', 'C9-b-8', 'C9-b-9', 'C9-b-10', 'C9-b-o',
 'C10', 'C11', 'C12', 'C13', 'C13-o', 'C14', 'C14-o', 'C15', 'C16', 'C17', 'C18', 'C18-o',
 'C19', 'C20', 'C20-o', 'C21', 'C22', 'C23-a', 'C23-1', 'C23-2', 'C23-3', 'C23-4', 'C23-5', 'C23-6', 'C23-7',
 'C23-8', 'C23-9', 'C23-o', 'C24-a', 'C24-1', 'C24-2', 'C24-3', 'C24-4', 'C24-5', 'C24-6', 'C24-7', 'C24-8', 'C24-o',
 'C25-a', 'C25-1', 'C25-2', 'C25-3', 'C25-4', 'C25-5', 'C25-o','C26', 'C27', 'C28', 'C29', 'C30', 'C31',
 'C32', 'C33', 'C34', 'C35', 'C36', 'C37', 'C38', 'C39', 'D1', 'D2','D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9',
 'D10a', 'D10-1', 'D10-2', 'D10-3', 'D10-4', 'D10-5', 'D10-6', 'D10-7', 'D10-8', 'D10-9', 'D10-10', 'D10-11', 'D10-o',
 'D11a', 'D11-1', 'D11-2', 'D11-3', 'D11-4', 'D11-5', 'D11-6', 'D11-7', 'D11-8', 'D11-9', 'D11-o',
 'D12a', 'D12-1', 'D12-2','D12-3', 'D12-4', 'D12-5', 'D12-6', 'D12-o', 'D13', 'D13-o',
 'D14-a-a','D14-a-1', 'D14-a-2', 'D14-a-3', 'D14-a-4', 'D14-a-5', 'D14-a-o', 'D14-b-a', 'D14-b-1', 'D14-b-2',
 'D14-b-3', 'D14-b-4', 'D14-b-5', 'D14-b-o', 'D14-c-a', 'D14-c-1', 'D14-c-2', 'D14-c-3', 'D14-c-4', 'D14-c-5', 'D14-c-6', 'D14-c-o',
 'D15a', 'D15-1', 'D15-2', 'D15-3', 'D15-4', 'D15-5', 'D15-6','D15-7', 'D15-8', 'D15-9', 'D15-o', 'D16', 'D16-o',
 'D17','D18', 'D19', 'D20', 'E1-1', 'E1-2', 'E1-3', 'E1-4', 'E1-5', 'E1-6', 'E1-7', 'E1-8', 'E2-1', 'E2-2', 'E2-3',
 'E2-4', 'E2-5', 'E2-6', 'E2-7', 'E2-8', 'E2-9', 'E2-10', 'E2-11', 'E2-12', 'E2-13', 'E2-14', 'E2-15', 'E2-16', 'E2-17',
 'E3-1', 'E3-2', 'E3-3', 'E3-4', 'E3-5', 'E3-6', 'E3-7', 'E3-8', 'E4-1', 'E4-2', 'E4-3', 'E4-4', 'E4-5', 'E4-6', 'E4-7', 'E4-8',
 'E5-1', 'E5-2', 'E5-3', 'E5-4', 'E5-5', 'E5-6', 'E5-7', 'E5-8', 'E5-9', 'E5-10',
 'E6-1', 'E6-2', 'E6-3', 'E6-4', 'E6-5', 'E6-6', 'E6-7', 'F1-1', 'F1-2', 'F1-3', 'F1-4', 'F1-5',
 'F1-6', 'F1-7', 'F1-8', 'F1-9', 'F1-10', 'F1-11', 'F1-12', 'F1-13', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F2-o',
 'F9-1', 'F10-1', 'F11-1', 'F12-1', 'F13-1', 'F14-1', 'F15-1', 'F9-2', 'F10-2', 'F11-2', 'F12-2', 'F13-2', 'F14-2', 'F15-2',
 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'F24', 'F25',
 'G1-a', 'G1-1', 'G1-2', 'G1-3', 'G1-4','G1-5', 'G1-6', 'G1-7', 'G1-8', 'G2a', 'G2-1', 'G2-2', 'G2-3', 'G2-4', 'G2-5', 'G2-6', 'G2-7', 'G2-8',
 'G3a', 'G3-1', 'G3-2', 'G3-3', 'G3-4', 'G3-5', 'G3-6', 'G3-7', 'G3-8', 'G3-9', 'G3-10', 'G3-o', 'G4', 'G4-o', 'G5-1a',
 'G5-1-1', 'G5-1-2', 'G5-1-3', 'G5-1-4', 'G5-1-5', 'G5-1-6', 'G5-1-7', 'G5-1-8', 'G5-1-9', 'G5-1o',
 'G5-2a', 'G5-2-1', 'G5-2-2', 'G5-2-3', 'G5-2-4', 'G5-2-5', 'G5-2-6', 'G5-2-7', 'G5-2o', 'G6', 'G7', 'G8a', 'G8-1',
 'G8-2', 'G8-3', 'G8-4', 'G8-5', 'G8-6', 'G8-7', 'G8-8', 'G8-o', 'G9a', 'G9-1', 'G9-2', 'G9-3',
 'G9-4', 'G9-5', 'G9-6', 'G9-7', 'G9-8', 'G9-o', 'G10', 'G10-o', 'G11', 'G12','G13', 'G14', 'G15', 'G16', 'G17', 'G11-o',
 'comments', 'GPS', '_GPS_latitude', '_GPS_longitude', '_GPS_altitude', '_GPS_precision', 'background-audio',
 'background-audio_URL', 'A17_b_Do_you_have_internet_ac', 'A18_Who_owns_the_device_you_u', 'A18_1_If_other_please_specify',
 'B15_Is_your_business_a_commer', 'B16_When_did_you_fi_mercial_registration', 'B13_Do_you_have_a_Taxpayer_Id', 'B14_If_yes_to_TIN_rst_receive_your_TIN',
 'B19_a_How_many_of_them_are_male','B20_a_How_many_of_them_are_male', 'C7_Which_of_these_b_o_you_know_how_to_do',
 'C7_Which_of_these_b_o_you_know_how_to_do/how_to_use_a_balance_sheet_to_determine_',
 'C7_Which_of_these_b_o_you_know_how_to_do/how_to_analyse_my_business_records_to_in',
 'C7_Which_of_these_b_o_you_know_how_to_do/how_to_develop_marketing_plans_that_are_',
 'C7_Which_of_these_b_o_you_know_how_to_do/how_to_overcome_slow_periods_my_business',
 'C7_Which_of_these_b_o_you_know_how_to_do/how_to_make_my_product_service_more_prof',
 'C7_Which_of_these_b_o_you_know_how_to_do/how_to_perform_a_risk_assessment_to_ensu',
 'C7_Which_of_these_b_o_you_know_how_to_do/none_of_the_above', 'C7a_To_what_extent_Customer_Engagement',
 'C7b_To_what_extent_Product_Development', 'C7c_To_what_extent_egic_Business_Growth', '_id', '_uuid', '_submission_time',
    '_validation_status', '_notes', '_status', '_submitted_by', '__version__', '_tags','_index']
# Specify new column names for data analysis (ensure they match the exact order of the existing columns)

list_del_cols = ['start','end', 'today', 'deviceid',
                 'Enumerator Name', 'Sector', 'Cell', 'Village', 'EA1', 'EA2','A21-a','C2-a', 'C6-b-a',
                 'C8a', 'C9-b-a', 'C23-a', 'C24-a', 'C25-a', 'D10a', 'D11a',
                 'D12a', 'D14-a-a', 'D14-b-a', 'D14-c-a', 'D15a', 'F2-o', 'G1-a', 'G2a', 'G3a', 'G5-1a',
                 'G5-2a', 'G8a', 'G9a', 'G11-o', 'A17_b_Do_you_have_internet_ac', 'A18_Who_owns_the_device_you_u', 'A18_1_If_other_please_specify',
                 'B15_Is_your_business_a_commer', 'B16_When_did_you_fi_mercial_registration', 'B13_Do_you_have_a_Taxpayer_Id', 'B14_If_yes_to_TIN_rst_receive_your_TIN',
                 'B19_a_How_many_of_them_are_male','B20_a_How_many_of_them_are_male', 'C7_Which_of_these_b_o_you_know_how_to_do',
                 'C7_Which_of_these_b_o_you_know_how_to_do/how_to_use_a_balance_sheet_to_determine_',
                 'C7_Which_of_these_b_o_you_know_how_to_do/how_to_analyse_my_business_records_to_in',
                 'C7_Which_of_these_b_o_you_know_how_to_do/how_to_develop_marketing_plans_that_are_',
                 'C7_Which_of_these_b_o_you_know_how_to_do/how_to_overcome_slow_periods_my_business',
                 'C7_Which_of_these_b_o_you_know_how_to_do/how_to_make_my_product_service_more_prof',
                 'C7_Which_of_these_b_o_you_know_how_to_do/how_to_perform_a_risk_assessment_to_ensu',
                 'C7_Which_of_these_b_o_you_know_how_to_do/none_of_the_above', 'C7a_To_what_extent_Customer_Engagement',
                 'C7b_To_what_extent_Product_Development', 'C7c_To_what_extent_egic_Business_Growth', '_id', '_uuid', '_submission_time',
                    '_validation_status', '_notes', '_status', '_submitted_by', '__version__', '_tags','_index']
# Specify the columns to be excluded from the data analysis

miss_col = ['0.Pathway', 'A2-1', 'A2-2', 'A4','A5','A9', 'A11','A13', 'A16-1', 'A16-2', 'A16-3', 'A16-4', 'A16-5', 'A16-6']
# Specify all columns that apply to all respondents for missing value detection

open_cols = ['A11-o','A12-o','A18-o','A20','A23-o','B2-o','B4-o','B7-o','B9-1o','C8-o','C9-a-o', 'C9-b-o', 'C13-o',
             'C14-o', 'C18-o', 'C20-o', 'C23-o', 'C24-o', 'C25-o', 'D10-o','D11-o', 'D12-o', 'D13-o', 'D14-a-o',
             'D14-b-o', 'D14-c-o', 'D15-o', 'D16-o', 'G3-o', 'G4-o', 'G5-1o', 'G5-2o', 'G7','G8-o', 'G9-o', 'G10-o', 'comments']
# Specify the open-ended columns (which will be saved in a separate Excel sheet and removed from the data frame)

age_col = 'A5'
# If we don't have age group in this dataset, please specify the age columns (as str)

diss_cols = ['A16-1', 'A16-2', 'A16-3', 'A16-4', 'A16-5', 'A16-6']
# If we have WG-SS questions in the dataset, please specify the columns (as list [])

anon_cols = ['GPS', '_GPS_latitude', '_GPS_longitude', '_GPS_altitude', '_GPS_precision','background-audio','background-audio_URL','start-geopoint','latitude', 'longitude', 'altitude', 'precision','Enumerator Code', 'Consent1','Consent2', 'Consent3', 'Consent4', 'A7']
# Columns need to be dropped for the data anonymisation


"""
Run the pipeline for data preprocessing
del_type = 0 or 1
-> 0: Remove all missing values from the columns where missing values are detected
-> 1: First, remove columns where missing values make up 10% or more of the total data points
      Then, remove all remaining missing values from the columns where they are detected
"""

ingongo = dp.Preprocessing(project_name, file_path, file_path_others, list_del_cols, dates, miss_col, respondent_name, enumerator_name, identifiers, open_cols, cols_new, anon_cols, age_col, diss_cols, del_type = 0, file_type=file_type)
ingongo.processing()