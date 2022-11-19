import streamlit as st
import plotly.express as px
import pandas as pd 
import matplotlib.pyplot as plt


urlpatterns = [
    
]
nyc_zipcode_dict = {
                    "Manhattan":range(10001,10283),
                    "Staten Island":range(10301,10315),
                    "Bronx":range(10451,10476),
                    "Queens":[range(11004,11110), range(11351,11698)],
                    "Brooklyn":range(11201,11257)
}

st.set_page_config( page_title="MVP_App",
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


st.markdown("###### Cluster Distribution")
col1, col2,col3 = st.columns((1,0.1,1))
col1, col2,col3 = st.columns((1,0.1,1))
st.markdown("###### Borough Distribution")
col1, col2,col3 = st.columns((1,0.1,1))
col1, col2,col3 = st.columns((1,0.1,1))
col1, col2,col3 = st.columns((1,0.1,1))


with col1:
    st.markdown("##### NYC Fire Department Residential Incidence")
    st.markdown("<center><img src='https://github.com/kkrusere/Developing-a-Score-to-Measure-Riskiness-of-Residential-Properties-Insurance/blob/main/assets/FDNYC.png?raw=1' width=100/></center>", unsafe_allow_html=True)
with col3:
    pass

st.markdown("###### Cluster Distribution")
col1, col2,col3 = st.columns((1,0.1,1))
col1, col2,col3 = st.columns((1,0.1,1))
st.markdown("###### Borough Distribution")
col1, col2,col3 = st.columns((1,0.1,1))
col1, col2,col3 = st.columns((1,0.1,1))

col1, col2,col3 = st.columns((1,0.1,1))
with col1:
    st.markdown("##### NYC Police Department Residential Incidences and Cases")
    st.markdown("<center><img src='https://github.com/kkrusere/Developing-a-Score-to-Measure-Riskiness-of-Residential-Properties-Insurance/blob/main/assets/NYPD.png?raw=1' width=100/></center>", unsafe_allow_html=True)
with col3:
    pass


nypd_data = pd.read_csv("https://raw.githubusercontent.com/kkrusere/Developing-a-Score-to-Measure-Riskiness-of-Residential-Properties-Insurance/main/data/MODEL_NYPD_Complaint_Data_Historic.csv")
nypd_data['ZIPCODE'] = nypd_data['ZIPCODE'].astype(str)
nypd_data['Cluster'] = nypd_data['Cluster'].astype(str)

#Lets start by looking at the number of cluster in our data modeled data 
temp_df = pd.DataFrame(nypd_data['Cluster'].value_counts())
temp_df = temp_df.reset_index()
temp_df.columns = [temp_df.columns[1], 'Count']


st.dataframe(nypd_data, use_container_width= True)

col1, col2,col3 = st.columns((1,0.1,1))
with col1:
    #let look at a histogram of the clusters 
    fig = px.histogram(nypd_data, x = 'Cluster', title="The Frequency Distribution of the Clusters in the NYPD Modeled Dataset")
    st.plotly_chart(fig)
with col3:
     #let look at a picture of the above dataframe
    fig = px.pie(temp_df, names='Cluster', values='Count', title="The Frequency Distribution of the Clusters in the NYPD Modeled Dataset")
    st.plotly_chart(fig)

st.markdown("###### Cluster Distribution")
col1, col2,col3 = st.columns((1,0.1,1))

with col1:

    #let look at a histogram of the clusters stratified by Borough distribution
    fig = px.histogram(nypd_data, x = 'Cluster',color="BOROUGH", title="The Frequency Distribution of the Clusters in the NYPD Modeled Dataset")
    st.plotly_chart(fig)


with col3:
    option = st.selectbox(
    'Please select a filter',
                ('Cluster',
                'OFNS_DESC',
                'CRM_ATPT_CPTD_CD',
                'LAW_CAT_CD',
                'BOROUGH',
                'LOC_OF_OCCUR_DESC',
                'PREM_TYP_DESC',
                'ZIPCODE'))

    #let look at a histogram of the clusters stratified by Borough distribution
    fig = px.histogram(nypd_data, x = 'Cluster',color=option, title="The Frequency Distribution of the Clusters in the NYPD Modeled Dataset")
    st.plotly_chart(fig)

st.markdown("###### Borough Distribution")
col1, col2,col3 = st.columns((1,0.1,1))
col1, col2,col3 = st.columns((1,0.1,1))

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
        if borough_option != " ":
            st.success(f"we are going to look at {borough_option}")
    else:
        try:
            zipcode = st.text_input("Please input the zipcode:")
            if zipcode != "":
                zipcode = int(zipcode)
                check = False
                for key in nyc_zipcode_dict:
                    if key == "Queens":
                        for alist in nyc_zipcode_dict[key]:
                            if zipcode in alist:
                                st.success(f"We are going to look at {zipcode} that is part of the {key} borough")
                                check = True
                                break
                    elif zipcode in nyc_zipcode_dict[key]:
                        st.success(f"We are going to look at {zipcode} that is part of the {key} borough")
                        check = True
                        break
                if check == False:
                    st.error("Zipcode not for NYC, Please enter an NYC zipcode")

            else:
                pass
        except:
            st.warning("Please enter a valid Zipcode")    

if zipcode != "" or borough_option != "":
    st.markdown("##### NYC 311 Residential Service Requests and Complaints Ranking and Score")
    nyc_csr311_data_cluster_belonging_dict_borough = {'MANHATTAN': '0',
                                            'BROOKLYN': '2',
                                            'BRONX': '3',
                                            'QUEENS': '1',
                                            'STATEN ISLAND': '1'}


    nyc_csr311_data_cluster_belonging_dict_zip = {'10031': '0',
    '10032': '0',
    '10034': '0',
    '10033': '0',
    '10040': '0',
    '10029': '0',
    '10027': '0',
    '10025': '0',
    '10030': '0',
    '11226': '2',
    '10467': '3',
    '10468': '3',
    '10002': '0',
    '10026': '0',
    '10039': '0',
    '10009': '0',
    '10035': '0',
    '10456': '3',
    '10452': '3',
    '10458': '3',
    '10003': '0',
    '10453': '3',
    '10457': '3',
    '11221': '2',
    '10463': '3',
    '11207': '2',
    '11237': '2',
    '11206': '2',
    '11212': '2',
    '10019': '0',
    '10011': '0',
    '11213': '2',
    '10472': '3',
    '10024': '0',
    '11216': '2',
    '10462': '3',
    '11385': '1',
    '11205': '0',
    '10460': '3',
    '11225': '2',
    '11233': '2',
    '11208': '2',
    '11368': '1',
    '10466': '3',
    '11238': '2',
    '10037': '0',
    '10128': '0',
    '10023': '0',
    '10016': '0',
    '11211': '2',
    '10036': '0',
    '11203': '2',
    '11419': '0',
    '11236': '2',
    '10459': '3',
    '10028': '0',
    '10451': '3',
    '10469': '3',
    '11373': '1',
    '10473': '3',
    '10014': '0',
    '11230': '2',
    '11372': '1',
    '10012': '0',
    '10454': '3',
    '10001': '0',
    '11435': '1',
    '11377': '1',
    '10455': '3',
    '11210': '2',
    '11201': '0',
    '11235': '2',
    '10022': '0',
    '10010': '0',
    '11220': '2',
    '10461': '3',
    '11209': '2',
    '11691': '1',
    '11218': '2',
    '11234': '2',
    '11229': '2',
    '11420': '1',
    '11421': '1',
    '10304': '1',
    '10013': '0',
    '10021': '0',
    '11106': '1',
    '11101': '1',
    '11375': '1',
    '10314': '0',
    '11223': '2',
    '10301': '1',
    '11214': '2',
    '11434': '1',
    '10465': '0',
    '11369': '1',
    '11433': '1',
    '11217': '2',
    '11432': '1',
    '11224': '2',
    '10065': '0',
    '11215': '2',
    '10075': '0',
    '11222': '2',
    '11204': '2',
    '11249': '2',
    '11355': '1',
    '11102': '1',
    '11354': '1',
    '11374': '1',
    '10310': '1',
    '10038': '0',
    '11417': '1',
    '11418': '1',
    '11231': '2',
    '11103': '1',
    '10306': '1',
    '11232': '2',
    '11104': '1',
    '11219': '2',
    '10474': '3',
    '11436': '1',
    '10302': '1',
    '11423': '1',
    '11415': '1',
    '11365': '0',
    '11370': '0',
    '11367': '1',
    '11416': '1',
    '10017': '0',
    '11105': '1',
    '10303': '1',
    '10312': '0',
    '11366': '0',
    '10470': '3',
    '11379': '0',
    '10305': '1',
    '11414': '1',
    '11356': '1',
    '11358': '1',
    '10471': '3',
    '11693': '1',
    '11413': '1',
    '11412': '1',
    '11428': '1',
    '10018': '0',
    '11427': '1',
    '11692': '1',
    '11378': '1',
    '11429': '1',
    '11422': '1',
    '11228': '2',
    '11694': '1',
    '11357': '0',
    '11426': '0',
    '11361': '1',
    '10308': '0',
    '10309': '1',
    '11360': '0',
    '11411': '1',
    '10044': '0',
    '10007': '0',
    '11364': '1',
    '10005': '0',
    '10475': '3',
    '10282': '0',
    '10307': '0',
    '11239': '2',
    '10006': '0',
    '10069': '0',
    '11362': '0',
    '10464': '3',
    '11004': '1',
    '10280': '0',
    '11363': '1',
    '10004': '0',
    '11001': '1',
    '11109': '0',
    '11040': '0',
    '10123': '0',
    '11697': '1',
    '10129': '1',
    '11430': '1'}   
    if zipcode != "":
        st.markdown(f"For NYC 311 Residential Service Requests and Complaints the zipcode you entered had is most likely to be in cluster: {nyc_csr311_data_cluster_belonging_dict_zip[str(zipcode)]}")
    else:
        st.markdown(f"For NYC 311 Residential Service Requests and Complaints the Borough you entered had is most likely to be in cluster: {nyc_csr311_data_cluster_belonging_dict_borough[borough_option]}")


    st.markdown("##### NYC Fire Department Residential Incidence Ranking and Score")
    fdnyc_data_cluster_belonging_dict_borough = {'BRONX': '6',
                            'MANHATTAN': '7',
                            'BROOKLYN': '2',
                            'QUEENS': '5',
                            'STATEN ISLAND': '5'}
    fdnyc_data_cluster_belonging_dict_zip = {'10453': '0',
    '10456': '6',
    '10467': '6',
    '10469': '0',
    '10454': '0',
    '10466': '0',
    '10473': '0',
    '10451': '6',
    '10460': '6',
    '10457': '6',
    '10452': '6',
    '10472': '6',
    '10458': '6',
    '11206': '2',
    '10455': '6',
    '10468': '6',
    '11226': '2',
    '10027': '7',
    '10463': '6',
    '10002': '7',
    '10462': '6',
    '10459': '6',
    '10475': '6',
    '11224': '2',
    '10465': '0',
    '10035': '7',
    '11213': '2',
    '10039': '7',
    '11233': '2',
    '10009': '7',
    '11221': '2',
    '10033': '7',
    '10461': '6',
    '10031': '7',
    '10032': '7',
    '10030': '7',
    '11225': '2',
    '11216': '2',
    '10026': '7',
    '10019': '7',
    '11205': '2',
    '11691': '2',
    '10003': '7',
    '10128': '7',
    '11211': '2',
    '10023': '7',
    '10024': '7',
    '10016': '7',
    '10011': '7',
    '11238': '2',
    '11201': '2',
    '11368': '2',
    '10014': '7',
    '11235': '2',
    '10034': '7',
    '10471': '6',
    '11377': '2',
    '11236': '8',
    '10040': '7',
    '10037': '7',
    '11210': '2',
    '10304': '5',
    '11215': '2',
    '10028': '7',
    '11203': '2',
    '11217': '2',
    '11101': '2',
    '11231': '2',
    '11223': '2',
    '10470': '0',
    '10013': '7',
    '11229': '2',
    '11373': '2',
    '11372': '2',
    '11355': '2',
    '11237': '2',
    '11230': '2',
    '11219': '2',
    '10012': '7',
    '10021': '7',
    '10036': '7',
    '11249': '2',
    '10010': '7',
    '10001': '7',
    '10038': '7',
    '11102': '2',
    '11220': '2',
    '11106': '2',
    '10474': '6',
    '11374': '2',
    '11214': '2',
    '11385': '2',
    '11209': '2',
    '10022': '7',
    '11432': '2',
    '10310': '5',
    '11218': '2',
    '10301': '5',
    '11692': '2',
    '10065': '7',
    '11204': '2',
    '11375': '2',
    '11222': '2',
    '11354': '2',
    '11435': '5',
    '11365': '2',
    '11433': '5',
    '10075': '7',
    '11103': '2',
    '10303': '5',
    '11367': '2',
    '11234': '8',
    '11693': '2',
    '10017': '4',
    '11239': '2',
    '10018': '4',
    '11104': '2',
    '10306': '5',
    '10314': '5',
    '11415': '2',
    '10007': '0',
    '11232': '2',
    '11105': '2',
    '11421': '5',
    '10305': '5',
    '11423': '5',
    '11418': '5',
    '10464': '0',
    '11427': '5',
    '11414': '5',
    '11417': '5',
    '11694': '5',
    '11419': '5',
    '11369': '5',
    '11412': '5',
    '11358': '5',
    '10044': '7',
    '11228': '8',
    '11378': '5',
    '11364': '5',
    '10302': '5',
    '11379': '5',
    '11360': '5',
    '11004': '5',
    '11356': '5',
    '11370': '5',
    '11357': '5',
    '11361': '5',
    '11416': '5',
    '11362': '5',
    '10280': '7',
    '10005': '7',
    '11420': '5',
    '11413': '5',
    '10309': '5',
    '11422': '5',
    '11363': '5',
    '11005': '0',
    '10006': '4',
    '10004': '7',
    '11429': '5',
    '11436': '5',
    '11426': '5',
    '10069': '7',
    '11428': '5',
    '10308': '5',
    '11366': '5',
    '11411': '5',
    '10312': '5',
    '10282': '7',
    '11109': '2',
    '11430': '4',
    '10020': '7',
    '11242': '0',
    '11001': '2',
    '11212': '2',
    '11207': '8',
    '11208': '2',
    '10307': '5',
    '11040': '5',
    '11697': '5',
    '10029': '7',
    '10106': '7',
    '10281': '7',
    '10162': '7',
    '10119': '7',
    '10103': '7',
    '10025': '4',
    '10000': '4',
    '11434': '5'}

    if zipcode != "":
        st.markdown(f"For NYC Fire Department Residential Incidence the zipcode you entered had is most likely to be in cluster: {fdnyc_data_cluster_belonging_dict_zip[str(zipcode)]}")
    else:
        st.markdown(f"For NYC Fire Department Residential Incidence the Borough you entered had is most likely to be in cluster: {fdnyc_data_cluster_belonging_dict_borough[borough_option]}")


    st.markdown("##### NYC Police Department Residential Incidences and Cases Ranking and Score")



    nypd_data_cluster_belonging_dict_borough = {'BROOKLYN': '1',
                                        'MANHATTAN': '5',
                                        'BRONX': '2',
                                        'QUEENS': '0',
                                        'STATEN ISLAND': '0'}
    nypd_data_cluster_belonging_dict_zip= {'11212': '1','11207': '1','11221': '1','11233': '1','11236': '1','11208': '1','11213': '1','11216': '1','11203': '1','11206': '1',
    '11224': '1',
    '11234': '1',
    '11225': '1',
    '10458': '2',
    '11226': '1',
    '11210': '1',
    '10459': '2',
    '10027': '5',
    '10457': '2',
    '11238': '1',
    '10453': '2',
    '10460': '2',
    '10025': '1',
    '11220': '1',
    '10002': '5',
    '10009': '1',
    '10467': '2',
    '11223': '1',
    '10473': '2',
    '10468': '2',
    '10472': '2',
    '11237': '1',
    '11211': '1',
    '10452': '2',
    '11385': '0',
    '11222': '1',
    '10454': '2',
    '11235': '1',
    '11218': '1',
    '10466': '2',
    '11217': '1',
    '10039': '1',
    '10032': '1',
    '11229': '1',
    '11219': '1',
    '10030': '1',
    '10035': '5',
    '11214': '1',
    '10463': '2',
    '11230': '1',
    '11204': '1',
    '10455': '2',
    '10003': '1',
    '10033': '1',
    '11103': '1',
    '11215': '1',
    '10001': '1',
    '10031': '5',
    '11373': '0',
    '10011': '1',
    '11368': '0',
    '11209': '4',
    '10016': '1',
    '11228': '1',
    '10019': '1',
    '10461': '1',
    '10451': '2',
    '11205': '1',
    '11231': '1',
    '10026': '5',
    '11432': '0',
    '11355': '0',
    '10037': '5',
    '11201': '1',
    '10024': '1',
    '11377': '0',
    '11249': '1',
    '10462': '2',
    '10314': '0',
    '10128': '5',
    '10301': '0',
    '10012': '1',
    '10034': '5',
    '10021': '1',
    '11375': '0',
    '10022': '1',
    '10474': '2',
    '10469': '2',
    '10014': '1',
    '11232': '1',
    '10013': '1',
    '11101': '0',
    '10018': '1',
    '11354': '0',
    '10040': '5',
    '11106': '0',
    '10475': '2','11691': '0','10029': '5','10010': '1','10470': '2','10465': '2','11239': '1',
    '10065': '1',
    '11372': '0',
    '10036': '5',
    '10456': '2',
    '11692': '0',
    '10304': '0',
    '11435': '0',
    '10038': '5',
    '10028': '1',
    '11102': '0',
    '10306': '4',
    '10309': '0',
    '10017': '1',
    '11420': '0',
    '11433': '0',
    '11421': '0',
    '11358': '0',
    '10007': '1',
    '11374': '0',
    '10075': '5',
    '10303': '0',
    '10023': '5',
    '10312': '0',
    '11104': '0',
    '11369': '0',
    '11413': '0',
    '11693': '0',
    '11367': '0',
    '11365': '0',
    '11360': '0',
    '10044': '0',
    '11378': '0',
    '11418': '0',
    '11370': '0',
    '11419': '0',
    '11412': '0',
    '10471': '2',
    '11361': '0',
    '11427': '0',
    '10105': '1',
    '10308': '0',
    '10302': '0',
    '11109': '1',
    '10005': '1',
    '11251': '1',
    '12692': '0',
    '11694': '0',
    '10305': '0',
    '11422': '0',
    '10310': '0',
    '11436': '0',
    '11423': '0',
    '11429': '0',
    '10307': '0',
    '11416': '0',
    '10069': '1',
    '11357': '0',
    '11364': '0',
    '11411': '0',
    '10158': '1',
    '10115': '5',
    '11004': '0',
    '11426': '0',
    '11363': '1',
    '10107': '1',
    '11428': '0',
    '11366': '0',
    '11105': '0',
    '11414': '0',
    '11379': '0',
    '11417': '0',
    '11434': '0',
    '11415': '0',
    '10464': '4',
    '11356': '0',
    '10280': '5',
    '10004': '4',
    '11362': '0',
    '10282': '2',
    '11001': '0',
    '11697': '0',
    '11040': '0',
    '11096': '0',
    '10285': '5',
    '10120': '5'}

    if zipcode != "":
        st.markdown(f"For NYC Police Department Residential Incidences and Cases the zipcode you entered had is most likely to be in cluster: {nypd_data_cluster_belonging_dict_zip[str(zipcode)]}")
    else:
        st.markdown(f"For NYC Police Department Residential Incidences and Cases the Borough you entered had is most likely to be in cluster: {nypd_data_cluster_belonging_dict_borough[borough_option]}")


st.markdown("----")



