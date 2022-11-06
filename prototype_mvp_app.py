import streamlit as st


st.set_page_config( page_title="Cultural Health Moments App",
                    page_icon= "random",
                    layout="wide"
 )

col1, col2, col3 = st.columns((.1,1,.1))

with col1:
    st.write("")

with col2:
    st.markdown(" <h1 style='text-align: center;'>Developing a Score to Measure Riskiness of Residential Properties as part of an Residential Insurance underwriting process</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'><i>Developing a Score to Measure Riskiness of Residential buildings, Homes, Apartments and Condos as "
                "part of an insurance policy underwriting. Insurance underwriting is how an insurance company evaluates its risk. In this project, we "
                "identify and explore multiple data sources to collect variables that could be used to develop a score that measures the riskiness of "
                "residential buildings to aid the insurance underwriting process.</i></p>", unsafe_allow_html=True)
    st.markdown("<center><img src='https://github.com/kkrusere/Developing-a-Score-to-Measure-Riskiness-of-Residential-Properties-Insurance/blob/main/assets/real-estate-risk.jpg?raw=1' width=600/></center>", unsafe_allow_html=True)


with col3:
    st.write("")


st.markdown("----")

col1, col2,col3 = st.columns((1,0.1,1))

with col1:
   
    st.markdown("### ***Project Contributors:***")
    st.markdown("Kuzi Rusere, Umair Shaikh")

    st.markdown("### **Project Introduction**")
    st.markdown("***Business Proposition:*** ")
    st.markdown("***Methodology:*** ")
    """

    """
    st.markdown("In addition, we created this `Streamlit` interactive data visualization "
                "tool that allows users interact with the data, model and analytics.")
with col2:
    pass
with col3:
    st.markdown("### ***Data Collection:***")

    """
    **General Information About the Data**


    ###### **The data source:**
    
    """

    st.image("https://github.com/kkrusere/Developing-a-Score-to-Measure-Riskiness-of-Residential-Properties-Insurance/blob/main/assets/nycOpenData.png?raw=1", caption="https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9")


st.markdown("----")
st.markdown("### Data Analysis")
st.markdown("#### NYC 311 Residential Service Requests and Complaints")
st.markdown("#### NYC Fire Department Residential Incidence")
st.markdown("#### NYC Police Department Residential Incidences and Cases")

st.markdown("----")
st.markdown("### Score Measurements by Borough and/or Zipcode")
st.markdown("\nHere we show the scoring measurements of each of the Boroughs and/or Zipcodes with respect to the fire department incedences, police department cases and incidences, and the 311 residential service request and complaints. So, depending on the zipcode or the borough in New York City, there is a ranking measurement score that has been assigned to it from our modeling and cluster analysis.") 
st.markdown("#### NYC 311 Residential Service Requests and Complaints Ranking and Score")
st.markdown("#### NYC Fire Department Residential Incidence Ranking and Score")
st.markdown("#### NYC Police Department Residential Incidences and Cases Ranking and Score")

st.markdown("----")
