import streamlit as st
import random

st.set_page_config(page_title="AI Listing Generator", layout="centered")

# 🔝 Header
st.title("🏠 AI Real Estate Listing Generator")
st.markdown("Create professional property listings in seconds — no writing needed.")

st.markdown("---")

# 📥 Input Section
st.subheader("📍 Property Details")

col1, col2 = st.columns(2)

with col1:
    address = st.text_input("Property Address")
    beds = st.number_input("Bedrooms", 0, 10)
    baths = st.number_input("Bathrooms", 0, 10)

with col2:
    sqft = st.number_input("Square Feet", 0)
    tone = st.selectbox("Listing Style", ["Luxury", "Family", "Investment"])

# 🏡 Features
st.markdown("### ✨ Property Features")
garage = st.checkbox("Garage")
yard = st.checkbox("Backyard")
pool = st.checkbox("Pool")
modern_kitchen = st.checkbox("Modern Kitchen")

st.markdown(" ")

# 🚀 Button
generate = st.button("🚀 Generate Listing")

# 📄 Output
if generate:

    # 🔀 AI-style sentence pools
    openings = [
        f"Welcome to {address}, a beautifully designed property that blends comfort and style.",
        f"Discover this exceptional home located at {address}, offering modern living at its finest.",
        f"Step into this stunning residence at {address}, where space and elegance meet."
    ]

    features = [
        f"This {beds}-bedroom, {baths}-bathroom home offers {sqft} sq ft of thoughtfully designed living space.",
        f"Boasting {beds} bedrooms and {baths} bathrooms, this property spans {sqft} sq ft of comfort and functionality.",
        f"Enjoy {sqft} sq ft with {beds} spacious bedrooms and {baths} well-appointed bathrooms."
    ]

    lifestyle = [
        "Perfect for families, entertaining, or simply relaxing in a peaceful environment.",
        "Ideal for both everyday living and hosting guests in style.",
        "Designed to fit a modern lifestyle with comfort and convenience in mind."
    ]

    closing = [
        "Don’t miss this incredible opportunity!",
        "Schedule your showing today!",
        "This property won’t last long on the market!"
    ]

    # 🏡 Feature builder
    extras = []
    if garage:
        extras.append("a spacious garage")
    if yard:
        extras.append("a private backyard")
    if pool:
        extras.append("a beautiful pool")
    if modern_kitchen:
        extras.append("a modern kitchen")

    if extras:
        extra_text = "This home includes " + ", ".join(extras) + "."
    else:
        extra_text = ""

    # 🎯 Tone customization
    if tone == "Luxury":
        tone_line = "Featuring high-end finishes and a refined atmosphere throughout."
    elif tone == "Family":
        tone_line = "A warm and welcoming space perfect for creating lasting memories."
    else:
        tone_line = "A strong investment opportunity with excellent potential."

    # 🧠 Generate listing
    listing = f"""
{random.choice(openings)}

{random.choice(features)}

{tone_line}

{extra_text}

{random.choice(lifestyle)}

{random.choice(closing)}
"""

    # 🏷️ Headline
    headline = f"{beds}BR / {baths}BA Home in {address}"

    # 📤 Display
    st.markdown("---")
    st.subheader(headline)

    st.subheader("📄 Generated Listing")
    st.success(listing)

    # Copy-friendly
    st.code(listing)

    # Download
    st.download_button("📥 Download Listing", listing)