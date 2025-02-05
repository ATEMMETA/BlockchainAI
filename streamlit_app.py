import streamlit as st
import requests
import json

st.title("Blockchain Interaction")

# FastAPI Backend URL (Important: Use the correct URL)
API_URL = "http://127.0.0.1:8000"  # For local development in the same network

# Input fields
sender_private_key = st.text_input("Sender Private Key (Hex)")
recipient = st.text_input("Recipient Public Key (Hex)")
amount = st.number_input("Amount")

if st.button("Add Transaction"):
    if sender_private_key and recipient and amount:
        try:
            # Send POST request to FastAPI
            headers = {'Content-Type': 'application/json'}  # Set content type
            data = {
                "sender_private_key_hex": sender_private_key,  # Send private key hex
                "recipient": recipient,
                "amount": amount
            }
            response = requests.post(f"{API_URL}/transactions", data=json.dumps(data), headers=headers)  # Send JSON data

            if response.status_code == 200:
                st.success(response.json().get('message', "Transaction added successfully!"))  # Display success message
            else:
                st.error(response.json().get('detail', f"Error: {response.status_code}"))  # Display error message from FastAPI

        except requests.exceptions.RequestException as e:
            st.error(f"Connection error: {e}")
    else:
        st.warning("Please fill in all fields.")

if st.button("Mine Block"):
    miner_public_key = st.text_input("Miner Public Key (Hex)") # Add miner public key field
    if miner_public_key:
        try:
            data = {"miner_public_key_hex": miner_public_key}
            response = requests.post(f"{API_URL}/mine", data=json.dumps(data), headers=headers)
            if response.status_code == 200:
                st.success("Block mined!")
                # Optionally display the new block
                st.write(response.json())
            else:
                st.error(response.json().get('detail', f"Error: {response.status_code}"))
        except requests.exceptions.RequestException as e:
            st.error(f"Connection error: {e}")
    else:
        st.warning("Please enter miner public key.")

# ... (Add more Streamlit components to interact with other API endpoints)

