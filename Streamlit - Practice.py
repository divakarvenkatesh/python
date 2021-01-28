#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import streamlit as st
import numpy as np
import time


#@st.cache(hash_funcs={FooType: lambda _: None})
st.title('My first app5')
st.write('HEre is my first program in streamlit')
st.write(pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
}))

#Syntax without st.write - Same result
df = pd.DataFrame({
    'first column':[1,3,5,7],
    'second column':[4,5,6,7]
})

df

#chart
chart_data = pd.DataFrame(np.random.randn(20,3),
                          columns=['a','b','c'])

st.line_chart(chart_data)


#Map data
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

#Checkbox
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

#Selectbox
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

#Sidebar
option1 = st.sidebar.selectbox(
    'Which number do you like best1?',
    df['first column'])

'You Selected:', option1


left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

#Dropdown with preferred values
display = ("male", "female")
option = list(range(len(display)))
value = st.selectbox("gender", option, format_func=lambda x: display[x])
st.write(value)

#My own program using Select Box
def get_data():
    path = "C:\\Divakar\\JKL_Learning\\Pandas_master_it\\Data\\data\\titles.csv" 
    return pd.read_csv(path)

df = get_data()

title = df['title'].drop_duplicates()
year  = df['year']
#components = df['components']
make_choice = st.sidebar.selectbox('Select your title:', title)
year_choice = st.sidebar.selectbox('Select Year', year)
df1 = df[(df['title'] == make_choice) & (df['year'] == year_choice)]
st.write('Results:', df1)


#Background color
import base64
st.markdown('<style>body{background-#f0f2f6: blue;}</style>',unsafe_allow_html=True)

