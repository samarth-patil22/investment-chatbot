# 📊 Investment Assistant Chatbot (BTC, ETH, Gold)  
A simple, fast, privacy-friendly investment analysis chatbot built using **Streamlit**, **Python**, and **Ollama LLaMA** (local LLM).

The bot calculates:
- Profit / Loss in %
- Profit / Loss in USD
- Entry Price, Current Price, Quantity
- Market-based suggestions (Buy / Hold / Sell)
- Clean LLaMA-powered natural-language answer with emojis

---

## 🚀 Features

### ✔ Crypto & Gold Support
- BTC
- ETH
- GOLD

### ✔ Live Price Fetching
- CoinGecko API for crypto  
- GoldPrice.org for gold

### ✔ Local LLM (No Cloud Required)
Uses **Ollama LLaMA** on your device:
- No API keys
- No internet required for LLM
- 100% private and local

### ✔ Automatic Profit/Loss Calculation
The system computes:
- Cost basis  
- Current value  
- P/L amount  
- P/L percentage  
- Smart suggestions  

### ✔ Clean UI
Built with Streamlit:
- Bot Answer  
- Investment Summary  
- Clear formatted values  

---

## 🧠 How It Works (Architecture)
User Input → Parser → Price Fetching → P/L Engine → LLaMA Prompt → Streamlit UI


### Workflow:
1. User asks: “I bought 0.1 BTC at 100000”
2. System detects:
   - Asset = BTC  
   - Quantity = 0.1  
   - Buy price = 100000  
3. Fetches live price (example: 87,019)
4. Calculates:
   - P/L = −1298.1 USD  
   - P/L% = −12.98%  
5. Generates rule-based suggestion
6. Sends structured prompt to LLaMA
7. Streamlit displays bot response + summary

---

## 📦 Installation

### 1️⃣ Clone the repo
```bash
git clone https://github.com/YOUR-USERNAME/investment-chatbot.git
cd investment-chatbot

