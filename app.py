import streamlit as st
import numpy as np
import joblib  

# Load the trained model
model = joblib.load("Farm_Irrigation_System.pkl")  

# Sidebar - About the Project
st.sidebar.title("About")
st.sidebar.info("""
This Smart Irrigation System predicts which sprinklers should be ON or OFF based on soil sensor input.

🧠 Built with AI and ML to support precision agriculture  
🌿 Focused on Sustainable Agricultural Practices  
🎓 A project submitted for **AICTE-Shell Edunet Internship Cycle 2**  
👩‍💻 Prepared by **Bhavana Uddanti**
""")

# Main Page
st.title("💧 Smart Sprinkler System")
st.subheader("Enter soil sensor values (0 to 1) to predict sprinkler status")

# Collect sensor inputs
sensor_values = []
for i in range(20):
    val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    sensor_values.append(val)

# Predict button
if st.button("Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("### 🔍 Prediction Results:")
    for i, status in enumerate(prediction):
        st.write(f"🚿 Sprinkler {i} (parcel_{i}): {'ON' if status == 1 else 'OFF'}")

# Footer
st.markdown("---")
