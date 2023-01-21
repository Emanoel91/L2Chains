# 📚 Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import PIL
from PIL import Image

theme_plotly = None # None or streamlit

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
🔘 **Layer 2 Solutions**

Layer 2 is a term used for solutions created to help scale an application by processing transactions off of the Ethereum Mainnet (layer 1) while still maintaining the 
same security measures and decentralization as the mainnet. Layer 2 solutions increase throughput (transaction speed) and reduce gas fees.

🔴 **Optimism**

Optimism is a layer 2 chain, meaning it functions on top of Ethereum mainnet (layer 1). Transactions take place on Optimism, but the data about transactions get posted
to mainnet where they are validated. It’s like driving in a less crowded side street while benefiting from the security of a highway. Optimism is the second-largest 
Ethereum layer 2 with a total of $1.61 B locked into its smart contracts, as of this writing, according to [l2beat](https://l2beat.com/scaling/tvl). Optimism uses a technology called rollups, 
specifically Optimistic rollups. They’re called rollups because they roll up (or bundle) the data about hundreds of transactions into a single transaction on Ethereum 
mainnet (layer 1). And they’re called Optimistic rollups because transactions are assumed to be valid until they are proven false, or in other words, innocent until proven guilty. 
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
     elif query1 == 'ALICE Price ATH':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/392bbd12-3ba3-4fa8-844b-6bf8f81405e5/data/latest')
     return None

Daily_Transactions = get_data('Daily Transactions')
ALICE_Price_ATH = get_data('ALICE Price ATH')

subtab_Daily, subtab_Weekly, subtab_Monthly = st.tabs(['Daily', 'Weekly', 'Monthly'])
with subtab_Daily:

            df = Daily_Transactions
            fig = px.bar(df, x='Day', y='TX Count', color='L2 Chain', title='Total Number of Transactions', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
	
		
            fig = px.bar(df, x='Day', y='Total TX Fee', color='L2 Chain', title='Total Transaction Fees', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Day', y='Average TX Fee', color='L2 Chain', title='Average Transaction Fees', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)			

            fig = px.line(df, x='Day', y='Average TX per Address', color='L2 Chain', title='Average Transaction Count per Address', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)		
	

with subtab_Weekly:
     c1, c2 = st.columns(2)
     with c1:
            df = ALICE_Price_ATH
            st.metric(label='ALICE Price ATH', value=df['Price ATH'])	
     with c2:
            df = ALICE_Price_ATH
            st.metric(label='Range of Price Change', value=df['RoPC'])
	   	
with subtab_Monthly:
     c1, c2 = st.columns(2)
     with c1:
            df = ALICE_Price_ATH
            st.metric(label='ALICE Price ATH', value=df['Price ATH'])	
     with c2:
            df = ALICE_Price_ATH
            st.metric(label='Range of Price Change', value=df['RoPC'])
                   
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




