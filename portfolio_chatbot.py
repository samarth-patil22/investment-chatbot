# import streamlit as st
# import requests
# import re
# from ollama import chat

# st.set_page_config(page_title="Portfolio Chatbot (CPU LLaMA)", layout="wide")
# st.title("🤖 Portfolio Chatbot (CPU LLaMA)")

# # -----------------------------
# # Symbol mapping
# # -----------------------------
# SYMBOL_MAP = {
#     "btc": "bitcoin",
#     "bitcoin": "bitcoin",
#     "eth": "ethereum",
#     "ethereum": "ethereum",
#     "gold": "gold",
#     "xau": "gold"
# }

# # -----------------------------
# # Fetch live prices
# # -----------------------------
# def fetch_price(symbol):
#     cg = SYMBOL_MAP.get(symbol.lower())
#     if not cg:
#         return None
#     if cg == "gold":
#         try:
#             r = requests.get("https://data-asg.goldprice.org/dbXRates/USD")
#             return float(r.json()["items"][0]["xauPrice"])
#         except:
#             return 2000.0
#     else:
#         try:
#             r = requests.get(
#                 f"https://api.coingecko.com/api/v3/simple/price?ids={cg}&vs_currencies=usd",
#                 timeout=10
#             )
#             return float(r.json().get(cg, {}).get("usd", 0.0))
#         except:
#             return 0.0

# # -----------------------------
# # Rule-based suggestion
# # -----------------------------
# def get_suggestion(pl_pct):
#     if pl_pct >= 10:
#         return "Consider selling some to take profit."
#     elif pl_pct <= -15:
#         return "Consider buying more (dollar-cost averaging)."
#     elif pl_pct < -5:
#         return "Hold and re-evaluate."
#     else:
#         return "Hold."

# # -----------------------------
# # Parse user input
# # -----------------------------
# def parse_input(text):
#     """
#     Parses input like:
#     'I bought 0.1 BTC at $103000'
#     Returns: symbol, entry_price, amount
#     """
#     symbol_match = re.search(r"(btc|bitcoin|eth|ethereum|gold|xau)", text, re.IGNORECASE)
#     symbol = symbol_match.group(1).lower() if symbol_match else None

#     numbers = [float(x) for x in re.findall(r"\$?([\d,]+\.?\d*)", text.replace(",", ""))]

#     if len(numbers) >= 2:
#         amount = min(numbers)
#         entry_price = max(numbers)
#     elif len(numbers) == 1:
#         amount = 1
#         entry_price = numbers[0]
#     else:
#         amount = entry_price = None

#     return symbol, entry_price, amount

# # -----------------------------
# # Streamlit UI
# # -----------------------------
# st.subheader("Ask about your investment")
# user_input = st.text_input("Enter your investment question:")

# if st.button("Ask Bot") and user_input:
#     symbol, entry_price, amount = parse_input(user_input)

#     if not symbol or not entry_price or not amount:
#         st.warning("Could not parse your input. Please specify symbol, entry price, and quantity.")
#     else:
#         current_price = fetch_price(symbol)
#         cost = entry_price * amount
#         current_value = current_price * amount
#         pl_abs = current_value - cost
#         pl_pct = (pl_abs / cost * 100) if cost != 0 else 0
#         suggestion = get_suggestion(pl_pct)

#         # -----------------------------
#         # Build prompt for LLaMA
#         # -----------------------------
#         prompt = (
#             f"User's investment P/L: ${pl_abs:.2f} ({pl_pct:.2f}%). "
#             f"Current price: ${current_price:.2f}. "
#             f"Suggestion: {suggestion}. "
#             f"Write a single concise friendly sentence including P/L, current price, and suggestion. "
#             f"Do not include amount or entry price."
#         )

#         try:
#             messages = [
#                 {"role": "system", "content": "You are a helpful portfolio assistant."},
#                 {"role": "user", "content": prompt}
#             ]
#             response = chat(model="llama2", messages=messages)
#             st.subheader("🤖 Bot Answer")
#             st.write(response.message.content)  # Display only the assistant's message
#         except Exception as e:
#             st.error(f"Error using Ollama LLaMA: {e}")
import streamlit as st
import requests
import re
from ollama import chat

st.set_page_config(page_title="Portfolio Chatbot (CPU LLaMA)", layout="wide")
st.title("🤖 Portfolio Chatbot (CPU LLaMA)")

# -----------------------------
# Symbol mapping
# -----------------------------
SYMBOL_MAP = {
    "btc": "bitcoin",
    "bitcoin": "bitcoin",
    "eth": "ethereum",
    "ethereum": "ethereum",
    "gold": "gold",
    "xau": "gold"
}

# -----------------------------
# Fetch live prices
# -----------------------------
def fetch_price(symbol):
    cg = SYMBOL_MAP.get(symbol.lower())
    if not cg:
        return None
    if cg == "gold":
        try:
            r = requests.get("https://data-asg.goldprice.org/dbXRates/USD")
            return float(r.json()["items"][0]["xauPrice"])
        except:
            return 2000.0
    else:
        try:
            r = requests.get(
                f"https://api.coingecko.com/api/v3/simple/price?ids={cg}&vs_currencies=usd",
                timeout=10
            )
            return float(r.json().get(cg, {}).get("usd", 0.0))
        except:
            return 0.0

# -----------------------------
# Rule-based suggestion
# -----------------------------
def get_suggestion(pl_pct):
    if pl_pct >= 10:
        return "Consider selling some to take profit. 🤑"
    elif pl_pct <= -15:
        return "Consider buying more (dollar-cost averaging). 🛒"
    elif pl_pct < -5:
        return "Hold and re-evaluate. 🤔"
    else:
        return "Hold. 👍"

# -----------------------------
# Parse user input
# -----------------------------
def parse_input(text):
    symbol_match = re.search(r"(btc|bitcoin|eth|ethereum|gold|xau)", text, re.IGNORECASE)
    symbol = symbol_match.group(1).lower() if symbol_match else None

    numbers = [float(x) for x in re.findall(r"\$?([\d,]+\.?\d*)", text.replace(",", ""))]

    if len(numbers) >= 2:
        amount = min(numbers)
        entry_price = max(numbers)
    elif len(numbers) == 1:
        amount = 1
        entry_price = numbers[0]
    else:
        amount = entry_price = None

    return symbol, entry_price, amount

# -----------------------------
# Streamlit UI
# -----------------------------
st.subheader("Ask about your investment")
user_input = st.text_input("Enter your investment question:")

if st.button("Ask Bot") and user_input:
    symbol, entry_price, amount = parse_input(user_input)

    if not symbol or not entry_price or not amount:
        st.warning("Could not parse your input. Please specify symbol, entry price, and quantity.")
    else:
        current_price = fetch_price(symbol)
        cost = entry_price * amount
        current_value = current_price * amount
        pl_abs = current_value - cost
        pl_pct = (pl_abs / cost * 100) if cost != 0 else 0
        suggestion = get_suggestion(pl_pct)

        # -----------------------------
        # Build profit/loss text dynamically
        # -----------------------------
        if pl_abs > 0:
            pl_text = f"a profit of {pl_abs:,.2f} USD (+{pl_pct:.2f}%)"
        elif pl_abs < 0:
            pl_text = f"a loss of {abs(pl_abs):,.2f} USD ({pl_pct:.2f}%)"
        else:
            pl_text = "no profit or loss (break-even)"

        # -----------------------------
        # Build prompt for LLaMA with emojis
        # -----------------------------
        prompt = (
            f"You bought {amount} units of {symbol.upper()} at {entry_price:,.2f} USD each. "
            f"The current price is {current_price:,.2f} USD. "
            f"Your investment currently has {pl_text}. "
            f"Suggested action: {suggestion}. "
            f"Write a single friendly, concise sentence including the buying price, current price, size, P/L, and suggestion. Add relevant emojis."
        )

        try:
            messages = [
                {"role":"system","content":"You are a helpful portfolio assistant."},
                {"role":"user","content":prompt}
            ]
            response = chat(model="llama2", messages=messages)
            st.subheader("🤖 Bot Answer")
            st.write(response.message.content)  # Friendly sentence with emojis

            # -----------------------------
            # Show structured info below
            # -----------------------------
            st.markdown("### 📊 Investment Summary")
            st.write(f"**Size / Quantity:** {amount}")
            st.write(f"**Buying Price:** {entry_price:,.2f} USD")
            st.write(f"**Current Price:** {current_price:,.2f} USD")
            st.write(f"**Profit / Loss:** {pl_abs:,.2f} USD ({pl_pct:.2f}%)")
            st.write(f"**Suggestion:** {suggestion}")

        except Exception as e:
            st.error(f"Error using Ollama LLaMA: {e}")
