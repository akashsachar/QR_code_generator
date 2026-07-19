import io

import qrcode
import streamlit as st

# Configure the page title and layout for a cleaner app appearance.
st.set_page_config(page_title="QR Code Generator", page_icon="📱", layout="centered")

# Sidebar content with a short app description.
st.sidebar.title("QR Code Generator")
st.sidebar.write("Convert any text or link into a scannable QR code.")

# Main page title and short instruction.
st.title("QR Code Generator")
st.write("Enter any text or URL below and generate a QR code.")

# Text input where the user can enter data.
user_input = st.text_input(
    "Enter text or URL",
    placeholder="Example: https://www.example.com",
)

# Generate button.
if st.button("Generate QR Code"):
    # Basic input validation.
    if not user_input.strip():
        st.warning("Please enter some text or a URL before generating the QR code.")
    else:
        # Create a QR code object with simple settings.
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )

        # Add the user's input to the QR code.
        qr.add_data(user_input)
        qr.make(fit=True)

        # Create the image.
        image = qr.make_image(fill_color="black", back_color="white")

        # Convert the QR image to PNG bytes for display.
        display_bytes = io.BytesIO()
        image.save(display_bytes, format="PNG")
        display_bytes.seek(0)

        # Display the generated QR code on the page.
        st.image(display_bytes.getvalue(), caption="Generated QR Code", width=300)

        # Let the user choose the download format.
        download_format = st.selectbox("Download as", ["PNG", "JPEG"])

        # Convert the image to bytes for downloading.
        download_bytes = io.BytesIO()
        if download_format == "PNG":
            image.save(download_bytes, format="PNG")
            mime_type = "image/png"
            file_name = "qrcode.png"
        else:
            image.save(download_bytes, format="JPEG")
            mime_type = "image/jpeg"
            file_name = "qrcode.jpg"

        download_bytes.seek(0)

        # Download button to save the QR code.
        st.download_button(
            label=f"Download as {download_format}",
            data=download_bytes.getvalue(),
            file_name=file_name,
            mime=mime_type,
        )
