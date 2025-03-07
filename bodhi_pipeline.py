#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thurs Jan 16 15:52:03 2025

@author: Bodhi Global Analysis
"""

import bodhi_indicator as bd
import bodhi_PMF as pmf
import pandas as pd

"""
Evaluation
"""
# Specify the file path for the clean dataset
df = pd.read_excel('data/raw_cleaned.xlsx')
indicators = []

# Create indicators and provide additional details as needed (Evaluation)
def descriptive_statistics(df, indicators):
    
    s_location = bd.Indicator(df, "Location", 0, ['A2-1'], i_cal=None, i_type='count', description='Location (Rwanda)', period='baseline', target = None)
    s_location.add_var_order(['Urban', 'Peri-urban', 'Rural'])
    indicators.append(s_location)
    
    s_region = bd.Indicator(df, "Province", 0, ['A2-2'], i_cal=None, i_type='count', description='Province (Rwanda)', period='baseline', target = None)
    s_region.add_var_order(['Kigali City', 'Western Province', 'Southern Province','Eastern Province','Northern Province'])
    indicators.append(s_region)

    s_gender = bd.Indicator(df, "Gender", 0, ['A4'], i_cal=None, i_type='count', description='Gender distribution', period='baseline', target = None)
    s_gender.add_breakdown({'A2-2':'Province'})
    s_gender.add_var_order(['Female', 'Male'])
    indicators.append(s_gender)
    
    s_age = bd.Indicator(df, "Age group", 0, ['Age Group'], i_cal=None, i_type='count', description='Age distribution', period='baseline', target = None)
    s_age.add_breakdown({'A4':'Gender', 'A2-2':'Province'})
    s_age.add_var_order(['18 - 24','25 - 34', '35 - 44', '45 - 54', '55 - 64', 'Above 65 years'])
    indicators.append(s_age)
    
    s_head = bd.Indicator(df, "Household head", 0, ['A11'], i_cal=None, i_type='count', description='Household head', period='baseline', target = None, visual = False)
    s_head.add_breakdown({'A4':'Gender', 'A2-2':'Province','Age Group':"Age group"})
    s_head.add_var_order(['You (respondent)', "Respondent's spouse", "Respondent's father",
                          "Respondent's mother","Respondent's son","Respondent's daughter","Other relatives","Other"])
    indicators.append(s_head)
    
    s_disability = bd.Indicator(df, "Disability", 0, ['Disability'], i_cal=None, i_type='count', description='Disability status', period='baseline', target = None)
    s_disability.add_breakdown({'A4':'Gender', 'A2-2':'Province','Age Group':"Age group"})
    s_disability.add_var_order(['No Disability', 'Disability'])
    indicators.append(s_disability)
    
    s_residency = bd.Indicator(df, "Residency situation", 0, ['A12'], i_cal=None, i_type='count', description='Residency status', period='baseline', target = None, visual = False)
    s_residency.add_breakdown({'A4':'Gender', 'A2-2':'Province','Age Group':"Age group", 'Disability':'Disability'})
    s_residency.add_var_order(['Citizen', 'Refugee',"Asylum Seeker"])
    indicators.append(s_residency)
    
    s_rtype = bd.Indicator(df, "Respondent type", 0, ['0.Pathway'], i_cal=None, i_type='count', description='Respondents Pathway', period='baseline', target = None)
    s_rtype.add_breakdown({'A4':'Gender', 'A2-2':'Province','Age Group':"Age group", 'Disability':'Disability','A12':'Residency'})
    s_rtype.add_var_order(['Recent university graduates', 'NEET youths','Young entrepreneurs',
                           'Refugee youth','Youth leaders'])
    indicators.append(s_rtype)  
    
    s_district = bd.Indicator(df, "District", 0, ['A3'], i_cal=None, i_type='count', description='District', period='baseline', target = None, visual = False)
    s_district.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province'})
    indicators.append(s_district)

    s_internet = bd.Indicator(df, "Internet access", 0, ['A17-a'], i_cal=None, i_type='count', description='Internet access', period='baseline', target = None)
    s_internet.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    s_internet.add_var_order(['Yes', 'No'])    
    indicators.append(s_internet)
    
    s_internet2 = bd.Indicator(df, "Internet connection", 0, ['A17-b'], i_cal=None, i_type='count', description='Internet condition', period='baseline', target = None)
    s_internet2.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    s_internet2.add_var_order(['Yes', 'No'])    
    indicators.append(s_internet2)
    
    s_internet3 = bd.Indicator(df, "Internet device", 0, ['A18'], i_cal=None, i_type='count', description='How do you access the internet?', period='baseline', target = None, visual = False)
    s_internet3.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    s_internet3.add_var_order(['I own a phone that I use to access the internet', 'I own a computer that I use to access the internet',"I don’t own a phone but share one with someone in my household",
                               "I have a sim card and occasionally borrow a phone to use it","I go to a cyber/internet cafe to access internet","Other"])    
    indicators.append(s_internet3)
    """    
    wage_field = bd.Indicator(df, "Wage Field", 0, ['B4-2'], i_cal=None, i_type='count', description='Wage Employment - Sector', period='baseline', target = None, visual = False)
    wage_field.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    wage_field.add_var_order(["Primary Industry",
                              "Secondary Industry",
                              "Wholesale, Retail, and Trade",
                              "Transportation and Storage",
                              "Accommodation and Food Services",
                              "Information and Communication",
                              "Financial and Insurance Services",
                              "Real Estate and Business Services",
                              "Public Services and Social Care",
                              "	Culture, Arts, and Recreation",
                              "Education",
                              "Other"])    
    indicators.append(wage_field)
    
    business_field = bd.Indicator(df, "Business Field", 0, ['B9-1'], i_cal=None, i_type='count', description='Youth Business - Sector', period='baseline', target = None, visual = False)
    business_field.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    business_field.add_var_order(["Agriculture",
                                  "Construction",
                                  "Arts, Media, and Creative Industries",
                                  "Food and Beverage",
                                  "Retail and Trade",
                                  "Crafts, Clothing and Textiles",
                                  "Education and Training",
                                  "Social enterprises",
                                  "Healthcare",
                                  "Tourism and Hospitality",
                                  "Technology and Digital Services",
                                  "Manufacturing",
                                  "Professional services",
                                  "Transportation",
                                  "Other"])    
    indicators.append(business_field)
    
    L221 = bd.Indicator(df, "L2.2.1", 0, ['L221'], i_cal=None, i_type='count', description='L2.2.1: Number of enterprises/groups accessing financial products/services', period='baseline', target = None)
    L221.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    L221.add_var_order(["Adequate","Inadequate"])    
    indicators.append(L221)
    
    L311 = bd.Indicator(df, "L3.1.1", 0, ['L311'], i_cal=None, i_type='count', description='L3.1.1: Number of youth accessing employment services or products', period='baseline', target = None)
    L311.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    L311.add_var_order(["Adequate","Inadequate"])    
    indicators.append(L311)
    
    L422 = bd.Indicator(df, "L4.2.2", 0, ['L422'], i_cal=None, i_type='count', description='L4.2.2: Number of participants in stakeholder and partner convenings', period='baseline', target = None)
    L422.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    L422.add_var_order(["Adequate","Inadequate"])    
    indicators.append(L422)
    
    L431 = bd.Indicator(df, "L4.3.1", 0, ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'], i_cal='score_sum', i_type='count', description='L4.3.1: Number of youth in dignified and fulfilling work', period='baseline', target = None)
    L431.add_score_map({'Strongly disagree': 1, 'Disagree': 2, 'Neither agree nor disagree': 3, 'Agree': 4, "Strongly agree":5})
    L431.add_valid_point(32)
    L431.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    L431.add_var_change({"Pass":"Adequate", "Not Pass":"Inadequate"})
    L431.add_var_order(['Adequate', 'Inadequate'])
    indicators.append(L431)
    
    L511 = bd.Indicator(df, "L5.1.1", 0, ['F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15'], i_cal='score_sum', i_type='count', description='L5.1.1: Views of youth on their abilities to access and participate in the growth of the sector and/or their communities', period='baseline', target = None)
    L511.add_score_map({'Strongly disagree': 1, 'Disagree': 2, 'Neither agree nor disagree': 3, 'Agree': 4, "Strongly agree":5})
    L511.add_valid_point(25)
    L511.add_condition((df['A4'] == "Female") | (df['Disability'] == 'Disability') | (df['A13'] == 'Refugee') | (df['A13'] == 'Asylum Seeker'))
    L511.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    L511.add_var_change({"Pass":"Adequate", "Not Pass":"Inadequate"})
    L511.add_var_order(['Adequate', 'Inadequate'])
    indicators.append(L511)

    L211_s = bd.Indicator(df, "L2.1.1 Soft", 0, ['L221_soft'], i_cal='divide', i_type='percentage', description='L2.1.1: Soft skills', period='baseline', target = None)
    L211_s.add_valid_point({20: 'Low level', (20, 35): 'Moderate level', 35: 'High level'})
    L211_s.add_var_order(['Low level', 'Moderate level', 'High level'])
    L211_s.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(L211_s)
    
    L211_g = bd.Indicator(df, "L2.1.1 General", 0, ['L221_general'], i_cal='divide', i_type='percentage', description='L2.1.1: General skills', period='baseline', target = None)
    L211_g.add_valid_point({35: 'Low level', (35, 65): 'Moderate level', 65: 'High level'})
    L211_g.add_var_order(['Low level', 'Moderate level', 'High level'])
    L211_g.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(L211_g)
    
    L211_y = bd.Indicator(df, "L2.1.1 Leadership", 0, ['L221_leadership'], i_cal='divide', i_type='percentage', description='L2.1.1: Youth leadership skills', period='baseline', target = None)
    L211_y.add_valid_point({20: 'Low level', (20, 35): 'Moderate level', 35: 'High level'})
    L211_y.add_var_order(['Low level', 'Moderate level', 'High level'])
    L211_y.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(L211_y)
    
    L211_i = bd.Indicator(df, "L2.1.1 Intermediate", 0, ['L221_intermediate'], i_cal='divide', i_type='percentage', description='L2.1.1: Intermediate digital skills', period='baseline', target = None)
    L211_i.add_valid_point({20: 'Low level', (20, 35): 'Moderate level', 35: 'High level'})
    L211_i.add_var_order(['Low level', 'Moderate level', 'High level'])
    L211_i.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(L211_i)
    
    L211_a = bd.Indicator(df, "L2.1.1 Advanced", 0, ['L221_advanced'], i_cal='divide', i_type='percentage', description='L2.1.1: Advanced digital skills', period='baseline', target = None)
    L211_a.add_valid_point({20: 'Low level', (20, 35): 'Moderate level', 35: 'High level'})
    L211_a.add_var_order(['Low level', 'Moderate level', 'High level'])
    L211_a.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(L211_a)
    
    L211_b = bd.Indicator(df, "L2.1.1 Business", 0, ['L221_business'], i_cal='divide', i_type='percentage', description='L2.1.1: Business skills', period='baseline', target = None)
    L211_b.add_valid_point({15: 'Low level', (15, 25): 'Moderate level', 25: 'High level'})
    L211_b.add_var_order(['Low level', 'Moderate level', 'High level'])
    L211_b.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(L211_b)

    L411 = bd.Indicator(df, "L4.1.1_Employment", 0, ['B1-1','B1-2','B1-3','B1-4'], i_cal=None, i_type='count', description='L4.1.1: Number of employed youth (wage employment)', period='baseline', target = None, visual = False)
    L411.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    L411.add_var_change({1: "Yes", 0: "No"})
    L411.add_var_order([1, 0])
    L411.add_label(['Yes – Self Employed', "Yes – Own Business","Yes – Wage Employed", "No"])    
    indicators.append(L411)
    
    wage_type = bd.Indicator(df, "Research3.1_wage", 0, ["B3"], i_cal=None, i_type='count', description='Research question 3.1: For your wage employment in 2024, which type of wage employment did you have?', period='baseline', target = None)
    wage_type.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    wage_type.add_var_order(["Full-time employment","Part-time employment",
                             "Seasonal","Casual"])
    indicators.append(wage_type)
    
    self_type = bd.Indicator(df, "Research3.1_self", 0, ["B6"], i_cal=None, i_type='count', description='Research question 3.1: For your self-employment in 2024, which type of wage employment did you have?', period='baseline', target = None, visual = False)
    self_type.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    self_type.add_var_order(["Full-time employment","Part-time employment",
                             "Seasonal","Casual"])
    indicators.append(self_type)
    
    L531 = bd.Indicator(df, "L5.3.1", 0, ['F1-1', 'F1-2', 'F1-3', 'F1-4', 'F1-5', 'F1-6', 'F1-7', 'F1-8', 'F1-9', 'F1-10', 'F1-11', 'F1-12', 'F1-13'], i_cal=None, i_type='count', description='L5.3.1: Share of individuals reporting improvements in their own well-being', period='baseline', target = None)
    L531.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    L531.add_var_order(['No access/Very difficult', "Difficult","Moderate", "Easy", "Very easy"])
    L531.add_label(['Food', "Healthcare", "Clean water","Safe sanitation", "Electricity", "Roads and trading points",
                    "Open a bank account", "Loans", "Internet", "Telephone services", "Transport services", "Places in nature to enjoy",
                    "Educational services"])
    indicators.append(L531)
    
    R12_p1 = bd.Indicator(df, "Research1.2_P1", 0, ["C26","C27","C28","C29"], i_cal=None, i_type='count', description='Research question 1.2: Perception 1', period='baseline', target = None)
    R12_p1.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R12_p1.add_var_order(['Strongly disagree', "Disagree","Neither agree nor disagree", "Agree", "Strongly agree"])
    R12_p1.add_label(["Using digital tools or technology is critical for the success of my business",
                      "I feel that youth-focused business support programs are effective in helping young entrepreneurs succeed",
                      "I feel that I lack access to the financial resources needed to start or grow my business",
                      "I feel confident that I could overcome my business challenges if I had access to the right resources and support"])
    indicators.append(R12_p1)
    
    R12_p2 = bd.Indicator(df, "Research1.2_P2", 0, ["D17","D18","D19","D20"], i_cal=None, i_type='count', description='Research question 1.2: Perception 2', period='baseline', target = None)
    R12_p2.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R12_p2.add_var_order(['Strongly disagree', "Disagree","Neither agree nor disagree", "Agree", "Strongly agree"])
    R12_p2.add_label(["Youth in Rwanda have access to opportunities to gain the digital skills needed by employers",
                      "Employers in Rwanda value digital skills as an essential requirement for jobs",
                      "Employers in the ICT sector are willing to hire youth with limited work experience if they have relevant digital skills",
                      "Young women face more barriers to accessing employment in the ICT sector than men"])
    indicators.append(R12_p2)  
    
    R12_p3 = bd.Indicator(df, "Research1.2_P3", 0, ["G11","G12","G13","G14","G15","G16","G17"], i_cal=None, i_type='count', description='Research question 1.2: Perception 3', period='baseline', target = None)
    R12_p3.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R12_p3.add_var_order(['Strongly disagree', "Disagree","Neither agree nor disagree", "Agree", "Strongly agree"])
    R12_p3.add_label(["Gaining digital skills and/or business skills training would improve my ability to find employment or start a business",
                      "Digital and business skills training are important for improving youth livelihoods in my community",
                      "The digital and business skills training programs currently available in my area are accessible to youth like me",
                      "The existing digital and business skills training programs in my area are effective in preparing youth for employment or running their own business",
                      "I am likely to attend a digital skills and/or business skills training program if it becomes available",
                      "I feel confident that I would overcome barriers to attend training programs if they were offered",
                      "Digital and business skills training programs are equally accessible to women and vulnerable groups in my community"])
    indicators.append(R12_p3)
    
    R12_outcomes = bd.Indicator(df, "Research1.2_outcomes", 0, ['G9-1', 'G9-2', 'G9-3','G9-4', 'G9-5', 'G9-6', 'G9-7', 'G9-8'], i_cal=None, i_type='count', description='Research question 1.2: Expected outcomes', period='baseline', target = None, visual = False)
    R12_outcomes.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R12_outcomes.add_var_change({1: "Yes", 0: "No"})
    R12_outcomes.add_var_order([1, 0])
    R12_outcomes.add_label(["Better digital skills aimed at employability",
                                "High income potential",
                                "Improved job opportunities",
                                "More social connections, including networking opportunities",
                                "Increased confidence in starting/running a business",
                                "Better resilience",
                                "Better mental well-being",
                                "Other"])
    indicators.append(R12_outcomes)
    
    R12_challenges = bd.Indicator(df, "Research1.2_challenges", 0, ["G10"], i_cal=None, i_type='count', description='Research question 1.2: Expected challenges', period='baseline', target = None, visual = False)
    R12_challenges.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R12_challenges.add_var_order(["Lack of access to funding to apply the skills learned",
                                  "Limited access to necessary technology or tools",
                                  "Lack of mentorship or ongoing support after training",
                                  "High competition in the industry or market",
                                  "Lack of confidence to apply the skills",
                                  "Family or community responsibilities that limit my time",
                                  "Cultural or social barriers (e.g., stigma)",
                                  "Other"])
    indicators.append(R12_challenges)
    
    R2_add = bd.Indicator(df, "Research1_add", 0, ['C25-1', 'C25-2', 'C25-3', 'C25-4', 'C25-5'], i_cal=None, i_type='count', description='Research question 2: What types of training would most benefit your business?', period='baseline', target = None, visual = False)
    R2_add.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R2_add.add_var_change({1: "Yes", 0: "No"})
    R2_add.add_var_order([1, 0])
    R2_add.add_label(["Financial management and budgeting",
                          "Digital marketing and online sales",
                          "Customer service and relationship management",
                          "Business planning and strategy development",
                          "Other"])
    indicators.append(R2_add)
    
    R21_1 = bd.Indicator(df, "Research2.1_1", 0, ['G1-1', 'G1-2', 'G1-3', 'G1-4','G1-5', 'G1-6', 'G1-7', 'G1-8'], i_cal=None, i_type='count', description='Research question 2.1: What are the primary sources of digital skills training programs in your area?', period='baseline', target = None, visual = False)
    R21_1.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R21_1.add_var_change({1: "Yes", 0: "No"})
    R21_1.add_var_order([1, 0])
    R21_1.add_label(["Government programs",
                         "NGO-led programs",
                         "Online courses",
                         "Private training centres",
                         "Vocational schools or Technical colleges",
                         "University",
                         "Informal mentorship or apprenticeship",
                         "None"])
    indicators.append(R21_1)
    
    R21_2 = bd.Indicator(df, "Research2.1_2", 0, ['G2-1', 'G2-2', 'G2-3', 'G2-4', 'G2-5', 'G2-6', 'G2-7', 'G2-8'], i_cal=None, i_type='count', description='Research question 2.1: What are the primary sources of business skills training programs in your area?', period='baseline', target = None, visual = False)
    R21_2.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R21_2.add_var_change({1: "Yes", 0: "No"})
    R21_2.add_var_order([1, 0])
    R21_2.add_label(["Government programs",
                         "NGO-led programs",
                         "Online courses",
                         "Private training centres",
                         "Vocational schools or Technical colleges",
                         "University",
                         "Informal mentorship or apprenticeship",
                         "None"])
    indicators.append(R21_2)
    
    R22_barriers = bd.Indicator(df, "Research2.2_b", 0, ["G4"], i_cal=None, i_type='count', description='Research question 2.2: What are the biggest barriers to youth accessing digital skills or business skills training programs?', period='baseline', target = None, visual = False)
    R22_barriers.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R22_barriers.add_var_order(["Financial constraints",
                                "Limited availability of training programs",
                                "Lack of transportation",
                                "Cultural or gender barriers",
                                "Lack of internet or technology access",
                                "Low quality of training offered",
                                "Limited time",
                                "Household commitments",
                                "Other"])
    indicators.append(R22_barriers)
    
    R22_enablers = bd.Indicator(df, "Research2.2_e", 0, ['G5-1-1', 'G5-1-2', 'G5-1-3', 'G5-1-4', 'G5-1-5', 'G5-1-6', 'G5-1-7', 'G5-1-8', 'G5-1-9'], i_cal=None, i_type='count', description='Research question 2.2: What factors would make it easier for you to attend digital skills or business skills training programs?', period='baseline', target = None, visual = False)
    R22_enablers.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R22_enablers.add_var_change({1: "Yes", 0: "No"})
    R22_enablers.add_var_order([1, 0])
    R22_enablers.add_label(["Free or low-cost programs",
                                "Flexible schedules",
                                "Stipend to cover time costs",
                                "Support with childcare",
                                "Programs offered in a nearby location",
                                "Hands-on or practical training",
                                "Mentorship or follow-up support",
                                "Job placements after training",
                                "Other"])
    indicators.append(R22_enablers)
    
    R32_2 = bd.Indicator(df, "Research2.2_add", 0, ['G8-1','G8-2', 'G8-3', 'G8-4', 'G8-5', 'G8-6', 'G8-7', 'G8-8'], i_cal=None, i_type='count', description='Research question 3.2: If you haven’t tried to attend a digital skills or business skills training program, what prevented you from attending?', period='baseline', target = None)
    R32_2.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R32_2.add_var_change({1: "Yes", 0: "No"})
    R32_2.add_var_order([1, 0])
    R32_2.add_label(["No interest",
                     "Lack of awareness about available programs",
                     "High cost of training programs",
                     "Lack of time due to other responsibilities",
                     "Distance was too far",
                     "Training programs are not relevant to my needs",
                     "Lack of internet or technology access",
                     "Other"])
    indicators.append(R32_2)
    
    R32 = bd.Indicator(df, "Research3.2", 0, ['D11-1', 'D11-2', 'D11-3', 'D11-4', 'D11-5', 'D11-6', 'D11-7', 'D11-8', 'D11-9'], i_cal=None, i_type='count', description='Research question 3.2: Employer demand', period='baseline', target = None)
    R32.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R32.add_var_change({1: "Yes", 0: "No"})
    R32.add_var_order([1, 0])
    R32.add_label(["Basic computer skills",
                   "Coding or programming",
                   "Digital marketing and social media management",
                   "Data analysis and visualization",
                   "Cybersecurity",
                   "E-commerce and online business management",
                   "User experience (UX) and graphic design",
                   "Emerging technologies (AI, machine learning, Big data, Metaverse)",
                   "Other"])
    indicators.append(R32)
    
    R33_1 = bd.Indicator(df, "Research3.3_1", 0, ["D13"], i_cal=None, i_type='count', description='Research question 3.3: What barriers do you think prevent youth from accessing dignified and fulfilling work in the ICT sector (or other sectors)?', period='baseline', target = None, visual = False)
    R33_1.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R33_1.add_var_order(["Lack of required digital skills",
                         "Limited access to technology or tools",
                         "Lack of work experience or internships",
                         "Lack of mentorship or career guidance",
                         "Limited job openings my sector",
                         "Other"])
    indicators.append(R33_1)
    
    R33_2 = bd.Indicator(df, "Research3.3_2", 0, ['D14-a-1', 'D14-a-2', 'D14-a-3', 'D14-a-4', 'D14-a-5'], i_cal=None, i_type='count', description='Research question 3.3: What challenges do young women face when seeking work in the ICT sector?', period='baseline', target = None, visual = False)
    R33_2.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R33_2.add_var_change({1: "Yes", 0: "No"})
    R33_2.add_var_order([1, 0])
    R33_2.add_label(["Gender stereotypes and bias in hiring",
                         "Lack of role models or mentors",
                         "Safety concerns in workplaces or transportation",
                         "Difficulty balancing family responsibilities with work",
                         "Other"])
    indicators.append(R33_2)
    
    R33_3 = bd.Indicator(df, "Research3.3_3", 0, ['D14-b-1', 'D14-b-2', 'D14-b-3', 'D14-b-4', 'D14-b-5'], i_cal=None, i_type='count', description='Research question 3.3: What challenges do people with disabilities face when seeking work in the ICT sector?', period='baseline', target = None, visual = False)
    R33_3.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R33_3.add_var_change({1: "Yes", 0: "No"})
    R33_3.add_var_order([1, 0])
    R33_3.add_label(["Limited access to inclusive training programs",
                         "Lack of workplace accommodations",
                         "Discrimination during hiring processes",
                         "Limited access to assistive technology",
                         "Other"])
    indicators.append(R33_3)
    
    R33_4 = bd.Indicator(df, "Research3.3_4", 0, ['D14-c-1', 'D14-c-2', 'D14-c-3', 'D14-c-4', 'D14-c-5', 'D14-c-6'], i_cal=None, i_type='count', description='Research question 3.3: What challenges do refugee or displaced youth face when seeking work in the ICT sector?', period='baseline', target = None, visual = False)
    R33_4.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R33_4.add_var_change({1: "Yes", 0: "No"})
    R33_4.add_var_order([1, 0])
    R33_4.add_label(["Language barriers",
                         "Cultural barriers",
                         "Lack of recognized certifications or credentials",
                         "Limited access to networks or job opportunities",
                         "Reluctance to hire and limited promotion of inclusion",
                         "Other"])
    indicators.append(R33_4)
    
    R3_add = bd.Indicator(df, "Research3_add", 0, ['F23','F24','F25'], i_cal=None, i_type='count', description='Research question 3.3: Youth influence in ICT sector', period='baseline', target = None, visual = False)
    R3_add.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R3_add.add_var_order(['Strongly disagree', "Disagree","Neither agree nor disagree", "Agree", "Strongly agree"])
    R3_add.add_label(["I feel that my voice carries influence in ICT sector discussions or projects",
                      "I am regularly invited to participate in decision-making forums or policy discussions in the ICT sector",
                      "I believe there are clear pathways for women/vulnerable groups to advance to leadership positions in the ICT sector"])
    indicators.append(R3_add)
    """    
    
    R41_1 = bd.Indicator(df, "Research4.1_1", 0, ["B9-2"], i_cal=None, i_type='count', description='Research question 4.1: How long ago did you start your business / self-employment?', period='baseline', target = None, visual = False)
    R41_1.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R41_1.add_var_order(["Less than six months",
                         "More than six months but less than a year",
                         "More than a year"])
    indicators.append(R41_1)
    
    R41_2 = bd.Indicator(df, "Research4.1_2", 0, ["B10"], i_cal=None, i_type='count', description='Research question 4.1: Is your business open all year long?', period='baseline', target = None, visual = False)
    R41_2.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R41_2.add_var_order(["Yes, I operate throughout the year",
                         "No, my business is seasonal (i.e.during certain seasons/parts of the year)",
                         "No, my business is casual (i.e. business is run on a part-time basis when I have the time or financial resources OR when the marketplace I sell in is open)"])
    indicators.append(R41_2)
    
    R41_3 = bd.Indicator(df, "Research4.1_3", 0, ["B11"], i_cal=None, i_type='count', description='Research question 4.1: Is your business an informal or formal business (i.e., you have a business license)?', period='baseline', target = None)
    R41_3.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R41_3.add_var_order(["Informal","Formal","Refused to answer"])
    indicators.append(R41_3)
   
    
    R41_5 = bd.Indicator(df, "Research4.1_5", 0, ["B13"], i_cal=None, i_type='count', description='Research question 4.1: Thinking about the ownership of your business, which of the following is most true?', period='baseline', target = None, visual = False)
    R41_5.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R41_5.add_var_order(["I'm a sole proprietor",
                         "I'm in a business partnership",
                         "I don’t own the business, I only manage it",])
    indicators.append(R41_5)
    
    R41_6 = bd.Indicator(df, "Research4.1_6", 0, ["B14-2"], i_cal=None, i_type='count', description='Research question 4.1: Do you employ any full-time employees?', period='baseline', target = None, visual = False)
    R41_6.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R41_6.add_var_order(["Yes","No"])
    indicators.append(R41_6)
    
    R41_7 = bd.Indicator(df, "Research4.1_7", 0, ["B18"], i_cal=None, i_type='count', description='Research question 4.1: Do you employ any part-time employees?', period='baseline', target = None, visual = False)
    R41_7.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R41_7.add_var_order(["Yes","No"])
    indicators.append(R41_7)
    
    R41_8 = bd.Indicator(df, "Research4.1_8", 0, ["gender_part"], i_cal=None, i_type='count', description='Research question 4.1: Gender inclusive (Part-time)', period='baseline', target = None, visual = False)
    R41_8.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R41_8.add_var_order(["Inclusive", "Not inclusive"])
    indicators.append(R41_8)
    
    R41_9 = bd.Indicator(df, "Research4.1_9", 0, ["gender_full"], i_cal=None, i_type='count', description='Research question 4.1: Gender inclusive (Full-time)', period='baseline', target = None, visual = False)
    R41_9.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R41_9.add_var_order(["Inclusive", "Not inclusive"])
    indicators.append(R41_9)
    
    R41_10 = bd.Indicator(df, "Research4.1_10", 0, ["youth_part"], i_cal=None, i_type='count', description='Research question 4.1: Youth inclusive (Part-time)', period='baseline', target = None, visual = False)
    R41_10.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R41_10.add_var_order(["Inclusive", "Not inclusive"])
    indicators.append(R41_10)
    
    R41_11 = bd.Indicator(df, "Research4.1_11", 0, ["youth_full"], i_cal=None, i_type='count', description='Research question 4.1: Youth inclusive (Full-time)', period='baseline', target = None, visual = False)
    R41_11.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R41_11.add_var_order(["Inclusive", "Not inclusive"])
    indicators.append(R41_11)
    
    R41_12 = bd.Indicator(df, "Research4.1_12", 0, ["B22"], i_cal=None, i_type='count', description='Research question 4.1: Over the past 12 months, or past fiscal year, has your business increased its revenues?', period='baseline', target = None, visual = False)
    R41_12.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R41_12.add_var_order(["Yes", "No"])
    indicators.append(R41_12)
    
    R41_13 = bd.Indicator(df, "Research4.1_13", 0, ["B23"], i_cal=None, i_type='count', description='Research question 4.1: How much has your business increased its revenues?', period='baseline', target = None, visual = False)
    R41_13.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R41_13.add_var_order(["Significantly increased (> 25%)",
                          "Slightly increased (up to 25%)",
                          "Remained the same (about 5%)",
                          "Slightly decreased (up to 25%)",
                          "Significantly decreased (>25%)"])
    indicators.append(R41_13)
    
    R41_add = bd.Indicator(df, "Research4.1_add", 0, ['C8-1', 'C8-2', 'C8-3', 'C8-4', 'C8-5', 'C8-6', 'C8-7', 'C8-8'], i_cal=None, i_type='count', description='Research question 4.1: Thinking about your business, do you incorporate technology or digital tools to support your business in any of the following ways?', period='baseline', target = None)
    R41_add.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R41_add.add_var_change({1: "Yes", 0: "No"})
    R41_add.add_var_order([1, 0])
    R41_add.add_label(["Use digital tools like MS Excel for record keeping / monitoring inventory and stock",
                       "Use digital tools like MS Publisher to prepare business cards or other business correspondence",
                       "Use digital tools like MS Word to produce marketing materials, create business plans etc",
                       "Use social media like TikTok, Instagram, Facebook, WhatsApp or X (Twitter), etc. to promote my business",
                       "Use an e-commerce platform to sell my products or services  provide local examples",
                       "Use a mobile money application or service for accepting payment from customers provide local examples",
                       "None of the above",
                       "Other"])
    indicators.append(R41_add)   
    
    
    R42 = bd.Indicator(df, "Research4.2", 0, ['C23-1', 'C23-2', 'C23-3', 'C23-4', 'C23-5', 'C23-6', 'C23-7', 'C23-8', 'C23-9'], i_cal=None, i_type='count', description='Research question 4.2: What are the biggest challenges you face in starting or running your business?', period='baseline', target = None)
    R42.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R42.add_var_change({1: "Yes", 0: "No"})
    R42.add_var_order([1, 0])
    R42.add_label(["Lack of access to funding or capital",
                   "Limited access to technology or digital tools",
                   "High competition in the market",
                   "Lack of business management or technical skills",
                   "Difficulty accessing markets or customers",
                   "Lack of mentorship or guidance",
                   "Poor infrastructure",
                   "Cultural or social barriers",
                   "Other"])
    indicators.append(R42)
    
    R42_add = bd.Indicator(df, "Research4.2_add", 0, ['C24-1', 'C24-2', 'C24-3', 'C24-4', 'C24-5', 'C24-6', 'C24-7', 'C24-8'], i_cal=None, i_type='count', description='Research question 4.2: What would help you overcome these challenges?', period='baseline', target = None)
    R42_add.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R42_add.add_var_change({1: "Yes", 0: "No"})
    R42_add.add_var_order([1, 0])
    R42_add.add_label(["Access to affordable financing options",
                       "Training in business management and technical skills",
                       "Improved access to technology or digital tools",
                       "Better market access",
                       "Mentorship from experienced entrepreneurs",
                       "Networking opportunities with other entrepreneurs",
                       "Supportive government or NGO programs",
                       "Other"])
    indicators.append(R42_add)  
    
    R43_1 = bd.Indicator(df, "Research4.3_1", 0, ["C9-a"], i_cal=None, i_type='count', description='Research question 4.3: What is the main source of funding you currently use for your business?', period='baseline', target = None)
    R43_1.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R43_1.add_var_order(["Personal savings",
                         "Family or friends",
                         "Microfinance institutions",
                         "Bank loans",
                         "NGO or government grants",
                         "Other"])
    indicators.append(R43_1)
    
    R43_2 = bd.Indicator(df, "Research4.3_2", 0, ['C9-b-1', 'C9-b-2', 'C9-b-3', 'C9-b-4', 'C9-b-5', 'C9-b-6', 'C9-b-7', 'C9-b-8', 'C9-b-9', 'C9-b-10'], i_cal=None, i_type='count', description='Research question 4.3: Has your business CURRENTLY OR IN THE PAST had a loan from a private or government bank, microfinance institution, family/friends or other sources?', period='baseline', target = None, visual = False)
    R43_2.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R43_2.add_var_change({1: "Yes", 0: "No"})
    R43_2.add_var_order([1, 0])
    R43_2.add_label(["Bank (Private/Government)",
                         "SACCO loans",
                         "Community Saving and lending groups",
                         "Youth fund",
                         "Women fund",
                         "Microfinance organisation",
                         "Family and friends",
                         "Grants from NGO",
                         "Other",
                         "None of the above"])
    indicators.append(R43_2)
    
    R43_3 = bd.Indicator(df, "Research4.3_3", 0, ["C11"], i_cal=None, i_type='count', description='Research question 4.3: Have you applied for seed funding or monetary support for your business?', period='baseline', target = None)
    R43_3.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R43_3.add_var_order(["Yes","No"])
    indicators.append(R43_3)
    
    R43_4 = bd.Indicator(df, "Research4.3_4", 0, ["C12"], i_cal=None, i_type='count', description='Research question 4.3: If you have applied for seed funding/monetary support, were you successful with your application?', period='baseline', target = None)
    R43_4.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R43_4.add_var_order(["Yes","No"])
    indicators.append(R43_4)
    
    R43_5 = bd.Indicator(df, "Research4.3_5", 0, ["C16"], i_cal=None, i_type='count', description='Research question 4.3: If you were successful, was the amount you received the ideal amount to support your business at the time?', period='baseline', target = None, visual = False)
    R43_5.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R43_5.add_var_order(["Yes","No"])
    indicators.append(R43_5)
    
    R43_6 = bd.Indicator(df, "Research4.3_6", 0, ["C17"], i_cal=None, i_type='count', description='Research question 4.3: Do you currently need seed funding or monetary support for your business?', period='baseline', target = None, visual = False)
    R43_6.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R43_6.add_var_order(["Yes","No"])
    indicators.append(R43_6)
    
    R43_7 = bd.Indicator(df, "Research4.3_7", 0, ["C18"], i_cal=None, i_type='count', description='Research question 4.3: What would you use the seed funding/monetary support for?', period='baseline', target = None, visual = False)
    R43_7.add_breakdown({'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    R43_7.add_var_order(["Equipment/tools",
                         "Raw materials or stock",
                         "Renting/improving business space",
                         "Marketing and advertising",
                         "Expanding range of products/services offered",
                         "Hiring additional help/staff",
                         "Technology (e.g., mobile phone, computer, software)",
                         "Training/skill development",
                         "Repaying existing debts or loans",
                         "Other"])
    indicators.append(R43_7)

    
    return indicators
    

def statistical_indicators(df, indicators):
    
    df_stats = df[df['A12'] != "Asylum Seeker"].copy()
    sL211_s = bd.Indicator(df_stats, "L2.1.1 Soft", 0, ['L221_soft'], i_cal='divide', i_type='percentage', description='L2.1.1: Soft skills', s_test = 'chi', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    sL211_s.add_valid_point({20: 'Low level', (20, 35): 'Moderate level', 35: 'High level'})
    sL211_s.add_var_order(['Low level', 'Moderate level', 'High level'])
    indicators.append(sL211_s)
    
    sL211_g = bd.Indicator(df_stats, "L2.1.1 General", 0, ['L221_general'], i_cal='divide', i_type='percentage', description='L2.1.1: General skills', s_test = 'chi', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    sL211_g.add_valid_point({35: 'Low level', (35, 65): 'Moderate level', 65: 'High level'})
    sL211_g.add_var_order(['Low level', 'Moderate level', 'High level'])
    indicators.append(sL211_g)
    
    sL211_y = bd.Indicator(df_stats, "L2.1.1 Leadership", 0, ['L221_leadership'], i_cal='divide', i_type='percentage', description='L2.1.1: Youth leadership skills', s_test = 'chi', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    sL211_y.add_valid_point({20: 'Low level', (20, 35): 'Moderate level', 35: 'High level'})
    sL211_y.add_var_order(['Low level', 'Moderate level', 'High level'])
    indicators.append(sL211_y)
    
    sL211_i = bd.Indicator(df_stats, "L2.1.1 Intermediate", 0, ['L221_intermediate'], i_cal='divide', i_type='percentage', description='L2.1.1: Intermediate digital skills', s_test = 'chi', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    sL211_i.add_valid_point({20: 'Low level', (20, 35): 'Moderate level', 35: 'High level'})
    sL211_i.add_var_order(['Low level', 'Moderate level', 'High level'])
    indicators.append(sL211_i)
    
    sL211_a = bd.Indicator(df_stats, "L2.1.1 Advanced", 0, ['L221_advanced'], i_cal='divide', i_type='percentage', description='L2.1.1: Advanced digital skills', s_test = 'chi', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    sL211_a.add_valid_point({20: 'Low level', (20, 35): 'Moderate level', 35: 'High level'})
    sL211_a.add_var_order(['Low level', 'Moderate level', 'High level'])
    indicators.append(sL211_a)
    
    sL211_b = bd.Indicator(df_stats, "L2.1.1 Business", 0, ['L221_business'], i_cal='divide', i_type='percentage', description='L2.1.1: Business skills', s_test = 'chi', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    sL211_b.add_valid_point({15: 'Low level', (15, 25): 'Moderate level', 25: 'High level'})
    sL211_b.add_var_order(['Low level', 'Moderate level', 'High level'])
    indicators.append(sL211_b)
    
    sR41_13 = bd.Indicator(df_stats, "Research4.1_13", 0, ["B23"], i_cal=None, i_type='count', description='Research question 4.1: How much has your business increased its revenues?', s_test = 'chi', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    sR41_13.add_var_order(["Significantly increased (> 25%)",
                          "Slightly increased (up to 25%)",
                          "Remained the same (about 5%)",
                          "Slightly decreased (up to 25%)",
                          "Significantly decreased (>25%)"])
    indicators.append(sR41_13)
    
    L531_stats = bd.Indicator(df, "L5.3.1", 0, ['foal'], i_cal=None, i_type='count', description='Feelings on aspects of life', s_test = 'stats', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(L531_stats)
    
    L411_hired = bd.Indicator(df, "L4.1.1", 0, ['hired_youth'], i_cal=None, i_type='count', description='Youth hired by participants', s_test = 'stats', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(L411_hired)
    
    L321_stats = bd.Indicator(df, "L3.2.1", 0, ['L321'], i_cal=None, i_type='count', description='L3.2.1: Change in practices of organizations', s_test = 'stats', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(L321_stats)
    
    L353_stats = bd.Indicator(df, "L3.5.3", 0, ['L353'], i_cal=None, i_type='count', description='L3.5.3: Views of youth (M/F) & organizations involved in changes in power dynamics', s_test = 'stats', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(L353_stats)
    
    financial_amount1 = bd.Indicator(df, "Loan", 0, ['C10'], i_cal=None, i_type='count', description='What was the value of this loan? (In local currency)', s_test = 'stats', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(financial_amount1)
    
    financial_amount2 = bd.Indicator(df, "Seed", 0, ['C15'], i_cal=None, i_type='count', description='If you were successful, how much seed funding/monetary support did you receive? (In RWF)', s_test = 'stats', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(financial_amount2)
    
    financial_need = bd.Indicator(df, "money_require", 0, ['C21'], i_cal=None, i_type='count', description='How much seed funding do you think you would need to meet your objective? (In local currency)', s_test = 'stats', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(financial_need)
    
    t_fulltime = bd.Indicator(df, "total_fulltime", 0, ['B15'], i_cal=None, i_type='count', description='How many full-time employees do you employ?', s_test = 'stats', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(t_fulltime)
    
    f_fulltime = bd.Indicator(df, "female_fulltime", 0, ['B16'], i_cal=None, i_type='count', description='How many of them are female?', s_test = 'stats', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(f_fulltime)
    
    y_fulltime = bd.Indicator(df, "youth_fulltime", 0, ['B17'], i_cal=None, i_type='count', description='Of your full-time employees, how many of them are between 18 and 35?', s_test = 'stats', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(y_fulltime)
    
    yf_fulltime = bd.Indicator(df, "youthfemale_fulltime", 0, ['B17-a'], i_cal=None, i_type='count', description='How many of them are female? (among youth)', s_test = 'stats', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(yf_fulltime)
    
    t_parttime = bd.Indicator(df, "total_parttime", 0, ['B19'], i_cal=None, i_type='count', description='How many part-time employees do you employ?', s_test = 'stats', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(t_parttime)
    
    y_parttime = bd.Indicator(df, "youth_parttime", 0, ['B20'], i_cal=None, i_type='count', description='Of your part-time employees, how many of them are between 18 and 35?', s_test = 'stats', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(y_parttime)
    
    yf_parttime = bd.Indicator(df, "youthfemale_parttime", 0, ['B20-b'], i_cal=None, i_type='count', description='How many of them are female? (among youth, part-time)', s_test = 'stats', s_group = {'A4':'Gender','A2-1':"Location", 'A12':'Residency', 'Disability':'Disability','A2-2':'Province','0.Pathway':"Pathway"})
    indicators.append(yf_parttime)
    return indicators


# Create the PMF class ('Project Title', 'Evaluation')
ingongo = pmf.PerformanceManagementFramework('Ingongo', 'Evaluation')

indicators = descriptive_statistics(df, indicators)
indicators = statistical_indicators(df, indicators)
ingongo.add_indicators(indicators)


file_path1 = 'data/Descriptive Statistics.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Test Results.xlsx'  # File path to save the statistical tests
folder = 'visuals/' # File path for saving visuals
ingongo.PMF_generation(file_path1, file_path2, folder) # Run the PMF
