import streamlit

streamlit.header('Breakfast Favorites')

streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Range-Free Egg')
streamlit.text('🥑🍞Avacado Toast')
streamlit.header('🍌🍓Build Your Own Smoothie🥝🍇')

import Pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(myfruitlist)
