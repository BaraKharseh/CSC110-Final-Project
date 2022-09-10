"""CSC110 Fall 2021 Project - Main

File that runs our entire project. Makes use of all other files either directly or indirectly.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of CSC110 instructors at the
University of Toronto St. George campus. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

This file is Copyright (c) 2021 Bara Kharseh and Patrick Fidler.
"""

# imports for the choropleth map (used when businesses are grouped into provinces and territories)
import json
import pandas as pd
import plotly.express as px

# import for creating a double bar graph
import plotly.graph_objects as go

# import for pygame
import pygame

# imports to use functions from other project files
from extract_data import read_csv_file
from other_functions import checkbox_array, convert_name
from graph_functions import double_bar_graph_variables

# setting up data for heatmap
provinces = json.load(open('canada_provinces.geojson'))
df = pd.read_csv('heatscale.csv')
cartodb_id_map = {}
for feature in provinces['features']:
    feature['id'] = feature['properties']['cartodb_id']
    cartodb_id_map[feature['properties']['name']] = feature['id']
df['id'] = df['Staffing action taken'][1:14].apply(lambda x: cartodb_id_map[x])

# initialize pygame
pygame.init()

# pygame text variables
l_font = pygame.font.SysFont("Times New Roman", 40)
m_font = pygame.font.SysFont("Times New Roman", 25)
s_font = pygame.font.SysFont("Times New Roman", 20)
title = l_font.render("Graph Customizer", True, (0, 0, 0))
subtitle1 = m_font.render("Business Groupings", True, (0, 0, 0))
subtitle2 = m_font.render("Staffing Actions", True, (0, 0, 0))
squares1_0 = s_font.render("Province/Territory", True, (0, 0, 0))
squares1_1 = s_font.render("Industry", True, (0, 0, 0))
squares1_2 = s_font.render("Size", True, (0, 0, 0))
squares2_0 = s_font.render("Reduced Staff Hours/Shifts", True, (0, 0, 0))
squares2_1 = s_font.render("Increased Staff Hours/Shifts", True, (0, 0, 0))
squares2_2 = s_font.render("Reduced Salaries or Wages", True, (0, 0, 0))
squares2_3 = s_font.render("Froze Salaries or Wages", True, (0, 0, 0))
squares2_4 = s_font.render("Increased Salaries or Wages", True, (0, 0, 0))
squares2_5 = s_font.render("Froze Bonus Payments", True, (0, 0, 0))
squares2_6 = s_font.render("Delayed Compensation", True, (0, 0, 0))
squares2_7 = s_font.render("Hired more Staff", True, (0, 0, 0))
squares2_8 = s_font.render("Laid off Staff", True, (0, 0, 0))
choropleth = s_font.render("Show as Choropleth", True, (0, 0, 0))
button = l_font.render("Graph!", True, (0, 0, 0))

# set-up variables
window = pygame.display.set_mode((640, 450))
pygame.display.set_caption('CSC110 Project: COVID 19\'s Impact on Canadian Businesses')
window.fill((255, 255, 255))
# tracks which checkbox is selected
squares1 = [False, False, False, False]
to_be_reset1 = 3
squares2 = [False, False, False, False, False, False, False, False, False, False]
to_be_reset2 = 9
square3 = False
business_grouping = None
staffing_decision = None
is_choropleth = False

# initial and changed data
initial_data = read_csv_file('initial_staffing_data.csv')
change_data = read_csv_file('change_staffing_data.csv')

while True:
    # title and subtitle text
    window.blit(title, (50, 20))
    window.blit(subtitle1, (50, 80))
    window.blit(subtitle2, (320, 80))

    # checkboxes
    # left array
    checkbox_array(window, 50, 120, 3)
    # right array
    checkbox_array(window, 320, 120, 9)
    # choropleth checkbox
    checkbox_array(window, 50, 320, 1)

    # checkbox text for left array
    window.blit(squares1_0, (80, 120))
    window.blit(squares1_1, (80, 155))
    window.blit(squares1_2, (80, 190))

    # checkbox text for right array
    window.blit(squares2_0, (350, 120))
    window.blit(squares2_1, (350, 155))
    window.blit(squares2_2, (350, 190))
    window.blit(squares2_3, (350, 225))
    window.blit(squares2_4, (350, 260))
    window.blit(squares2_5, (350, 295))
    window.blit(squares2_6, (350, 330))
    window.blit(squares2_7, (350, 365))
    window.blit(squares2_8, (350, 400))

    # checkbox text for choropleth checkbox
    window.blit(choropleth, (80, 320))

    # graph button
    pygame.draw.rect(window, 0, (50, 360, 200, 60), 2)
    window.blit(button, (95, 365))

    # "covers" the button until a box has been selected in both the left and right arrays
    if all(x is False for x in squares1) or all(x is False for x in squares2):
        pygame.draw.rect(window, (255, 255, 255), (50, 360, 201, 61), 0)

    # tracks mouse position
    mouse_pos = pygame.mouse.get_pos()

    # "covers" any previously filled checkboxes in the left array
    pygame.draw.rect(window, (255, 255, 255), (52, 122, 17, 17), 0)
    pygame.draw.rect(window, (255, 255, 255), (52, 157, 17, 17), 0)
    pygame.draw.rect(window, (255, 255, 255), (52, 192, 17, 17), 0)

    # fills in checkboxes based on which square has been clicked in the left array
    if squares1[0]:
        pygame.draw.rect(window, 0, (52, 122, 17, 17), 0)
    if squares1[1]:
        pygame.draw.rect(window, 0, (52, 157, 17, 17), 0)
    if squares1[2]:
        pygame.draw.rect(window, 0, (52, 192, 17, 17), 0)

    # "covers" any previously filled checkboxes in the right array
    pygame.draw.rect(window, (255, 255, 255), (322, 122, 17, 17), 0)
    pygame.draw.rect(window, (255, 255, 255), (322, 157, 17, 17), 0)
    pygame.draw.rect(window, (255, 255, 255), (322, 192, 17, 17), 0)
    pygame.draw.rect(window, (255, 255, 255), (322, 227, 17, 17), 0)
    pygame.draw.rect(window, (255, 255, 255), (322, 262, 17, 17), 0)
    pygame.draw.rect(window, (255, 255, 255), (322, 297, 17, 17), 0)
    pygame.draw.rect(window, (255, 255, 255), (322, 332, 17, 17), 0)
    pygame.draw.rect(window, (255, 255, 255), (322, 367, 17, 17), 0)
    pygame.draw.rect(window, (255, 255, 255), (322, 402, 17, 17), 0)

    # fills in checkboxes based on which square has been clicked in the right array
    if squares2[0]:
        pygame.draw.rect(window, 0, (322, 122, 17, 17), 0)
    if squares2[1]:
        pygame.draw.rect(window, 0, (322, 157, 17, 17), 0)
    if squares2[2]:
        pygame.draw.rect(window, 0, (322, 192, 17, 17), 0)
    if squares2[3]:
        pygame.draw.rect(window, 0, (322, 227, 17, 17), 0)
    if squares2[4]:
        pygame.draw.rect(window, 0, (322, 262, 17, 17), 0)
    if squares2[5]:
        pygame.draw.rect(window, 0, (322, 297, 17, 17), 0)
    if squares2[6]:
        pygame.draw.rect(window, 0, (322, 332, 17, 17), 0)
    if squares2[7]:
        pygame.draw.rect(window, 0, (322, 367, 17, 17), 0)
    if squares2[8]:
        pygame.draw.rect(window, 0, (322, 402, 17, 17), 0)

    # "covers" the choropleth checkbox if it's been previously filled
    pygame.draw.rect(window, (255, 255, 255), (52, 322, 17, 17), 0)

    # fills in choropleth checkbox based on if it's been clicked
    if square3:
        pygame.draw.rect(window, 0, (52, 322, 17, 17), 0)

    # "covers" the choropleth checkbox unless the business grouping selected is province/territory
    if business_grouping != "Province/Territory":
        pygame.draw.rect(window, (255, 255, 255), (50, 320, 200, 30))

    # checks for certain pygame actions
    for action in pygame.event.get():
        # when the mouse is pushed down:
        if action.type == pygame.MOUSEBUTTONDOWN:
            # when the mouse is in the boxes of the left array:
            if 50 <= mouse_pos[0] <= 70:
                if 120 <= mouse_pos[1] <= 140 and not squares1[0]:
                    squares1[0] = True
                    squares1[to_be_reset1] = False
                    to_be_reset1 = 0
                    business_grouping = 'Province/Territory'
                if 155 <= mouse_pos[1] <= 175 and not squares1[1]:
                    squares1[1] = True
                    squares1[to_be_reset1] = False
                    to_be_reset1 = 1
                    business_grouping = 'Industry'
                if 190 <= mouse_pos[1] <= 210 and not squares1[2]:
                    squares1[2] = True
                    squares1[to_be_reset1] = False
                    to_be_reset1 = 2
                    business_grouping = 'Size'
            # when the mouse is in the boxes of the right array:
            if 320 <= mouse_pos[0] <= 340:
                if 120 <= mouse_pos[1] <= 140 and not squares2[0]:
                    squares2[0] = True
                    squares2[to_be_reset2] = False
                    to_be_reset2 = 0
                    staffing_decision = 'r_staff_hours'
                if 155 <= mouse_pos[1] <= 175 and not squares2[1]:
                    squares2[1] = True
                    squares2[to_be_reset2] = False
                    to_be_reset2 = 1
                    staffing_decision = 'i_staff_hours'
                if 190 <= mouse_pos[1] <= 210 and not squares2[2]:
                    squares2[2] = True
                    squares2[to_be_reset2] = False
                    to_be_reset2 = 2
                    staffing_decision = 'r_salaries'
                if 225 <= mouse_pos[1] <= 245 and not squares2[3]:
                    squares2[3] = True
                    squares2[to_be_reset2] = False
                    to_be_reset2 = 3
                    staffing_decision = 'froze_salaries'
                if 260 <= mouse_pos[1] <= 280 and not squares2[4]:
                    squares2[4] = True
                    squares2[to_be_reset2] = False
                    to_be_reset2 = 4
                    staffing_decision = 'i_salaries'
                if 295 <= mouse_pos[1] <= 315 and not squares2[5]:
                    squares2[5] = True
                    squares2[to_be_reset2] = False
                    to_be_reset2 = 5
                    staffing_decision = 'froze_bonus'
                if 330 <= mouse_pos[1] <= 350 and not squares2[6]:
                    squares2[6] = True
                    squares2[to_be_reset2] = False
                    to_be_reset2 = 6
                    staffing_decision = 'delayed_compensation'
                if 365 <= mouse_pos[1] <= 385 and not squares2[7]:
                    squares2[7] = True
                    squares2[to_be_reset2] = False
                    to_be_reset2 = 7
                    staffing_decision = 'hired_staff'
                if 400 <= mouse_pos[1] <= 420 and not squares2[8]:
                    squares2[8] = True
                    squares2[to_be_reset2] = False
                    to_be_reset2 = 8
                    staffing_decision = 'laid_off_staff'
            # when the mouse is in the choropleth checkbox:
            if 50 <= mouse_pos[0] <= 70 and 320 <= mouse_pos[1] <= 340:
                square3 = not square3
                is_choropleth = not is_choropleth
            # when the mouse is in the graph button:
            if 50 <= mouse_pos[0] <= 250 and 360 <= mouse_pos[1] <= 420:
                if any(x is True for x in squares1) and any(x is True for x in squares2):
                    if business_grouping == 'Province/Territory' and is_choropleth:
                        # creates choropleth graph
                        fig = px.choropleth(df,
                                            locations='id',
                                            geojson=provinces,
                                            color=convert_name(staffing_decision),
                                            hover_name='Staffing action taken',
                                            color_continuous_scale=px.colors.diverging.RdBu,
                                            color_continuous_midpoint=0,
                                            scope='north america')
                        fig.update_geos(fitbounds='locations', visible=False)
                        fig.update_layout(margin={
                            "r": 0,
                            "t": 0,
                            "l": 0,
                            "b": 0
                        })
                        fig.show()
                    else:
                        # creates double bar graph
                        x, y1, y2, n1, n2 = double_bar_graph_variables(business_grouping,
                                                                       staffing_decision,
                                                                       initial_data, change_data)

                        fig = go.Figure(data=[go.Bar(name=n1, x=x, y=y1),
                                              go.Bar(name=n2, x=x, y=y2)])

                        fig.update_layout(barmode='group', xaxis=dict(title='Businesses by Group'),
                                          yaxis=dict(title='Percentage of Businesses'))
                        xaxis = dict(title='Businesses by Group')
                        yaxis = dict(title='Percentage of Businesses')
                        fig.show()

        # when the pygame window is closed:
        if action.type == pygame.QUIT:
            pygame.quit()
            quit()

    # updates the display
    pygame.display.flip()
