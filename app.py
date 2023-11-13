import pandas as pd
import plotly.express as px
import streamlit as st

vehicles = pd.read_csv('/Users/bnutw/DS_items/GitHub/project_4/vehicles_us.csv')
vehicles['model_year'].fillna(0, inplace=True)
vehicles['cylinders'].fillna(0, inplace=True)
vehicles['odometer'].fillna(0, inplace=True)
vehicles['paint_color'].fillna(0, inplace=True)
vehicles['is_4wd'].fillna(0, inplace=True)
vehicles['is_4wd'] = vehicles['is_4wd'].map({1.0: 'yes', 0.0: 'no'})

make_model = vehicles['model'].str.split(' ', n=1, expand=True)
make_model = make_model.rename(columns={0: 'make', 1: 'model'})

vehicles = vehicles.drop('model', axis=1)

vehicles_info = pd.concat([make_model, vehicles], axis=1)


st.header('US Vehicles for Sale')

st.write("""
#### Chart below
""")

checkbox = st.checkbox('Show 4wd')

if checkbox:
    filtered_data = vehicles
else:
    filtered_data = vehicles[vehicles['is_4wd'] == 'no']

fig_1 = px.scatter(filtered_data, x='odometer', y='days_listed', title='Days Listed vs Odometer')
st.plotly_chart(fig_1)






prices_below_50k = vehicles[vehicles['price'] < 50000]['price']

st.title('Price of cars')

checkbox_like_new = st.checkbox("Show 'like new' condition")

if checkbox_like_new:
    filtered_prices = prices_below_50k
else:
    filtered_prices = prices_below_50k[vehicles['condition'] == 'like new']


fig = px.histogram(filtered_prices, x=filtered_prices, nbins=20)
fig.update_layout(
    title='Number of Cars by Price (Max $50,000)',
    xaxis_title='Price',
    yaxis_title='Number of Cars',
    bargap=0.1
)
st.plotly_chart(fig)




st.table(vehicles_info.head(100))