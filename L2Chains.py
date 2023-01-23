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
     elif query1 == 'Arbitrum TX Status':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/cfc29701-c6f0-4a71-b102-7f119313dda9/data/latest')
     elif query1 == 'Optimism TX Status':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/880cf7d7-70ab-4cff-b926-3b6df8a28c59/data/latest')
     elif query1 == 'Arbitrum TX Status Weekly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a7c937c0-1a3f-4d47-8e9f-daece6bcab95/data/latest')
     elif query1 == 'Optimism TX Status Weekly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ef59f00d-7aff-42ea-9c8c-f7da9bf07f31/data/latest')
     elif query1 == 'Arbitrum TX Status Monthly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8007648b-997a-4647-9900-ebb983e78c23/data/latest')
     elif query1 == 'Optimism TX Status Monthly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/73494d91-353c-4d8a-aa52-d6eb9f112e10/data/latest')
     elif query1 == 'Top 20 Events Based on TXs Count Arbitrum':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/eb082222-8ccf-4e35-ae4d-238f1fa70f2d/data/latest')
     elif query1 == 'Top 20 Events Based on TXs Count Optimism':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c4cf84bd-d545-4620-ba8d-2949ac7b929b/data/latest')
     elif query1 == 'Classification of Activity of Addresses Arbitrum':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/06ff575c-8b6b-43ca-b973-21e2dd759071/data/latest')
     elif query1 == 'Classification of Activity of Addresses Optimism':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/bb5316a1-9a0e-42d2-aef9-b9e82b0dc36d/data/latest')
     elif query1 == 'Status of Total Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a2b49ba0-adb2-4834-bd8a-6d8c6fbff7ba/data/latest')
     elif query1 == 'Heat Map of Transactions Arbitrum':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/450b8565-460f-4913-a299-4a4b4fd98bee/data/latest')
     elif query1 == 'Heat Map of Transactions Optimism':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ecacbbd4-fd7f-417a-99b4-80fd0a4fef8f/data/latest')
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
Arbitrum_TX_Status = get_data('Arbitrum TX Status')
Optimism_TX_Status = get_data('Optimism TX Status')
Arbitrum_TX_Status_Weekly = get_data('Arbitrum TX Status Weekly')
Optimism_TX_Status_Weekly = get_data('Optimism TX Status Weekly')
Arbitrum_TX_Status_Monthly = get_data('Arbitrum TX Status Monthly')
Optimism_TX_Status_Monthly = get_data('Optimism TX Status Monthly')
Top_20_Events_Based_on_TXs_Count_Arbitrum = get_data('Top 20 Events Based on TXs Count Arbitrum')
Top_20_Events_Based_on_TXs_Count_Optimism = get_data('Top 20 Events Based on TXs Count Optimism')
Classification_of_Activity_of_Addresses_Arbitrum = get_data('Classification of Activity of Addresses Arbitrum')
Classification_of_Activity_of_Addresses_Optimism = get_data('Classification of Activity of Addresses Optimism')
Status_of_Total_Transactions = get_data('Status of Total Transactions')
Heat_Map_of_Transactions_Optimism = get_data('Heat Map of Transactions Optimism')
Heat_Map_of_Transactions_Arbitrum = get_data('Heat Map of Transactions Arbitrum')

st.subheader('📄 Comparison of L2 chains')
st.write(
    """
**Although the number of transactions and TPS of Arbitrum chain is more than the number of transactions and TPS of Optimism, but because the average transaction fee 
of Arbitrum is lower than Optimism, so the total fees collected in Optimism are more than Arbitrum. On the other hand, although the number of unique addresses of 
Arbitrum is more than that of Optimism, the average number of recorded transactions per address is the same in the two chains. The results show that the average 
transaction value of Arbitrum is higher than Optimism.**
    """
)
df = Transaction_Overview
c1, c2, c3, c4 = st.columns(4)

with c1:
    fig = px.bar(df, x='L2 Chain', y='TX Count', color='L2 Chain', title='Total Transactions Count', log_y=False)
    fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = px.bar(df, x='L2 Chain', y='Total TX Fee', color='L2 Chain', title='Total Transaction Fees', log_y=False)
    fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
with c3:
    fig = px.bar(df, x='L2 Chain', y='Active Address', color='L2 Chain', title='Total Number of Addresses', log_y=False)
    fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='Addresses Count', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
with c4:
    fig = px.bar(df, x='L2 Chain', y='Total TX Value', color='L2 Chain', title='Total Transactions Value', log_y=False)
    fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2, c3, c4 = st.columns(4)

with c1:
    fig = px.bar(df, x='L2 Chain', y='TPS', color='L2 Chain', title='Aerage TPS', log_y=False)
    fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = px.bar(df, x='L2 Chain', y='Average TX Value', color='L2 Chain', title='Average Transactions Value', log_y=False)
    fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
with c3:
    fig = px.bar(df, x='L2 Chain', y='Average TX Fee', color='L2 Chain', title='Average Transactions Fee', log_y=False)
    fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
with c4:
    fig = px.bar(df, x='L2 Chain', y='Average TX per Address', color='L2 Chain', title='Average TX per Address', log_y=False)
    fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write(
    """
**The results show that the top 3 events in both chains are 'Transfer', 'Approval' and 'Swap' respectively.**
    """
)
df = Top_20_Events_Based_on_TXs_Count_Arbitrum
c1, c2 = st.columns(2)
            
with c1:
    fig = px.bar(df, x='Event', y='TX Count', color='Event', title='🔵Arbitrum: Top 20 Events Based TXs Count', log_y=False)
    fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
df = Top_20_Events_Based_on_TXs_Count_Optimism
with c2:
    fig = px.bar(df, x='Event', y='TX Count', color='Event', title='🔴Optimism: Top 20 Events Based TXs Count', log_y=False)
    fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	

st.write(
    """
**Most addresses of both chains have only been active for one day (Arbitrum: 912k vs. Optimism: 722k). 43 addresses on the Arbitrum chain have been active for the 
most days (these addresses have been active for more than 281 days). Likewise, there are two addresses on the Optimism chain that have been active for 438 days.**
    """
)

df = Classification_of_Activity_of_Addresses_Arbitrum
fig = px.scatter(df.sort_values(['Active Day Count', 'Address Count'], ascending=[True, True]), x='Active Day Count', y='Address Count', title='🔵Arbitrum: Classification of the Number of Days of Activity', log_x=False, log_y=True)
fig.update_layout(legend_title=None, xaxis_title='Active Day Count', yaxis_title='Address Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Classification_of_Activity_of_Addresses_Optimism
fig = px.scatter(df.sort_values(['Active Day Count', 'Address Count'], ascending=[True, True]), x='Active Day Count', y='Address Count', title='🔴Optimism: Classification of the Number of Days of Activity', log_x=False, log_y=True)
fig.update_layout(legend_title=None, xaxis_title='Active Day Count', yaxis_title='Address Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write(
    """
**Optimism chain transaction success rate is 94.5%. Meanwhile, this rate for the Arbitrum chain is about 97%. On the other hand, the number of failed transactions of 
Arbitrum is less than Optimism, while the total number of transactions of Arbitrum is more than Optimism. The amount of fees paid for failed transactions in the 
Optimism chain is about 2 times that of Arbitrum (Optimism: 762 ETH & Arbitrum: 379 ETH)**
    """
)

df = Status_of_Total_Transactions
c1, c2 = st.columns(2)
            
with c1:
    fig = px.bar(df, x='L2 Chain', y='Total TXs Count', color='Status', title='Status of Total Transactions', log_y=False, barmode='group')
    fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Status', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
with c2:
    fig = px.bar(df, x='L2 Chain', y='Total TX Fees', color='Status', title='Status of Total Transaction Fees', log_y=False, barmode='group')
    fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Status', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write(
    """
**The number of transactions at the end of the night and the beginning of the morning in both chains is less than at other times. The highest number of transactions 
and transaction fees were recorded on the Arbitrum network at 13:00 on Wednesdays. Meanwhile, the highest number of Optimism network transactions are recorded at 8 am 
on Wednesdays. Optimism transaction fees are higher on Tuesdays at 19:00, 13:00, 16:00 on Wednesdays and 15:00 on Thursdays than at other times. The fees collected at 
the end of the week in both chains are lower than at other times.**
    """
)

df = Heat_Map_of_Transactions_Arbitrum
fig = px.density_heatmap(df, x='Hour', y='Day Name', z='TX Count', histfunc='avg', title='🔵Arbitrum: Transactions Count Heat map, Days of Week vs. Hours of Day', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, yaxis={'dtick': 1}, coloraxis_colorbar=dict(title='TXs Count'))
fig.update_yaxes(categoryorder='array', categoryarray=Heat_Map_of_Transactions_Arbitrum)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Heat_Map_of_Transactions_Optimism
fig = px.density_heatmap(df, x='Hour', y='Day Name', z='TX Count', histfunc='avg', title='🔴Optimism: Transactions Count Heat map, Days of Week vs. Hours of Day', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, yaxis={'dtick': 1}, coloraxis_colorbar=dict(title='TXs Count'))
fig.update_yaxes(categoryorder='array', categoryarray=Heat_Map_of_Transactions_Optimism)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Heat_Map_of_Transactions_Arbitrum
fig = px.density_heatmap(df, x='Hour', y='Day Name', z='TX Fees', histfunc='avg', title='🔵Arbitrum: Transaction Fees Heat map, Days of Week vs. Hours of Day', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, yaxis={'dtick': 1}, coloraxis_colorbar=dict(title='TX Fees'))
fig.update_yaxes(categoryorder='array', categoryarray=Heat_Map_of_Transactions_Arbitrum)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Heat_Map_of_Transactions_Optimism
fig = px.density_heatmap(df, x='Hour', y='Day Name', z='TX Fees', histfunc='avg', title='🔴Optimism: Transaction Fees Heat map, Days of Week vs. Hours of Day', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, yaxis={'dtick': 1}, coloraxis_colorbar=dict(title='TX Fees'))
fig.update_yaxes(categoryorder='array', categoryarray=Heat_Map_of_Transactions_Optimism)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.subheader('📊 Charts Analysis in Different Time Frames')

subtab_Daily, subtab_Weekly, subtab_Monthly = st.tabs(['Daily', 'Weekly', 'Monthly'])
with subtab_Daily:
            st.write(
                """
             **Ethereum layer-2 on-chain activity has been increasing to the extent that the leading two networks now process more transaction volume than mainnet 
	       Ethereum. Layer-2 networks Arbitrum and Optimism have seen an increase in transactions over the past three months. Comparatively, aside from a few 
	       spikes, transactions on the Ethereum network have declined by around 33% since late October, according to Etherscan. Ethereum processed 
	       over 1.06 million transactions on Jan. 10, whereas Arbitrum and Optimism combined processed over 1,139,136 transactions. Additionally, Optimism has 
	       now surpassed Arbitrum in terms of daily transactions following a steady uptrend in activity since September.**
                """
            )
            df = Daily_Transactions
            fig = px.line(df, x='Day', y='TX Count', color='L2 Chain', title='Total Number of Transactions', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	

            df = Arbitrum_TX_Status
            c1, c2 = st.columns(2)
             
            with c1:
                fig = px.bar(df, x='Day', y='TX Count', color='STATUS', title='🔵Arbitrum: Status of Transactions', log_y=False)
                fig.update_layout(showlegend=True, xaxis_title=None, legend_title='STATUS', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
                st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
            df = Optimism_TX_Status
            with c2:
                fig = px.bar(df, x='Day', y='TX Count', color='STATUS', title='🔴Optimism: Status of Transactions', log_y=False)
                fig.update_layout(showlegend=True, xaxis_title=None, legend_title='STATUS', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
                st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)		
		
with subtab_Daily:

            df = Daily_Transactions		
            fig = px.line(df, x='Day', y='TPS', color='L2 Chain', title='Transaction per Second (TPS)', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
		
	    
            st.write(
                """
            **From September 2022 onwards, there will be an upward trend in the fees collected by the Optimism chain. The reason for this upward trend is the increase 
	    in the number of Optimism chain transactions from September onwards. On the other hand, since August 31, 2022, the average transaction fees of Optimism 
	    network have always been higher than Arbitrum.**
                """
            )	
		
            fig = px.bar(df, x='Day', y='Total TX Fee', color='L2 Chain', title='Total Transaction Fees', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Day', y='Average TX Fee', color='L2 Chain', title='Average Transaction Fees', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
		
            st.write(
                """
            **On December 20, 2022, the number of daily active addresses of the Optimism chain surpassed Arbitrum. On December 21, 2022, the number of active 
	    addresses of the Optimism network reached 111,224 addresses, which is a new record among layer 2 chains. The number of new addresses in the Optimism chain 
	    also grew significantly in late December**
                """
            )
		
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
            st.write(
                """
            **The charts below show that almost most of the time, the value of daily transactions of Arbitrum chain was more than Optimism. On the other hand, in a 
	    large number of days, the value of Arbitrum network transactions has increased dramatically.**
                """
            )		
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
	
            df = Arbitrum_TX_Status_Weekly
            c1, c2 = st.columns(2)
             
            with c1:
                fig = px.bar(df, x='Week', y='TX Count', color='STATUS', title='🔵Arbitrum: Status of Transactions', log_y=False)
                fig.update_layout(showlegend=True, xaxis_title=None, legend_title='STATUS', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
                st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
            df = Optimism_TX_Status_Weekly
            with c2:
                fig = px.bar(df, x='Week', y='TX Count', color='STATUS', title='🔴Optimism: Status of Transactions', log_y=False)
                fig.update_layout(showlegend=True, xaxis_title=None, legend_title='STATUS', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
                st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
with subtab_Weekly:
            df = Weekly_Transactions		
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
	
            df = Arbitrum_TX_Status_Monthly
            c1, c2 = st.columns(2)
             
            with c1:
                fig = px.bar(df, x='Month', y='TX Count', color='STATUS', title='🔵Arbitrum: Status of Transactions', log_y=False)
                fig.update_layout(showlegend=True, xaxis_title=None, legend_title='STATUS', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
                st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
            df = Optimism_TX_Status_Monthly
            with c2:
                fig = px.bar(df, x='Month', y='TX Count', color='STATUS', title='🔴Optimism: Status of Transactions', log_y=False)
                fig.update_layout(showlegend=True, xaxis_title=None, legend_title='STATUS', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
                st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	

with subtab_Monthly:
            df = Monthly_Transactions			
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
st.subheader('📊 Conclusion')
            st.write(
                """
            **In this dashboard, the transaction status of two of the most important layer 2 chains, Arbitrum and Optimism, were compared. In many indicators, Arbitrum
	    has a better situation than Optimism, while we see a significant growth in the Optimism transactions from September 2022 onwards, which indicates the 
	    desire of the Optimism chain to take the first place among the layer 2 chains and pass Arbitrum.**
                """
            )	
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




