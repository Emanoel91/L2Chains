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

c1.image(Image.open('Images/op-arb.JPG'))


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
     if query1 == 'Daily Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8481f651-ec83-44a4-8aa5-d79ef14de8d9/data/latest')
     return None

Daily_Transactions = get_data('Daily Transactions')


subtab_Daily, subtab_Weekly, subtab_Monthly = st.tabs(['Daily', 'Weekly', 'Monthly'])
with subtab_Daily:
	          fig = px.bar(df, x='Day', y='TX Count', color='L2Chain', title='Total Users Count (2023)', log_y=False)
                  fig.update_layout(showlegend=True, xaxis_title=None, legend_title='ACTION', yaxis_title='', xaxis={'categoryorder':'total ascending'})
                  st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with subtab_Weekly:	
	          fig = px.bar(df, x='Day', y='Total Users Count', color='L2Chain', title='Total Users Count (2023)', log_y=False)
                  fig.update_layout(showlegend=True, xaxis_title=None, legend_title='ACTION', yaxis_title='', xaxis={'categoryorder':'total ascending'})
                  st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)   
with subtab_Monthly:     	
                  fig = px.bar(df, x='Day', y='Total Users Count', color='L2Chain', title='Total Users Count (2023)', log_y=False)
                  fig.update_layout(showlegend=True, xaxis_title=None, legend_title='ACTION', yaxis_title='', xaxis={'categoryorder':'total ascending'})
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




