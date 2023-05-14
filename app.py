import streamlit as st
from streamlit.components.v1 import html

st.markdown("<h1 style='text-align: center; color: #2a2b2a;'>Heart Disease Prediction Web Application</h1>", unsafe_allow_html=True)
#st.title("Heart Disease Prediction")

# # Set the page title
# with st.container():
#   st.title("COVID-19 Prediction App")

# Add a picture
#st.image("https://editor.analyticsvidhya.com/uploads/95051Cardiovascular-Disease.jpg", width=500)
#st.image("https://cdn.analyticsvidhya.com/wp-content/uploads/2018/08/health.jpg")
#st.image("https://www.lenmed.co.za/wp-content/uploads/How-do-you-know-if-you-are-having-a-heart-attack.png")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    #st.image("https://editor.analyticsvidhya.com/uploads/95051Cardiovascular-Disease.jpg")
    st.image("https://www.cardio.com/hubfs/human%20heart%20illustration.jpeg")

st.write(" ")
st.write(" ")

col1, col2 = st.columns(2)

with col1:
   st.write("<h1 style='text-align: center; color: #d91002;'>What is heart disease?</h1>", unsafe_allow_html=True)
with col2:
   st.write("<h4 style='text-align: left; color: #2a2b2a;'>Heart disease is a general term that means the heart is not working properly. Some forms of heart disease are present at birth, while others develop as we age. Many forms of heart disease can be prevented by living an active, healthy lifestyle.</h4>", unsafe_allow_html=True)

st.write(" ")
st.write(" ")

col1, col2 = st.columns(2)

with col1:
   st.write("<h1 style='text-align: center; color: #2a2b2a;'>Signs of a heart attack</h1>", unsafe_allow_html=True)
with col2:
   st.write("<h4 style='text-align: left; color: #d91002;'>Signs can vary and may be different for men and women. If you experience any of these signs, call your local emergency number immediately.</h4>", unsafe_allow_html=True)
  
st.write(" ")
st.write(" ") 
st.write(" ")
    
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
   st.image("heart-attack-signs-chest-discomfort.svg")
   st.markdown("<h5 style='text-align: center; color: #2a2b2a;'>Chest discomfort</h5>", unsafe_allow_html=True)
   st.write("<p style='text-align: center; color: #2a2b2a;'>Pressure, squeezing, fullness or pain, burning or heaviness</p>", unsafe_allow_html=True)
   
with col2:
   st.image("heart-attack-signs-sweating.svg")
   st.markdown("<h5 style='text-align: center; color: #2a2b2a;'>Sweating</h5>", unsafe_allow_html=True)
   
with col3:
   st.image("heart-attack-signs-upper-body-discomfort.svg")
   st.markdown("<h5 style='text-align: center; color: #2a2b2a;'>Upper body discomfort</h5>", unsafe_allow_html=True)
   st.write("<p style='text-align: center; color: #2a2b2a;'>Neck, jaw, shoulder, arms, back</p>", unsafe_allow_html=True)

with col4:
   st.image("heart-attack-signs-nausea.svg")
   st.markdown("<h5 style='text-align: center; color: #2a2b2a;'>Nausea</h5>", unsafe_allow_html=True)

with col5:
   st.image("heart-attack-signs-shortness-of-breath.svg")
   st.markdown("<h5 style='text-align: center; color: #2a2b2a;'>Shortness of breath</h5>", unsafe_allow_html=True)
   
with col6:
   st.image("heart-attack-signs-light-headedness.svg")
   st.markdown("<h5 style='text-align: center; color: #2a2b2a;'>Light-headedness</h5>", unsafe_allow_html=True)
   
st.write(" ")
st.write(" ")

col1, col2 = st.columns(2)

with col1:
   st.markdown("""<h1 style='text-align: center; color: #2a2b2;'>Experiencing the signs?</h1>""", unsafe_allow_html=True)
with col2:
   st.write("<h4 style='text-align: left; color: #2a2b2a;'>Thousands of Nigerians die from heart attacks each year. Recognize the signs. Act quickly.</h4>", unsafe_allow_html=True)
      
st.write(" ")
st.write(" ")
st.write(" ")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
   st.markdown("<h3 style='text-align: center; color: #d91002;'>1. Call 1-1-2</h3>", unsafe_allow_html=True)
   st.write("<p style='text-align: center; color: #2a2b2a;'>Or your local emergency number Immediately. Emergency personnel can start treatment enroute to the hospital.</p>", unsafe_allow_html=True)
    
with col2:
   st.markdown("<h3 style='text-align: center; color: #2a2b2a;'>2. Stop all activity</h3>", unsafe_allow_html=True)
   st.write("<p style='text-align: center; color: #2a2b2a;'>Sit or lie down, in whatever position is most comfortable.</p>", unsafe_allow_html=True)   
    
with col3:
   st.markdown("<h3 style='text-align: center; color: #d91002;'>3. Take your nitroglycerin</h3>", unsafe_allow_html=True)
   st.write("<p style='text-align: center; color: #2a2b2a;'>If you take nitroglycerin, take your normal dosage.</p>", unsafe_allow_html=True)      

with col4:
   st.markdown("<h3 style='text-align: center; color: #2a2b2a;'>4. Take ASA (Aspirin)</h3>", unsafe_allow_html=True)
   st.write("<p style='text-align: center; color: #2a2b2a;'>Chew and swallow ASA (Aspirin), if you are not allergic or intolerant (either one 325 mg tablet or two 81 mg tablets).</p>", unsafe_allow_html=True)        
    
with col5:
   st.markdown("<h3 style='text-align: center; color: #d91002;'>5. Rest and wait</h3>", unsafe_allow_html=True)
   st.write("<p style='text-align: center; color: #2a2b2a;'>Stay calm while waiting for help to arrive.</p>", unsafe_allow_html=True)      
    
with col6:
   st.markdown("<h3 style='text-align: center; color: #2a2b2a;'>6. Keep a list of your medications in your wallet and by the phone</h3>", unsafe_allow_html=True)
   st.write("<p style='text-align: center; color: #2a2b2a;'>Emergency personnel will want this information.</p>", unsafe_allow_html=True)      
    
    
# Add buttons
def open_page1(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)

def open_page2(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script) 
    
# Add textual information
st.markdown("<h1 style='text-align: left; color: red;'>To Learn More About Heart Disease, Click the button below.</h1>", unsafe_allow_html=True)
st.button('Learn More', on_click=open_page2, args=('https://www.medicalnewstoday.com/articles/237191',))

st.markdown("<h2 style='text-align: left; color: #2a2b2a;'>Know your Heart Disease status using our machine learning model</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: left; color: #2a2b2a;'>Click the button below</h1>", unsafe_allow_html=True)
st.button('Check my status', on_click=open_page1, args=('https://heartygo.streamlit.app/',))


# Add buttons
#col1, col2 = st.beta_columns(2)
#with col1:
#    st.button('Know Your Covid-19 Status', on_click=open_page1, args=('https://predictcovidgo.streamlit.app/',))
#with col2:
#    st.button('Learn More', on_click=open_page2, args=('https://my.clevelandclinic.org/health/diseases/21214-coronavirus-covid-19',))




# # Display the page
# st.show()
