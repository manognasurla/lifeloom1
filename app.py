import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load passive and active mental wellness dataset (simulated)
df = pd.read_csv("1- mental-illnesses-prevalence.csv")
df = df.rename(columns={
    df.columns[3]: "Schizophrenia",
    df.columns[4]: "Depression",
    df.columns[5]: "Anxiety",
    df.columns[6]: "Bipolar",
    df.columns[7]: "Eating_Disorder"
})
df["Most_Prevalent_Disorder"] = df[["Schizophrenia", "Depression", "Anxiety", "Bipolar", "Eating_Disorder"]].idxmax(axis=1)
df["Lifeloom_Risk_Score"] = df[["Schizophrenia", "Depression", "Anxiety", "Bipolar", "Eating_Disorder"]].sum(axis=1)

# Encode countries
le = LabelEncoder()
df["Entity_Code"] = le.fit_transform(df["Entity"])

# Train model to predict mental health risk score
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(df[["Entity_Code", "Year"]], df["Lifeloom_Risk_Score"])

# Streamlit UI
st.set_page_config(page_title="Lifeloom - AI-Powered Mental Wellness Platform", layout="wide")
st.title("🌿 LifeLoom – AI-Powered Mental Wellness Platform")
st.markdown("""
LifeLoom analyzes passive data (like **sleep**, **steps**, **screen time**, **typing patterns**) and active inputs 
like **mood check-ins**, **journals**, and **voice notes** to detect early signs of **stress**, **anxiety**, or **depression**.

It delivers:
- 🎯 Personal Risk Score
- 🙌 Tailored Interventions (Gratitude Nudges, CBT Tips)
- 🤖 24/7 Empathetic AI Chatbot
- 📊 Anonymized Dashboards for Schools & Organizations

All while **safeguarding privacy**.
""")

# User Inputs (Simulated Country/Year Context)
country = st.selectbox("Select Your Region", sorted(df["Entity"].unique()))
year = st.slider("Select Year", int(df["Year"].min()), int(df["Year"].max()), 2020)

encoded_country = le.transform([country])[0]
input_df = pd.DataFrame([[encoded_country, year]], columns=["Entity_Code", "Year"])
predicted_score = model.predict(input_df)[0]

st.metric("🧠 Your AI-Predicted Mental Wellness Risk Score", f"{predicted_score:.2f}")

row = df[(df["Entity"] == country) & (df["Year"] == year)]
if not row.empty:
    prevalent = row.iloc[0]["Most_Prevalent_Disorder"]
    st.markdown(f"**Top Risk Indicator for {country} ({year}):** `{prevalent}`")
else:
    st.warning("No data available for the selected context.")

# Visualization of Passive Data Trends (Simulated)
st.subheader("📊 Simulated Trends in Passive Data (Sleep, Screen Time, Mood)")
plot_df = df[df["Entity"] == country]

fig, ax = plt.subplots(figsize=(10, 5))
for disorder in ["Schizophrenia", "Depression", "Anxiety", "Bipolar", "Eating_Disorder"]:
    ax.plot(plot_df["Year"], plot_df[disorder], label=disorder)
ax.set_title(f"Passive Indicator Trends in {country}")
ax.set_xlabel("Year")
ax.set_ylabel("% of Population Affected")
ax.legend()
st.pyplot(fig)

# Personalized CBT Suggestions
st.subheader("💡 Personalized Well-being Suggestion")
tips = {
    "Depression": "📝 Practice gratitude journaling daily.",
    "Anxiety": "🧘 Use 4-7-8 breathing for calming your nervous system.",
    "Schizophrenia": "📅 Stick to routines and reduce digital overload.",
    "Bipolar": "📈 Track mood with a daily log app.",
    "Eating_Disorder": "🍽️ Try mindful meals and daily affirmations."
}
if not row.empty:
    tip = tips.get(prevalent, "🧠 Maintain a healthy sleep, screen, and journaling routine.")
    st.info(tip)

# Empathetic AI Chatbot Placeholder
st.subheader("🤖 Need to Talk? Meet Your 24/7 AI Companion")
st.markdown("Chatbot feature coming soon. You'll be able to talk freely, and it will listen empathetically.")

# Organizational Dashboard Placeholder
st.subheader("🏫 Organization / School Dashboard (Anonymized Insights)")
st.markdown("Schools and workplaces can use anonymized risk data to create timely interventions.")

st.markdown("---")
st.caption("Developed with ❤️ by Manogna | LifeLoom 2025 – AI for Mental Wellness")
