import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime,timedelta
import os
import warnings
#import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

st.set_page_config(page_title="PML 2_3 PROD REPORT", page_icon=":bar_chart:",layout="wide")

#@st.cache_data
data = pd.read_excel('https://github.com/code-aliu/dwprodreport/blob/main/SampleDataProd.xlsx')
#st.image('data:image/jpeg;base64,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')
#st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuwoecKBOtDIEkRakOOVHJj_yhnNKeGF5RYA&usqp=CAU')

st.title("PML 2/3 DAILY PRODUCTION REPORT")
st.sidebar.image('totalLogo.JPEG')
st.sidebar.subheader('Select Date Range')
#st.sidebar.header("Select Report to view: ")

#s_d=pd.to_datetime
en_date=pd.to_datetime(data['Date'].max())


start_date = pd.to_datetime(st.sidebar.date_input('Start Date',en_date-timedelta(days=7)))
end_date = pd.to_datetime(st.sidebar.date_input('End Date (Latest Report Date)',data['Date'].max()))
st.sidebar.header("Select Report to view: ")
sideBars = st.sidebar
pml23= sideBars.button("PML 2/3 REPORT")
egina = sideBars.button("EGINA REPORT")
akpo = sideBars.button("AKPO REPORT")


filtered_data=data[(data['Date']>=start_date) & (data['Date']<=end_date)]

latest_data=filtered_data.iloc[-1]

st.write('Latest Report Date (You can change it with the End Date selection at the side bar on the left Pane)')
st.write(f"{latest_data['Date'].strftime('%d, %B, %Y')}")
st.subheader('SUMMARY')
st.markdown("""---""")

#def creat_gauge_chart(value,max_val,title):
coool1, coool2, coool3 = st.columns(3)
coool1.subheader("BU23")
coool2.subheader("MTD")
coool3.subheader("DAY")
cool1, cool2, cool3 = st.columns(3)
cool1.metric("Oil Production", "183.2 kbopd", "1.2 kbopd")
cool2.metric("Oil Production", "161.6 kbopd", "-8%")
cool3.metric("Oil Production", "161.9 kbopd", "4%")

cool1, cool2, cool3 = st.columns(3)
cool1.metric("DW Gas (MSm3/d)", "7.7 MSm3/d", "1.2 MSm3/d")
cool2.metric("DW Gas (MSm3/d)", "10.4 MSm3/d", "-8%")
cool3.metric("DW Gas (MSm3/d)", "10.4 MSm3/d", "4%")


st.markdown("""---""")

col_1,col_2,col_3,col_4,col_5 = st.columns((5))
#gauge_container=st.container()
with col_1:
    #st.subheader("Oil Production")
    oil_gauge = go.Figure(go.Indicator(
    mode = 'gauge+number',
    value = latest_data['Oil Production'],
    title={'text':'Oil Production (bb/d)'},
    gauge={
    'axis':{'range':[0,latest_data['Target']]},
    'threshold':{
    'line':{'color':"red",'width':2},
    'thickness':0.75,
    'value':latest_data['Target']
    },
    #'bgcolor':'green'
    }
    ))
    oil_gauge.update_layout(
        margin=dict(l=10,r=10,t=50,b=10,pad=8),
        #showlegend=True,
        #plot_bgcolor="white",
        height=200,
    )
    st.plotly_chart(oil_gauge,use_container_width=True)
    #st.write(f" {latest_data['Oil Production']}")
with col_2:
    #st.subheader("Gas Export")
   
    oil_gauge = go.Figure(go.Indicator(
    mode = 'gauge+number',
    value = latest_data['Gas Export'],
    title={'text':'Gas Export (MSm3/d)'},
    gauge={
    'axis':{'range':[0,data['Gas Export'].max()]},
    'bar':{'color':'yellow'},
    'threshold':{
    'line':{'color':"orange",'width':5},
    'thickness':0.75,
    'value':data['Gas Export'].max()
    },
    }

    ))
    oil_gauge.update_layout(
        margin=dict(l=10,r=10,t=50,b=10,pad=8),
        #showlegend=True,
        #plot_bgcolor="white",
        height=200,
    )
    st.plotly_chart(oil_gauge,use_container_width=True)
   # st.write(f"{latest_data['Gas Export']}")
with col_3:
    #st.subheader("Flaring")
    
    oil_gauge = go.Figure(go.Indicator(
    mode = 'gauge+number',
    value = latest_data['Flaring'],
    title={'text':'Flaring (kSm3/d)'},
    gauge={
    'axis':{'range':[0,data['Flaring'].max()]},
    'bar':{'color':'orange'},
    'threshold':{
    'line':{'color':"yellow",'width':5},
    'thickness':0.75,
    'value':data['Flaring'].max()
    }
    }
    ))
    oil_gauge.update_layout(
        margin=dict(l=10,r=10,t=50,b=10,pad=8),
        #showlegend=True,
        #plot_bgcolor="white",
        height=200,
    )
    st.plotly_chart(oil_gauge,use_container_width=True)

with col_4:
    #st.subheader("Flaring")
    
    oil_gauge = go.Figure(go.Indicator(
    mode = 'gauge+number',
    value = latest_data['Water Injection'],
    title={'text':'Water Injection (bwpd)'},
    gauge={
    'axis':{'range':[0,data['Water Injection'].max()]},
    'bar':{'color':'orange'},
    'threshold':{
    'line':{'color':"yellow",'width':5},
    'thickness':0.75,
    'value':data['Flaring'].max()
    }
    }
    ))
    oil_gauge.update_layout(
        margin=dict(l=10,r=10,t=50,b=10,pad=8),
        #showlegend=True,
        #plot_bgcolor="white",
        height=200,
    )
    st.plotly_chart(oil_gauge,use_container_width=True)

with col_5:
    #st.subheader("Flaring")
    
    oil_gauge = go.Figure(go.Indicator(
    mode = 'gauge+number',
    value = latest_data['Fuel Gas'],
    title={'text':'Fuel Gas (kSm3/d)'},
    gauge={
    'axis':{'range':[0,data['Fuel Gas'].max()]},
    'bar':{'color':'orange'},
    'threshold':{
    'line':{'color':"yellow",'width':5},
    'thickness':0.75,
    'value':data['Fuel Gas'].max()
    }
    }
    ))
    oil_gauge.update_layout(
        margin=dict(l=10,r=10,t=50,b=10,pad=8),
        #showlegend=True,
        #plot_bgcolor="white",
        height=200,
    )
    st.plotly_chart(oil_gauge,use_container_width=True)
   # st.write(f"{latest_data['Flaring']}")
#st.subheader('Trends of Data for Selected time range')
#fig=px.line(filtered_data, x='Date',y=['Oil Production','Gas Export','Flaring'])
#st.plotly_chart(fig)
#st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

com_1,com_2,com_3=st.columns((3))
with com_1:
    st.subheader("Production Comment")
    st.write(f"{latest_data['Production Comment']}")
with com_2:
    st.subheader("Flaring Comment")
    st.write(f"{latest_data['Flaring Comments']}")
with com_3:
    st.subheader("Water Injection Comment")
    st.write(f"{latest_data['Water Injection Comments']}")



st.markdown("""---""")
st.subheader("PRODUCTION REPORT FIGURES BASED ON SELECTED DATE RANGE")
st.dataframe(filtered_data)
st.markdown("""---""")

st.subheader("Oil Production Trend")
fig1=go.Figure()
fig1.add_trace(go.Scatter(
    x=filtered_data['Date'],
    y=filtered_data['Oil Production'],
    #axis='range':[0,data['Oil Production'].max()]
    #orientation = 'v',
    name ='Oil Production',
    line=dict(color='green', width=5)
))
fig1.add_trace(go.Scatter(
    x=filtered_data['Date'],
    y=filtered_data['Target'],
    #orientation = 'v',
    name ='Oil Production Target',
    line=dict(color='red', width=2)
))

fig1.update_layout(yaxis=dict(range=[60000,data['Oil Production'].max()+5000]),barmode='relative',title='Oil Production Trend and Target')
st.plotly_chart(fig1,use_container_width=True, height = 200)

oil_chart = px.line(filtered_data,x='Date',y='Oil Production',title='Oil Production Trend')
st.plotly_chart(oil_chart,use_container_width=True, height = 200)

st.subheader('DW DAILY OIL PRODUCTION [KBOPD]')
fig =go.Figure()


fig.add_trace(go.Bar(
    x=filtered_data['Date'],
    y=filtered_data['Oil Production'],
    orientation = 'v',
    name ='Egina',
    #marker = dict(color='')
    marker = dict(color='#154c79')
))


#fig.add_trace(go.Scatter(
 #   x=filtered_data['Date'],
  #  y=filtered_data['Target'],
   # #orientation = 'v',
    #name ='Oil Target',
    #line=dict(color='red', width=5)
#))

fig.add_trace(go.Bar(
    x=filtered_data['Date'],
    y=filtered_data['Akpo Oil Production'],
    orientation = 'v',
    name ='Akpo',
    marker = dict(color='rgb(37, 150, 190)')
))

fig.add_trace(go.Scatter(
    x=filtered_data['Date'],
    y=filtered_data['DW Oil Target'],
    #orientation = 'v',
    name ='DW Oil Production Target',
    line=dict(color='green', width=2)
))

fig.update_layout(barmode='relative',title='Egina and Akpo Oil Chart Trend')
st.plotly_chart(fig,use_container_width=True, height = 200)
