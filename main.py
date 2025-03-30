import streamlit as st
import tensorflow as tf
import numpy as np
import os
import torch
from torchvision import transforms
from datetime import datetime

# Ensure CUDA if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

SAVE_DIR = "history"
os.makedirs(SAVE_DIR, exist_ok=True)


def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #return index of max element

#Sidebar
st.sidebar.title("AI Plant Detection")
app_mode = st.sidebar.selectbox("Select Page",["HOME","DISEASE DETECTION", "CROP VIABILITY GUIDE", "FARMING GUIDE", "ABOUT US"])
#app_mode = st.sidebar.selectbox("Select Page",["Home","About","Disease Recognition"])

# import Image from pillow to open images
from PIL import Image
img = Image.open("Diseases.png")

# display image using streamlit
st.image(img)

#Main Page
if(app_mode=="HOME"):
        # Homepage UI
    st.markdown("""
        <h1 style='text-align: center; color: green;'>🌿 Plant Disease Detection 🌿</h1>
        <p style='text-align: center; font-size: 18px;'>Harness the power of AI to diagnose plant diseases and ensure healthier crops.</p>
        <hr>
    """, unsafe_allow_html=True)

    # About Section
    st.markdown("""
    ### 🌱 About This App
    This application helps farmers and agricultural experts detect plant diseases with the help of AI-powered image processing. 
    Simply upload a picture of a leaf, and our model will analyze and predict potential diseases.

    ### 🔍 How It Works
    1. **Capture or Upload**: Take a clear picture of the affected plant.
    2. **Analyze**: The AI model processes the image and identifies possible diseases.
    3. **Get Results**: Receive an instant diagnosis with suggestions for treatment.

    ### 🚀 Get Started
    Use the sidebar to navigate and start detecting plant diseases!
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <hr>
        <p style='text-align: center;'>© 2025 Plant Health AI | Powered by Machine Learning & Computer Vision</p>
    """, unsafe_allow_html=True)


# CROP VIABILITY GUIDE Page 
elif app_mode == "CROP VIABILITY GUIDE":
    st.markdown("""
        <h1 style='text-align: center; color: green;'>🌿 CROP VIABILITY GUIDE 🌿</h1>
    """, unsafe_allow_html=True)


    cropData = [
        {"name": "Apple", "nitrogen": 20.80, "phosphorus": 134.22, "potassium": 199.89, "temperature": 22.63, "humidity": 92.33, "pH": 5.93, "rainfall": 112.65},
        {"name": "Banana", "nitrogen": 100.23, "phosphorus": 82.01, "potassium": 50.05, "temperature": 27.38, "humidity": 80.36, "pH": 5.98, "rainfall": 104.63},
        {"name": "Blackgram", "nitrogen": 40.02, "phosphorus": 67.47, "potassium": 19.24, "temperature": 29.97, "humidity": 65.12, "pH": 7.13, "rainfall": 67.88},
        {"name": "Chickpea", "nitrogen": 40.09, "phosphorus": 67.79, "potassium": 79.92, "temperature": 18.87, "humidity": 16.86, "pH": 7.34, "rainfall": 80.06},
        {"name": "Coconut", "nitrogen": 21.98, "phosphorus": 16.93, "potassium": 30.59, "temperature": 27.41, "humidity": 94.84, "pH": 5.98, "rainfall": 175.69},
        {"name": "Coffee", "nitrogen": 101.20, "phosphorus": 28.74, "potassium": 29.94, "temperature": 25.54, "humidity": 58.87, "pH": 6.81, "rainfall": 158.07},
        {"name": "Cotton", "nitrogen": 117.77, "phosphorus": 46.24, "potassium": 19.56, "temperature": 23.99, "humidity": 79.84, "pH": 6.92, "rainfall": 80.09},
        {"name": "Grapes", "nitrogen": 23.18, "phosphorus": 132.53, "potassium": 200.11, "temperature": 23.87, "humidity": 81.87, "pH": 6.25, "rainfall": 69.91},
        {"name": "Jute", "nitrogen": 78.40, "phosphorus": 46.86, "potassium": 39.99, "temperature": 24.96, "humidity": 79.64, "pH": 6.73, "rainfall": 174.79},
        {"name": "Lentil", "nitrogen": 18.77, "phosphorus": 68.36, "potassium": 19.41, "temperature": 24.51, "humidity": 64.80, "pH": 6.99, "rainfall": 45.68},
        {"name": "Maize", "nitrogen": 77.76, "phosphorus": 48.44, "potassium": 19.79, "temperature": 22.61, "humidity": 65.92, "pH": 6.26, "rainfall": 84.76},
        {"name": "Mango", "nitrogen": 20.07, "phosphorus": 27.18, "potassium": 29.92, "temperature": 31.90, "humidity": 50.05, "pH": 5.77, "rainfall": 94.99},
        {"name": "Mothbeans", "nitrogen": 21.44, "phosphorus": 48.01, "potassium": 20.23, "temperature": 28.52, "humidity": 53.16, "pH": 6.85, "rainfall": 51.22},
        {"name": "Mungbean", "nitrogen": 20.99, "phosphorus": 47.28, "potassium": 19.87, "temperature": 28.27, "humidity": 85.95, "pH": 6.74, "rainfall": 48.44},
        {"name": "Muskmelon", "nitrogen": 100.32, "phosphorus": 17.72, "potassium": 50.08, "temperature": 28.66, "humidity": 92.34, "pH": 6.36, "rainfall": 24.69},
        {"name": "Orange", "nitrogen": 19.58, "phosphorus": 16.55, "potassium": 10.01, "temperature": 22.77, "humidity": 92.50, "pH": 7.01, "rainfall": 110.41},
        {"name": "Papaya", "nitrogen": 49.88, "phosphorus": 59.05, "potassium": 50.04, "temperature": 33.72, "humidity": 92.40, "pH": 6.74, "rainfall": 142.63},
        {"name": "Pigeonpeas", "nitrogen": 20.73, "phosphorus": 67.73, "potassium": 20.29, "temperature": 27.74, "humidity": 48.06, "pH": 5.79, "rainfall": 149.46},
        {"name": "Pomegranate", "nitrogen": 18.87, "phosphorus": 18.75, "potassium": 40.21, "temperature": 21.84, "humidity": 90.13, "pH": 6.43, "rainfall": 107.53},
        {"name": "Rice", "nitrogen": 79.89, "phosphorus": 47.58, "potassium": 39.87, "temperature": 23.69, "humidity": 82.27, "pH": 6.43, "rainfall": 236.18},
        {"name": "Watermelon", "nitrogen": 99.42, "phosphorus": 17.00, "potassium": 50.22, "temperature": 25.59, "humidity": 85.16, "pH": 6.50, "rainfall": 50.79},
        {"name": "Kidneybeans", "nitrogen": 20.75, "phosphorus": 67.54, "potassium": 20.05, "temperature": 20.05, "humidity": 21.61, "pH": 5.78, "rainfall": 105.92}
    ];

    # Display Team Cards
    cols = st.columns(3)  
    for index, member in enumerate(cropData):
        with cols[index % 3]:
            st.markdown(f"**    **")
            st.markdown(f"**{member['name']}**")
            st.markdown(f"Nitrogen: {member['nitrogen']}")
            st.markdown(f"Phosphorus: {member['phosphorus']}")
            st.markdown(f"Potassium: {member['potassium']}")
            st.markdown(f"Temperature: {member['temperature']}")
            st.markdown(f"pH: {member['pH']}")
            st.markdown(f"Rainfall: {member['rainfall']}")

#
# About Us Page - Team Members Section
elif app_mode == "ABOUT US":
    st.markdown("<h1 style='text-align: center; color: white;'>Team Members</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: white;'>Meet The Developers</h5>", unsafe_allow_html=True)

    # Team Member Data
    team_members = [
        {"name": "Srija Kontham", "linkedin": "#", "github": "#", "instagram": "#"},
        {"name": "Sowmya Sri Devagoni", "linkedin": "#", "github": "#", "instagram": "#"},
        {"name": "Sai Vishnu Teja Madhanambeti", "linkedin": "#", "github": "#", "instagram": "#"},
    ]

    # Display Team Cards
    cols = st.columns(3)  
    for index, member in enumerate(team_members):
        with cols[index % 3]:
            st.markdown(f"**    **")
            st.markdown(f"**{member['name']}**")
            st.markdown(f"**Masters | CSE**  \nCentral Michigan University")


#Prediction Page
elif(app_mode=="DISEASE DETECTION"):


    st.markdown("""
        <h1 style='text-align: center; color: green;'>🌿 DISEASE DETECTION 🌿</h1>
    """, unsafe_allow_html=True)
    test_image = st.file_uploader("Choose an Image:", type=["jpg", "png", "jpeg"])

    # if test_image:
    #     # Create a unique filename with timestamp
    #     timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    #     file_path = os.path.join(SAVE_DIR, f"{timestamp}.jpg")

    #     # Open and save the image
    #     image = Image.open(test_image)
    #     image.save(file_path)


    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)
    #Predict button
    if(st.button("Predict")):
        if test_image:
            # Create a unique filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            file_path = os.path.join(SAVE_DIR, f"{timestamp}.jpg")

            # Open and save the image
            image = Image.open(test_image).convert("RGB")  
            image.save(file_path)
        st.snow()
        st.write("Our Prediction")
        result_index = model_prediction(file_path)
        #Reading Labels
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                      'Tomato___healthy']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))
        disease_name = class_name[result_index]



        # Disease Treatment Mapping
        treatment_dict = { 
                'Apple___Apple_scab': "Apply fungicides like Captan or Mancozeb. Prune and destroy infected leaves.",
                'Apple___Black_rot': "Remove infected fruits and twigs. Apply copper-based fungicides. Improve air circulation.",
                'Apple___Cedar_apple_rust': "Use fungicides before bud break. Remove nearby cedar trees to prevent spread.",
                'Apple___healthy': "No disease detected. Maintain proper watering and pruning practices.",
                'Blueberry___healthy': "No disease detected. Ensure proper drainage and balanced fertilization.",
                'Cherry_(including_sour)___Powdery_mildew': "Use sulfur or neem oil sprays. Prune to improve airflow.",
                'Cherry_(including_sour)___healthy': "No disease detected. Avoid overwatering and ensure good soil health.",
                'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': "Apply fungicides like Azoxystrobin. Rotate crops and use resistant varieties.",
                'Corn_(maize)___Common_rust_': "Use rust-resistant varieties. Apply fungicides if severe.",
                'Corn_(maize)___Northern_Leaf_Blight': "Remove infected leaves, improve air circulation, and apply fungicides if needed.",
                'Corn_(maize)___healthy': "No disease detected. Maintain proper crop rotation and avoid excessive nitrogen fertilization.",
                'Grape___Black_rot': "Prune infected vines. Apply fungicides like Myclobutanil early in the season.",
                'Grape___Esca_(Black_Measles)': "Remove infected vines. Improve drainage and apply protective fungicides.",
                'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': "Spray with copper-based fungicides. Remove infected leaves.",
                'Grape___healthy': "No disease detected. Maintain regular pruning and disease monitoring.",
                'Orange___Haunglongbing_(Citrus_greening)': "No cure available. Remove infected trees and control psyllid insects.",
                'Peach___Bacterial_spot': "Use copper sprays in early spring. Remove and destroy infected leaves.",
                'Peach___healthy': "No disease detected. Maintain balanced fertilization and irrigation.",
                'Pepper,_bell___Bacterial_spot': "Use copper-based fungicides. Avoid overhead watering. Rotate crops.",
                'Pepper,_bell___healthy': "No disease detected. Maintain optimal watering and nutrient balance.",
                'Potato___Early_blight': "Apply fungicides like Chlorothalonil. Remove infected leaves. Rotate crops.",
                'Potato___Late_blight': "Use fungicides with Mancozeb or Chlorothalonil. Destroy infected plants immediately.",
                'Potato___healthy': "No disease detected. Ensure proper soil drainage and avoid overcrowding plants.",
                'Raspberry___healthy': "No disease detected. Regularly prune and remove weak canes.",
                'Soybean___healthy': "No disease detected. Monitor for pests and ensure soil fertility.",
                'Squash___Powdery_mildew': "Apply sulfur or potassium bicarbonate sprays. Ensure proper spacing for airflow.",
                'Strawberry___Leaf_scorch': "Use copper-based fungicides. Remove infected leaves. Avoid overhead watering.",
                'Strawberry___healthy': "No disease detected. Maintain healthy soil and avoid excessive moisture.",
                'Tomato___Bacterial_spot': "Use copper-based sprays. Avoid handling wet plants. Remove infected leaves.",
                'Tomato___Early_blight': "Apply fungicides like Mancozeb. Mulch around plants to prevent soil splash.",
                'Tomato___Late_blight': "Destroy infected plants. Apply fungicides containing Chlorothalonil.",
                'Tomato___Leaf_Mold': "Improve ventilation. Use copper or sulfur-based fungicides.",
                'Tomato___Septoria_leaf_spot': "Apply fungicides. Remove infected lower leaves.",
                'Tomato___Spider_mites Two-spotted_spider_mite': "Spray with neem oil or insecticidal soap. Increase humidity.",
                'Tomato___Target_Spot': "Use fungicides. Rotate crops. Improve airflow around plants.",
                'Tomato___Tomato_Yellow_Leaf_Curl_Virus': "Use resistant varieties. Control whiteflies with neem oil or insecticidal soap.",
                'Tomato___Tomato_mosaic_virus': "Remove infected plants. Disinfect tools regularly.",
                'Tomato___healthy': "No disease detected. Ensure balanced fertilization and disease prevention measures."
            }
        
                
        # Get treatment
        treatment = treatment_dict.get(disease_name, "No specific treatment found. Consult an expert.")
        st.info(f"**Suggested Treatment** {treatment}")


        

        treatment_dictHindi = {
                    "Apple___Apple_scab": "कैप्टन या मैंकोजेब जैसे फफूंदनाशकों का प्रयोग करें। संक्रमित पत्तियों को काटकर नष्ट करें।",
                    "Apple___Black_rot": "संक्रमित फलों और टहनियों को हटा दें। तांबा-आधारित फफूंदनाशकों का प्रयोग करें। हवा के संचार में सुधार करें।",
                    "Apple___Cedar_apple_rust": "कली निकलने से पहले फफूंदनाशकों का उपयोग करें। प्रसार को रोकने के लिए नज़दीकी देवदार के पेड़ों को हटाएं।",
                    "Apple___healthy": "कोई रोग नहीं पाया गया। उचित सिंचाई और छंटाई प्रथाओं का पालन करें।",
                    "Blueberry___healthy": "कोई रोग नहीं पाया गया। उचित जल निकासी और संतुलित उर्वरक का प्रयोग करें।",
                    "Cherry_(including_sour)___Powdery_mildew": "गंधक या नीम तेल स्प्रे का प्रयोग करें। हवा के संचार में सुधार के लिए छंटाई करें।",
                    "Cherry_(including_sour)___healthy": "कोई रोग नहीं पाया गया। अधिक पानी देने से बचें और अच्छी मिट्टी के स्वास्थ्य को बनाए रखें।",
                    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": "एज़ॉक्सिस्ट्रोबिन जैसे फफूंदनाशकों का प्रयोग करें। फसल चक्र अपनाएं और प्रतिरोधी किस्मों का उपयोग करें।",
                    "Corn_(maize)___Common_rust_": "जंग-रोधी किस्मों का उपयोग करें। यदि गंभीर हो, तो फफूंदनाशकों का प्रयोग करें।",
                    "Corn_(maize)___Northern_Leaf_Blight": "संक्रमित पत्तियों को हटा दें, हवा के संचार में सुधार करें, और आवश्यकतानुसार फफूंदनाशकों का उपयोग करें।",
                    "Corn_(maize)___healthy": "कोई रोग नहीं पाया गया। उचित फसल चक्र बनाए रखें और अत्यधिक नाइट्रोजन उर्वरक से बचें।",
                    "Grape___Black_rot": "संक्रमित बेलों की छंटाई करें। मौसम की शुरुआत में माइकलोबुटानिल जैसे फफूंदनाशकों का उपयोग करें।",
                    "Grape___Esca_(Black_Measles)": "संक्रमित बेलों को हटा दें। जल निकासी में सुधार करें और सुरक्षात्मक फफूंदनाशकों का प्रयोग करें।",
                    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": "तांबा-आधारित फफूंदनाशकों का छिड़काव करें। संक्रमित पत्तियों को हटा दें।",
                    "Grape___healthy": "कोई रोग नहीं पाया गया। नियमित छंटाई और रोग निगरानी बनाए रखें।",
                    "Orange___Haunglongbing_(Citrus_greening)": "कोई इलाज उपलब्ध नहीं है। संक्रमित पेड़ों को हटा दें और सिल्लिड कीड़ों को नियंत्रित करें।",
                    "Peach___Bacterial_spot": "वसंत ऋतु की शुरुआत में तांबा स्प्रे का उपयोग करें। संक्रमित पत्तियों को हटा दें और नष्ट करें।",
                    "Peach___healthy": "कोई रोग नहीं पाया गया। संतुलित उर्वरक और सिंचाई बनाए रखें।",
                    "Pepper,_bell___Bacterial_spot": "तांबा-आधारित फफूंदनाशकों का प्रयोग करें। ओवरहेड सिंचाई से बचें। फसल चक्र अपनाएं।",
                    "Pepper,_bell___healthy": "कोई रोग नहीं पाया गया। इष्टतम सिंचाई और पोषक तत्व संतुलन बनाए रखें।",
                    "Potato___Early_blight": "क्लोरोथालोनिल जैसे फफूंदनाशकों का प्रयोग करें। संक्रमित पत्तियों को हटा दें। फसल चक्र अपनाएं।",
                    "Potato___Late_blight": "मैंकोजेब या क्लोरोथालोनिल युक्त फफूंदनाशकों का प्रयोग करें। संक्रमित पौधों को तुरंत नष्ट करें।",
                    "Potato___healthy": "कोई रोग नहीं पाया गया। उचित मिट्टी जल निकासी सुनिश्चित करें और पौधों की भीड़ से बचें।",
                    "Raspberry___healthy": "कोई रोग नहीं पाया गया। नियमित रूप से छंटाई करें और कमजोर शाखाओं को हटा दें।",
                    "Soybean___healthy": "कोई रोग नहीं पाया गया। कीटों की निगरानी करें और मिट्टी की उर्वरता बनाए रखें।",
                    "Squash___Powdery_mildew": "गंधक या पोटेशियम बाइकार्बोनेट स्प्रे का प्रयोग करें। उचित वायु संचार के लिए पौधों के बीच पर्याप्त दूरी रखें।",
                    "Strawberry___Leaf_scorch": "तांबा-आधारित फफूंदनाशकों का प्रयोग करें। संक्रमित पत्तियों को हटा दें। ओवरहेड सिंचाई से बचें।",
                    "Strawberry___healthy": "कोई रोग नहीं पाया गया। स्वस्थ मिट्टी बनाए रखें और अत्यधिक नमी से बचें।",
                    "Tomato___Bacterial_spot": "तांबा-आधारित स्प्रे का प्रयोग करें। गीले पौधों को न छूएं। संक्रमित पत्तियों को हटा दें।",
                    "Tomato___Early_blight": "मैंकोजेब जैसे फफूंदनाशकों का प्रयोग करें। मिट्टी की छींटों से बचाव के लिए पौधों के चारों ओर मल्च बिछाएं।",
                    "Tomato___Late_blight": "संक्रमित पौधों को नष्ट करें। क्लोरोथालोनिल युक्त फफूंदनाशकों का प्रयोग करें।",
                    "Tomato___Leaf_Mold": "हवा के संचार में सुधार करें। तांबा या गंधक-आधारित फफूंदनाशकों का उपयोग करें।",
                    "Tomato___Septoria_leaf_spot": "फफूंदनाशकों का प्रयोग करें। संक्रमित निचली पत्तियों को हटा दें।",
                    "Tomato___Spider_mites Two-spotted_spider_mite": "नीम तेल या कीटनाशक साबुन का छिड़काव करें। आर्द्रता बढ़ाएं।",
                    "Tomato___Target_Spot": "फफूंदनाशकों का प्रयोग करें। फसल चक्र अपनाएं। पौधों के आसपास वायु संचार में सुधार करें।",
                    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": "प्रतिरोधी किस्मों का उपयोग करें। नीम तेल या कीटनाशक साबुन से सफेद मक्खियों को नियंत्रित करें।",
                    "Tomato___Tomato_mosaic_virus": "संक्रमित पौधों को हटा दें। उपकरणों को नियमित रूप से कीटाणुरहित करें।",
                    "Tomato___healthy": "कोई रोग नहीं पाया गया। संतुलित उर्वरक और रोग निवारण उपाय सुनिश्चित करें।",
            }
        
        class_nameHindi = {
                    'Apple___Apple_scab': "सेब का कवक",
                    'Apple___Black_rot': "सेब का काला सड़न.",
                    'Apple___Cedar_apple_rust': "सीडर सेब का रस्ट",
                    'Apple___healthy': "सेब स्वस्थ है",
                    'Blueberry___healthy': "ब्लूबेरी___स्वस्थ",
                    'Cherry_(including_sour)___Powdery_mildew': "चेरी (खट्टे सहित)___पाउडरी फफूंदी",
                    'Cherry_(including_sour)___healthy': "चेरी (खट्टे सहित)___स्वस्थ",
                    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': "मक्का___पत्ते दाग ग्रे पत्ते दाग",
                    'Corn_(maize)___Common_rust_': "मकई सामान्य कवक",
                    'Corn_(maize)___Northern_Leaf_Blight': "मक्का (मकई)___उत्तरी पत्तों का जलना",
                    'Corn_(maize)___healthy': "मक्का (मकई)___स्वस्थ",
                    'Grape___Black_rot': "अंगूर___काली सड़न",
                    'Grape___Esca_(Black_Measles)': "अंगूर___एस्का_(काली_चकत्ते)",
                    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': "अंगूर की पत्तियों का मुंहास",
                    'Grape___healthy': "अंगूर स्वस्थ",
                    'Orange___Haunglongbing_(Citrus_greening)': "संतरा___हुआंगलोंगबिंग_",
                    'Peach___Bacterial_spot': "पीच___बैक्टीरियल स्पॉट",
                    'Peach___healthy': "पीच___स्वस्थ",
                    'Pepper,_bell___Bacterial_spot': "शिमला मिर्च___बैक्टीरियल स्पॉट",
                    'Pepper,_bell___healthy': "शिमला मिर्च___स्वस्थ",
                    'Potato___Early_blight': "आलू___प्रारंभिक रोग",
                    'Potato___Late_blight': "आलू___लेट ब्लाइट",
                    'Potato___healthy': "आलू___स्वस्थ",
                    'Raspberry___healthy': "रास्पबेरी___स्वास्थ्यवर्धक",
                    'Soybean___healthy': "सोयाबीन___स्वस्थ",
                    'Squash___Powdery_mildew': "स्क्वैश___पाउडरी फफूंदी",
                    'Strawberry___Leaf_scorch': "स्ट्रॉबेरी___पत्याँ का जलना",
                    'Strawberry___healthy': "स्ट्रॉबेरी____स्वस्थ",
                    'Tomato___Bacterial_spot': "टमाटर___बैक्टीरियल स्पॉट",
                    'Tomato___Early_blight': "टमाटर___प्रारंभिक बीमारी",
                    'Tomato___Late_blight': "टमाटर___लेट ब्लाइट",
                    'Tomato___Leaf_Mold': "टमाटर___पत्ती___साँचा",
                    'Tomato___Septoria_leaf_spot': "टमाटर___सेप्टोरिया_पत्ते_पर_धब्बा",
                    'Tomato___Spider_mites Two-spotted_spider_mite': "टमाटर___मुंहजुखा",
                    'Tomato___Target_Spot': "टमाटर___टारगेट_स्पॉट",
                    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': "टमाटर___टमाटर_पीला_पत्ता_कर्ल_वायरस",
                    'Tomato___Tomato_mosaic_virus': "टमाटर___टमाटर_मोज़ेक_वायरस",
                    'Tomato___healthy': "टमाटर स्वास्थ्य"
             }
        # language = st.selectbox("भाषा चुनें | Select Language:", ["English", "हिन्दी"])
        st.markdown(f"**HINDI/हिंदी:**")

        treatmentHindi = treatment_dictHindi.get(disease_name, "No specific treatment found. Consult an expert.")
        disease_nameHindi = class_nameHindi.get(disease_name, "रोग XX")
        st.success(f"**रोग:** {disease_nameHindi}")

        st.info(f"**सुझाए गए उपचार:** {treatmentHindi}")




# FARMING GUIDE Page 
elif(app_mode == "FARMING GUIDE"):
    st.markdown("""
         <h1 style='text-align: center; color: green;'>🌿 CROP FARMING GUIDE 🌿</h1>
    """, unsafe_allow_html=True)


    cropGuide = [
            {"name": "Maize Cultivation Guide", 
                "Introduction": "Maize (Zea mays), also known as corn, is a key cereal crop widely cultivated for its grains. This guide covers the complete process for cultivating maize from seed selection to harvesting.",
                "Materials Required": "- High-quality maize seeds (hybrid or improved varieties)\n- Fertilizers (Nitrogen, Phosphorus, Potassium)\n- Machinery (tractors, hand tools, seed planters)\n- Pest control (herbicides, insecticides)\n- Irrigation equipment (drip or furrow irrigation)",
                "Soil Preparation": "Maize thrives in well-drained loam soils with a pH of 5.8 to 7.0. Till the soil to improve aeration and break up clods.",
                "Seed Selection & Treatment": "Choose high-yielding, drought-resistant varieties. Treat seeds with fungicides or insecticides for protection.",
                "Field Preparation": "Level the field for even water distribution. Optimize row spacing for maximum sunlight exposure.",
                "Planting Time": "Typically planted at the beginning of the rainy season, between April and June, depending on the region.",
                "Spacing & Depth": "Plant seeds at 20-25 cm within rows and 60-75 cm between rows, at a depth of 2-5 cm.",
                "Seeding Methods": "- **Direct Seeding:** Plant seeds manually or with seed planters.",
                "Watering Requirements": "Requires regular watering, especially during silking and tasseling. Use irrigation if rain is insufficient.",
                "Nutrient Management": "Apply fertilizers in split doses: at planting, early growth, and tasseling stages.",
                "Weed Control": "Manual weeding, hoeing, or herbicides. First weeding at 15-20 days after planting, followed by another at 30-40 days.",
                "Pest & Disease Management": "Monitor for maize borers, armyworms, and aphids. Use pesticides and integrated pest management (IPM).",
                "Harvesting": "Harvest when maize ears mature and husks dry. Moisture content should be 20-25%. Use handpicking or mechanical harvesters.",
                "Post-Harvest Management": "Dry grains to 13-14% moisture. Shell, clean, and store properly.",
                "Storage Conditions": "Store in a cool, dry place with ventilation to prevent mold and pests.",
                "Processing": "If needed, dry and mill the maize for further use.",
                "Challenges & Solutions": "Common issues: weather variability, pests, and water scarcity. Solutions: IPM, soil moisture monitoring, and resilient varieties."
            },
            
            {"name": "Rice Cultivation Guide", 
                "Introduction": "Rice Oryza sativa is a staple food crop in many parts of the world. This guide covers the complete process of cultivating rice from seed selection to harvesting.",
                "Materials Required": "- High-quality seeds\n- Fertilizers (Nitrogen, Phosphorus, Potassium)\n- Irrigation system\n- Machinery (tractors, transplanting machines, sickles)\n- Pest control (herbicides, pesticides)", 
                "Soil Preparation": "Rice grows best in clay or clay-loam soils with pH 5.5 to 6.5. Till the soil and level the field for even water distribution.", 
                "Seed Selection & Treatment": "Use high-yielding, pest-resistant seeds. Treat them with fungicides or insecticides to prevent infestations.", 
                "Field Preparation": "Level the field and create bunds (raised edges) to retain water.", 
                "Planting Time": "Plant at the onset of the rainy season, usually from May to June depending on the region.", 
                "Spacing & Depth": "For transplanting, use 20x15 cm spacing. For direct seeding, plant 2-3 cm deep.",
                "Seeding Methods": "- **Direct Seeding:** Broadcasting seeds or planting in rows.\n- **Transplanting:** Grow in a nursery and transfer seedlings after 20-30 days.",
                "Watering Requirements": "Maintain 5-10 cm of water during growth. Reduce water at the grain ripening stage.",
                "Nutrient Management": "Apply fertilizers in split doses: at planting, during tillering, and at panicle initiation.",
                "Weed Control": "Use manual weeding or herbicides. Weed 15-20 days after transplanting, then again at 40 days.",
                "Pest & Disease Management": "Watch for pests like stem borers and leafhoppers. Use pesticides and integrated pest management (IPM) practices.",
                "Harvesting": "Harvest when grains turn golden-yellow and 80-90% of grains are mature. Use sickles for small farms or mechanical harvesters for efficiency.",
                "Post-Harvest Management": "Dry grains to 14% moisture, thresh, winnow, and store in a cool, dry place to prevent spoilage.",
                "Challenges & Solutions": "Common issues include adverse weather, pests, and water scarcity. Use IPM, monitor water levels, and diversify crop varieties to mitigate risks."
            },
            
            {"name": "Jute Cultivation Guide",
                "Introduction": "Jute is a fibrous crop mainly grown for its strong, natural fibers, widely used in textiles and packaging. This guide covers the complete process for cultivating jute from seed selection to harvesting.",
                "Materials Required": "- High-quality, certified jute seeds (Corchorus olitorius or Corchorus capsularis)\n- Organic compost, nitrogen, phosphorus, and potassium fertilizers\n- Hand tools or tractors for soil preparation\n- Herbicides and pesticides for pest control\n- Irrigation system for controlled watering",
                "Soil Preparation": "Jute grows best in loamy, sandy-loam soils with good drainage and a pH range of 6.0 to 7.5. Prepare the soil by plowing and leveling it to break up clods and ensure good seedbed preparation.",
                "Seed Selection & Treatment": "Choose high-yielding and disease-resistant seed varieties. Soak seeds in water for 24 hours before planting to encourage germination.",
                "Field Preparation": "Clear and level the field for uniform water distribution. Create small bunds around the field if flooding is expected.",
                "Planting Time": "Jute is usually planted with the arrival of the monsoon, typically between March and May.",
                "Spacing & Depth": "Sow seeds in rows with a spacing of 25-30 cm between rows. Plant seeds 1-2 cm deep for optimal germination.",
                "Seeding Methods": "- **Broadcasting:** Scatter seeds evenly over the field.\n- **Row Planting:** Sow seeds in rows, which facilitates weeding and other management activities.",
                "Watering Requirements": "Jute requires regular moisture; maintain adequate moisture, especially during the early growth phase. Avoid waterlogging by ensuring proper drainage, particularly after heavy rains.",
                "Nutrient Management": "Apply a basal dose of nitrogen, phosphorus, and potassium fertilizers at planting. Additional nitrogen can be applied after thinning, about 20-25 days after sowing.",
                "Weed Control": "Perform manual weeding or apply selective herbicides as needed, especially in the early stages. Conduct the first weeding 15-20 days after sowing, followed by another after 30-40 days.",
                "Pest & Disease Management": "Monitor for common pests like jute hairy caterpillars and aphids. Use pesticides or integrated pest management (IPM) practices to control pests and diseases like stem rot and anthracnose.",
                "Harvesting": "Harvest jute when the plants are 10-12 feet tall and the lower leaves start to yellow, typically 100-120 days after planting. Cut the plants close to the base using a sickle or knife. For best fiber quality, harvest before the plants begin to flower.",
                "Post-Harvest Management": "Bundle the harvested jute plants and submerge them in clean, slow-moving water for retting (fermentation process to loosen the fibers). Retting usually takes 10-15 days; check fiber separation regularly.",
                "Challenges & Solutions": "Common issues include water availability, pest infestations, and improper retting. Use efficient irrigation and pest control methods, and monitor water levels carefully during retting to ensure fiber quality."
            },

            {"name": "Cotton Cultivation Guide",
                "Introduction": "Cotton is a major fiber crop valued for its soft, fluffy fibers used in textiles. This guide covers the complete process for cultivating cotton from seed selection to harvesting.",
                "Materials Required": "- High-quality, certified cotton seeds (e.g., Bt cotton or other pest-resistant varieties)\n- Nitrogen, phosphorus, potassium, and micronutrient fertilizers\n- Drip or furrow irrigation system\n- Herbicides and pesticides for pest control\n- Plows, tractors, and sprayers for field preparation and maintenance",
                "Soil Preparation": "Cotton grows best in well-drained sandy-loam soils with a pH of 6.0 to 7.5. Prepare the field by deep plowing, followed by harrowing to break clods and smooth the surface.",
                "Seed Selection & Treatment": "Choose high-yielding, pest-resistant seed varieties. Treat seeds with fungicides or insecticides to protect against soil-borne diseases and early pest infestations.",
                "Field Preparation": "Create furrows or beds for planting, depending on irrigation method. Ensure good drainage to prevent waterlogging, which cotton is sensitive to.",
                "Planting Time": "Cotton is typically planted in spring, from March to May, depending on the region and temperature.",
                "Spacing & Depth": "Plant seeds 3-5 cm deep, with a spacing of 75-100 cm between rows and 25-30 cm between plants.",
                "Seeding Methods": "- **Direct Seeding:** Plant seeds directly into prepared furrows or beds using seed drills or by hand.",
                "Watering Requirements": "Cotton requires consistent moisture, especially during the flowering and boll formation stages. Use drip or furrow irrigation to maintain adequate soil moisture, particularly during dry spells.",
                "Nutrient Management": "Apply basal fertilizer with phosphorus and potassium at planting. Apply nitrogen in split doses: one-third at planting, one-third during vegetative growth, and one-third at flowering.",
                "Weed Control": "Use manual weeding, hoeing, or herbicides to control weeds, particularly during early growth stages. Perform weeding about 20-30 days after planting and again if necessary at 45 days.",
                "Pest & Disease Management": "Monitor for common pests like bollworms, aphids, and whiteflies. Use integrated pest management (IPM) practices, including biological controls, to minimize pesticide use.",
                "Harvesting": "Harvest cotton when the bolls are fully open and the fibers are fluffy, typically 150-180 days after planting. Manual harvesting involves picking mature bolls by hand, while large farms use cotton-picking machines.",
                "Post-Harvest Management": "Allow harvested cotton to dry in a shaded, ventilated area. Clean and gin the cotton to separate seeds from fiber. Store cotton fibers in a dry, well-ventilated place to avoid moisture-related damage.",
                "Challenges & Solutions": "Common issues include pest infestations, water availability, and soil nutrient depletion. Use drought-resistant varieties, implement efficient irrigation, and follow IPM practices to manage pests."
            },

            {"name": "Coconut Cultivation Guide",
                "Introduction": "The coconut palm (Cocos nucifera) is cultivated for its fruit, providing oil, milk, and fiber. This guide covers key steps from seed selection to harvesting.",
                "Materials Required": "- High-quality coconut seedlings (dwarf or tall varieties)\n- Organic manure, NPK fertilizers\n- Drip or basin irrigation\n- Pesticides or biocontrol agents\n- Hand tools or mechanical equipment",
                "Soil Preparation": "Coconuts thrive in well-drained sandy loam with pH 5.5-7.5. Dig 1 x 1 x 1 m pits, fill with soil, compost, and organic manure for strong root growth.",
                "Seed Selection & Treatment": "Use disease-resistant, high-yielding seedlings. Dwarf varieties allow easy harvesting, while tall varieties are drought-resistant.",
                "Field Preparation": "Clear weeds and debris, ensure proper drainage, and space pits as per variety needs.",
                "Planting Time": "Best planted at the rainy season’s onset to reduce irrigation needs; can be planted year-round with irrigation.",
                "Spacing & Depth": "Tall varieties: 7.5-9m apart; Dwarf: 6.5-7m. Ensure roots are well covered.",
                "Seeding Methods": "Place seedlings in pits with the collar just above ground level.",
                "Watering Requirements": "Water regularly for the first three years. Mature trees are drought-resistant but benefit from consistent irrigation.",
                "Nutrient Management": "Apply balanced fertilizers three times a year with micronutrients like magnesium and boron. Add organic manure annually.",
                "Weed Control": "Weed regularly, especially in early growth. Mulching helps retain moisture and suppress weeds.",
                "Pest & Disease Management": "Control pests like rhinoceros beetles and red palm weevils using pesticides or biocontrols. Manage root wilt and bud rot with fungicides and pruning.",
                "Harvesting": "Mature coconuts (12 months after flowering) turn brown. Harvest every 45-60 days using climbing tools or mechanical lifters.",
                "Post-Harvest Management": "Store in a dry, ventilated area. Process copra by sun-drying or mechanical drying. Pack dried coconuts securely for transport.",
                "Challenges & Solutions": "Drought, pests, and soil depletion can be managed with drip irrigation, pest management, and organic soil amendments."
            },

            {"name": "Chickpea Cultivation Guide",
                "Introduction": "Chickpea (Cicer arietinum) is a popular legume grown for its protein-rich seeds, widely used in food production. This guide covers the complete process for cultivating chickpeas from seed selection to harvesting.",
                "Materials Required": "- High-quality, disease-resistant chickpea seeds (desi or kabuli types)\n- Phosphorus-based fertilizers; minimal nitrogen\n- Drip or sprinkler irrigation\n- Herbicides and pesticides\n- Plows, tractors, and sprayers",
                "Soil Preparation": "Chickpeas grow best in well-drained, loamy soils with a pH of 6.0-7.5. Plow and harrow the field for good root penetration.",
                "Seed Selection & Treatment": "Choose high-yielding, disease-resistant seeds. Treat with rhizobium bacteria for nitrogen fixation and fungicides to prevent diseases.",
                "Field Preparation": "Clear weeds and level the field. Space rows to allow air circulation and reduce disease risk.",
                "Planting Time": "Best planted in cool, dry seasons, typically October-November.",
                "Spacing & Depth": "Space plants 30-40 cm apart in rows 45-60 cm apart. Sow seeds 5-8 cm deep based on soil moisture.",
                "Seeding Methods": "Direct seeding using seed drills or manual planting.",
                "Watering Requirements": "Chickpeas require minimal watering but benefit from irrigation during flowering and pod filling. Avoid waterlogging.",
                "Nutrient Management": "Apply phosphorus at planting. Use potassium and micronutrients as needed based on soil tests.",
                "Weed Control": "Weed early and regularly, either manually or with herbicides. First weeding at 20-30 days, second at 45-50 days if needed.",
                "Pest & Disease Management": "Monitor for pests like pod borers and aphids. Use integrated pest management (IPM) and biopesticides as needed.",
                "Special Care During Growth": "- Seedling stage: Protect from pests, maintain moderate moisture.\n- Vegetative stage: Maintain phosphorus levels.\n- Flowering & pod-filling: Ensure adequate moisture for optimal yield.",
                "Harvesting": "Chickpeas mature in 3-4 months. Harvest when plants yellow and pods dry. Cut by hand for small farms; use combine harvesters for large-scale farming.",
                "Post-Harvest Management": "Sun-dry seeds to reduce moisture, thresh, and clean before storage or sale.",
                "Storage Conditions": "Store in dry, cool places with ventilation to prevent insect infestations and spoilage.",
                "Processing & Packaging": "Clean and grade seeds before packaging in breathable bags.",
                "Challenges & Solutions": "Common issues include pests, diseases, water stress, and nutrient deficiencies. Use IPM, resistant varieties, and soil testing to mitigate risks."
            },

            {"name": "Pigeon Pea Cultivation Guide",
                "Introduction": "Pigeon peas (Cajanus cajan) are a drought-resistant legume valued for their high protein content and use in various dishes. This guide covers the complete process for cultivating pigeon peas from seed selection to harvesting.",
                "Materials Required": "- High-quality, disease-resistant pigeon pea seeds (early, medium, or late-maturing varieties)\n- Nitrogen, phosphorus, and potassium fertilizers; minimal nitrogen needed\n- Drip or furrow irrigation equipment\n- Herbicides and pesticides specific to pigeon pea pests\n- Hand tools or tractors for soil preparation, planting, and weeding",
                "Soil Preparation": "Pigeon peas grow best in well-drained sandy loam to clay loam soils with a pH of 6.0-7.5. Plow and harrow the field to create a fine seedbed.",
                "Seed Selection & Treatment": "Choose high-yielding, disease-resistant varieties suitable for your region. Treat seeds with fungicides to prevent seed-borne diseases.",
                "Field Preparation": "Clear the field of weeds and debris, ensuring good drainage.",
                "Planting Time": "Typically planted at the beginning of the rainy season or during the dry season in subtropical regions.",
                "Spacing & Depth": "Space plants 30-40 cm apart in rows 60-75 cm apart. Sow seeds 3-5 cm deep, depending on soil moisture and texture.",
                "Seeding Methods": "Direct seeding using seed drills or manual planting.",
                "Watering Requirements": "Pigeon peas are drought-resistant but require adequate moisture during flowering and pod development. Irrigation may be necessary, especially in the first 60 days.",
                "Nutrient Management": "Apply phosphorus and potassium at planting and top-dress with nitrogen if necessary. Organic amendments can improve soil fertility.",
                "Weed Control": "Control weeds during early growth stages using manual weeding or herbicides. Mulching can help suppress weeds and retain soil moisture.",
                "Pest & Disease Management": "Monitor for pests such as pod borers, aphids, and whiteflies. Implement integrated pest management (IPM) strategies, including biological controls and chemical pesticides as needed.",
                "Special Care During Growth": "- Seedling stage: Protect young seedlings from pests and maintain soil moisture.\n- Vegetative stage: Ensure adequate nutrients for strong growth.\n- Flowering & pod-filling: Maintain consistent moisture to maximize yield and seed quality.",
                "Harvesting": "Pigeon peas mature in 4-6 months. Harvest when pods are mature and dry. Cut by hand for small farms or use combine harvesters for large-scale farming.",
                "Post-Harvest Management": "Allow harvested plants to sun-dry before threshing to reduce seed moisture content.",
                "Storage Conditions": "Store pigeon peas in a dry, cool, and well-ventilated area to prevent spoilage and insect infestations.",
                "Processing & Packaging": "Clean and grade seeds before packaging in breathable bags or containers.",
                "Challenges & Solutions": "Common issues include pest infestations, diseases, water stress, and nutrient deficiencies. Use disease-resistant varieties, practice crop rotation, and apply IPM strategies to manage risks."
            },

            {"name": "Moth Bean Cultivation Guide",
                "Introduction": "Moth beans (Vigna aconitifolia) are a drought-resistant legume commonly grown in arid regions. They are valued for their high protein content and culinary applications. This guide covers the complete process for cultivating moth beans from seed selection to harvesting.",
                "Materials Required": "- High-quality, disease-resistant moth bean seeds\n- Phosphorus and potassium fertilizers; minimal nitrogen\n- Drip or furrow irrigation\n- Herbicides and pesticides\n- Hand tools or tractors",
                "Soil Preparation": "Moth beans thrive in well-drained sandy loam or clay soils with a pH of 6.0-8.0. Prepare the field by plowing and harrowing for a fine seedbed.",
                "Seed Selection & Treatment": "Choose high-yielding, drought-tolerant varieties. Treat seeds with fungicides or insecticides to prevent seed-borne diseases.",
                "Field Preparation": "Clear the field of weeds and debris to ensure good seed-to-soil contact.",
                "Planting Time": "Typically planted at the onset of the monsoon season, between June and July.",
                "Spacing & Depth": "Space plants 30-45 cm apart in rows 60-75 cm apart. Sow seeds 3-5 cm deep based on soil moisture.",
                "Seeding Methods": "Direct seeding using seed drills or manual planting.",
                "Watering Requirements": "Moth beans are drought-resistant but benefit from consistent moisture during flowering and pod development. Water if rainfall is insufficient.",
                "Nutrient Management": "Apply phosphorus and potassium at planting. Use nitrogen only if soil tests indicate a deficiency. Organic amendments improve soil fertility.",
                "Weed Control": "Control weeds early with manual weeding or herbicides. Mulching helps suppress weeds and retain soil moisture.",
                "Pest & Disease Management": "Monitor for pests like aphids, pod borers, and leafhoppers. Use integrated pest management (IPM) strategies as needed.",
                "Special Care During Growth": "- Seedling stage: Maintain moderate moisture and protect from pests.\n- Vegetative stage: Ensure adequate nutrients.\n- Flowering & pod-filling: Maintain moisture for optimal yield.",
                "Harvesting": "Harvest when pods mature and dry, typically 90-120 days after planting. Hand-harvest for small farms; use combine harvesters for large-scale operations.",
                "Post-Harvest Management": "Sun-dry plants before threshing to reduce moisture content.",
                "Storage Conditions": "Store in dry, cool places with ventilation to prevent spoilage and insect infestations.",
                "Processing & Packaging": "Clean and grade seeds before packaging in breathable bags.",
                "Challenges & Solutions": "Common issues include pests, diseases, and adverse weather. Use drought-resistant varieties, IPM practices, and proper soil management to mitigate risks."
            },

            {"name": "Mung Bean Cultivation Guide",
                "Introduction": "Mung beans (Vigna radiata) are small, green legumes highly valued for their nutritional content and culinary versatility. This guide covers the complete process for cultivating mung beans from seed selection to harvesting.",
                "Materials Required": "- High-quality, disease-resistant mung bean seeds\n- Nitrogen, phosphorus, and potassium fertilizers (minimal nitrogen needed)\n- Drip or furrow irrigation\n- Herbicides and pesticides\n- Hand tools or tractors",
                "Soil Preparation": "Mung beans prefer well-drained sandy loam to loamy soils with a pH of 6.0-7.5. Prepare the field by plowing and harrowing to achieve a fine seedbed.",
                "Seed Selection & Treatment": "Choose high-yielding, disease-resistant varieties suitable for your climate. Treat seeds with fungicides to protect against soil-borne diseases.",
                "Field Preparation": "Clear the field of weeds and debris to ensure good seed-to-soil contact.",
                "Planting Time": "Typically planted at the beginning of the rainy season or in warm, dry conditions between April and June.",
                "Spacing & Depth": "Space plants 30-40 cm apart in rows 45-60 cm apart. Sow seeds 2-4 cm deep based on soil moisture.",
                "Seeding Methods": "Direct seeding using seed drills or manual planting.",
                "Watering Requirements": "Mung beans require adequate moisture, particularly during germination and flowering. Water if rainfall is insufficient, ensuring not to overwater to prevent root rot.",
                "Nutrient Management": "Apply phosphorus and potassium at planting. Additional nitrogen may be applied if needed, but usually, the natural fixation suffices. Incorporate organic matter to improve soil fertility.",
                "Weed Control": "Control weeds early through manual weeding or herbicides. Mulching helps suppress weeds and conserve soil moisture.",
                "Pest & Disease Management": "Monitor for pests like aphids, beetles, and thrips. Use integrated pest management (IPM) strategies as needed.",
                "Special Care During Growth": "- Seedling stage: Protect young seedlings from pests and maintain adequate moisture.\n- Vegetative stage: Ensure sufficient nutrients for strong growth.\n- Flowering & pod-filling: Maintain moisture for optimal yield and quality.",
                "Harvesting": "Harvest when pods mature and dry, typically 60-90 days after planting. Hand-harvest for small farms; use combine harvesters for large-scale operations.",
                "Post-Harvest Management": "Sun-dry plants before threshing to reduce moisture content.",
                "Storage Conditions": "Store in dry, cool places with ventilation to prevent spoilage and insect infestations.",
                "Processing & Packaging": "Clean and grade seeds before packaging in breathable bags.",
                "Challenges & Solutions": "Common issues include pests, diseases, and adverse weather. Use disease-resistant varieties, IPM practices, and proper soil and water management to mitigate risks."
            },

            {"name": "Black Gram Cultivation Guide",
                "Introduction": "Black gram (Vigna mungo) is a highly nutritious legume valued for its high protein content and is widely used in various culinary dishes. This guide covers the complete process for cultivating black gram from seed selection to harvesting.",
                "Materials Required": "- High-quality, disease-resistant black gram seeds\n- Phosphorus and potassium fertilizers (minimal nitrogen needed)\n- Drip or furrow irrigation\n- Herbicides and pesticides\n- Hand tools or tractors",
                "Soil Preparation": "Black gram prefers well-drained sandy loam to clay loam soils with a pH of 6.0-7.5. Prepare the field by plowing and harrowing to create a fine seedbed.",
                "Seed Selection & Treatment": "Choose high-yielding, disease-resistant varieties suitable for your climate. Treat seeds with fungicides or insecticides to protect against soil-borne diseases.",
                "Field Preparation": "Clear the field of weeds and debris to ensure good seed-to-soil contact.",
                "Planting Time": "Typically planted at the beginning of the monsoon season or during warm, dry conditions between June and July.",
                "Spacing & Depth": "Space plants 30-45 cm apart in rows 60-75 cm apart. Sow seeds 3-5 cm deep based on soil moisture.",
                "Seeding Methods": "Direct seeding using seed drills or manual planting.",
                "Watering Requirements": "Black gram requires adequate moisture, particularly during germination and flowering. Water if rainfall is insufficient, ensuring not to overwater to prevent root rot.",
                "Nutrient Management": "Apply phosphorus and potassium at planting. Additional nitrogen is generally not necessary due to nitrogen fixation. Incorporate organic matter to improve soil fertility.",
                "Weed Control": "Control weeds early through manual weeding or herbicides. Mulching helps suppress weeds and conserve soil moisture.",
                "Pest & Disease Management": "Monitor for pests like aphids, pod borers, and thrips. Use integrated pest management (IPM) strategies as needed.",
                "Special Care During Growth": "- Seedling stage: Protect young seedlings from pests and maintain adequate moisture.\n- Vegetative stage: Ensure sufficient nutrients for strong growth.\n- Flowering & pod-filling: Maintain moisture for optimal yield and quality.",
                "Harvesting": "Harvest when pods mature and dry, typically 60-90 days after planting. Hand-harvest for small farms; use combine harvesters for large-scale operations.",
                "Post-Harvest Management": "Sun-dry plants before threshing to reduce moisture content.",
                "Storage Conditions": "Store in dry, cool places with ventilation to prevent spoilage and insect infestations.",
                "Processing & Packaging": "Clean and grade seeds before packaging in breathable bags.",
                "Challenges & Solutions": "Common issues include pests, diseases, and adverse weather. Use disease-resistant varieties, IPM practices, and proper soil and water management to mitigate risks."
            },

            {"name": "Lentil Cultivation Guide",
                "Introduction": "Lentils (Lens culinaris) are nutritious legumes known for their high protein and fiber content. They are widely cultivated for food and are a staple in many cuisines. This guide covers the complete process for cultivating lentils from seed selection to harvesting.",
                "Materials Required": "- High-quality, disease-resistant lentil seeds\n- Phosphorus and potassium fertilizers (minimal nitrogen needed)\n- Drip or furrow irrigation\n- Herbicides and pesticides\n- Hand tools or tractors",
                "Soil Preparation": "Lentils prefer well-drained loamy or sandy soils with a pH of 6.0-7.5. Prepare the field by plowing and harrowing to create a fine seedbed.",
                "Seed Selection & Treatment": "Choose high-yielding, disease-resistant varieties suited to your region. Treat seeds with fungicides or insecticides to protect against seed-borne diseases.",
                "Field Preparation": "Clear the field of weeds and debris to ensure good seed-to-soil contact.",
                "Planting Time": "Lentils are typically planted in early spring or late winter, depending on the climate, when soil temperatures reach around 10-15°C (50-59°F).",
                "Spacing & Depth": "Space plants 25-30 cm apart in rows 45-60 cm apart. Sow seeds 2-3 cm deep based on soil moisture.",
                "Seeding Methods": "Direct seeding using seed drills or manual planting.",
                "Watering Requirements": "Lentils are drought-tolerant but need adequate moisture during germination and pod development. Water if rainfall is insufficient, particularly during flowering and seed filling.",
                "Nutrient Management": "Apply phosphorus and potassium at planting. Additional nitrogen is typically not needed due to nitrogen fixation. Incorporate organic matter to enhance soil fertility.",
                "Weed Control": "Control weeds during early growth using manual weeding or herbicides. Mulching can also help suppress weeds and retain soil moisture.",
                "Pest & Disease Management": "Monitor for pests such as aphids, lygus bugs, and root rots. Implement integrated pest management (IPM) strategies as needed.",
                "Special Care During Growth": "- Seedling stage: Protect young seedlings from pests and maintain adequate moisture.\n- Vegetative stage: Ensure sufficient nutrients for strong growth.\n- Flowering & pod-filling: Maintain moisture for optimal yield and quality.",
                "Harvesting": "Harvest when pods turn brown and dry, typically 80-100 days after planting. Hand-harvest for small farms; use combine harvesters for large-scale operations.",
                "Post-Harvest Management": "Sun-dry plants before threshing to reduce moisture content.",
                "Storage Conditions": "Store in dry, cool places with ventilation to prevent spoilage and insect infestations.",
                "Processing & Packaging": "Clean and grade seeds before packaging in breathable bags.",
                "Challenges & Solutions": "Common issues include pests, diseases, and variable weather. Use disease-resistant varieties, IPM practices, and proper soil and water management to mitigate risks."
            },

            {"name": "Pomegranate Cultivation Guide",
                "Introduction": "Pomegranates (Punica granatum) are nutritious fruits known for their health benefits and vibrant flavor. They are cultivated in many parts of the world and thrive in warm climates. This guide covers the complete process for cultivating pomegranates from planting to harvesting.",
                "Materials Required": "- High-quality pomegranate seeds or healthy seedlings from reputable nurseries\n- Balanced fertilizers with nitrogen, phosphorus, and potassium\n- Drip irrigation systems or furrow irrigation\n- Insecticides and fungicides for pest and disease management\n- Hand tools or tractors for planting, pruning, and maintenance",
                "Soil Preparation": "Pomegranates prefer well-drained, sandy loam to loamy soils with a pH of 5.5 to 7.0. Prepare the planting site by plowing and incorporating organic matter.",
                "Seed Selection & Treatment": "Choose disease-resistant varieties suitable for your region's climate. If using seeds, soak them overnight in water before planting to improve germination rates.",
                "Field Preparation": "Clear the site of weeds, rocks, and debris to ensure a clean planting environment.",
                "Planting Time": "Pomegranates are typically planted in spring after the last frost.",
                "Spacing & Depth": "Space plants 5-8 feet apart to allow for proper growth and air circulation. Plant seeds or seedlings at a depth of 1-2 inches, ensuring good soil contact.",
                "Seeding Methods": "Direct Seeding: Sow seeds directly into the prepared site. Transplanting: For seedlings, dig a hole slightly larger than the root ball and backfill with soil.",
                "Watering Requirements": "Pomegranates require regular watering, especially during the establishment phase; once established, they are drought-tolerant. Water deeply but infrequently to encourage deep root growth.",
                "Nutrient Management": "Apply a balanced fertilizer during the growing season, typically in early spring and again in late summer. Incorporate organic compost to improve soil fertility.",
                "Weed Control": "Control weeds using mulching and manual weeding to reduce competition for nutrients.",
                "Pest & Disease Management": "Monitor for pests such as aphids, whiteflies, and pomegranate butterflies. Implement integrated pest management (IPM) strategies, including the use of natural predators and organic pesticides.",
                "Special Care During Growth": "- Seedling stage: Protect young plants from extreme weather and pests. Use mulch to retain moisture.\n- Vegetative stage: Regularly check for nutrient deficiencies and pest infestations; apply fertilizers as needed.\n- Flowering & fruit development: Ensure adequate water during flowering and fruit set to promote healthy development.",
                "Harvesting": "Pomegranates are typically ready for harvest 5-7 months after flowering, when the fruit has a deep color and makes a metallic sound when tapped. Use sharp pruning shears to cut the fruit from the tree, avoiding damage to the branches and other fruit.",
                "Post-Harvest Management": "Handle fruits gently to prevent bruising; store in a cool, dry place.",
                "Storage Conditions": "Store pomegranates in a cool, dry environment; they can last several weeks to months in proper conditions.",
                "Processing & Packaging": "Clean and sort harvested fruits, discarding any damaged or rotten ones. Pack fruits in breathable containers to maintain quality during storage.",
                "Challenges & Solutions": "Common issues include susceptibility to pests, diseases, and environmental stresses such as drought or excessive moisture. Use disease-resistant varieties, implement proper irrigation practices, and monitor pest populations to mitigate challenges."
            },

            {"name": "Kidney Bean Cultivation Guide",
                "Introduction": "Kidney beans (Phaseolus vulgaris) are a high-protein legume commonly used in various cuisines. This guide covers the complete process for cultivating kidney beans from seed selection to harvesting.",
                "Materials Required": "- High-quality, disease-resistant kidney bean seeds\n- Phosphorus and potassium fertilizers; minimal nitrogen as beans fix their own nitrogen\n- Drip or sprinkler irrigation\n- Herbicides and pesticides for common kidney bean pests\n- Hand tools or tractors for soil preparation, planting, and weeding",
                "Soil Preparation": "Kidney beans thrive in well-drained, loamy soils with a pH between 6.0 and 7.0. Prepare the field by plowing and harrowing to create a fine tilth for easy root penetration.",
                "Seed Selection & Treatment": "Choose high-yielding, disease-resistant seed varieties. Treat seeds with fungicides or insecticides to protect against early soil-borne diseases and pests.",
                "Field Preparation": "Clear the field of weeds and debris, then level it. Mark rows with adequate spacing for air circulation and sunlight penetration.",
                "Planting Time": "Kidney beans are typically planted in spring when soil temperatures reach 15°C (59°F) and there is no risk of frost.",
                "Spacing & Depth": "Plant seeds 3-5 cm deep, with 8-10 cm between plants and 45-60 cm between rows.",
                "Seeding Methods": "Direct Seeding: Sow seeds directly into the field by hand or using a seed drill.",
                "Watering Requirements": "Kidney beans need regular watering, particularly during flowering and pod development. Avoid overwatering, as beans are sensitive to waterlogging.",
                "Nutrient Management": "Apply phosphorus and potassium at planting. Limit nitrogen since kidney beans fix atmospheric nitrogen. Supplement micronutrients if soil tests indicate deficiencies.",
                "Weed Control": "Weed control is essential, particularly in the early stages. Use manual weeding or herbicides as needed. Mulching around plants can help retain moisture and suppress weeds.",
                "Pest & Disease Management": "Monitor for pests like aphids, leafhoppers, and bean beetles. Use integrated pest management (IPM) practices and apply pesticides if necessary. Prevent diseases like root rot and blight by practicing crop rotation and avoiding waterlogged soil.",
                "Special Care During Growth": "- Seedling stage: Ensure moderate soil moisture and protect seedlings from pests.\n- Vegetative stage: Maintain nutrient levels to support robust leaf and stem growth.\n- Flowering & pod-filling stage: Provide consistent moisture during pod development to enhance yield and seed quality.",
                "Harvesting": "Harvest kidney beans when the pods are fully mature and dry, usually 90-120 days after planting. For small farms, harvest by hand by pulling up the entire plant. For larger farms, use a combine harvester to gather beans efficiently.",
                "Post-Harvest Management": "Allow the harvested plants to dry in the sun to reduce moisture in the seeds. Thresh the beans to separate them from the pods, then clean the seeds.",
                "Storage Conditions": "Store kidney beans in a dry, well-ventilated place to prevent mold and insect infestations.",
                "Processing & Packaging": "Clean and grade the beans for quality assurance before packaging. Pack beans in breathable bags or containers to maintain quality during storage.",
                "Challenges & Solutions": "Common issues include susceptibility to pests, diseases, and nutrient imbalances. Use disease-resistant seeds, monitor soil health, and apply IPM practices to control pests and diseases effectively."
            },

            {"name": "Banana Cultivation Guide",
                "Introduction": "Bananas (Musa spp.) are tropical fruits renowned for their sweet flavor and nutritional benefits. They thrive in warm, humid climates and are cultivated worldwide for both commercial and home production. This guide outlines the complete process for cultivating bananas, from planting to harvesting.",
                "Materials Required": "- Healthy banana suckers or tissue-cultured plantlets\n- Balanced fertilizers with nitrogen, phosphorus, and potassium; organic matter such as compost\n- Drip or sprinkler irrigation systems for adequate moisture management\n- Insecticides and fungicides to manage pests and diseases\n- Hand tools (shovels, pruners) or tractors for planting, maintenance, and harvesting",
                "Soil Preparation": "Bananas prefer well-drained, rich loamy soils with a pH of 5.5 to 7.0. Prepare the soil by plowing and incorporating organic matter to improve fertility and drainage.",
                "Plant Selection & Treatment": "Select disease-free suckers from healthy parent plants or obtain tissue-cultured plantlets from a reputable source. If using suckers, cut them from the parent plant with a clean knife to avoid contamination.",
                "Field Preparation": "Clear the planting site of weeds, stones, and debris to ensure a clean environment for planting.",
                "Planting Time": "The ideal time to plant bananas is at the beginning of the rainy season or during the warmer months.",
                "Spacing & Depth": "Space plants 8-10 feet apart in rows that are 10-12 feet apart to allow for proper growth and air circulation. Plant suckers or plantlets at the same depth they were growing in the nursery.",
                "Transplanting Methods": "Transplanting: Dig a hole large enough to accommodate the roots and backfill gently to avoid air pockets.",
                "Watering Requirements": "Bananas require consistent moisture; irrigate regularly, especially during dry spells. Aim for 1-2 inches of water per week.",
                "Nutrient Management": "Apply a balanced fertilizer in early spring and again mid-season. Add compost or organic mulch to enhance soil fertility.",
                "Weed Control": "Control weeds using mulching, which also helps retain soil moisture, and manual weeding to reduce competition for nutrients.",
                "Pest & Disease Management": "Monitor for pests such as banana weevils and aphids. Manage diseases like Panama disease and leaf spot with proper sanitation and resistant varieties. Implement integrated pest management (IPM) strategies, including cultural controls and the use of biological pest control methods.",
                "Special Care During Growth": "- Seedling stage: Protect young plants from extreme weather and pests; consider using shade cloth if necessary.\n- Vegetative stage: Regularly check for nutrient deficiencies, especially potassium and magnesium, and address them promptly.\n- Flowering & fruit development stage: Ensure adequate water supply during flowering and fruit development to support healthy fruit formation.",
                "Harvesting": "Bananas are typically ready for harvest 9-12 months after planting, depending on the variety and growing conditions. Harvest when the fruit is plump, green, and the angle between the fruit and the stalk becomes more pronounced. Use a sharp knife or machete to cut the entire bunch from the plant. Handle the fruit carefully to avoid bruising.",
                "Post-Harvest Management": "Remove any excess leaves and handle harvested bananas gently to prevent damage. Store them in a cool, shaded area.",
                "Storage Conditions": "Store bananas at room temperature until they ripen. Avoid exposure to direct sunlight or excessive heat.",
                "Processing & Packaging": "If needed, bananas can be processed into products like banana chips or puree. Pack bananas in breathable boxes to allow for airflow and reduce spoilage during transport.",
                "Challenges & Solutions": "Common issues include susceptibility to pests and diseases, environmental stresses, and improper watering. Choose disease-resistant varieties, implement good cultural practices, and monitor environmental conditions to mitigate these challenges."
            },

            {"name": "Banana Cultivation Guide",
                "Introduction": "Bananas (Musa spp.) are tropical fruits renowned for their sweet flavor and nutritional benefits. They thrive in warm, humid climates and are cultivated worldwide for both commercial and home production. This guide outlines the complete process for cultivating bananas, from planting to harvesting.",
                "Materials Required": "- Healthy banana suckers or tissue-cultured plantlets\n- Balanced fertilizers with nitrogen, phosphorus, and potassium; organic matter such as compost\n- Drip or sprinkler irrigation systems for adequate moisture management\n- Insecticides and fungicides to manage pests and diseases\n- Hand tools (shovels, pruners) or tractors for planting, maintenance, and harvesting",
                "Soil Preparation": "Bananas prefer well-drained, rich loamy soils with a pH of 5.5 to 7.0. Prepare the soil by plowing and incorporating organic matter to improve fertility and drainage.",
                "Plant Selection & Treatment": "Select disease-free suckers from healthy parent plants or obtain tissue-cultured plantlets from a reputable source. If using suckers, cut them from the parent plant with a clean knife to avoid contamination.",
                "Field Preparation": "Clear the planting site of weeds, stones, and debris to ensure a clean environment for planting.",
                "Planting Time": "The ideal time to plant bananas is at the beginning of the rainy season or during the warmer months.",
                "Spacing & Depth": "Space plants 8-10 feet apart in rows that are 10-12 feet apart to allow for proper growth and air circulation. Plant suckers or plantlets at the same depth they were growing in the nursery.",
                "Transplanting Methods": "Transplanting: Dig a hole large enough to accommodate the roots and backfill gently to avoid air pockets.",
                "Watering Requirements": "Bananas require consistent moisture; irrigate regularly, especially during dry spells. Aim for 1-2 inches of water per week.",
                "Nutrient Management": "Apply a balanced fertilizer in early spring and again mid-season. Add compost or organic mulch to enhance soil fertility.",
                "Weed Control": "Control weeds using mulching, which also helps retain soil moisture, and manual weeding to reduce competition for nutrients.",
                "Pest & Disease Management": "Monitor for pests such as banana weevils and aphids. Manage diseases like Panama disease and leaf spot with proper sanitation and resistant varieties. Implement integrated pest management (IPM) strategies, including cultural controls and the use of biological pest control methods.",
                "Special Care During Growth": "- Seedling stage: Protect young plants from extreme weather and pests; consider using shade cloth if necessary.\n- Vegetative stage: Regularly check for nutrient deficiencies, especially potassium and magnesium, and address them promptly.\n- Flowering & fruit development stage: Ensure adequate water supply during flowering and fruit development to support healthy fruit formation.",
                "Harvesting": "Bananas are typically ready for harvest 9-12 months after planting, depending on the variety and growing conditions. Harvest when the fruit is plump, green, and the angle between the fruit and the stalk becomes more pronounced. Use a sharp knife or machete to cut the entire bunch from the plant. Handle the fruit carefully to avoid bruising.",
                "Post-Harvest Management": "Remove any excess leaves and handle harvested bananas gently to prevent damage. Store them in a cool, shaded area.",
                "Storage Conditions": "Store bananas at room temperature until they ripen. Avoid exposure to direct sunlight or excessive heat.",
                "Processing & Packaging": "If needed, bananas can be processed into products like banana chips or puree. Pack bananas in breathable boxes to allow for airflow and reduce spoilage during transport.",
                "Challenges & Solutions": "Common issues include susceptibility to pests and diseases, environmental stresses, and improper watering. Choose disease-resistant varieties, implement good cultural practices, and monitor environmental conditions to mitigate these challenges."
            },


            {"name": "Grape Cultivation Guide",
                "Introduction": "Grapes (Vitis vinifera and other species) are versatile fruits used for fresh eating, drying (raisins), and wine production. They thrive in temperate climates and require specific growing conditions to produce high-quality fruit. This guide outlines the complete process for cultivating grapes, from planting to harvesting.",
                "Materials Required": "- Quality grapevines, either bare-root or potted, from reputable nurseries\n- Balanced fertilizers containing nitrogen, phosphorus, and potassium; organic compost\n- Drip irrigation systems for efficient moisture management\n- Insecticides, fungicides, and organic pest management solutions\n- Hand tools (pruners, shovels) or tractors for planting, maintenance, and harvesting",
                "Soil Preparation": "Grapes prefer well-drained, sandy loam or clay loam soils with a pH of 6.0 to 6.8. Prepare the soil by tilling and incorporating organic matter to enhance fertility and drainage.",
                "Plant Selection & Treatment": "Select disease-resistant grape varieties suitable for your climate and purpose (table grapes, wine grapes, etc.). Inspect vines for signs of disease or damage before planting.",
                "Field Preparation": "Clear the planting site of weeds, stones, and debris to ensure a clean environment for planting.",
                "Planting Time": "The ideal time to plant grapes is in early spring after the last frost or in the fall before the ground freezes.",
                "Spacing & Depth": "Space vines 6-10 feet apart in rows that are 8-10 feet apart to allow for proper air circulation and growth. Plant vines at the same depth they were growing in the nursery.",
                "Transplanting Methods": "Transplanting: Dig a hole large enough to accommodate the roots, backfill gently, and water thoroughly after planting.",
                "Watering Requirements": "Grapes require regular watering during the first year to establish roots. Once established, they are drought-tolerant but still benefit from supplemental irrigation during dry spells, especially during fruit development.",
                "Nutrient Management": "Apply a balanced fertilizer in early spring and again mid-season. Use organic compost to improve soil health.",
                "Weed Control": "Control weeds through mulching, hand weeding, or the use of herbicides to reduce competition for nutrients and moisture.",
                "Pest & Disease Management": "Monitor for pests such as grapevine moths, aphids, and spider mites. Manage diseases like powdery mildew and downy mildew with proper sanitation and resistant varieties. Implement integrated pest management (IPM) strategies, including cultural controls and natural predators.",
                "Special Care During Growth": "- Young Vine Stage: Protect young vines from extreme weather and pests; use support stakes or trellises to help young plants grow upward.\n- Vegetative Stage: Regularly check for nutrient deficiencies and address them promptly. Prune to encourage a strong structure and air circulation.\n- Flowering & Fruit Development Stage: Ensure consistent moisture during flowering and fruit set to maximize yield and fruit quality. Thin clusters if necessary to promote larger fruit size.",
                "Harvesting": "Grapes are typically ready for harvest 4-6 months after flowering, depending on the variety. They should be harvested when fully ripe, showing deep color and sweet flavor. Use sharp pruning shears to cut clusters from the vine. Handle the fruit carefully to avoid bruising.",
                "Post-Harvest Management": "Remove any damaged or rotten grapes and store them in a cool, shaded area.",
                "Storage Conditions": "Store grapes in a cool, dry place. Refrigeration can extend their shelf life, but they should be kept in breathable containers.",
                "Processing & Packaging": "If needed, grapes can be processed into products like grape juice, jelly, or wine. Pack grapes in breathable containers to allow airflow and reduce spoilage during transport.",
                "Challenges & Solutions": "Common issues include susceptibility to pests and diseases, climate-related issues, and improper watering. Choose disease-resistant varieties, implement good cultural practices, and monitor environmental conditions to mitigate these challenges."
            },

            {"name": "Muskmelon Cultivation Guide",
                "Introduction": "Muskmelons (Cucumis melo var. cantaloupe) are sweet, aromatic fruits known for their juicy flesh and distinctive netted skin. They thrive in warm climates and are popular for their refreshing taste. This guide outlines the complete process for cultivating muskmelons, from planting to harvesting.",
                "Materials Required": "- Quality muskmelon seeds or seedlings from reputable sources\n- Balanced fertilizers with nitrogen, phosphorus, and potassium; organic compost\n- Drip or overhead irrigation systems for efficient moisture management\n- Insecticides, fungicides, and organic pest management solutions\n- Hand tools (shovels, hoes, pruners) or tractors for planting, maintenance, and harvesting",
                "Soil Preparation": "Muskmelons prefer well-drained, sandy loam or loamy soils with a pH of 6.0 to 6.8. Prepare the soil by tilling and mixing in organic matter to enhance drainage and fertility.",
                "Plant Selection & Treatment": "Choose disease-resistant varieties suited for your climate and market. If using seeds, soak them in water for a few hours before planting to improve germination rates.",
                "Field Preparation": "Clear the planting site of weeds, stones, and debris to ensure a clean environment for planting.",
                "Planting Time": "The ideal time to plant muskmelons is after the last frost date when soil temperatures are consistently above 70°F (21°C).",
                "Spacing & Depth": "Space muskmelon plants 3-4 feet apart in rows that are 6-8 feet apart to allow for sprawling vines. Plant seeds or seedlings at a depth of about 1 inch.",
                "Seeding/Transplanting Methods": "Direct Seeding: Plant seeds directly into the ground after the soil warms up. Transplanting: Start seedlings indoors and transplant them once they are strong enough.",
                "Watering Requirements": "Muskmelons need consistent moisture, especially during germination and fruit development. Aim for about 1-2 inches of water per week, adjusting for rainfall.",
                "Nutrient Management": "Apply a balanced fertilizer at planting and again when vines begin to run. Use organic compost or mulch to enhance soil health.",
                "Weed Control": "Control weeds through mulching, which helps retain moisture and suppress weed growth, and manual weeding to reduce competition.",
                "Pest & Disease Management": "Monitor for pests such as aphids, cucumber beetles, and spider mites. Manage diseases like powdery mildew and downy mildew with proper sanitation and resistant varieties. Implement integrated pest management (IPM) strategies, including cultural controls and the use of biological controls.",
                "Special Care During Growth": "- Seedling Stage: Protect young plants from pests and extreme weather. Use row covers if necessary to protect against pests and frost.\n- Vegetative Stage: Regularly check for nutrient deficiencies and address them promptly. Support vines if necessary, especially when fruit begins to develop.\n- Fruit Development Stage: Ensure adequate water supply during fruit development to promote healthy growth and sweetness. Avoid watering directly on the fruit to prevent rot.",
                "Harvesting": "Muskmelons are typically ready for harvest 70-90 days after planting. Indicators include a change in color from green to yellow at the blossom end and a sweet aroma. Use a sharp knife or pruning shears to cut the fruit from the vine, leaving a short stem attached to the melon.",
                "Post-Harvest Management": "Handle harvested muskmelons gently to avoid bruising. Store them in a cool, shaded area.",
                "Storage Conditions": "Store muskmelons at room temperature until they are fully ripe. Once ripe, they can be refrigerated for a short period to extend freshness.",
                "Processing & Packaging": "If needed, muskmelons can be processed into smoothies, sorbets, or fruit salads. Pack muskmelons in breathable containers to help maintain quality during storage and transport.",
                "Challenges & Solutions": "Common challenges include susceptibility to pests and diseases, environmental stresses such as drought or excessive moisture, and improper watering practices. Choose disease-resistant varieties, implement good cultural practices, and monitor environmental conditions to mitigate these challenges."
            },

            {"name": "Apple Cultivation Guide",
                "Introduction": "Apples (Malus domestica) are one of the most popular fruits worldwide, appreciated for their taste, versatility, and nutritional value. They grow best in temperate climates and can be cultivated in various soil types. This guide outlines the complete process for cultivating apples, from planting to harvesting.",
                "Materials Required": "- Quality apple tree seedlings or grafted varieties from reputable nurseries\n- Balanced fertilizers containing nitrogen, phosphorus, and potassium; organic compost\n- Drip irrigation systems or hoses for effective moisture management\n- Insecticides, fungicides, and organic pest management solutions\n- Hand tools (shovels, pruning shears, hoes) or tractors for planting, maintenance, and harvesting",
                "Soil Preparation": "Apples prefer well-drained, loamy soils with a pH of 6.0 to 7.0. Prepare the soil by tilling and incorporating organic matter to improve fertility and drainage.",
                "Plant Selection & Treatment": "Choose disease-resistant apple varieties suited to your climate, considering factors such as fruit flavor and harvest time. Inspect seedlings for signs of disease or damage before planting.",
                "Field Preparation": "Clear the planting area of weeds, stones, and debris to ensure a clean environment for planting.",
                "Planting Time": "The best time to plant apple trees is in the fall or early spring when the trees are dormant.",
                "Spacing & Depth": "Space dwarf varieties 4-6 feet apart and standard varieties 10-15 feet apart to allow for proper growth and air circulation. Plant trees at a depth that matches their nursery height, ensuring the graft union is above soil level.",
                "Seeding/Transplanting Methods": "Transplanting: Dig a hole large enough to accommodate the roots, place the tree in the hole, backfill gently, and water thoroughly after planting.",
                "Watering Requirements": "Water young apple trees regularly to establish roots, especially during dry spells. Once established, they are drought-tolerant but benefit from deep watering during fruit development.",
                "Nutrient Management": "Apply a balanced fertilizer in early spring and again in mid-season. Use organic compost to enhance soil health.",
                "Weed Control": "Control weeds through mulching, which helps retain moisture and suppress weed growth, and manual weeding to reduce competition.",
                "Pest & Disease Management": "Monitor for pests such as codling moths, aphids, and spider mites. Manage diseases like apple scab and powdery mildew with proper sanitation and resistant varieties. Implement integrated pest management (IPM) strategies, including cultural controls and the use of beneficial insects.",
                "Special Care During Growth": "- Young Tree Stage: Protect young trees from extreme weather and pests; consider using tree guards to prevent animal damage.\n- Vegetative Stage: Regularly check for nutrient deficiencies and address them promptly. Prune to shape trees and encourage a strong structure.\n- Flowering and Fruit Development Stage: Ensure consistent moisture during flowering and fruit set to maximize yield and fruit quality. Thin fruit if necessary to promote larger apples.",
                "Harvesting": "Apples are typically ready for harvest 4-6 months after flowering, depending on the variety. Indicators include a change in color, firm texture, and ease of detachment from the tree. Use sharp pruning shears to cut apples from the tree, leaving a short stem attached to the fruit.",
                "Post-Harvest Management": "Handle harvested apples gently to avoid bruising. Store them in a cool, shaded area.",
                "Storage Conditions": "Store apples in a cool, dark place. They can be refrigerated to extend their shelf life.",
                "Processing & Packaging": "If needed, apples can be processed into applesauce, cider, or dried slices. Pack apples in breathable containers to help maintain quality during storage and transport.",
                "Challenges & Solutions": "Common challenges include susceptibility to pests and diseases, environmental stresses (such as drought or frost), and improper pruning techniques. Choose disease-resistant varieties, implement good cultural practices, and monitor environmental conditions to mitigate these challenges."
            },

            {"name": "Orange Cultivation Guide",
                "Introduction": "Oranges (Citrus sinensis) are one of the most popular citrus fruits, valued for their sweet, juicy flesh and high vitamin C content. They thrive in warm, subtropical to tropical climates. This guide outlines the complete process for cultivating oranges, from planting to harvesting.",
                "Materials Required": "- Quality orange tree seedlings or grafted varieties from reputable nurseries\n- Citrus-specific fertilizers containing nitrogen, phosphorus, and potassium; organic compost\n- Drip irrigation systems or hoses for efficient moisture management\n- Insecticides, fungicides, and organic pest management solutions\n- Hand tools (shovels, pruning shears, hoes) or tractors for planting, maintenance, and harvesting",
                "Soil Preparation": "Oranges prefer well-drained, sandy loam or clay loam soils with a pH of 6.0 to 7.5. Prepare the soil by tilling and incorporating organic matter to improve fertility and drainage.",
                "Plant Selection & Treatment": "Choose disease-resistant orange varieties suited to your climate, considering factors such as fruit flavor and harvest time. Inspect seedlings for signs of disease or damage before planting.",
                "Field Preparation": "Clear the planting area of weeds, stones, and debris to ensure a clean environment for planting.",
                "Planting Time": "The best time to plant orange trees is in the spring after the danger of frost has passed.",
                "Spacing & Depth": "Space trees 12-25 feet apart, depending on the rootstock and tree variety, to allow for proper growth and air circulation. Plant trees at a depth that matches their nursery height, ensuring the graft union is above soil level.",
                "Seeding/Transplanting Methods": "Transplanting: Dig a hole large enough to accommodate the roots, place the tree in the hole, backfill gently, and water thoroughly after planting.",
                "Watering Requirements": "Water young orange trees regularly to establish roots, especially during dry spells. Mature trees require deep watering during dry periods.",
                "Nutrient Management": "Apply a citrus-specific fertilizer in early spring and again in mid-season. Use organic compost to enhance soil health.",
                "Weed Control": "Control weeds through mulching, which helps retain moisture and suppress weed growth, and manual weeding to reduce competition.",
                "Pest & Disease Management": "Monitor for pests such as aphids, spider mites, and citrus leaf miners. Manage diseases like citrus canker and root rot with proper sanitation and resistant varieties. Implement integrated pest management (IPM) strategies, including cultural controls and the use of beneficial insects.",
                "Special Care During Growth": "- Young Tree Stage: Protect young trees from extreme weather and pests; consider using tree guards to prevent animal damage.\n- Vegetative Stage: Regularly check for nutrient deficiencies and address them promptly. Prune to shape trees and encourage a strong structure.\n- Flowering and Fruit Development Stage: Ensure consistent moisture during flowering and fruit set to maximize yield and fruit quality. Thin fruit if necessary to promote larger oranges.",
                "Harvesting": "Oranges are typically ready for harvest 7-12 months after flowering, depending on the variety. Indicators include a change in color, firmness, and sweetness. Use sharp pruning shears to cut oranges from the tree, leaving a short stem attached to the fruit.",
                "Post-Harvest Management": "Handle harvested oranges gently to avoid bruising. Store them in a cool, shaded area.",
                "Storage Conditions": "Store oranges in a cool, dark place. They can be refrigerated to extend their shelf life.",
                "Processing & Packaging": "If needed, oranges can be processed into juice, marmalade, or dried slices. Pack oranges in breathable containers to help maintain quality during storage and transport.",
                "Challenges & Solutions": "Common challenges include susceptibility to pests and diseases, environmental stresses (such as drought or frost), and improper pruning techniques. Choose disease-resistant varieties, implement good cultural practices, and monitor environmental conditions to mitigate these challenges."
            },

            {"name": "Papaya Cultivation Guide",
                "Introduction": "Papayas (Carica papaya) are tropical fruit trees known for their sweet, juicy flesh and vibrant orange color. They thrive in warm climates and can produce fruit year-round under optimal conditions. This guide outlines the complete process for cultivating papayas, from planting to harvesting.",
                "Materials Required": "- Quality papaya seeds or seedlings from reputable nurseries\n- Balanced fertilizers with nitrogen, phosphorus, and potassium; organic compost\n- Drip irrigation systems or hoses for effective moisture management\n- Insecticides, fungicides, and organic pest management solutions\n- Hand tools (shovels, pruning shears, hoes) or tractors for planting, maintenance, and harvesting",
                "Soil Preparation": "Papayas prefer well-drained, sandy loam or loamy soils with a pH of 6.0 to 6.5. Prepare the soil by tilling and incorporating organic matter to enhance drainage and fertility.",
                "Plant Selection & Treatment": "Choose disease-resistant papaya varieties suited to your climate. If using seeds, soak them for a few hours before planting to improve germination rates.",
                "Field Preparation": "Clear the planting area of weeds, stones, and debris to ensure a clean environment for planting.",
                "Planting Time": "The best time to plant papayas is in the spring when temperatures are consistently warm.",
                "Spacing & Depth": "Space papaya plants 6-10 feet apart to allow for their large canopy and root system. Plant seeds or seedlings at a depth of about 0.5 to 1 inch.",
                "Seeding/Transplanting Methods": "Direct Seeding: Plant seeds directly in the ground after the last frost.\nTransplanting: Start seedlings indoors and transplant them when they are about 12 inches tall.",
                "Watering Requirements": "Water young papaya plants regularly, especially during dry spells. Papayas require consistent moisture but do not tolerate waterlogging.",
                "Nutrient Management": "Apply a balanced fertilizer every 4-6 weeks during the growing season. Use organic compost to enhance soil fertility.",
                "Weed Control": "Control weeds through mulching, which helps retain moisture and suppress weed growth, and manual weeding to reduce competition.",
                "Pest & Disease Management": "Monitor for pests such as aphids, whiteflies, and fruit flies. Manage diseases like powdery mildew and root rot with proper sanitation and resistant varieties. Implement integrated pest management (IPM) strategies, including cultural controls and the use of beneficial insects.",
                "Special Care During Growth": "- Seedling Stage: Protect young plants from extreme weather and pests. Use row covers if necessary to shield from frost and insects.\n- Vegetative Stage: Regularly check for nutrient deficiencies and address them promptly. Prune any dead or damaged leaves to promote healthy growth.\n- Fruit Development Stage: Ensure adequate water supply during fruit development. Thin excess fruits if necessary to allow for larger fruit size.",
                "Harvesting": "Papayas are typically ready for harvest 6-12 months after planting, depending on the variety. Indicators include a change in skin color from green to yellow and a sweet aroma. Use a sharp knife to cut the fruit from the tree, leaving a small portion of the stem attached.",
                "Post-Harvest Management": "Handle harvested papayas gently to avoid bruising. Store them in a cool, shaded area.",
                "Storage Conditions": "Store papayas at room temperature to ripen further. Once ripe, they can be refrigerated for a short period to extend freshness.",
                "Processing & Packaging": "If needed, papayas can be processed into smoothies, salads, or dried fruit. Pack papayas in breathable containers to maintain quality during storage and transport.",
                "Challenges & Solutions": "Common challenges include susceptibility to pests and diseases, environmental stresses (such as drought or flooding), and improper watering practices. Choose disease-resistant varieties, implement good cultural practices, and monitor environmental conditions to mitigate these challenges."
            },

            {"name": "Coffee Cultivation Guide",
                "Introduction": "Coffee (Coffea spp.) is one of the most widely consumed beverages globally, known for its stimulating properties and rich flavor. It thrives in tropical climates, typically at higher altitudes, where conditions are ideal for its growth. This guide outlines the complete process for cultivating coffee, from planting to harvesting.",
                "Materials Required": "- Quality coffee seedlings or seeds from reputable nurseries\n- Balanced fertilizers rich in nitrogen, phosphorus, and potassium; organic compost\n- Drip irrigation systems or hoses for effective moisture management\n- Insecticides, fungicides, and organic pest management solutions\n- Hand tools (shovels, pruning shears, hoes) or tractors for planting, maintenance, and harvesting",
                "Soil Preparation": "Coffee prefers well-drained, loamy soils with a pH of 6.0 to 6.5. Prepare the soil by tilling and incorporating organic matter to enhance fertility and drainage.",
                "Plant Selection & Treatment": "Choose disease-resistant coffee varieties suitable for your climate. If using seeds, soak them for 24 hours to improve germination rates.",
                "Field Preparation": "Clear the planting area of weeds, stones, and debris to ensure a clean environment for planting.",
                "Planting Time": "The best time to plant coffee is at the beginning of the rainy season.",
                "Spacing & Depth": "Space coffee plants 5-8 feet apart to allow for proper growth and air circulation. Plant seedlings at a depth that matches their nursery height, ensuring the root collar is level with the soil surface.",
                "Seeding/Transplanting Methods": "Transplanting: Dig a hole large enough to accommodate the roots, place the seedling in the hole, backfill gently, and water thoroughly after planting.",
                "Watering Requirements": "Water young coffee plants regularly to establish roots, especially during dry spells. Mature plants prefer consistent moisture but should not be waterlogged.",
                "Nutrient Management": "Apply a balanced fertilizer every 3-4 months during the growing season. Use organic compost to enhance soil fertility.",
                "Weed Control": "Control weeds through mulching, which helps retain moisture and suppress weed growth, and manual weeding to reduce competition.",
                "Pest & Disease Management": "Monitor for pests such as coffee borer beetles and leaf rust. Manage diseases like root rot and leaf spot with proper sanitation and resistant varieties. Implement integrated pest management (IPM) strategies, including cultural controls and the use of beneficial insects.",
                "Special Care During Growth": "- Seedling Stage: Protect young plants from extreme weather and pests. Use shade cloth if necessary to shield from intense sunlight.\n- Vegetative Stage: Regularly check for nutrient deficiencies and address them promptly. Prune to shape plants and remove any dead or diseased branches.\n- Flowering and Fruit Development Stage: Ensure adequate water supply during flowering and fruit set to maximize yield and fruit quality. Monitor for fruit fly infestations and control as necessary.",
                "Harvesting": "Coffee cherries are typically ready for harvest 7-9 months after flowering, depending on the variety. Indicators include a change in color from green to bright red or yellow. Harvest coffee cherries by hand, picking only the ripe ones. Use a selective picking method for quality.",
                "Post-Harvest Management": "Handle harvested cherries gently to avoid bruising. Process them as soon as possible to prevent spoilage.",
                "Processing Methods": "Use either the dry method (sun-drying cherries) or the wet method (fermenting and washing cherries) to extract the coffee beans.",
                "Storage Conditions": "Store processed coffee beans in a cool, dry place to prevent spoilage and maintain flavor.",
                "Processing & Packaging": "Pack coffee beans in airtight containers to help preserve freshness during storage and transport.",
                "Challenges & Solutions": "Common challenges include susceptibility to pests and diseases, environmental stresses (such as drought or frost), and fluctuating market prices. Choose disease-resistant varieties, implement good cultural practices, and monitor environmental conditions to mitigate these challenges."
            }

        ]
    
    cropGuideHindi = [
        
            {
                "name": "मक्का की खेती गाइड",
                "Introduction": "मक्का (Zea mays), जिसे मकई के name से भी जाना जाता है, एक प्रमुख अनाज फसल है जिसे इसके दानों के लिए व्यापक रूप से उगाया जाता है। यह गाइड बीज चयन से लेकर कटाई तक मक्का की खेती की पूरी प्रक्रिया को कवर करता है।",
                "Materials Required": "- उच्च गुणवत्ता वाले मक्का के बीज (संकर या सुधारित किस्में)\n- उर्वरक (नाइट्रोजन, फॉस्फोरस, पोटैशियम)\n- मशीनरी (ट्रैक्टर, हाथ उपकरण, बीज बोने की मशीन)\n- कीट नियंत्रण (हर्बिसाइड्स, कीटनाशक)\n- सिंचाई उपकरण (ड्रिप या फरो सिंचाई)",
                "Soil Preparation": "मक्का अच्छी जल निकासी वाली दोमट मिट्टी में अच्छी तरह से उगता है, जिसका pH 5.8 से 7.0 हो। मिट्टी को हवादार बनाने और ढेले तोड़ने के लिए जुताई करें।",
                "Seed Selection & Treatment": "उच्च उपज वाली, सूखा प्रतिरोधी किस्मों का चयन करें। बीजों को फफूंदनाशक या कीटनाशक से उपचारित करें।",
                "Field Preparation": "समान जल वितरण के लिए खेत को समतल करें। अधिकतम सूर्य के प्रकाश के लिए पंक्ति की दूरी को अनुकूलित करें।",
                "Planting Time": "आमतौर पर बारिश के मौसम की शुरुआत में, अप्रैल से जून के बीच बोया जाता है।",
                "Spacing & Depth": "पंक्तियों में 20-25 सेमी और पंक्तियों के बीच 60-75 सेमी की दूरी पर बीज बोएं, 2-5 सेमी की गहराई पर।",
                "Seeding Methods": "- **सीधी बुवाई:** बीजों को हाथ से या बीज बोने की मशीन से बोएं।",
                "Watering Requirements": "मक्का को नियमित सिंचाई की आवश्यकता होती है, विशेष रूप से सिल्किंग और टैसलिंग के दौरान। यदि बारिश कम हो तो सिंचाई का उपयोग करें।",
                "Nutrient Management": "उर्वरकों को विभाजित मात्रा में लगाएं: बुवाई के समय, प्रारंभिक विकास के दौरान और टैसलिंग के दौरान।",
                "Weed Control": "हाथ से निराई, होइंग या हर्बिसाइड्स का उपयोग करें। पहली निराई 15-20 दिनों के बाद और दूसरी 30-40 दिनों के बाद करें।",
                "Pest & Disease Management": "मक्का बोरर, आर्मीवर्म और एफिड्स के लिए निगरानी करें। कीटनाशक और एकीकृत कीट प्रबंधन (IPM) का उपयोग करें।",
                "Harvesting": "जब मक्का के भुट्टे पक जाएं और भूसी सूख जाए तो कटाई करें। नमी की मात्रा 20-25% होनी चाहिए। हाथ से या मशीन से कटाई करें।",
                "Post-Harvest Management": "दानों को 13-14% नमी तक सुखाएं। छिलके निकालें, साफ करें और ठीक से भंडारण करें।",
                "Storage Conditions": "दानों को ठंडी, सूखी और हवादार जगह पर रखें ताकि फफूंद और कीटों से बचाव हो सके।",
                "Processing": "यदि आवश्यक हो, तो मक्का को सुखाकर पीस लें।",
                "Challenges & Solutions": "सामान्य समस्याएं: मौसम में परिवर्तन, कीट और पानी की कमी। समाधान: IPM, मिट्टी की नमी की निगरानी और प्रतिरोधी किस्में।"
            },

            {
                "name": "चावल की खेती गाइड",
                "Introduction": "चावल (Oryza sativa) दुनिया के कई हिस्सों में एक मुख्य खाद्य फसल है। यह गाइड बीज चयन से लेकर कटाई तक चावल की खेती की पूरी प्रक्रिया को कवर करता है।",
                "Materials Required": "- उच्च गुणवत्ता वाले बीज\n- उर्वरक (नाइट्रोजन, फॉस्फोरस, पोटैशियम)\n- सिंचाई प्रणाली\n- मशीनरी (ट्रैक्टर, रोपाई मशीन, सिकल)\n- कीट नियंत्रण (हर्बिसाइड्स, कीटनाशक)",
                "Soil Preparation": "चावल मिट्टी या मिट्टी-दोमट मिट्टी में सबसे अच्छा उगता है, जिसका pH 5.5 से 6.5 हो। मिट्टी को जोतकर और समतल करें।",
                "Seed Selection & Treatment": "उच्च उपज वाले, कीट प्रतिरोधी बीजों का उपयोग करें। बीजों को फफूंदनाशक या कीटनाशक से उपचारित करें।",
                "Field Preparation": "खेत को समतल करें और पानी को रोकने के लिए मेड़ बनाएं।",
                "Planting Time": "बारिश के मौसम की शुरुआत में, आमतौर पर मई से जून के बीच बोया जाता है।",
                "Spacing & Depth": "रोपाई के लिए 20x15 सेमी की दूरी का उपयोग करें। सीधी बुवाई के लिए 2-3 सेमी की गहराई पर बोएं।",
                "Seeding Methods": "- **सीधी बुवाई:** बीजों को छिड़काव या पंक्तियों में बोएं।\n- **रोपाई:** नर्सरी में उगाएं और 20-30 दिनों के बाद पौधों को स्थानांतरित करें।",
                "Watering Requirements": "विकास के दौरान 5-10 सेमी पानी बनाए रखें। दाने पकने के दौरान पानी कम करें।",
                "Nutrient Management": "उर्वरकों को विभाजित मात्रा में लगाएं: बुवाई के समय, टिलरिंग के दौरान और पैनिकल इनिशिएशन के दौरान।",
                "Weed Control": "हाथ से निराई या हर्बिसाइड्स का उपयोग करें। रोपाई के 15-20 दिनों के बाद और फिर 40 दिनों के बाद निराई करें।",
                "Pest & Disease Management": "स्टेम बोरर और लीफहॉपर जैसे कीटों के लिए निगरानी करें। कीटनाशक और एकीकृत कीट प्रबंधन (IPM) का उपयोग करें।",
                "Harvesting": "जब दाने सुनहरे पीले हो जाएं और 80-90% दाने पक जाएं तो कटाई करें। छोटे खेतों के लिए सिकल का उपयोग करें, बड़े खेतों के लिए मशीन का उपयोग करें।",
                "Post-Harvest Management": "दानों को 14% नमी तक सुखाएं, फिर भंडारण करें।",
                "Challenges & Solutions": "सामान्य समस्याएं: प्रतिकूल मौसम, कीट और पानी की कमी। समाधान: IPM, पानी के स्तर की निगरानी और फसल विविधीकरण।"
            },

            {
                "name": "जूट की खेती गाइड",
                "Introduction": "जूट एक रेशेदार फसल है जिसे मुख्य रूप से इसके मजबूत, प्राकृतिक रेशों के लिए उगाया जाता है, जो कपड़े और पैकेजिंग में व्यापक रूप से उपयोग किए जाते हैं। यह गाइड बीज चयन से लेकर कटाई तक जूट की खेती की पूरी प्रक्रिया को कवर करता है।",
                "Materials Required": "- उच्च गुणवत्ता वाले, प्रमाणित जूट के बीज (Corchorus olitorius या Corchorus capsularis)\n- जैविक खाद, नाइट्रोजन, फॉस्फोरस और पोटैशियम उर्वरक\n- Soil Preparation के लिए हाथ उपकरण या ट्रैक्टर\n- कीट नियंत्रण के लिए हर्बिसाइड्स और कीटनाशक\n- नियंत्रित सिंचाई के लिए सिंचाई प्रणाली",
                "Soil Preparation": "जूट दोमट, बलुई दोमट मिट्टी में सबसे अच्छा उगता है, जिसका pH 6.0 से 7.5 हो। मिट्टी को जोतकर और समतल करें।",
                "Seed Selection & Treatment": "उच्च उपज वाले और रोग प्रतिरोधी बीजों का चयन करें। बुवाई से पहले बीजों को 24 घंटे के लिए पानी में भिगोएं।",
                "Field Preparation": "खेत को साफ करें और समतल करें। यदि बाढ़ की संभावना हो तो छोटे मेड़ बनाएं।",
                "Planting Time": "जूट आमतौर पर मानसून की शुरुआत में, मार्च से मई के बीच बोया जाता है।",
                "Spacing & Depth": "पंक्तियों में 25-30 सेमी की दूरी पर बीज बोएं। बीजों को 1-2 सेमी की गहराई पर बोएं।",
                "Seeding Methods": "- **छिड़काव:** बीजों को खेत में समान रूप से छिड़कें।\n- **पंक्ति बुवाई:** बीजों को पंक्तियों में बोएं।",
                "Watering Requirements": "जूट को नियमित नमी की आवश्यकता होती है। भारी बारिश के बाद जल निकासी सुनिश्चित करें।",
                "Nutrient Management": "बुवाई के समय नाइट्रोजन, फॉस्फोरस और पोटैशियम उर्वरक लगाएं। 20-25 दिनों के बाद अतिरिक्त नाइट्रोजन लगाएं।",
                "Weed Control": "हाथ से निराई या हर्बिसाइड्स का उपयोग करें। बुवाई के 15-20 दिनों के बाद और फिर 30-40 दिनों के बाद निराई करें।",
                "Pest & Disease Management": "जूट के कीटों जैसे जूट हेयरी कैटरपिलर और एफिड्स के लिए निगरानी करें। कीटनाशक या एकीकृत कीट प्रबंधन (IPM) का उपयोग करें।",
                "Harvesting": "जब पौधे 10-12 फीट लंबे हो जाएं और निचली पत्तियां पीली होने लगें तो कटाई करें। सिकल या चाकू का उपयोग करें।",
                "Post-Harvest Management": "कटाई के बाद पौधों को बांधकर साफ, धीमी गति वाले पानी में डुबोएं। रेटिंग प्रक्रिया 10-15 दिनों तक चलती है।",
                "Challenges & Solutions": "सामान्य समस्याएं: पानी की उपलब्धता, कीट और अनुचित रेटिंग। समाधान: कुशल सिंचाई और कीट नियंधन का उपयोग करें।"
            },

            {
                "name": "कपास की खेती गाइड",
                "Introduction": "कपास एक प्रमुख रेशेदार फसल है जिसे इसके नरम, रूईदार रेशों के लिए उगाया जाता है, जो कपड़े बनाने में उपयोग किए जाते हैं। यह गाइड बीज चयन से लेकर कटाई तक कपास की खेती की पूरी प्रक्रिया को कवर करता है।",
                "Materials Required": "- उच्च गुणवत्ता वाले, प्रमाणित कपास के बीज (जैसे Bt कपास या अन्य कीट प्रतिरोधी किस्में)\n- नाइट्रोजन, फॉस्फोरस, पोटैशियम और सूक्ष्म पोषक तत्व उर्वरक\n- ड्रिप या फरो सिंचाई प्रणाली\n- कीट और बीमारी नियंत्रण के लिए हर्बिसाइड्स और कीटनाशक\n- खेत की तैयारी और रखरखाव के लिए हल, ट्रैक्टर और स्प्रेयर",
                "Soil Preparation": "कपास अच्छी जल निकासी वाली बलुई दोमट मिट्टी में सबसे अच्छा उगता है, जिसका pH 6.0 से 7.5 हो। खेत को गहरी जुताई करके और ढेले तोड़कर तैयार करें।",
                "Seed Selection & Treatment": "उच्च उपज वाले, कीट प्रतिरोधी बीजों का चयन करें। बीजों को फफूंदनाशक या कीटनाशक से उपचारित करें।",
                "Field Preparation": "बुवाई के लिए फरो या बेड बनाएं। जल निकासी सुनिश्चित करें।",
                "Planting Time": "कपास आमतौर पर वसंत ऋतु में, मार्च से मई के बीच बोया जाता है।",
                "Spacing & Depth": "बीजों को 3-5 सेमी की गहराई पर बोएं, पंक्तियों के बीच 75-100 सेमी और पौधों के बीच 25-30 सेमी की दूरी रखें।",
                "Seeding Methods": "- **सीधी बुवाई:** बीजों को तैयार फरो या बेड में सीधे बोएं।",
                "Watering Requirements": "कपास को नियमित नमी की आवश्यकता होती है, विशेष रूप से फूल आने और बोल बनने के दौरान। ड्रिप या फरो सिंचाई का उपयोग करें।",
                "Nutrient Management": "बुवाई के समय फॉस्फोरस और पोटैशियम उर्वरक लगाएं। नाइट्रोजन को विभाजित मात्रा में लगाएं: एक तिहाई बुवाई के समय, एक तिहाई वानस्पतिक विकास के दौरान और एक तिहाई फूल आने के दौरान।",
                "Weed Control": "हाथ से निराई, होइंग या हर्बिसाइड्स का उपयोग करें। बुवाई के 20-30 दिनों के बाद और फिर 45 दिनों के बाद निराई करें।",
                "Pest & Disease Management": "बोलवर्म, एफिड्स और व्हाइटफ्लाइ जैसे कीटों के लिए निगरानी करें। एकीकृत कीट प्रबंधन (IPM) का उपयोग करें।",
                "Harvesting": "जब बोल पूरी तरह से खुल जाएं और रूई फूल जाए तो कटाई करें। छोटे खेतों के लिए हाथ से कटाई करें, बड़े खेतों के लिए मशीन का उपयोग करें।",
                "Post-Harvest Management": "कटाई के बाद रूई को छायादार, हवादार जगह पर सुखाएं। बीजों को अलग करें और रूई को साफ करके भंडारण करें।",
                "Challenges & Solutions": "सामान्य समस्याएं: कीट, पानी की उपलब्धता और मिट्टी की पोषक तत्वों की कमी। समाधान: सूखा प्रतिरोधी किस्में, कुशल सिंचाई और IPM का उपयोग करें।"
            },

            {
                "name": "नारियल की खेती गाइड",
                "Introduction": "नारियल (Cocos nucifera) एक प्रमुख फल है जिसे इसके तेल, दूध और रेशों के लिए उगाया जाता है। यह गाइड बीज चयन से लेकर कटाई तक नारियल की खेती की पूरी प्रक्रिया को कवर करता है।",
                "Materials Required": "- उच्च गुणवत्ता वाले नारियल के पौधे (बौनी या लंबी किस्में)\n- जैविक खाद, NPK उर्वरक\n- ड्रिप या बेसिन सिंचाई\n- कीटनाशक या जैविक नियंत्रण एजेंट\n- हाथ उपकरण या मशीनरी",
                "Soil Preparation": "नारियल अच्छी जल निकासी वाली बलुई दोमट मिट्टी में सबसे अच्छा उगता है, जिसका pH 5.5-7.5 हो। 1 x 1 x 1 मीटर के गड्ढे खोदें और उन्हें मिट्टी, खाद और जैविक खाद से भरें।",
                "Seed Selection & Treatment": "रोग प्रतिरोधी, उच्च उपज वाले पौधों का चयन करें। बौनी किस्में आसान कटाई के लिए उपयुक्त हैं, जबकि लंबी किस्में सूखा प्रतिरोधी हैं।",
                "Field Preparation": "खेत को साफ करें और जल निकासी सुनिश्चित करें। पौधों के बीच उचित दूरी रखें।",
                "Planting Time": "बारिश के मौसम की शुरुआत में लगाएं ताकि सिंचाई की आवश्यकता कम हो।",
                "Spacing & Depth": "लंबी किस्मों के लिए 7.5-9 मीटर की दूरी रखें; बौनी किस्मों के लिए 6.5-7 मीटर। जड़ों को अच्छी तरह से ढकें।",
                "Seeding Methods": "पौधों को गड्ढे में लगाएं, जड़ गर्दन जमीन से ऊपर रखें।",
                "Watering Requirements": "पहले तीन वर्षों तक नियमित सिंचाई करें। परिपक्व पेड़ सूखा प्रतिरोधी होते हैं लेकिन नियमित सिंचाई से लाभ होता है।",
                "Nutrient Management": "संतुलित उर्वरक साल में तीन बार लगाएं। सालाना जैविक खाद डालें।",
                "Weed Control": "नियमित निराई करें, विशेष रूप से प्रारंभिक विकास के दौरान। मल्चिंग से नमी बनाए रखें।",
                "Pest & Disease Management": "राइनोसेरोस बीटल और रेड पाम वीविल जैसे कीटों को नियंत्रित करें। रूट विल्ट और बड रोट को प्रबंधित करें।",
                "Harvesting": "नारियल 12 महीने के बाद पक जाते हैं। हर 45-60 दिनों में कटाई करें।",
                "Post-Harvest Management": "नारियल को सुखाकर भंडारण करें।",
                "Challenges & Solutions": "सूखा, कीट और मिट्टी की कमी को ड्रिप सिंचाई, कीट प्रबंधन और जैविक खाद से नियंत्रित करें।"
            },

            {
                "name": "चने की खेती गाइड",
                "Introduction": "चना (Cicer arietinum) एक प्रमुख दलहनी फसल है जिसे इसके प्रोटीन युक्त दानों के लिए उगाया जाता है। यह गाइड बीज चयन से लेकर कटाई तक चने की खेती की पूरी प्रक्रिया को कवर करता है।",
                "Materials Required": "- उच्च गुणवत्ता वाले, रोग प्रतिरोधी चने के बीज (देसी या काबुली प्रकार)\n- फॉस्फोरस आधारित उर्वरक; न्यूनतम नाइट्रोजन\n- ड्रिप या स्प्रिंकलर सिंचाई\n- हर्बिसाइड्स और कीटनाशक\n- हल, ट्रैक्टर और स्प्रेयर",
                "Soil Preparation": "चना अच्छी जल निकासी वाली दोमट मिट्टी में सबसे अच्छा उगता है, जिसका pH 6.0-7.5 हो। मिट्टी को जोतकर और हैरो करके तैयार करें।",
                "Seed Selection & Treatment": "उच्च उपज वाले, रोग प्रतिरोधी बीजों का चयन करें। बीजों को राइजोबियम बैक्टीरिया से उपचारित करें।",
                "Field Preparation": "खेत को साफ करें और समतल करें। पंक्तियों के बीच उचित दूरी रखें।",
                "Planting Time": "ठंडे, शुष्क मौसम में, आमतौर पर अक्टूबर-नवंबर में बोया जाता है।",
                "Spacing & Depth": "पौधों के बीच 30-40 सेमी और पंक्तियों के बीच 45-60 सेमी की दूरी रखें। बीजों को 5-8 सेमी की गहराई पर बोएं।",
                "Seeding Methods": "सीधी बुवाई का उपयोग करें।",
                "Watering Requirements": "चने को कम पानी की आवश्यकता होती है, लेकिन फूल आने और फली भरने के दौरान सिंचाई करें।",
                "Nutrient Management": "बुवाई के समय फॉस्फोरस उर्वरक लगाएं। मिट्टी परीक्षण के आधार पर पोटैशियम और सूक्ष्म पोषक तत्व लगाएं।",
                "Weed Control": "हाथ से निराई या हर्बिसाइड्स का उपयोग करें। बुवाई के 20-30 दिनों के बाद और फिर 45-50 दिनों के बाद निराई करें।",
                "Pest & Disease Management": "पॉड बोरर और एफिड्स जैसे कीटों के लिए निगरानी करें। एकीकृत कीट प्रबंधन (IPM) का उपयोग करें।",
                "Harvesting": "चने 3-4 महीने में पक जाते हैं। जब पौधे पीले पड़ जाएं और फलियां सूख जाएं तो कटाई करें।",
                "Post-Harvest Management": "दानों को सुखाकर भंडारण करें।",
                "Challenges & Solutions": "सामान्य समस्याएं: कीट, बीमारियां और पोषक तत्वों की कमी। समाधान: IPM, प्रतिरोधी किस्में और मिट्टी परीक्षण का उपयोग करें।"
            },

            {
                "name": "चने की खेती का मार्गदर्शिका",
                "Introduction": "चना (Cicer arietinum) एक लोकप्रिय फलीदार फसल है जिसे इसके प्रोटीन से भरपूर बीजों के लिए उगाया जाता है, जो खाद्य उत्पादन में व्यापक रूप से उपयोग किए जाते हैं। यह मार्गदर्शिका बीज चयन से लेकर फसल कटाई तक चने की खेती की पूरी प्रक्रिया को कवर करती है।",
                "Materials Required": "- उच्च गुणवत्ता वाले, रोग-प्रतिरोधी चने के बीज (देसी या काबुली प्रकार)\n- फास्फोरस आधारित उर्वरक; न्यूनतम नाइट्रोजन\n- ड्रिप या स्प्रिंकलर सिंचाई\n- खरपतवारनाशक और कीटनाशक\n- हल, ट्रैक्टर और स्प्रेयर",
                "Soil Preparation": "चने की खेती के लिए अच्छी जल निकासी वाली दोमट मिट्टी जिसका पीएच 6.0-7.5 हो, सबसे उपयुक्त है। अच्छे जड़ प्रवेश के लिए खेत को जोतें और हैरो करें।",
                "Seed Selection & Treatment": "उच्च उपज देने वाले, रोग-प्रतिरोधी बीज चुनें। नाइट्रोजन स्थिरीकरण के लिए राइजोबियम बैक्टीरिया से और रोगों को रोकने के लिए फफूंदनाशकों से उपचारित करें।",
                "Field Preparation": "खरपतवार साफ करें और खेत को समतल करें। हवा के संचार की अनुमति देने और रोग के जोखिम को कम करने के लिए पंक्तियों को उचित दूरी पर रखें।",
                "Planting Time": "ठंडे, शुष्क मौसम में सबसे अच्छा लगाया जाता है, आमतौर पर अक्टूबर-नवंबर में।",
                "Spacing & Depth": "पौधों को पंक्तियों में 30-40 सेमी की दूरी पर और पंक्तियों को 45-60 सेमी की दूरी पर रखें। मिट्टी की नमी के आधार पर बीज 5-8 सेमी गहराई पर बोएं।",
                "Seeding Methods": "सीड ड्रिल का उपयोग करके या मैनुअल रूप से सीधे बीज बोना।",
                "Watering Requirements": "चने को न्यूनतम पानी की आवश्यकता होती है लेकिन फूल आने और फली भरने के दौरान सिंचाई से लाभ होता है। जलभराव से बचें।",
                "Nutrient Management": "बुवाई के समय फास्फोरस डालें। मिट्टी परीक्षण के आधार पर आवश्यकतानुसार पोटैशियम और सूक्ष्म पोषक तत्वों का उपयोग करें।",
                "Weed Control": "जल्दी और नियमित रूप से निराई करें, या तो मैनुअल रूप से या खरपतवारनाशकों के साथ। पहली निराई 20-30 दिनों पर, यदि आवश्यक हो तो दूसरी 45-50 दिनों पर करें।",
                "Pest & Disease Management": "फली छेदक और एफिड जैसे कीटों की निगरानी करें। आवश्यकतानुसार एकीकृत कीट प्रबंधन (IPM) और जैव-कीटनाशकों का उपयोग करें।",
                "Special Care During Growth": "- अंकुरण अवस्था: कीटों से बचाव करें, मध्यम नमी बनाए रखें।\n- वानस्पतिक अवस्था: फास्फोरस स्तर बनाए रखें।\n- फूल और फली भरने की अवस्था: इष्टतम उपज के लिए पर्याप्त नमी सुनिश्चित करें।",
                "Harvesting": "चने 3-4 महीने में पकते हैं। जब पौधे पीले हो जाएं और फलियां सूख जाएं तब कटाई करें। छोटे खेतों के लिए हाथ से काटें; बड़े पैमाने पर खेती के लिए कंबाइन हार्वेस्टर का उपयोग करें।",
                "Post-Harvest Management": "भंडारण या बिक्री से पहले नमी कम करने के लिए बीजों को धूप में सुखाएं, थ्रेश करें और साफ करें।",
                "Storage Conditions": "कीट संक्रमण और खराब होने से बचाने के लिए सूखे, ठंडे स्थानों पर वेंटिलेशन के साथ स्टोर करें।",
                "Processing & Packaging": "सांस लेने वाले बैग में पैकेजिंग से पहले बीजों को साफ और ग्रेड करें।",
                "Challenges & Solutions": "सामान्य समस्याओं में कीट, रोग, पानी का तनाव और पोषक तत्वों की कमी शामिल है। जोखिमों को कम करने के लिए IPM, प्रतिरोधी किस्मों और मिट्टी परीक्षण का उपयोग करें।"
            },

            {
                "name": "अरहर की खेती का मार्गदर्शिका",
                "Introduction": "अरहर (Cajanus cajan) एक सूखा-प्रतिरोधी फलीदार फसल है जिसे इसकी उच्च प्रोटीन सामग्री और विभिन्न व्यंजनों में उपयोग के लिए महत्व दिया जाता है। यह मार्गदर्शिका बीज चयन से लेकर फसल कटाई तक अरहर की खेती की पूरी प्रक्रिया को कवर करती है।",
                "Materials Required": "- उच्च गुणवत्ता वाले, रोग-प्रतिरोधी अरहर के बीज (जल्दी, मध्यम, या देर से पकने वाली किस्में)\n- नाइट्रोजन, फास्फोरस और पोटैशियम उर्वरक; न्यूनतम नाइट्रोजन की आवश्यकता\n- ड्रिप या फरो सिंचाई उपकरण\n- अरहर के कीटों के लिए विशिष्ट खरपतवारनाशक और कीटनाशक\n- Soil Preparation, रोपण और निराई के लिए हाथ के उपकरण या ट्रैक्टर",
                "Soil Preparation": "अरहर अच्छी जल निकासी वाली बलुई दोमट से लेकर चिकनी दोमट मिट्टी में सबसे अच्छी तरह से उगती है, जिसका पीएच 6.0-7.5 हो। एक अच्छे बीज बिस्तर बनाने के लिए खेत को जोतें और हैरो करें।",
                "Seed Selection & Treatment": "अपने क्षेत्र के लिए उपयुक्त उच्च उपज देने वाली, रोग-प्रतिरोधी किस्मों का चयन करें। बीज जनित रोगों को रोकने के लिए बीजों को फफूंदनाशकों से उपचारित करें।",
                "Field Preparation": "खरपतवार और मलबे से खेत को साफ करें, अच्छी जल निकासी सुनिश्चित करें।",
                "Planting Time": "आमतौर पर बारिश के मौसम की शुरुआत में या उपोष्णकटिबंधीय क्षेत्रों में शुष्क मौसम के दौरान लगाया जाता है।",
                "Spacing & Depth": "पौधों को पंक्तियों में 30-40 सेमी की दूरी पर और पंक्तियों को 60-75 सेमी की दूरी पर रखें। मिट्टी की नमी और बनावट के आधार पर बीज 3-5 सेमी गहराई पर बोएं।",
                "Seeding Methods": "सीड ड्रिल का उपयोग करके या मैनुअल रूप से सीधे बीज बोना।",
                "Watering Requirements": "अरहर सूखा-प्रतिरोधी है लेकिन फूल और फली विकास के दौरान पर्याप्त नमी की आवश्यकता होती है। सिंचाई की आवश्यकता हो सकती है, विशेष रूप से पहले 60 दिनों में।",
                "Nutrient Management": "बुवाई के समय फास्फोरस और पोटैशियम डालें और यदि आवश्यक हो तो नाइट्रोजन का टॉप-ड्रेसिंग करें। जैविक संशोधन मिट्टी की उर्वरता में सुधार कर सकते हैं।",
                "Weed Control": "प्रारंभिक विकास चरणों के दौरान मैनुअल निराई या खरपतवारनाशकों का उपयोग करके खरपतवार नियंत्रित करें। मल्चिंग खरपतवार को दबाने और मिट्टी की नमी बनाए रखने में मदद कर सकती है।",
                "Pest & Disease Management": "फली छेदक, एफिड और सफेदमक्खी जैसे कीटों की निगरानी करें। एकीकृत कीट प्रबंधन (IPM) रणनीतियों को लागू करें, जिसमें जैविक नियंत्रण और आवश्यकतानुसार रासायनिक कीटनाशक शामिल हैं।",
                "Special Care During Growth": "- अंकुरण अवस्था: युवा अंकुरों को कीटों से बचाएं और मिट्टी की नमी बनाए रखें।\n- वानस्पतिक अवस्था: मजबूत विकास के लिए पर्याप्त पोषक तत्व सुनिश्चित करें।\n- फूल और फली भरने की अवस्था: उपज और बीज गुणवत्ता को अधिकतम करने के लिए लगातार नमी बनाए रखें।",
                "Harvesting": "अरहर 4-6 महीने में पकती है। जब फलियां पक जाएं और सूख जाएं तब कटाई करें। छोटे खेतों के लिए हाथ से काटें या बड़े पैमाने पर खेती के लिए कंबाइन हार्वेस्टर का उपयोग करें।",
                "Post-Harvest Management": "बीज की नमी सामग्री को कम करने के लिए थ्रेशिंग से पहले कटी हुई फसल को धूप में सुखाएं।",
                "Storage Conditions": "खराब होने और कीट संक्रमण को रोकने के लिए अरहर को सूखे, ठंडे और अच्छे वेंटिलेशन वाले क्षेत्र में स्टोर करें।",
                "Processing & Packaging": "सांस लेने वाले बैग या कंटेनरों में पैकेजिंग से पहले बीजों को साफ और ग्रेड करें।",
                "Challenges & Solutions": "सामान्य समस्याओं में कीट संक्रमण, रोग, पानी का तनाव और पोषक तत्वों की कमी शामिल हैं। जोखिमों को प्रबंधित करने के लिए रोग-प्रतिरोधी किस्मों का उपयोग करें, फसल चक्र का अभ्यास करें और IPM रणनीतियों को लागू करें।"
            },

            {
                "name": "मोठ की खेती का मार्गदर्शिका",
                "Introduction": "मोठ (Vigna aconitifolia) एक सूखा-प्रतिरोधी फलीदार फसल है जो आमतौर पर शुष्क क्षेत्रों में उगाई जाती है। इन्हें उच्च प्रोटीन सामग्री और पाक अनुप्रयोगों के लिए महत्व दिया जाता है। यह मार्गदर्शिका बीज चयन से लेकर फसल कटाई तक मोठ की खेती की पूरी प्रक्रिया को कवर करती है।",
                "Materials Required": "- उच्च गुणवत्ता वाले, रोग-प्रतिरोधी मोठ के बीज\n- फास्फोरस और पोटैशियम उर्वरक; न्यूनतम नाइट्रोजन\n- ड्रिप या फरो सिंचाई\n- खरपतवारनाशक और कीटनाशक\n- हाथ के उपकरण या ट्रैक्टर",
                "Soil Preparation": "मोठ अच्छी जल निकासी वाली बलुई दोमट या चिकनी मिट्टी में फलती-फूलती है, जिसका पीएच 6.0-8.0 हो। एक अच्छे बीज बिस्तर के लिए खेत को जोतें और हैरो करें।",
                "Seed Selection & Treatment": "उच्च उपज देने वाली, सूखा-सहिष्णु किस्मों का चयन करें। बीज जनित रोगों को रोकने के लिए बीजों को फफूंदनाशक या कीटनाशकों से उपचारित करें।",
                "Field Preparation": "अच्छे बीज-से-मिट्टी संपर्क सुनिश्चित करने के लिए खेत को खरपतवार और मलबे से साफ करें।",
                "Planting Time": "आमतौर पर मानसून के मौसम की शुरुआत में, जून और जुलाई के बीच बोया जाता है।",
                "Spacing & Depth": "पौधों को पंक्तियों में 30-45 सेमी की दूरी पर और पंक्तियों को 60-75 सेमी की दूरी पर रखें। मिट्टी की नमी के आधार पर बीज 3-5 सेमी गहराई पर बोएं।",
                "Seeding Methods": "सीड ड्रिल का उपयोग करके या मैनुअल रूप से सीधे बीज बोना।",
                "Watering Requirements": "मोठ सूखा-प्रतिरोधी है लेकिन फूल और फली विकास के दौरान लगातार नमी से लाभ होता है। यदि वर्षा अपर्याप्त है तो पानी दें।",
                "Nutrient Management": "बुवाई के समय फास्फोरस और पोटैशियम डालें। नाइट्रोजन का उपयोग केवल तभी करें जब मिट्टी परीक्षण कमी का संकेत दें। जैविक संशोधन मिट्टी की उर्वरता में सुधार करते हैं।",
                "Weed Control": "मैनुअल निराई या खरपतवारनाशकों के साथ जल्दी खरपतवार नियंत्रित करें। मल्चिंग खरपतवार को दबाने और मिट्टी की नमी बनाए रखने में मदद करती है।",
                "Pest & Disease Management": "एफिड, फली छेदक और लीफहॉपर जैसे कीटों की निगरानी करें। आवश्यकतानुसार एकीकृत कीट प्रबंधन (IPM) रणनीतियों का उपयोग करें।",
                "Special Care During Growth": "- अंकुरण अवस्था: मध्यम नमी बनाए रखें और कीटों से बचाव करें।\n- वानस्पतिक अवस्था: पर्याप्त पोषक तत्व सुनिश्चित करें।\n- फूल और फली भरने की अवस्था: इष्टतम उपज के लिए नमी बनाए रखें।",
                "Harvesting": "जब फलियां पक जाएं और सूख जाएं, आमतौर पर बुवाई के 90-120 दिनों बाद कटाई करें। छोटे खेतों के लिए हाथ से कटाई करें; बड़े पैमाने पर संचालन के लिए कंबाइन हार्वेस्टर का उपयोग करें।",
                "Post-Harvest Management": "नमी सामग्री को कम करने के लिए थ्रेशिंग से पहले पौधों को धूप में सुखाएं।",
                "Storage Conditions": "खराब होने और कीट संक्रमण को रोकने के लिए सूखे, ठंडे स्थानों पर वेंटिलेशन के साथ स्टोर करें।",
                "Processing & Packaging": "सांस लेने वाले बैग में पैकेजिंग से पहले बीजों को साफ और ग्रेड करें।",
                "Challenges & Solutions": "सामान्य समस्याओं में कीट, रोग और प्रतिकूल मौसम शामिल हैं। जोखिमों को कम करने के लिए सूखा-प्रतिरोधी किस्मों, IPM प्रथाओं और उचित मिट्टी प्रबंधन का उपयोग करें।"
            },

            {
                "name": "मूंग की खेती का मार्गदर्शिका",
                "Introduction": "मूंग (Vigna radiata) छोटी, हरी फलीदार फसलें हैं जिन्हें उनकी पोषण सामग्री और पाक बहुमुखी प्रतिभा के लिए अत्यधिक महत्व दिया जाता है। यह मार्गदर्शिका बीज चयन से लेकर फसल कटाई तक मूंग की खेती की पूरी प्रक्रिया को कवर करती है।",
                "Materials Required": "- उच्च गुणवत्ता वाले, रोग-प्रतिरोधी मूंग के बीज\n- नाइट्रोजन, फास्फोरस और पोटैशियम उर्वरक (न्यूनतम नाइट्रोजन की आवश्यकता)\n- ड्रिप या फरो सिंचाई\n- खरपतवारनाशक और कीटनाशक\n- हाथ के उपकरण या ट्रैक्टर",
                "Soil Preparation": "मूंग अच्छी जल निकासी वाली बलुई दोमट से लेकर दोमट मिट्टी पसंद करती है जिसका पीएच 6.0-7.5 हो। एक अच्छे बीज बिस्तर प्राप्त करने के लिए खेत को जोतें और हैरो करें।",
                "Seed Selection & Treatment": "अपनी जलवायु के लिए उपयुक्त उच्च उपज देने वाली, रोग-प्रतिरोधी किस्मों का चयन करें। मिट्टी जनित रोगों से बचाव के लिए बीजों को फफूंदनाशकों से उपचारित करें।",
                "Field Preparation": "अच्छे बीज-से-मिट्टी संपर्क सुनिश्चित करने के लिए खेत को खरपतवार और मलबे से साफ करें।",
                "Planting Time": "आमतौर पर बारिश के मौसम की शुरुआत में या अप्रैल और जून के बीच गर्म, शुष्क परिस्थितियों में बोया जाता है।",
                "Spacing & Depth": "पौधों को पंक्तियों में 30-40 सेमी की दूरी पर और पंक्तियों को 45-60 सेमी की दूरी पर रखें। मिट्टी की नमी के आधार पर बीज 2-4 सेमी गहराई पर बोएं।",
                "Seeding Methods": "सीड ड्रिल का उपयोग करके या मैनुअल रूप से सीधे बीज बोना।",
                "Watering Requirements": "मूंग को पर्याप्त नमी की आवश्यकता होती है, विशेष रूप से अंकुरण और फूल आने के दौरान। यदि वर्षा अपर्याप्त है तो पानी दें, जड़ सड़न को रोकने के लिए अधिक पानी न दें।",
                "Nutrient Management": "बुवाई के समय फास्फोरस और पोटैशियम डालें। अतिरिक्त नाइट्रोजन यदि आवश्यक हो तो लगाया जा सकता है, लेकिन आमतौर पर, प्राकृतिक स्थिरीकरण पर्याप्त होता है। मिट्टी की उर्वरता में सुधार के लिए जैविक पदार्थ शामिल करें।",
                "Weed Control": "मैनुअल निराई या खरपतवारनाशकों के माध्यम से जल्दी खरपतवार नियंत्रित करें। मल्चिंग खरपतवार को दबाने और मिट्टी की नमी संरक्षित करने में मदद करती है।",
                "Pest & Disease Management": "एफिड, बीटल और थ्रिप्स जैसे कीटों की निगरानी करें। आवश्यकतानुसार एकीकृत कीट प्रबंधन (IPM) रणनीतियों का उपयोग करें।",
                "Special Care During Growth": "- अंकुरण अवस्था: युवा अंकुरों को कीटों से बचाएं और पर्याप्त नमी बनाए रखें।\n- वानस्पतिक अवस्था: मजबूत विकास के लिए पर्याप्त पोषक तत्व सुनिश्चित करें।\n- फूल और फली भरने की अवस्था: इष्टतम उपज और गुणवत्ता के लिए नमी बनाए रखें।",
                "Harvesting": "जब फलियां पक जाएं और सूख जाएं, आमतौर पर बुवाई के 60-90 दिनों बाद कटाई करें। छोटे खेतों के लिए हाथ से कटाई करें; बड़े पैमाने पर संचालन के लिए कंबाइन हार्वेस्टर का उपयोग करें।",
                "Post-Harvest Management": "नमी सामग्री को कम करने के लिए थ्रेशिंग से पहले पौधों को धूप में सुखाएं।",
                "Storage Conditions": "खराब होने और कीट संक्रमण को रोकने के लिए सूखे, ठंडे स्थानों पर वेंटिलेशन के साथ स्टोर करें।",
                "Processing & Packaging": "सांस लेने वाले बैग में पैकेजिंग से पहले बीजों को साफ और ग्रेड करें।",
                "Challenges & Solutions": "सामान्य समस्याओं में कीट, रोग और प्रतिकूल मौसम शामिल हैं। जोखिमों को कम करने के लिए रोग-प्रतिरोधी किस्मों, IPM प्रथाओं और उचित मिट्टी और जल प्रबंधन का उपयोग करें।"
            },

            {
                "name": "उड़द की खेती का मार्गदर्शिका",
                "Introduction": "उड़द (Vigna mungo) एक अत्यधिक पौष्टिक फलीदार फसल है जिसे इसकी उच्च प्रोटीन सामग्री के लिए महत्व दिया जाता है और इसका उपयोग विभिन्न व्यंजनों में व्यापक रूप से किया जाता है। यह मार्गदर्शिका बीज चयन से लेकर फसल कटाई तक उड़द की खेती की पूरी प्रक्रिया को कवर करती है।",
                "Materials Required": "- उच्च गुणवत्ता वाले, रोग-प्रतिरोधी उड़द के बीज\n- फास्फोरस और पोटैशियम उर्वरक (न्यूनतम नाइट्रोजन की आवश्यकता)\n- ड्रिप या फरो सिंचाई\n- खरपतवारनाशक और कीटनाशक\n- हाथ के उपकरण या ट्रैक्टर",
                "Soil Preparation": "उड़द अच्छी जल निकासी वाली बलुई दोमट से लेकर चिकनी दोमट मिट्टी पसंद करता है जिसका पीएच 6.0-7.5 हो। अच्छा बीज बिस्तर बनाने के लिए खेत को जोतें और हैरो करें।",
                "Seed Selection & Treatment": "अपनी जलवायु के लिए उपयुक्त उच्च उपज देने वाली, रोग-प्रतिरोधी किस्मों का चयन करें। मिट्टी जनित रोगों से बचाव के लिए बीजों को फफूंदनाशकों या कीटनाशकों से उपचारित करें।",
                "Field Preparation": "अच्छे बीज-से-मिट्टी संपर्क सुनिश्चित करने के लिए खेत को खरपतवार और मलबे से साफ करें।",
                "Planting Time": "आमतौर पर मानसून के मौसम की शुरुआत में या जून और जुलाई के बीच गर्म, शुष्क परिस्थितियों में बोया जाता है।",
                "Spacing & Depth": "पौधों को पंक्तियों में 30-45 सेमी की दूरी पर और पंक्तियों को 60-75 सेमी की दूरी पर रखें। मिट्टी की नमी के आधार पर बीज 3-5 सेमी गहराई पर बोएं।",
                "Seeding Methods": "सीड ड्रिल का उपयोग करके या मैनुअल रूप से सीधे बीज बोना।",
                "Watering Requirements": "उड़द को पर्याप्त नमी की आवश्यकता होती है, विशेष रूप से अंकुरण और फूल आने के दौरान। यदि वर्षा अपर्याप्त है तो पानी दें, जड़ सड़न को रोकने के लिए अधिक पानी न दें।",
                "Nutrient Management": "बुवाई के समय फास्फोरस और पोटैशियम डालें। नाइट्रोजन स्थिरीकरण के कारण अतिरिक्त नाइट्रोजन आमतौर पर आवश्यक नहीं होता। मिट्टी की उर्वरता में सुधार के लिए जैविक पदार्थ शामिल करें।",
                "Weed Control": "मैनुअल निराई या खरपतवारनाशकों के माध्यम से जल्दी खरपतवार नियंत्रित करें। मल्चिंग खरपतवार को दबाने और मिट्टी की नमी संरक्षित करने में मदद करती है।",
                "Pest & Disease Management": "एफिड, फली छेदक और थ्रिप्स जैसे कीटों की निगरानी करें। आवश्यकतानुसार एकीकृत कीट प्रबंधन (IPM) रणनीतियों का उपयोग करें।",
                "Special Care During Growth": "- अंकुरण अवस्था: युवा अंकुरों को कीटों से बचाएं और पर्याप्त नमी बनाए रखें।\n- वानस्पतिक अवस्था: मजबूत विकास के लिए पर्याप्त पोषक तत्व सुनिश्चित करें।\n- फूल और फली भरने की अवस्था: इष्टतम उपज और गुणवत्ता के लिए नमी बनाए रखें।",
                "Harvesting": "जब फलियां पक जाएं और सूख जाएं, आमतौर पर बुवाई के 60-90 दिनों बाद कटाई करें। छोटे खेतों के लिए हाथ से कटाई करें; बड़े पैमाने पर संचालन के लिए कंबाइन हार्वेस्टर का उपयोग करें।",
                "Post-Harvest Management": "नमी सामग्री को कम करने के लिए थ्रेशिंग से पहले पौधों को धूप में सुखाएं।",
                "Storage Conditions": "खराब होने और कीट संक्रमण को रोकने के लिए सूखे, ठंडे स्थानों पर वेंटिलेशन के साथ स्टोर करें।",
                "Processing & Packaging": "सांस लेने वाले बैग में पैकेजिंग से पहले बीजों को साफ और ग्रेड करें।",
                "Challenges & Solutions": "सामान्य समस्याओं में कीट, रोग और प्रतिकूल मौसम शामिल हैं। जोखिमों को कम करने के लिए रोग-प्रतिरोधी किस्मों, IPM प्रथाओं और उचित मिट्टी और जल प्रबंधन का उपयोग करें।"
            },

            {
                "name": "मसूर की खेती का मार्गदर्शिका",
                "Introduction": "मसूर (Lens culinaris) पौष्टिक फलीदार फसलें हैं जो अपनी उच्च प्रोटीन और फाइबर सामग्री के लिए जानी जाती हैं। इनकी खेती व्यापक रूप से खाद्य पदार्थों के लिए की जाती है और ये कई व्यंजनों में मुख्य भोजन हैं। यह मार्गदर्शिका बीज चयन से लेकर फसल कटाई तक मसूर की खेती की पूरी प्रक्रिया को कवर करती है।",
                "Materials Required": "- उच्च गुणवत्ता वाले, रोग-प्रतिरोधी मसूर के बीज\n- फास्फोरस और पोटैशियम उर्वरक (न्यूनतम नाइट्रोजन की आवश्यकता)\n- ड्रिप या फरो सिंचाई\n- खरपतवारनाशक और कीटनाशक\n- हाथ के उपकरण या ट्रैक्टर",
                "Soil Preparation": "मसूर अच्छी जल निकासी वाली दोमट या बलुई मिट्टी पसंद करती है जिसका पीएच 6.0-7.5 हो। अच्छा बीज बिस्तर बनाने के लिए खेत को जोतें और हैरो करें।",
                "Seed Selection & Treatment": "अपने क्षेत्र के अनुकूल उच्च उपज देने वाली, रोग-प्रतिरोधी किस्मों का चयन करें। बीज जनित रोगों से बचाव के लिए बीजों को फफूंदनाशकों या कीटनाशकों से उपचारित करें।",
                "Field Preparation": "अच्छे बीज-से-मिट्टी संपर्क सुनिश्चित करने के लिए खेत को खरपतवार और मलबे से साफ करें।",
                "Planting Time": "मसूर आमतौर पर वसंत की शुरुआत या सर्दियों के अंत में बोई जाती है, जलवायु के आधार पर, जब मिट्टी का तापमान लगभग 10-15°C (50-59°F) तक पहुंच जाता है।",
                "Spacing & Depth": "पौधों को पंक्तियों में 25-30 सेमी की दूरी पर और पंक्तियों को 45-60 सेमी की दूरी पर रखें। मिट्टी की नमी के आधार पर बीज 2-3 सेमी गहराई पर बोएं।",
                "Seeding Methods": "सीड ड्रिल का उपयोग करके या मैनुअल रूप से सीधे बीज बोना।",
                "Watering Requirements": "मसूर सूखा-सहिष्णु होती है लेकिन अंकुरण और फली विकास के दौरान पर्याप्त नमी की आवश्यकता होती है। यदि वर्षा अपर्याप्त है तो पानी दें, विशेष रूप से फूल आने और बीज भरने के दौरान।",
                "Nutrient Management": "बुवाई के समय फास्फोरस और पोटैशियम डालें। नाइट्रोजन स्थिरीकरण के कारण अतिरिक्त नाइट्रोजन आमतौर पर आवश्यक नहीं होता। मिट्टी की उर्वरता बढ़ाने के लिए जैविक पदार्थ शामिल करें।",
                "Weed Control": "प्रारंभिक विकास के दौरान मैनुअल निराई या खरपतवारनाशकों का उपयोग करके खरपतवार नियंत्रित करें। मल्चिंग भी खरपतवार को दबाने और मिट्टी की नमी बनाए रखने में मदद कर सकती है।",
                "Pest & Disease Management": "एफिड, लाइगस बग और रूट रॉट जैसे कीटों की निगरानी करें। आवश्यकतानुसार एकीकृत कीट प्रबंधन (IPM) रणनीतियों को लागू करें।",
                "Special Care During Growth": "- अंकुरण अवस्था: युवा अंकुरों को कीटों से बचाएं और पर्याप्त नमी बनाए रखें।\n- वानस्पतिक अवस्था: मजबूत विकास के लिए पर्याप्त पोषक तत्व सुनिश्चित करें।\n- फूल और फली भरने की अवस्था: इष्टतम उपज और गुणवत्ता के लिए नमी बनाए रखें।",
                "Harvesting": "जब फलियां भूरी हो जाएं और सूख जाएं, आमतौर पर बुवाई के 80-100 दिनों बाद कटाई करें। छोटे खेतों के लिए हाथ से कटाई करें; बड़े पैमाने पर संचालन के लिए कंबाइन हार्वेस्टर का उपयोग करें।",
                "Post-Harvest Management": "नमी सामग्री को कम करने के लिए थ्रेशिंग से पहले पौधों को धूप में सुखाएं।",
                "Storage Conditions": "खराब होने और कीट संक्रमण को रोकने के लिए सूखे, ठंडे स्थानों पर वेंटिलेशन के साथ स्टोर करें।",
                "Processing & Packaging": "सांस लेने वाले बैग में पैकेजिंग से पहले बीजों को साफ और ग्रेड करें।",
                "Challenges & Solutions": "सामान्य समस्याओं में कीट, रोग और परिवर्तनशील मौसम शामिल हैं। जोखिमों को कम करने के लिए रोग-प्रतिरोधी किस्मों, IPM प्रथाओं और उचित मिट्टी और जल प्रबंधन का उपयोग करें।"
            },

            {
                "name": "अनार की खेती गाइड",
                "Introduction": "अनार (Punica granatum) एक पौष्टिक फल है जो अपने स्वास्थ्य लाभों और समृद्ध स्वाद के लिए जाना जाता है। यह कई हिस्सों में उगाया जाता है और गर्म जलवायु में अच्छा पनपता है। यह गाइड रोपण से लेकर कटाई तक की पूरी प्रक्रिया को कवर करता है।",
                "Materials Required": "- उच्च गुणवत्ता वाले अनार के बीज या विश्वसनीय नर्सरी से स्वस्थ पौधे\n- नाइट्रोजन, फास्फोरस और पोटैशियम युक्त संतुलित उर्वरक\n- ड्रिप सिंचाई प्रणाली या फरो सिंचाई\n- कीटनाशक और कवकनाशक कीट और रोग प्रबंधन के लिए\n- रोपण, छंटाई और रखरखाव के लिए हाथ के उपकरण या ट्रैक्टर",
                "Soil Preparation": "अनार को अच्छे जल निकास वाली, रेतीली दोमट से दोमट मिट्टी पसंद है, जिसका pH 5.5 से 7.0 के बीच हो। जैविक पदार्थ मिलाकर भूमि की जुताई करें।",
                "Seed Selection & Treatment": "अपने क्षेत्र की जलवायु के लिए उपयुक्त रोग प्रतिरोधी किस्में चुनें। यदि बीजों का उपयोग कर रहे हैं, तो अंकुरण दर में सुधार के लिए उन्हें रात भर पानी में भिगोएं।",
                "Field Preparation": "जमीन से खरपतवार, पत्थर और मलबे को हटा दें ताकि एक स्वच्छ रोपण वातावरण सुनिश्चित हो।",
                "Planting Time": "अनार को आमतौर पर वसंत में अंतिम ठंढ के बाद लगाया जाता है।",
                "Spacing & Depth": "पौधों को 5-8 फीट की दूरी पर लगाएं ताकि उचित विकास और वायु संचार सुनिश्चित हो सके। बीजों या पौधों को 1-2 इंच गहराई में लगाएं और मिट्टी को अच्छे से दबाएं।",
                "Seeding Methods": "सीधा बुआई: बीजों को सीधे तैयार किए गए स्थान पर बोएं।\nप्रतिरोपण: यदि पौधे लगा रहे हैं, तो जड़ के आकार से थोड़ा बड़ा गड्ढा खोदें और मिट्टी से भरें।",
                "Watering Requirements": "अनार को विशेष रूप से प्रारंभिक अवस्था में नियमित पानी देने की आवश्यकता होती है। एक बार स्थापित होने के बाद, यह सूखा सहिष्णु होता है। गहरे जड़ विकास को बढ़ावा देने के लिए गहराई से लेकिन कम बार पानी दें।",
                "Nutrient Management": "विकास के मौसम के दौरान संतुलित उर्वरक डालें, आमतौर पर शुरुआती वसंत और देर से गर्मियों में। मिट्टी की उर्वरता बढ़ाने के लिए जैविक खाद मिलाएं।",
                "Weed Control": "पोषक तत्वों के लिए प्रतिस्पर्धा कम करने के लिए मल्चिंग और हाथ से निराई करके खरपतवारों को नियंत्रित करें।",
                "Pest & Disease Management": "कीटों जैसे एफिड्स, सफेद मक्खी और अनार तितलियों पर नजर रखें। प्राकृतिक शत्रुओं और जैविक कीटनाशकों का उपयोग करके एकीकृत कीट प्रबंधन (IPM) रणनीतियाँ लागू करें।",
                "Special Care During Growth": "- अंकुर अवस्था: युवा पौधों को अत्यधिक मौसम और कीटों से बचाएं। नमी बनाए रखने के लिए मल्च का उपयोग करें।\n- वनस्पति अवस्था: पोषक तत्वों की कमी और कीट संक्रमण के लिए नियमित रूप से जाँच करें और आवश्यकतानुसार उर्वरक डालें।\n- फूल और फल बनने की अवस्था: स्वस्थ विकास को बढ़ावा देने के लिए फूल लगने और फल बनने के दौरान पर्याप्त पानी सुनिश्चित करें।",
                "Harvesting": "अनार आमतौर पर फूल आने के 5-7 महीने बाद कटाई के लिए तैयार होता है, जब फल गहरे रंग का हो जाता है और थपथपाने पर धातु जैसी आवाज करता है। फलों को तेज कैंची से काटें ताकि शाखाओं और अन्य फलों को नुकसान न पहुंचे।",
                "Post-Harvest Management": "फलों को धीरे से संभालें ताकि चोट न लगे; उन्हें ठंडी और सूखी जगह पर रखें।",
                "Storage Conditions": "अनार को ठंडी और सूखी जगह पर स्टोर करें; उचित परिस्थितियों में यह कई हफ्तों से महीनों तक टिक सकता है।",
                "Processing & Packaging": "फलों को साफ और छांटकर किसी भी खराब या सड़े हुए फलों को अलग करें। भंडारण के दौरान गुणवत्ता बनाए रखने के लिए फलों को सांस लेने योग्य कंटेनरों में पैक करें।",
                "Challenges & Solutions": "सामान्य समस्याओं में कीट, रोग और सूखा या अत्यधिक नमी जैसी पर्यावरणीय चुनौतियाँ शामिल हैं। रोग प्रतिरोधी किस्मों का उपयोग करें, उचित सिंचाई तकनीकों को लागू करें, और कीट नियंत्रण के लिए नियमित निगरानी करें।"
            },

            {
                "name": "राजमा की खेती गाइड",
                "Introduction": "राजमा (Phaseolus vulgaris) एक उच्च प्रोटीन युक्त दलहन है जो विभिन्न व्यंजनों में उपयोग किया जाता है। यह गाइड बीज चयन से लेकर कटाई तक की पूरी प्रक्रिया को कवर करता है।",
                "Materials Required": "- उच्च गुणवत्ता वाले, रोग प्रतिरोधी राजमा के बीज\n- फास्फोरस और पोटैशियम उर्वरक; सीमित नाइट्रोजन क्योंकि राजमा स्वयं नाइट्रोजन फिक्स करता है\n- ड्रिप या स्प्रिंकलर सिंचाई प्रणाली\n- खरपतवारनाशी और कीटनाशक सामान्य राजमा कीटों के लिए\n- Soil Preparation, रोपण और निराई के लिए हाथ के उपकरण या ट्रैक्टर",
                "Soil Preparation": "राजमा अच्छे जल निकास वाली, दोमट मिट्टी में सबसे अच्छा बढ़ता है, जिसका pH 6.0 से 7.0 के बीच होता है। जुताई और जड़ें आसानी से फैलाने के लिए हल्की मिट्टी तैयार करें।",
                "Seed Selection & Treatment": "उच्च उपज देने वाली, रोग प्रतिरोधी किस्में चुनें। बीजों को शुरुआती मिट्टी जनित रोगों और कीटों से बचाने के लिए कवकनाशी या कीटनाशक से उपचारित करें।",
                "Field Preparation": "खेत से खरपतवार और मलबे को साफ करें, फिर समतल करें। पंक्तियों को इस तरह चिह्नित करें कि वायु संचार और सूर्य का प्रकाश अच्छी तरह मिल सके।",
                "Planting Time": "राजमा को आमतौर पर वसंत में तब बोया जाता है जब मिट्टी का तापमान 15°C (59°F) तक पहुँच जाता है और ठंढ का कोई खतरा नहीं होता।",
                "Spacing & Depth": "बीजों को 3-5 सेमी गहराई में लगाएं, पौधों के बीच 8-10 सेमी और पंक्तियों के बीच 45-60 सेमी दूरी रखें।",
                "Seeding Methods": "सीधी बुआई: बीजों को सीधे खेत में हाथ से या बीज ड्रिल से बोएं।",
                "Watering Requirements": "राजमा को नियमित रूप से पानी देने की आवश्यकता होती है, विशेष रूप से फूल और फली बनने के दौरान। अधिक पानी देने से बचें क्योंकि यह जलभराव के प्रति संवेदनशील होता है।",
                "Nutrient Management": "रोपण के समय फास्फोरस और पोटैशियम लागू करें। नाइट्रोजन की मात्रा सीमित रखें क्योंकि राजमा स्वयं नाइट्रोजन का स्थिरीकरण करता है।",
                "Weed Control": "खरपतवारों को नियंत्रित करने के लिए शुरुआती चरणों में निराई करें। जरूरत पड़ने पर खरपतवारनाशी का उपयोग करें।",
                "Harvesting": "राजमा की कटाई तब करें जब फली पूरी तरह परिपक्व और सूखी हो, आमतौर पर 90-120 दिनों में।",
                "Storage Conditions": "राजमा को सूखी, हवादार जगह पर स्टोर करें ताकि फफूंदी और कीटों से बचा जा सके।"
            },

            {
                "name": "केला खेती गाइड",
                "Introduction": "केले (Musa spp.) एक उष्णकटिबंधीय फल हैं जो अपने मीठे स्वाद और पोषण गुणों के लिए प्रसिद्ध हैं। ये गर्म, आर्द्र जलवायु में अच्छी तरह से विकसित होते हैं और व्यावसायिक तथा घरेलू उत्पादन दोनों के लिए उगाए जाते हैं। यह गाइड केले की खेती की पूरी प्रक्रिया को कवर करता है, जिसमें रोपण से लेकर कटाई तक की जानकारी दी गई है।",
                "Materials Required": "- स्वस्थ केला चूसक या ऊतक-संस्कृत पौधे\n- नाइट्रोजन, फॉस्फोरस और पोटैशियम युक्त संतुलित उर्वरक; जैविक खाद जैसे कंपोस्ट\n- सिंचाई प्रबंधन के लिए ड्रिप या स्प्रिंकलर प्रणाली\n- कीटनाशक और कवकनाशक ताकि कीट और रोगों को प्रबंधित किया जा सके\n- रोपण, रखरखाव और कटाई के लिए हाथ के उपकरण (फावड़ा, छंटाई कैंची) या ट्रैक्टर",
                "Soil Preparation": "केले अच्छी जल निकासी वाली, समृद्ध दोमट मिट्टी को पसंद करते हैं जिसका पीएच 5.5 से 7.0 के बीच हो। मिट्टी को जोतकर उसमें जैविक खाद मिलाएं ताकि उर्वरता और जल निकासी में सुधार हो।",
                "Plant Selection & Treatment": "स्वस्थ माता-पिता पौधों से रोग-मुक्त चूसक चुनें या प्रमाणित स्रोत से ऊतक-संस्कृत पौधे प्राप्त करें। चूसक को माता-पिता पौधे से काटने के लिए स्वच्छ चाकू का उपयोग करें ताकि संक्रमण न फैले।",
                "Field Preparation": "रोपण स्थल को खरपतवार, पत्थरों और मलबे से साफ करें ताकि स्वस्थ वातावरण बनाया जा सके।",
                "Planting Time": "केले के लिए सबसे अच्छा रोपण समय वर्षा ऋतु की शुरुआत या गर्म महीनों के दौरान होता है।",
                "Spacing & Depth": "पौधों को पंक्तियों में 8-10 फीट की दूरी पर और पंक्तियों के बीच 10-12 फीट की दूरी पर लगाएं ताकि उचित वृद्धि और वायु संचार हो सके। चूसकों या पौधों को उसी गहराई पर लगाएं जिस गहराई पर वे नर्सरी में उग रहे थे।",
                "Seeding Methods": "केले को लगातार नमी की आवश्यकता होती है; विशेष रूप से सूखे समय में नियमित रूप से सिंचाई करें। प्रति सप्ताह 1-2 इंच पानी देने का प्रयास करें।",
                "Nutrient Management": "वसंत ऋतु की शुरुआत में और फिर मध्य ऋतु में संतुलित उर्वरक लगाएं। मिट्टी की उर्वरता बढ़ाने के लिए जैविक खाद या गीली घास का उपयोग करें।",
                "Weed Control": "गीली घास का उपयोग करके खरपतवारों को नियंत्रित करें, जिससे नमी भी बनी रहती है, और हाथ से निराई करके पोषक तत्वों की प्रतिस्पर्धा को कम करें।",
                "Pest & Disease Management": "केले के भूरे धब्बे की बीमारी और बनाना वीविल जैसे कीटों की निगरानी करें। उचित स्वच्छता और प्रतिरोधी किस्मों के उपयोग से रोगों को रोकें। एकीकृत कीट प्रबंधन (IPM) रणनीतियों को लागू करें, जिनमें जैविक नियंत्रण विधियाँ भी शामिल हैं।",
                "Harvesting": "केले आमतौर पर रोपण के 9-12 महीने बाद कटाई के लिए तैयार होते हैं। जब फल मोटे हो जाते हैं और डंठल और फल के बीच का कोण अधिक स्पष्ट हो जाता है, तो उन्हें काट लें। तेज चाकू या खुरपी का उपयोग करके पूरे गुच्छे को काटें। फलों को सावधानीपूर्वक संभालें ताकि वे क्षतिग्रस्त न हों।",
                "Storage Conditions": "केले को कमरे के तापमान पर रखें जब तक वे पूरी तरह से पक न जाएँ। सीधे धूप या अत्यधिक गर्मी से बचाएं।",
                "Challenges & Solutions": "सामान्य समस्याओं में कीट और रोग संवेदनशीलता, पर्यावरणीय तनाव और अनुचित सिंचाई शामिल हैं। रोग प्रतिरोधी किस्मों का चयन करें, अच्छे कृषि अभ्यासों को लागू करें और पर्यावरणीय स्थितियों की निगरानी करें।"
            },


            {"name": "अंगूर की खेती मार्गदर्शिका",
                "Introduction": "अंगूर (Vitis vinifera और अन्य प्रजातियाँ) बहुउद्देश्यीय फल हैं, जिनका उपयोग ताजे फल के रूप में खाने, सूखाकर किशमिश बनाने और वाइन उत्पादन के लिए किया जाता है। ये समशीतोष्ण जलवायु में अच्छे से विकसित होते हैं और उच्च गुणवत्ता वाले फल उत्पादन के लिए विशिष्ट बढ़ती परिस्थितियों की आवश्यकता होती है। यह मार्गदर्शिका अंगूर की खेती की पूरी प्रक्रिया को कवर करती है, जिसमें रोपण से लेकर कटाई तक की जानकारी दी गई है।",
                "Materials Required": "- उच्च गुणवत्ता वाली अंगूर की बेलें, नग्न जड़ या गमले में उगाई गई, विश्वसनीय नर्सरी से\n- संतुलित उर्वरक जिसमें नाइट्रोजन, फास्फोरस और पोटैशियम हों; जैविक खाद\n- प्रभावी नमी प्रबंधन के लिए ड्रिप सिंचाई प्रणाली\n- कीटनाशक, फफूंदनाशक और जैविक कीट प्रबंधन समाधान\n- रोपण, रखरखाव और कटाई के लिए हाथ के औजार (प्रूनर, फावड़ा) या ट्रैक्टर",
                "Soil Preparation": "अंगूर को अच्छी जल निकासी वाली, रेतीली दोमट या चिकनी दोमट मिट्टी पसंद होती है, जिसकी पीएच 6.0 से 6.8 के बीच हो। मिट्टी को जोतकर और जैविक पदार्थ मिलाकर उर्वरता और जल निकासी में सुधार करें।",
                "Plant Selection & Treatment": "अपने जलवायु और उद्देश्य (टेबल अंगूर, वाइन अंगूर आदि) के लिए रोग-प्रतिरोधी अंगूर की किस्में चुनें। रोपण से पहले बेलों की बीमारी या क्षति के लिए जाँच करें।",
                "Field Preparation": "रोपण स्थल को खरपतवार, पत्थरों और मलबे से साफ करें ताकि स्वच्छ वातावरण सुनिश्चित हो।",
                "Planting Time": "अंगूर को शुरुआती वसंत में अंतिम ठंढ के बाद या सर्दियों से पहले पतझड़ में लगाना सबसे अच्छा होता है।",
                "Spacing & Depth": "बेलों को 6-10 फीट की दूरी पर और पंक्तियों को 8-10 फीट की दूरी पर लगाएँ ताकि उचित वायु संचार और विकास सुनिश्चित हो सके। बेलों को उसी गहराई पर लगाएँ जिस पर वे नर्सरी में उग रही थीं।",
                "Seed Selection & Treatment": "पुनः प्रत्यारोपण: जड़ों को समायोजित करने के लिए पर्याप्त बड़ा गड्ढा खोदें, धीरे-धीरे मिट्टी भरें और रोपण के बाद अच्छी तरह पानी दें।",
                "Watering Requirements": "अंगूर को पहले वर्ष में नियमित रूप से पानी देने की आवश्यकता होती है ताकि जड़ें स्थापित हो सकें। एक बार स्थापित हो जाने के बाद, वे सूखा-सहिष्णु होते हैं, लेकिन सूखे की स्थिति में, विशेष रूप से फल विकास के दौरान, अतिरिक्त सिंचाई लाभकारी होती है।",
                "Nutrient Management": "शुरुआती वसंत में और मध्य सीजन में संतुलित उर्वरक डालें। जैविक खाद का उपयोग करें ताकि मिट्टी की सेहत में सुधार हो।",
                "Weed Control": "खरपतवारों को रोकने के लिए गीली घास (मल्चिंग), हाथ से निराई या शाकनाशी का उपयोग करें ताकि पोषक तत्वों और नमी के लिए प्रतिस्पर्धा कम हो।",
                "Pest & Disease Management": "अंगूर कीट जैसे अंगूर की बेल कीट, एफिड्स और मकड़ी के कणों के लिए निगरानी रखें। पाउडरी मिल्ड्यू और डाउनरी मिल्ड्यू जैसी बीमारियों को स्वच्छता और रोग-प्रतिरोधी किस्मों के माध्यम से नियंत्रित करें। एकीकृत कीट प्रबंधन (IPM) रणनीतियों को अपनाएँ, जिसमें सांस्कृतिक नियंत्रण और प्राकृतिक शिकारी शामिल हों।",
                "Special Care During Growth": "- युवा बेल चरण: युवा बेलों को चरम मौसम और कीटों से बचाएँ; उन्हें ऊपर बढ़ने में मदद के लिए सहारा स्टेक्स या ट्रेलिस का उपयोग करें।\n- वनस्पति चरण: पोषक तत्वों की कमी के लिए नियमित रूप से जाँच करें और उन्हें तुरंत पूरा करें। मजबूत संरचना और वायु संचार को प्रोत्साहित करने के लिए छँटाई करें।\n- फूल और फल विकास चरण: फूल आने और फल बनने के दौरान निरंतर नमी सुनिश्चित करें ताकि उपज और गुणवत्ता बढ़ सके। बड़े फलों को बढ़ावा देने के लिए यदि आवश्यक हो तो गुच्छों को पतला करें।",
                "Harvesting": "अंगूर फूल आने के 4-6 महीने बाद कटाई के लिए तैयार होते हैं, जो किस्म के आधार पर भिन्न हो सकता है। उन्हें पूरी तरह से पका होने पर काटना चाहिए, जब वे गहरे रंग के हो जाएँ और मीठे स्वाद वाले हों। बेल से गुच्छों को काटने के लिए तेज कैंची या प्रूनर का उपयोग करें। फलों को नुकसान से बचाने के लिए सावधानीपूर्वक संभालें।",
                "Post-Harvest Management": "किसी भी क्षतिग्रस्त या सड़े हुए अंगूर को हटा दें और उन्हें ठंडी, छायादार जगह पर रखें।",
                "Storage Conditions": "अंगूर को ठंडी, सूखी जगह पर स्टोर करें। प्रशीतन से उनका शेल्फ लाइफ बढ़ाया जा सकता है, लेकिन उन्हें हवादार कंटेनरों में रखना चाहिए।",
                "Processing & Packaging": "यदि आवश्यक हो, तो अंगूर को अंगूर का रस, जैली या वाइन में संसाधित किया जा सकता है। परिवहन के दौरान खराब होने से बचाने के लिए अंगूर को हवादार कंटेनरों में पैक करें।",
                "Challenges & Solutions": "सामान्य समस्याओं में कीट और बीमारियों की संवेदनशीलता, जलवायु से संबंधित समस्याएँ और अनुचित सिंचाई शामिल हैं। रोग-प्रतिरोधी किस्में चुनें, अच्छे कृषि पद्धतियों को अपनाएँ और पर्यावरणीय परिस्थितियों की निगरानी करें ताकि इन चुनौतियों को कम किया जा सके।"
            },

            {
                "name": "मस्कमेलन की खेती गाइड",
                "Introduction": "मस्कमेलन (Cucumis melo var. cantaloupe) मीठे, सुगंधित फल होते हैं, जो अपने रसीले गूदे और विशिष्ट जालदार छिलके के लिए जाने जाते हैं। ये गर्म जलवायु में अच्छी तरह से पनपते हैं और अपने ताजगी भरे स्वाद के लिए लोकप्रिय हैं। यह गाइड मस्कमेलन की खेती की पूरी प्रक्रिया को कवर करता है, रोपण से लेकर कटाई तक।",
                "Materials Required": "- विश्वसनीय स्रोतों से उच्च गुणवत्ता वाले मस्कमेलन के बीज या पौधे\n- नाइट्रोजन, फॉस्फोरस और पोटैशियम युक्त संतुलित उर्वरक; जैविक खाद\n- नमी प्रबंधन के लिए ड्रिप या ओवरहेड सिंचाई प्रणाली\n- कीटनाशक, फफूंदनाशी और जैविक कीट प्रबंधन समाधान\n- फावड़े, कुदाल, छंटाई कैंची जैसे हाथ के औजार या खेती के लिए ट्रैक्टर",
                "Soil Preparation": "मस्कमेलन को अच्छी जल निकासी वाली, बलुई दोमट या दोमट मिट्टी पसंद होती है, जिसकी pH 6.0 से 6.8 के बीच हो। मिट्टी को जोतकर और जैविक पदार्थ मिलाकर जल निकासी और उर्वरता बढ़ाएं।",
                "Plant Selection & Treatment": "अपने जलवायु और बाजार के अनुसार रोग प्रतिरोधी किस्मों का चयन करें। यदि बीज उपयोग कर रहे हैं, तो उन्हें बोने से पहले कुछ घंटों के लिए पानी में भिगोएँ ताकि अंकुरण दर में सुधार हो सके।",
                "Field Preparation": "रोपण स्थल को खरपतवार, पत्थरों और मलबे से साफ करें ताकि एक स्वच्छ वातावरण सुनिश्चित हो सके।",
                "Planting Time": "मस्कमेलन लगाने का आदर्श समय अंतिम पाले के बाद होता है जब मिट्टी का तापमान लगातार 70°F (21°C) से अधिक हो।",
                "Spacing & Depth": "मस्कमेलन के पौधों को 3-4 फीट की दूरी पर और पंक्तियों को 6-8 फीट की दूरी पर लगाएं ताकि बेलें फैल सकें। बीजों या पौधों को लगभग 1 इंच की गहराई में लगाएं।",
                "Seed Selection & Treatment": "- प्रत्यक्ष बीजारोपण: जब मिट्टी गर्म हो जाए तो बीजों को सीधे जमीन में बोएं।\n- पुनःरोपण: पौधों को पहले अंदर उगाएं और जब वे मजबूत हो जाएं तो उन्हें खेत में प्रत्यारोपित करें।",
                "Watering Requirements": "मस्कमेलन को विशेष रूप से अंकुरण और फल विकास के दौरान लगातार नमी की आवश्यकता होती है। प्रति सप्ताह लगभग 1-2 इंच पानी देने का लक्ष्य रखें, वर्षा के अनुसार समायोजन करें।",
                "Nutrient Management": "रोपण के समय और जब बेलें बढ़ने लगें तो संतुलित उर्वरक लगाएं। जैविक खाद या गीली घास का उपयोग मिट्टी के स्वास्थ्य को बढ़ाने के लिए करें।",
                "Weed Control": "गीली घास के उपयोग से नमी बनाए रखने और खरपतवार के विकास को दबाने में मदद मिलती है। नियमित रूप से हाथ से खरपतवार निकालें ताकि वे पौधों से पोषक तत्व न छीनें।",
                "Pest & Disease Management": "कीटों जैसे कि एफिड्स, ककड़ी बीटल और मकड़ी के कणों की निगरानी करें। पाउडरी मिल्ड्यू और डाउनी मिल्ड्यू जैसे रोगों का प्रबंधन उचित स्वच्छता और प्रतिरोधी किस्मों के माध्यम से करें। एकीकृत कीट प्रबंधन (IPM) रणनीतियों को अपनाएं।",
                "Special Care During Growth": "- अंकुर अवस्था: युवा पौधों को कीटों और अत्यधिक मौसम से बचाएं।\n- वनस्पति अवस्था: पोषक तत्वों की कमी की नियमित जांच करें और तुरंत समाधान करें।\n- फल विकास अवस्था: फल के विकास के दौरान पर्याप्त पानी की आपूर्ति करें ताकि फल स्वस्थ और मीठे बनें।",
                "Harvesting": "मस्कमेलन आमतौर पर रोपण के 70-90 दिन बाद कटाई के लिए तैयार हो जाते हैं। संकेतों में रंग का हरे से पीले की ओर परिवर्तन और मीठी सुगंध शामिल हैं। फल को बेल से काटने के लिए तेज चाकू या छंटाई कैंची का उपयोग करें।",
                "Post-Harvest Management": "कटे हुए फलों को सावधानीपूर्वक संभालें ताकि चोट या क्षति से बचा जा सके। उन्हें एक ठंडी, छायादार जगह में रखें।",
                "Storage Conditions": "मस्कमेलन को पूरी तरह पकने तक कमरे के तापमान पर रखें। एक बार पक जाने के बाद, उन्हें थोड़े समय के लिए फ्रिज में रखा जा सकता है ताकि ताजगी बनी रहे।",
                "Processing & Packaging": "यदि आवश्यक हो, तो मस्कमेलन को स्मूदी, शर्बत या फलों के सलाद में संसाधित किया जा सकता है। भंडारण और परिवहन के दौरान गुणवत्ता बनाए रखने के लिए मस्कमेलन को सांस लेने योग्य कंटेनरों में पैक करें।",
                "Challenges & Solutions": "सामान्य चुनौतियों में कीट और रोग संवेदनशीलता, पर्यावरणीय तनाव जैसे सूखा या अत्यधिक नमी, और अनुचित सिंचाई प्रथाएँ शामिल हैं। रोग-प्रतिरोधी किस्मों का चयन करें, अच्छी खेती की प्रथाएँ अपनाएँ और पर्यावरणीय परिस्थितियों की निगरानी करें।"
            },

            {
                "name": "सेब की खेती गाइड",
                "Introduction": "सेब (Malus domestica) दुनिया में सबसे लोकप्रिय फलों में से एक हैं, जो अपने स्वाद, बहुमुखी उपयोग और पोषण मूल्य के लिए सराहे जाते हैं। ये समशीतोष्ण जलवायु में सबसे अच्छा विकसित होते हैं और विभिन्न प्रकार की मिट्टी में उगाए जा सकते हैं। यह गाइड सेब की खेती की पूरी प्रक्रिया को रेखांकित करता है, जिसमें रोपण से लेकर कटाई तक की जानकारी शामिल है।",
                "Materials Required": "- प्रतिष्ठित नर्सरी से उच्च गुणवत्ता वाले सेब के पौधे या ग्राफ्टेड किस्में\n- नाइट्रोजन, फॉस्फोरस और पोटैशियम युक्त संतुलित उर्वरक; जैविक खाद\n- प्रभावी नमी प्रबंधन के लिए ड्रिप सिंचाई प्रणाली या नली\n- कीटनाशक, फफूंदनाशी और जैविक कीट प्रबंधन समाधान\n- रोपण, रखरखाव और कटाई के लिए हाथ के उपकरण (फावड़ा, छंटाई कैंची, कुदाल) या ट्रैक्टर",
                "Soil Preparation": "सेब को अच्छी जल निकासी वाली, दोमट मिट्टी पसंद होती है, जिसका pH 6.0 से 7.0 के बीच हो। मिट्टी को जोतकर उसमें जैविक पदार्थ मिलाएं ताकि उपजाऊपन और जल निकासी में सुधार हो।",
                "Plant Selection & Treatment": "अपने जलवायु के अनुसार रोग-प्रतिरोधी सेब की किस्में चुनें, जिसमें फल के स्वाद और कटाई के समय को ध्यान में रखें। पौधों को लगाने से पहले किसी भी बीमारी या क्षति के लक्षणों की जांच करें।",
                "Field Preparation": "रोपण क्षेत्र को खरपतवार, पत्थर और मलबे से साफ करें ताकि एक स्वच्छ वातावरण सुनिश्चित हो।",
                "Planting Time": "सेब के पौधों को लगाने का सबसे अच्छा समय पतझड़ या शुरुआती वसंत ऋतु होता है, जब पेड़ सुप्त अवस्था में होते हैं।",
                "Spacing & Depth": "बौनी किस्मों को 4-6 फीट की दूरी पर और मानक किस्मों को 10-15 फीट की दूरी पर लगाएं ताकि उचित वृद्धि और वायु संचलन हो सके। पेड़ों को उसी गहराई पर लगाएं जिस गहराई पर वे नर्सरी में थे, और यह सुनिश्चित करें कि ग्राफ्ट यूनियन मिट्टी के स्तर से ऊपर रहे।",
                "Seeding/Transplanting Methods": "रोपण: जड़ों के आकार के अनुसार एक गड्ढा खोदें, पौधे को उसमें रखें, धीरे-धीरे मिट्टी भरें और रोपण के बाद अच्छी तरह पानी दें।",
                "Watering Requirements": "छोटे सेब के पौधों को जड़ जमाने के लिए नियमित रूप से पानी दें, विशेष रूप से शुष्क मौसम में। स्थापित पेड़ सूखा-सहिष्णु होते हैं, लेकिन फल के विकास के दौरान गहरे पानी की आवश्यकता होती है।",
                "Nutrient Management": "वसंत ऋतु की शुरुआत में और मध्य मौसम में संतुलित उर्वरक लगाएं। जैविक खाद का उपयोग करके मिट्टी के स्वास्थ्य में सुधार करें।",
                "Weed Control": "मल्चिंग से खरपतवारों को नियंत्रित करें, जिससे नमी बनाए रखने और खरपतवार वृद्धि को दबाने में मदद मिलती है। साथ ही, प्रतिस्पर्धा को कम करने के लिए समय-समय पर खरपतवार निकालें।",
                "Pest & Disease Management": "कोडिंग मॉथ, एफिड्स और स्पाइडर माइट्स जैसे कीटों की निगरानी करें। सेब स्कैब और पाउडरी मिल्ड्यू जैसी बीमारियों का उचित स्वच्छता और रोग प्रतिरोधी किस्मों के माध्यम से प्रबंधन करें। एकीकृत कीट प्रबंधन (IPM) रणनीतियों को लागू करें, जिसमें सांस्कृतिक नियंत्रण और लाभकारी कीटों का उपयोग शामिल हो।",
                "Special Care During Growth": "- युवा पौधा चरण: युवा पेड़ों को चरम मौसम और कीटों से बचाएं; पशु क्षति से बचाने के लिए ट्री गार्ड का उपयोग करें।\n- वनस्पति वृद्धि चरण: नियमित रूप से पोषक तत्वों की कमी की जांच करें और उन्हें तुरंत ठीक करें। पेड़ों की सही आकार में छंटाई करें और मजबूत संरचना विकसित करने में मदद करें।\n- फूल और फल विकास चरण: अधिकतम उपज और फल की गुणवत्ता सुनिश्चित करने के लिए फूल आने और फल लगने के दौरान निरंतर नमी बनाए रखें। यदि आवश्यक हो, तो बड़े सेब पैदा करने के लिए कुछ फलों को पतला करें।",
                "Harvesting": "सेब आमतौर पर फूल आने के 4-6 महीने बाद कटाई के लिए तैयार होते हैं, जो किस्म पर निर्भर करता है। कटाई के संकेतों में रंग परिवर्तन, मजबूत बनावट और पेड़ से आसानी से अलग होना शामिल हैं। तेज छंटाई कैंची से सेब काटें, जिससे फल से एक छोटा तना जुड़ा रहे।",
                "Post-Harvest Management": "कटे हुए सेबों को धीरे से संभालें ताकि चोट लगने से बचा जा सके। उन्हें ठंडी और छायादार जगह पर संग्रहित करें।",
                "Storage Conditions": "सेब को ठंडी, अंधेरी जगह में रखें। उनकी शेल्फ लाइफ बढ़ाने के लिए इन्हें रेफ्रिजरेटर में संग्रहीत किया जा सकता है।",
                "Processing & Packaging": "यदि आवश्यक हो, तो सेब को सेब सॉस, साइडर या सूखे टुकड़ों में संसाधित किया जा सकता है। सेबों को सांस लेने योग्य कंटेनरों में पैक करें ताकि भंडारण और परिवहन के दौरान उनकी गुणवत्ता बनी रहे।",
                "Challenges & Solutions": "आम चुनौतियों में कीट और रोगों की संवेदनशीलता, पर्यावरणीय तनाव (जैसे सूखा या पाला) और अनुचित छंटाई तकनीक शामिल हैं। रोग-प्रतिरोधी किस्मों का चयन करें, अच्छे कृषि अभ्यासों को लागू करें, और इन चुनौतियों को कम करने के लिए पर्यावरणीय परिस्थितियों की निगरानी करें।"
            },

           {
                "name": "संतरा खेती गाइड",
                "Introduction": "संतरा (Citrus sinensis) सबसे लोकप्रिय खट्टे फलों में से एक है, जो अपने मीठे, रसदार गूदे और उच्च विटामिन C सामग्री के लिए मूल्यवान है। ये गर्म, उपोष्णकटिबंधीय से लेकर उष्णकटिबंधीय जलवायु में पनपते हैं। यह गाइड संतरे की खेती की पूरी प्रक्रिया को रेखांकित करता है, जिसमें रोपण से लेकर कटाई तक की जानकारी शामिल है।",
                "Materials Required": "- प्रतिष्ठित नर्सरी से उच्च गुणवत्ता वाले संतरे के पौधे या ग्राफ्टेड किस्में\n- नाइट्रोजन, फॉस्फोरस और पोटैशियम युक्त खट्टे फलों के लिए विशेष उर्वरक; जैविक खाद\n- प्रभावी नमी प्रबंधन के लिए ड्रिप सिंचाई प्रणाली या नली\n- कीटनाशक, फफूंदनाशी और जैविक कीट प्रबंधन समाधान\n- रोपण, रखरखाव और कटाई के लिए हाथ के उपकरण (फावड़ा, छंटाई कैंची, कुदाल) या ट्रैक्टर",
                "Soil Preparation": "संतरा अच्छी जल निकासी वाली, बलुई दोमट या चिकनी दोमट मिट्टी को पसंद करता है, जिसका pH 6.0 से 7.5 के बीच हो। मिट्टी को जोतकर उसमें जैविक पदार्थ मिलाएं ताकि उपजाऊपन और जल निकासी में सुधार हो।",
                "Plant Selection & Treatment": "अपने जलवायु के अनुसार रोग-प्रतिरोधी संतरे की किस्में चुनें, जिसमें फल के स्वाद और कटाई के समय को ध्यान में रखें। पौधों को लगाने से पहले किसी भी बीमारी या क्षति के लक्षणों की जांच करें।",
                "Field Preparation": "रोपण क्षेत्र को खरपतवार, पत्थर और मलबे से साफ करें ताकि एक स्वच्छ वातावरण सुनिश्चित हो।",
                "Planting Time": "संतरे के पौधों को लगाने का सबसे अच्छा समय वसंत ऋतु होता है, जब ठंढ का खतरा समाप्त हो जाता है।",
                "Spacing & Depth": "पेड़ों को 12-25 फीट की दूरी पर लगाएं, जो कि जड़स्टॉक और पेड़ की किस्म पर निर्भर करता है, ताकि उचित वृद्धि और वायु संचलन हो सके। पेड़ों को उसी गहराई पर लगाएं जिस गहराई पर वे नर्सरी में थे, और यह सुनिश्चित करें कि ग्राफ्ट यूनियन मिट्टी के स्तर से ऊपर रहे।",
                "Seeding/Transplanting Methods": "रोपण: जड़ों के आकार के अनुसार एक गड्ढा खोदें, पौधे को उसमें रखें, धीरे-धीरे मिट्टी भरें और रोपण के बाद अच्छी तरह पानी दें।",
                "Watering Requirements": "छोटे संतरे के पौधों को जड़ जमाने के लिए नियमित रूप से पानी दें, विशेष रूप से शुष्क मौसम में। स्थापित पेड़ शुष्क अवधि के दौरान गहरे पानी की आवश्यकता रखते हैं।",
                "Nutrient Management": "वसंत ऋतु की शुरुआत में और मध्य मौसम में खट्टे फलों के लिए विशेष उर्वरक लगाएं। जैविक खाद का उपयोग करके मिट्टी के स्वास्थ्य में सुधार करें।",
                "Weed Control": "मल्चिंग से खरपतवारों को नियंत्रित करें, जिससे नमी बनाए रखने और खरपतवार वृद्धि को दबाने में मदद मिलती है। साथ ही, प्रतिस्पर्धा को कम करने के लिए समय-समय पर खरपतवार निकालें।",
                "Pest & Disease Management": "एफिड्स, स्पाइडर माइट्स और साइट्रस लीफ माइनर जैसे कीटों की निगरानी करें। साइट्रस कैंकर और रूट रॉट जैसी बीमारियों का उचित स्वच्छता और रोग प्रतिरोधी किस्मों के माध्यम से प्रबंधन करें। एकीकृत कीट प्रबंधन (IPM) रणनीतियों को लागू करें, जिसमें सांस्कृतिक नियंत्रण और लाभकारी कीटों का उपयोग शामिल हो।",
                "Special Care During Growth": "- युवा पौधा चरण: युवा पेड़ों को चरम मौसम और कीटों से बचाएं; पशु क्षति से बचाने के लिए ट्री गार्ड का उपयोग करें।\n- वनस्पति वृद्धि चरण: नियमित रूप से पोषक तत्वों की कमी की जांच करें और उन्हें तुरंत ठीक करें। पेड़ों की सही आकार में छंटाई करें और मजबूत संरचना विकसित करने में मदद करें।\n- फूल और फल विकास चरण: अधिकतम उपज और फल की गुणवत्ता सुनिश्चित करने के लिए फूल आने और फल लगने के दौरान निरंतर नमी बनाए रखें। यदि आवश्यक हो, तो बड़े संतरे पैदा करने के लिए कुछ फलों को पतला करें।",
                "Harvesting": "संतरे आमतौर पर फूल आने के 7-12 महीने बाद कटाई के लिए तैयार होते हैं, जो किस्म पर निर्भर करता है। कटाई के संकेतों में रंग परिवर्तन, मजबूत बनावट और मिठास शामिल हैं। तेज छंटाई कैंची से संतरे काटें, जिससे फल से एक छोटा तना जुड़ा रहे।",
                "Post-Harvest Management": "कटे हुए संतरों को धीरे से संभालें ताकि चोट लगने से बचा जा सके। उन्हें ठंडी और छायादार जगह पर संग्रहित करें।",
                "Storage Conditions": "संतरे को ठंडी, अंधेरी जगह में रखें। उनकी शेल्फ लाइफ बढ़ाने के लिए इन्हें रेफ्रिजरेटर में संग्रहीत किया जा सकता है।",
                "Processing & Packaging": "यदि आवश्यक हो, तो संतरे को जूस, मुरब्बा या सूखे टुकड़ों में संसाधित किया जा सकता है। संतरों को सांस लेने योग्य कंटेनरों में पैक करें ताकि भंडारण और परिवहन के दौरान उनकी गुणवत्ता बनी रहे।",
                "Challenges & Solutions": "आम चुनौतियों में कीट और रोगों की संवेदनशीलता, पर्यावरणीय तनाव (जैसे सूखा या पाला) और अनुचित छंटाई तकनीक शामिल हैं। रोग-प्रतिरोधी किस्मों का चयन करें, अच्छे कृषि अभ्यासों को लागू करें, और इन चुनौतियों को कम करने के लिए पर्यावरणीय परिस्थितियों की निगरानी करें।"
            },


           {
                "name": "पपीता खेती गाइड",
                "Introduction": "पपीता (Carica papaya) एक उष्णकटिबंधीय फलदार वृक्ष है, जो अपने मीठे, रसदार गूदे और चमकीले नारंगी रंग के लिए प्रसिद्ध है। यह गर्म जलवायु में पनपता है और अनुकूल परिस्थितियों में वर्षभर फल प्रदान कर सकता है। यह गाइड पपीते की खेती की पूरी प्रक्रिया को रेखांकित करता है, जिसमें रोपण से लेकर कटाई तक की जानकारी शामिल है।",
                "Materials Required": "- प्रतिष्ठित नर्सरी से उच्च गुणवत्ता वाले पपीते के बीज या पौधे\n- नाइट्रोजन, फॉस्फोरस और पोटैशियम युक्त संतुलित उर्वरक; जैविक खाद\n- प्रभावी नमी प्रबंधन के लिए ड्रिप सिंचाई प्रणाली या नली\n- कीटनाशक, फफूंदनाशी और जैविक कीट प्रबंधन समाधान\n- रोपण, रखरखाव और कटाई के लिए हाथ के उपकरण (फावड़ा, छंटाई कैंची, कुदाल) या ट्रैक्टर",
                "Soil Preparation": "पपीता अच्छी जल निकासी वाली, बलुई दोमट या दोमट मिट्टी को पसंद करता है, जिसका pH 6.0 से 6.5 के बीच हो। मिट्टी को जोतकर उसमें जैविक पदार्थ मिलाएं ताकि जल निकासी और उपजाऊपन में सुधार हो।",
                "Plant Selection & Treatment": "अपने जलवायु के अनुसार रोग-प्रतिरोधी पपीते की किस्में चुनें। यदि बीजों का उपयोग कर रहे हैं, तो रोपण से पहले उन्हें कुछ घंटों के लिए भिगोएं ताकि अंकुरण दर में सुधार हो।",
                "Field Preparation": "रोपण क्षेत्र को खरपतवार, पत्थर और मलबे से साफ करें ताकि एक स्वच्छ वातावरण सुनिश्चित हो।",
                "Planting Time": "पपीते के पौधों को लगाने का सबसे अच्छा समय वसंत ऋतु होता है, जब तापमान लगातार गर्म रहता है।",
                "Spacing & Depth": "पपीते के पौधों को 6-10 फीट की दूरी पर लगाएं ताकि उनकी बड़ी छतरी और जड़ प्रणाली के लिए पर्याप्त जगह हो। बीजों या पौधों को 0.5 से 1 इंच की गहराई पर लगाएं।",
                "Seeding/Transplanting Methods": "प्रत्यक्ष बीजाई: अंतिम ठंढ के बाद बीजों को सीधे जमीन में बोएं।\nरोपाई: बीजों को घर के अंदर अंकुरित करें और जब वे लगभग 12 इंच लंबे हो जाएं, तब उन्हें खेत में प्रत्यारोपित करें।",
                "Watering Requirements": "छोटे पपीते के पौधों को नियमित रूप से पानी दें, विशेष रूप से शुष्क मौसम में। पपीते को लगातार नमी की आवश्यकता होती है लेकिन जलभराव सहन नहीं होता।",
                "Nutrient Management": "वृद्धि के मौसम में हर 4-6 सप्ताह में संतुलित उर्वरक लगाएं। जैविक खाद का उपयोग करके मिट्टी की उपजाऊपन में सुधार करें।",
                "Weed Control": "मल्चिंग से खरपतवारों को नियंत्रित करें, जिससे नमी बनाए रखने और खरपतवार वृद्धि को दबाने में मदद मिलती है। साथ ही, प्रतिस्पर्धा को कम करने के लिए समय-समय पर खरपतवार निकालें।",
                "Pest & Disease Management": "एफिड्स, सफेद मक्खियाँ और फल मक्खियों जैसे कीटों की निगरानी करें। पाउडरी मिल्ड्यू और जड़ सड़न जैसी बीमारियों का उचित स्वच्छता और रोग-प्रतिरोधी किस्मों के माध्यम से प्रबंधन करें। एकीकृत कीट प्रबंधन (IPM) रणनीतियों को लागू करें, जिसमें सांस्कृतिक नियंत्रण और लाभकारी कीटों का उपयोग शामिल हो।",
                "Special Care During Growth": "- अंकुर अवस्था: युवा पौधों को चरम मौसम और कीटों से बचाएं। यदि आवश्यक हो तो पाले और कीड़ों से बचाने के लिए रो कवर का उपयोग करें।\n- वनस्पति वृद्धि अवस्था: नियमित रूप से पोषक तत्वों की कमी की जांच करें और उन्हें तुरंत ठीक करें। स्वस्थ वृद्धि को प्रोत्साहित करने के लिए मरे हुए या क्षतिग्रस्त पत्तों की छंटाई करें।\n- फल विकास अवस्था: फल बनने के दौरान पर्याप्त पानी की आपूर्ति सुनिश्चित करें। यदि आवश्यक हो, तो बड़े फल प्राप्त करने के लिए अतिरिक्त फलों को पतला करें।",
                "Harvesting": "पपीते आमतौर पर रोपण के 6-12 महीने बाद कटाई के लिए तैयार होते हैं, जो किस्म पर निर्भर करता है। कटाई के संकेतों में त्वचा का हरा से पीला रंग में परिवर्तन और मीठी सुगंध शामिल हैं। तेज चाकू से फल को पेड़ से काटें, जिससे फल के साथ थोड़ा सा तना जुड़ा रहे।",
                "Post-Harvest Management": "कटे हुए पपीते को धीरे से संभालें ताकि चोट लगने से बचा जा सके। उन्हें ठंडी और छायादार जगह पर संग्रहित करें।",
                "Storage Conditions": "पपीते को कमरे के तापमान पर रखा जा सकता है ताकि वे और अधिक पक सकें। एक बार पकने के बाद, उनकी ताजगी बढ़ाने के लिए उन्हें थोड़े समय के लिए रेफ्रिजरेटर में संग्रहीत किया जा सकता है।",
                "Processing & Packaging": "यदि आवश्यक हो, तो पपीते को स्मूदी, सलाद या सूखे फलों में संसाधित किया जा सकता है। पपीतों को सांस लेने योग्य कंटेनरों में पैक करें ताकि भंडारण और परिवहन के दौरान उनकी गुणवत्ता बनी रहे।",
                "Challenges & Solutions": "आम चुनौतियों में कीट और रोगों की संवेदनशीलता, पर्यावरणीय तनाव (जैसे सूखा या बाढ़) और अनुचित सिंचाई पद्धतियाँ शामिल हैं। रोग-प्रतिरोधी किस्मों का चयन करें, अच्छे कृषि अभ्यासों को लागू करें, और इन चुनौतियों को कम करने के लिए पर्यावरणीय परिस्थितियों की निगरानी करें।"
            },


            {
                "name": "कॉफी की खेती गाइड",
                "Introduction": "कॉफी (Coffea spp.) दुनिया में सबसे अधिक उपभोग किए जाने वाले पेयों में से एक है, जो अपनी उत्तेजक विशेषताओं और समृद्ध स्वाद के लिए प्रसिद्ध है। यह उष्णकटिबंधीय जलवायु में पनपती है, विशेष रूप से ऊँचाई वाले क्षेत्रों में, जहाँ इसकी वृद्धि के लिए अनुकूल परिस्थितियाँ होती हैं। यह गाइड रोपण से लेकर कटाई तक कॉफी की खेती की पूरी प्रक्रिया को रेखांकित करता है।",
                "Materials Required": "- प्रतिष्ठित नर्सरी से उच्च गुणवत्ता वाले कॉफी के पौधे या बीज\n- नाइट्रोजन, फॉस्फोरस और पोटैशियम से भरपूर संतुलित उर्वरक; जैविक खाद\n- प्रभावी नमी प्रबंधन के लिए ड्रिप सिंचाई प्रणाली या नली\n- कीटनाशक, फफूंदनाशी और जैविक कीट प्रबंधन समाधान\n- रोपण, रखरखाव और कटाई के लिए हाथ के उपकरण (फावड़ा, छंटाई कैंची, कुदाल) या ट्रैक्टर",
                "Soil Preparation": "कॉफी अच्छी जल निकासी वाली, दोमट मिट्टी को पसंद करती है, जिसका pH 6.0 से 6.5 के बीच होना चाहिए। मिट्टी को जोतकर उसमें जैविक पदार्थ मिलाएँ ताकि उपजाऊपन और जल निकासी में सुधार हो।",
                "Plant Selection & Treatment": "अपने जलवायु के अनुसार रोग-प्रतिरोधी कॉफी की किस्में चुनें। यदि बीजों का उपयोग कर रहे हैं, तो रोपण से पहले उन्हें 24 घंटे के लिए भिगोएँ ताकि अंकुरण दर में सुधार हो।",
                "Field Preparation": "रोपण क्षेत्र को खरपतवार, पत्थर और मलबे से साफ करें ताकि एक स्वच्छ वातावरण सुनिश्चित हो।",
                "Planting Time": "कॉफी लगाने का सबसे अच्छा समय बारिश के मौसम की शुरुआत में होता है।",
                "Spacing & Depth": "कॉफी के पौधों को 5-8 फीट की दूरी पर लगाएँ ताकि उचित वृद्धि और वायु संचार सुनिश्चित हो सके। पौधों को इतनी गहराई पर रोपें कि उनकी जड़ गर्दन मिट्टी की सतह के समान रहे।",
                "Seeding/Transplanting Methods": "रोपाई: गड्ढा इतना बड़ा खोदें कि जड़ों के लिए पर्याप्त जगह हो, फिर पौधे को उसमें रखें, हल्के से मिट्टी भरें और रोपण के बाद अच्छी तरह से पानी दें।",
                "Watering Requirements": "छोटे कॉफी के पौधों को नियमित रूप से पानी दें ताकि जड़ें स्थापित हो सकें, विशेष रूप से शुष्क मौसम में। परिपक्व पौधों को लगातार नमी की आवश्यकता होती है लेकिन जलभराव नहीं होना चाहिए।",
                "Nutrient Management": "वृद्धि के मौसम में हर 3-4 महीने में संतुलित उर्वरक लगाएँ। जैविक खाद का उपयोग करके मिट्टी की उपजाऊपन में सुधार करें।",
                "Weed Control": "मल्चिंग से खरपतवारों को नियंत्रित करें, जिससे नमी बनाए रखने और खरपतवार वृद्धि को दबाने में मदद मिलती है। साथ ही, प्रतिस्पर्धा को कम करने के लिए समय-समय पर खरपतवार निकालें।",
                "Pest & Disease Management": "कॉफी बोरर बीटल और लीफ रस्ट जैसे कीटों की निगरानी करें। जड़ सड़न और पत्ती के धब्बे जैसी बीमारियों का उचित स्वच्छता और रोग-प्रतिरोधी किस्मों के माध्यम से प्रबंधन करें। एकीकृत कीट प्रबंधन (IPM) रणनीतियों को लागू करें, जिसमें सांस्कृतिक नियंत्रण और लाभकारी कीटों का उपयोग शामिल हो।",
                "Special Care During Growth": "- अंकुर अवस्था: युवा पौधों को चरम मौसम और कीटों से बचाएँ। यदि आवश्यक हो तो तेज धूप से बचाने के लिए छायादार कपड़े का उपयोग करें।\n- वनस्पति वृद्धि अवस्था: नियमित रूप से पोषक तत्वों की कमी की जांच करें और उन्हें तुरंत ठीक करें। पौधों को आकार देने और मृत या रोगग्रस्त शाखाओं को हटाने के लिए छँटाई करें।\n- फूल और फल विकास अवस्था: फूल और फल बनने के दौरान पर्याप्त पानी की आपूर्ति सुनिश्चित करें ताकि उपज और गुणवत्ता में सुधार हो सके। फलों पर मक्खियों के संक्रमण की निगरानी करें और आवश्यकतानुसार नियंत्रण करें।",
                "Harvesting": "कॉफी चेरी फूल आने के 7-9 महीने बाद कटाई के लिए तैयार होती हैं, जो किस्म पर निर्भर करती है। कटाई के संकेतों में चेरी का रंग हरे से चमकदार लाल या पीले में बदलना शामिल है। कॉफी चेरी को हाथ से चुनें, केवल पकी हुई चेरी ही तोड़ें। उच्च गुणवत्ता के लिए चयनात्मक कटाई विधि अपनाएँ।",
                "Post-Harvest Management": "कटे हुए चेरी को धीरे से संभालें ताकि चोट लगने से बचा जा सके। खराब होने से रोकने के लिए उन्हें यथाशीघ्र प्रोसेस करें।",
                "Processing Methods": "कॉफी बीज निकालने के लिए या तो सूखी विधि (सूरज में चेरी सुखाना) या गीली विधि (किण्वन और धोने की प्रक्रिया) का उपयोग करें।",
                "Storage Conditions": "प्रसंस्करण किए गए कॉफी बीजों को ठंडी, शुष्क जगह पर संग्रहीत करें ताकि खराबी से बचा जा सके और स्वाद बरकरार रहे।",
                "Processing & Packaging": "कॉफी बीजों को एयरटाइट कंटेनरों में पैक करें ताकि भंडारण और परिवहन के दौरान उनकी ताजगी बनी रहे।",
                "Challenges & Solutions": "आम चुनौतियों में कीट और रोगों की संवेदनशीलता, पर्यावरणीय तनाव (जैसे सूखा या पाला), और बाजार मूल्य में उतार-चढ़ाव शामिल हैं। रोग-प्रतिरोधी किस्मों का चयन करें, अच्छे कृषि अभ्यासों को लागू करें, और इन चुनौतियों को कम करने के लिए पर्यावरणीय परिस्थितियों की निगरानी करें।"
            }

        ]
    
    # # Dropdown to select crop
    # selected_crop = st.selectbox("Select a crop to view details:", [crop["name"] for crop in cropGuide])

    # # Display selected crop details
    # crop_details = next((crop for crop in cropGuide if crop["name"] == selected_crop), None)

    # if crop_details:
    #     st.subheader(f"{selected_crop} Cultivation Details")
    #     for index, (key, value) in enumerate(crop_details.items()):
    #         if key != "name":
    #                 st.markdown(f"**{key}:** {value}")

    language = st.selectbox("भाषा चुनें | Select Language:", ["English", "हिन्दी"])
        
        # Select crop guide based on language choice
    selected_guide = cropGuide if language == "English" else cropGuideHindi

        # Dropdown to select crop
    selected_crop = st.selectbox("Select a crop to view details:", [crop["name"] for crop in selected_guide])

        # Display selected crop details
    crop_details = next((crop for crop in selected_guide if crop["name"] == selected_crop), None)

    if crop_details:
            st.subheader(f"{selected_crop} Cultivation Details")
            for key, value in crop_details.items():
                if key != "name":
                    st.markdown(f"**{key}:** {value}")


