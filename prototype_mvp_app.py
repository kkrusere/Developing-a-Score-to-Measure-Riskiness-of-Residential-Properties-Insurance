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


    st.markdown("***Business Proposition:*** ")
    st.markdown("Developing a Score to Measure the Riskiness of Residential buildings, Homes, Apartments, and Condos as part of an insurance policy underwriting. "
                "The idea is to design and develop a model that will aid insurance underwriters in assessing the riskiness of residential properties in New York City. "
                "For this, we utilized data collected from the NYC Opendata repository, created a Machine Learning Clustering model, and Analyzed the clusters, "
                "depending on the characteristics of the clusters, they were ranked thus providing a scoring mechanism. We used the FDNY incident data, the NYPD crime "
                "data and the 311 service request and complaints data for our ML clustering models and for the scoring measurement.")
    st.markdown("***Methodology:*** ")
    """
    1. Data Collection 
    2. Data Cleaning, Preparation and Preprocessing 
    3. Modeling and Evaluation (Creating clusters in each of the datasets using Kmodes clustering algorithm)
    4. Analysis of the clusters creating a ranking score measure for each of the datasets

    """
    st.markdown("In addition, we created this `Streamlit` interactive data visualization "
                "tool that allows users interact with the data, model and analytics.")
with col2:
    pass
with col3:
    st.markdown("### ***Data Collection:***")

    """
    **General Information About the Data:**
    NYC Open Data makes the wealth of public data generated by various New York City agencies and other City organizations available for public use. 
    As part of an initiative to improve the accessibility, transparency, and accountability of City government, this catalog offers access to a 
    repository of government-produced, machine-readable data sets. 


    ###### **The data source:**
    We collected 3 datasets from the NYC OpenData,  NYC311 service request and complaints data, FDNYC (New York City Fire Department) incidents data and the NYPD (New York City Police Department) crime data 
    
    """

    st.image("https://github.com/kkrusere/Developing-a-Score-to-Measure-Riskiness-of-Residential-Properties-Insurance/blob/main/assets/nycOpenData.png?raw=1", caption="https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9")


st.markdown("----")
st.markdown("### Data Analysis")
col1, col2,col3 = st.columns((1,0.1,1))
with col1:
    st.markdown("##### NYC 311 Residential Service Requests and Complaints")
    st.markdown("<center><img src='https://github.com/kkrusere/Developing-a-Score-to-Measure-Riskiness-of-Residential-Properties-Insurance/blob/main/assets/nyc311-logo.png?raw=1' width=100/></center>", unsafe_allow_html=True)
with col3:
    pass
col1, col2,col3 = st.columns((1,0.1,1))
with col1:
    st.markdown("##### NYC Fire Department Residential Incidence")
    st.markdown("<center><img src='https://github.com/kkrusere/Developing-a-Score-to-Measure-Riskiness-of-Residential-Properties-Insurance/blob/main/assets/FDNYC.png?raw=1' width=100/></center>", unsafe_allow_html=True)
with col3:
    pass

col1, col2,col3 = st.columns((1,0.1,1))
with col1:
    st.markdown("##### NYC Police Department Residential Incidences and Cases")
    st.markdown("<center><img src='https://github.com/kkrusere/Developing-a-Score-to-Measure-Riskiness-of-Residential-Properties-Insurance/blob/main/assets/NYPD.png?raw=1' width=100/></center>", unsafe_allow_html=True)
with col3:
    pass

st.markdown("----")
st.markdown("### Score Measurements by Borough and/or Zipcode")
st.markdown("\nHere we show the scoring measurements of each of the Boroughs and/or Zipcodes with respect to the fire department incedences, police department cases and "
            "incidences, and the 311 residential service request and complaints. So, depending on the zipcode or the borough in New York City, there is a ranking measurement "
            "score that has been assigned to it from our modeling and cluster analysis.") 

st.markdown("##### Here, Please select the method you want to use for looking up the riskiness of the residential property, either Borough or Zipcode.")
col1, col2,col3 = st.columns((0.1,1,0.8))
with col2:
    option = st.selectbox(
    'Please select a method:',
    (" ",'Borough', 'Zipcode'))

    st.write('You selected:', option)
    if option == 'Borough':
        borough_option = st.selectbox(
            'Which Borough?:',
            (" ","Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"))
        st.success(f"we are going to look at {borough_option}")
        
st.markdown("##### NYC 311 Residential Service Requests and Complaints Ranking and Score")
st.markdown("##### NYC Fire Department Residential Incidence Ranking and Score")
st.markdown("##### NYC Police Department Residential Incidences and Cases Ranking and Score")

st.markdown("----")
