# 📚 Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import PIL
from PIL import Image


l2chains = PIL.Image.open('op-arb.JPG')

# Title
st.set_page_config(page_title='Arbitrum vs. Optimism', page_icon=l2chains , layout='wide')
st.title('Arbitrum vs. Optimism')

# Content
c1, c2 = st.columns(2)

#c1.image(Image.open('Images/LUNA.png'))

st.subheader('📃 Introduction')


st.write(
    """
    111
    """
)

st.subheader('🎯 Purposes of Dashboard')
st.write(
    """
222
    """
)

st.subheader('🔑 Methodology')
st.write(
    """
333
    """
)
#---------------------------------------------------------------------------------------------------------
# dash_style
with open('style.css')as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
	
# flipside API
@st.cache(ttl=600)
def get_data(query1):
     if query1 == 'ALICE Price':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4ccb8e8b-f402-45f1-b566-ffd4137b3f40/data/latest')
     elif query1 == 'AXS Price':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a0bdfb0c-682b-4ce8-9dc4-0eca09ff67cc/data/latest')
     elif query1 == 'ENJ Price':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/52cfb301-f485-45a8-b530-150327c33a74/data/latest')
     elif query1 == 'MANA Price':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/41239f41-1c18-430c-98ff-ae270dc63733/data/latest')
     elif query1 == 'SAND Price':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/44390576-c37d-47ce-a965-e46ae0b7589d/data/latest')
     elif query1 == 'ALICE Price Metric':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/50fdb41c-bd0f-40ed-aa99-7d26473f6a2f/data/latest')
     elif query1 == 'AXS Price Metric':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6cbdb3c4-ddac-4c58-b8c5-a9f663b06338/data/latest')
     elif query1 == 'ENJ Price Metric':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fcb52c3f-fe06-40da-8533-424085c7681b/data/latest')
     elif query1 == 'MANA Price Metric':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c6bc79d1-1cc2-4194-a7c5-54a7613dfe4f/data/latest')
     elif query1 == 'SAND Price Metric':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/23e7ef45-1c0c-47ad-9601-0704189452d4/data/latest')
     elif query1 == 'ALICE Price ATH':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/392bbd12-3ba3-4fa8-844b-6bf8f81405e5/data/latest')
     return None

ALICE_Price = get_data('ALICE Price')
AXS_Price = get_data('AXS Price')
ENJ_Price = get_data('ENJ Price')
MANA_Price = get_data('MANA Price')
SAND_Price = get_data('SAND Price')
ALICE_Price_Metric = get_data('ALICE Price Metric')
AXS_Price_Metric = get_data('AXS Price Metric')
ENJ_Price_Metric = get_data('ENJ Price Metric')
MANA_Price_Metric = get_data('MANA Price Metric')
SAND_Price_Metric = get_data('SAND Price Metric')
ALICE_Price_ATH = get_data('ALICE Price ATH')

subtab_Daily, subtab_Weekly, subtab_Monthly = st.tabs(['Daily', 'Weekly', 'Monthly'])
with subtab_Daily:
     c1, c2 = st.columns(2)
     with c1:
            df = ALICE_Price_ATH
            st.metric(label='ALICE Price ATH', value=df['Price ATH'])	
     with c2:
            df = ALICE_Price_ATH
            st.metric(label='Range of Price Change', value=df['RoPC'])
     c1, c2 = st.columns(2)
     with c1:             
             df = ALICE_Price
             fig = px.bar(df, x='DATE', y='RoPC', title='Range of Price Changes', log_y=False)
             fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$USD')
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
     with c2:
            df = ALICE_Price_Metric
            fig = px.line(df, x='Day', y='Price', color='TYPE', title='Price per Day', log_y=False)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	

with subtab_Weekly:
  c1, c2 = st.columns(2)
  with c1:
        df = ALICE_Price
        fig = px.bar(df, x='DATE', y='RoPC', title='Range of Price Changes', log_y=False)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$USD')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
	
	
  with c2:
        df = AXS_Price_Metric
        fig = px.line(df, x='Day', y='Price', color='TYPE', title='Price per Day', log_y=False)
        fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
	   	
with subtab_Monthly:
     c1, c2 = st.columns(2)
     with c1:
             df = ALICE_Price
             fig = px.bar(df, x='DATE', y='RoPC', title='Range of Price Changes', log_y=False)
             fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$USD')
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
     with c2:
            df = ENJ_Price_Metric
            fig = px.line(df, x='Day', y='Price', color='TYPE', title='Price per Day', log_y=False)
            fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly) 
         


#-----------------------------------------------------------------------------------------------------------
c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Analyst: [Emanoel](https://twitter.com/Astiran91)**', icon="📌")
    #c1.image(Image.open('Images/analyst2.JPG'))
with c2:
    st.info('**Database: [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="📚")
    #c2.image(Image.open('Images/flipside.JPG'))
with c3:
    st.info('**Provided for: [MetricsDao](https://metricsdao.xyz/)**', icon="💡")
    #c3.image(Image.open('Images/metricsdao.JPG'))




