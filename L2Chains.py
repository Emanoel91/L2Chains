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

🔵 **Arbitrum**

Arbitrum is the first-largest Ethereum layer 2 with a total of $2.68B locked into its smart contracts, as of this writing, according to [l2beat](https://l2beat.com/scaling/tvl).
Arbitrum uses a technique known as transaction rollups to record batches of submitted transactions on the Ethereum main chain, and execute them on a cheap, scalable 
layer 2 sidechain while leveraging Ethereum to ensure correct results. This process helps to offload most of the computational and storage burden Ethereum currently 
suffers from, while enabling new classes of powerful layer 2-based DApps. [[1]](https://coinmarketcap.com/alexandria/article/what-is-arbitrum)

🔴 **Optimism**

Optimism is a layer 2 chain, meaning it functions on top of Ethereum mainnet (layer 1). Transactions take place on Optimism, but the data about transactions get posted
to mainnet where they are validated. It’s like driving in a less crowded side street while benefiting from the security of a highway. Optimism is the second-largest 
Ethereum layer 2 with a total of $1.61B locked into its smart contracts, as of this writing, according to [l2beat](https://l2beat.com/scaling/tvl). Optimism uses a technology called rollups, 
specifically Optimistic rollups. They’re called rollups because they roll up (or bundle) the data about hundreds of transactions into a single transaction on Ethereum 
mainnet (layer 1). And they’re called Optimistic rollups because transactions are assumed to be valid until they are proven false, or in other words, innocent until proven guilty. 

🟢 **Arbitrum Versus Optimism**

The largest difference between Arbitrum and Optimism is how the technology resolves a dispute on Layer 2. Both projects are optimistic rollups and use a challenge 
system where any validator can dispute a block on the chain. This is where the technology of the 2 projects diverge. Optimism re-executes the disputed transaction on 
Layer 1 and checks which party is correct in their assertion. 
The Arbitrum team realized that this process can contribute to network congestion significantly. Optimism needs to port a large amount of data to Layer 1 to compute 
the disputed transaction and resolve it. Instead, Arbitrum continuously subdivides the challenge until the disputed information is so small that it can be quickly sent
to and resolved on Layer 1. Because they both use optimistic rollups, some trust in the validators is required. If all validators for a dApp collude in a malicious 
attack and no one challenges it, Arbitrum’s bridge between Layer 1 and 2 will assume the transaction is valid.[[2]](https://www.benzinga.com/money/what-is-arbitrum)



    """
)

st.subheader('🎯 Purposes of Dashboard')
st.write(
    """
**In this Dashboard we compare and contrast two major L2 chains: Arbitrum & Optimism. We analysis metrics such as total and average transaction volume, average 
transaction size, active users, new users added, and many intersting metrics relevant to this comparison.**
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
     elif query1 == 'New Addresses':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/90828ee6-8f67-47de-8812-29d302b22d4c/data/latest')
     elif query1 == 'Daily Transactions Value':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ea6888d0-422a-4bce-bb77-da7ec1410cbc/data/latest')
     elif query1 == 'Weekly Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/29ad802c-4267-4cc7-8458-b48f17d6898b/data/latest')
     elif query1 == 'Monthly Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8fd56cb3-9123-407b-9c95-0f215202a1a2/data/latest')
     elif query1 == 'New Addresses Weekly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ca20a9b0-a0c5-49c9-b3d3-5a16a11e6b45/data/latest')
     elif query1 == 'New Addresses Monthly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/37b83485-1817-4ca3-bf57-8157ff28addc/data/latest')
     elif query1 == 'Transaction Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/335e43c1-ebc8-4117-80be-b97f3d0945a7/data/latest')
     return None

Daily_Transactions = get_data('Daily Transactions')
ALICE_Price_ATH = get_data('ALICE Price ATH')
New_Addresses = get_data('New Addresses')
Daily_Transactions_Value = get_data('Daily Transactions Value')
Weekly_Transactions = get_data('Weekly Transactions')
Monthly_Transactions = get_data('Monthly Transactions')
New_Addresses_Weekly = get_data('New Addresses Weekly')
New_Addresses_Monthly = get_data('New Addresses Monthly')
Transaction_Overview = get_data('Transaction Overview')

st.subheader('📄 Overview')

            df = Transaction_Overview
            c1, c2, c3, c4 = st.columns(4)

            with c1:
	    fig = px.bar(df, x='L2 Chain', y='TX Count', color='L2 Chain', title='Total Transactions Count', log_y=False)
            fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

	
st.subheader('📊 Analysis')

subtab_Daily, subtab_Weekly, subtab_Monthly = st.tabs(['Daily', 'Weekly', 'Monthly'])
with subtab_Daily:

            df = Daily_Transactions
            fig = px.bar(df, x='Day', y='TX Count', color='L2 Chain', title='Total Number of Transactions', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	

            fig = px.line(df, x='Day', y='TPS', color='L2 Chain', title='Transaction per Second (TPS)', log_y=False)
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
	
            fig = px.line(df, x='Day', y='Active Address', color='L2 Chain', title='Number of Active Addresses', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with subtab_Daily:
	
             df = New_Addresses
             fig = px.line(df, x='Date', y='New Address', color='L2 Chain', title='Number of New Addresses', log_y=False)
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
	
with subtab_Daily:
	
             df = Daily_Transactions_Value	
             fig = px.line(df, x='Day', y='Total TX Value', color='L2 Chain', title='Total Transactions Value', log_y=False)
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
             fig = px.line(df, x='Day', y='Average TX Value', color='L2 Chain', title='Average Transactions Value', log_y=False)
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)		
#----------------------------------------------------------------------------------------------------------------------------------------------------------------		
with subtab_Weekly:
            df = Weekly_Transactions
            fig = px.bar(df, x='Week', y='TX Count', color='L2 Chain', title='Total Number of Transactions', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	

            fig = px.bar(df, x='Week', y='TPS', color='L2 Chain', title='Transaction per Second (TPS)', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
		
            fig = px.bar(df, x='Week', y='Total TX Fee', color='L2 Chain', title='Total Transaction Fees', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Week', y='Average TX Fee', color='L2 Chain', title='Average Transaction Fees', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)			

            fig = px.line(df, x='Week', y='Average TX per Address', color='L2 Chain', title='Average Transaction Count per Address', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
	
            fig = px.bar(df, x='Week', y='Active Address', color='L2 Chain', title='Number of Active Addresses', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)			
		
with subtab_Weekly:
	
             df = New_Addresses_Weekly
             fig = px.bar(df, x='Week', y='New Address', color='L2 Chain', title='Number of New Addresses', log_y=False, barmode='group')
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
	
with subtab_Weekly:
	
             df = Weekly_Transactions	
             fig = px.bar(df, x='Week', y='Total TX Value', color='L2 Chain', title='Total Transactions Value', log_y=False, barmode='group')
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
             fig = px.line(df, x='Week', y='Average TX Value', color='L2 Chain', title='Average Transactions Value', log_y=False)
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
#-----------------------------------------------------------------------------------------------------------------------------------------------------------	   	
with subtab_Monthly:
            df = Monthly_Transactions
            fig = px.bar(df, x='Month', y='TX Count', color='L2 Chain', title='Total Number of Transactions', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	

            fig = px.bar(df, x='Month', y='TPS', color='L2 Chain', title='Transaction per Second (TPS)', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
		
            fig = px.bar(df, x='Month', y='Total TX Fee', color='L2 Chain', title='Total Transaction Fees', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Month', y='Average TX Fee', color='L2 Chain', title='Average Transaction Fees', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)			

            fig = px.line(df, x='Month', y='Average TX per Address', color='L2 Chain', title='Average Transaction Count per Address', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
	
            fig = px.bar(df, x='Month', y='Active Address', color='L2 Chain', title='Number of Active Addresses', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
with subtab_Monthly:
	
             df = New_Addresses_Monthly
             fig = px.bar(df, x='Month', y='New Address', color='L2 Chain', title='Number of New Addresses', log_y=False, barmode='group')
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
	
with subtab_Monthly:
	
             df = Monthly_Transactions	
             fig = px.bar(df, x='Month', y='Total TX Value', color='L2 Chain', title='Total Transactions Value', log_y=False, barmode='group')
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
             fig = px.line(df, x='Month', y='Average TX Value', color='L2 Chain', title='Average Transactions Value', log_y=False)
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
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




