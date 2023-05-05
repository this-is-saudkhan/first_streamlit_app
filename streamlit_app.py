
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title("healthy diner")
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
    fruityvice_normalized= pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  
  fruit_choice=streamlit.text_input('what fruit?')
  if not fruit_choice:
    streamlit.error("Plz select a fruit")
  else:
    back_from_funct=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_funct)
  
  
except URLError as e:
  streamlit.error()
  
  

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("fruit list contains:")
streamlit.dataframe(my_data_rows)
add_my_fruit=streamlit.text_input('what fruit?','jackfruit')
streamlit.write('user entered',add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")

streamlit.stop()
import snowflake.connector

my_cnx= snowflake.conenctor.connect(**strealit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
strealit.header("fruit load list contains")
streamlit.dataframe(my_data_rows)
