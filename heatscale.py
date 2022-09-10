"""Python file for creating the heat scale csv."""
import csv
import pandas as pd
import calculate_heat as calc

df1 = pd.read_csv('initial_staffing_data.csv')
df2 = pd.read_csv('change_staffing_data.csv')

r_staff_hours_heat_scale = []

for i in range(14):
    r_staff_hours_heat_scale.append(calc.heat_calculator(df1['Reduced staff hours or shifts'][i],
                                                         df2['Reduced staff hours or shifts'][i],
                                                         calc.evaluate_sign('r_staff_hours')))

i_staff_hours_heat_scale = []

for i in range(14):
    i_staff_hours_heat_scale.append(calc.heat_calculator(df1['Increased staff hours or shifts'][i],
                                                         df2['Increased staff hours or shifts'][i],
                                                         calc.evaluate_sign('i_staff_hours')))

r_salaries_heat_scale = []

for i in range(14):
    r_salaries_heat_scale.append(calc.heat_calculator(df1['Reduced salaries or wages'][i],
                                                      df2['Reduced salaries or wages'][i],
                                                      calc.evaluate_sign('r_salaries')))

froze_salaries_heat_scale = []

for i in range(14):
    froze_salaries_heat_scale.append(calc.heat_calculator(df1['Froze salaries or wages'][i],
                                                          df2['Froze salaries or wages'][i],
                                                          calc.evaluate_sign('froze_salaries')))

i_salaries_heat_scale = []

for i in range(14):
    i_salaries_heat_scale.append(calc.heat_calculator(df1['Increased salaries or wages'][i],
                                                      df2['Increased salaries or wages'][i],
                                                      calc.evaluate_sign('i_salaries')))

froze_bonus_heat_scale = []

for i in range(14):
    froze_bonus_heat_scale.append(calc.heat_calculator(df1['Froze bonus payments'][i],
                                                       df2['Froze bonus payments'][i],
                                                       calc.evaluate_sign('froze_bonus')))

delayed_compensation_heat_scale = []

for i in range(14):
    delayed_compensation_heat_scale.append(calc.heat_calculator(df1['Delayed compensation'][i],
                                                                df2['Delayed compensation'][i],
                                                                calc.evaluate_sign('delayed_compensation')))

hired_staff_heat_scale = []

for i in range(14):
    hired_staff_heat_scale.append(calc.heat_calculator(df1['Hired more staff'][i],
                                                       df2['Hired more staff'][i],
                                                       calc.evaluate_sign('hired_staff')))

laid_off_staff_heat_scale = []

for i in range(14):
    laid_off_staff_heat_scale.append(calc.heat_calculator(df1['Laid off staff'][i],
                                                          df2['Laid off staff'][i],
                                                          calc.evaluate_sign('laid_off_staff')))

header = ["Staffing action taken", "Reduced staff hours or shifts", "Increased staff hours or shifts",
          "Reduced salaries or wages", "Froze salaries or wages", "Increased salaries or wages", "Froze bonus payments",
          "Delayed compensation", "Hired more staff", "Laid off staff"]

data = []

province = ["Canada, all provinces and territories",
            "Newfoundland and Labrador",
            "Prince Edward Island",
            "Nova Scotia",
            "New Brunswick",
            "Quebec",
            "Ontario",
            "Manitoba",
            "Saskatchewan",
            "Alberta",
            "British Columbia",
            "Northwest Territories",
            "Yukon",
            "Nunavut"]

for i in range(14):
    data.append([province[i],
                 r_staff_hours_heat_scale[i],
                 i_staff_hours_heat_scale[i],
                 r_salaries_heat_scale[i],
                 froze_salaries_heat_scale[i],
                 i_salaries_heat_scale[i],
                 froze_bonus_heat_scale[i],
                 delayed_compensation_heat_scale[i],
                 hired_staff_heat_scale[i],
                 laid_off_staff_heat_scale[i]])

with open('heatscale.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
