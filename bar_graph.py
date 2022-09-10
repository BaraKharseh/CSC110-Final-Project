"""Python file for plotting industry data on a bar graph."""
import plotly.graph_objects as go
import extract_data

staffing_actions_taken = ['Reduced Staff Hours or Shifts',
                          'Increased Staff Hours or Shifts',
                          'Reduced Salaries or Wages',
                          'Froze Salaries or Wages',
                          'Increased Salaries or Wages',
                          'Froze Bonus Payments',
                          'Delayed Compensation',
                          'Hired More Staff',
                          'Laid Off Staff']

canada_i = extract_data.read_csv_file('initial_staffing_data.csv')[0]
canada_c = extract_data.read_csv_file('change_staffing_data.csv')[0]

fig = go.Figure(data=[
    go.Bar(name='Initial Staffing Actions Taken', x=staffing_actions_taken,
           y=[canada_i.r_staff_hours, canada_i.i_staff_hours, canada_i.r_salaries, canada_i.froze_salaries,
              canada_i.i_salaries, canada_i.froze_bonus, canada_i.delayed_compensation, canada_i.hired_staff,
              canada_i.laid_off_staff]),
    go.Bar(name='Staffing Actions Taken After 3 Months', x=staffing_actions_taken,
           y=[canada_c.r_staff_hours, canada_c.i_staff_hours, canada_c.r_salaries, canada_c.froze_salaries,
              canada_c.i_salaries, canada_c.froze_bonus, canada_c.delayed_compensation, canada_c.hired_staff,
              canada_c.laid_off_staff])])

fig.update_layout(barmode='group', title='Canada Staffing Actions',
                  yaxis=dict(title='% of Businesses',
                             titlefont_size=16,
                             tickfont_size=14,))
fig.show()
