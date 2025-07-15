# 🔍 Blockchain Anomaly Detection – Splunk App for Monitoring Unconfirmed Transactions

As part of our Data Mining with Splunk course, we developed two custom **Splunk apps** to analyze unconfirmed Bitcoin transactions from the **blockchain.com** network. These apps visualize suspicious transaction patterns and help identify high-risk addresses and unusual activity using real-time data streams.

---

## 🎯 Objective

To design and deploy Splunk apps that ingest live blockchain transaction data and:
- Visualize transactional trends and address behavior
- Detect anomalies such as high-frequency microtransactions
- Enable pattern analysis for fraud or bot-like activity

---

## 🛠️ Tools & Technologies

- **Splunk Enterprise** – Custom app creation, dashboards, and alerting
- **Splunk Search Processing Language (SPL)** – Advanced queries
- **Blockchain.com API** – Real-time feed of unconfirmed transactions
- **HTTP Event Collector (HEC)** – For data ingestion
- **Custom Dashboards** – Using Trellis layout, timecharts, stats panels

---

## 📦 Splunk Apps Created

### 1. **📊 Market Analysis App**
- Visualizes overall transaction frequency and volume
- Shows distribution of transaction value over time
- Identifies spikes in average BTC per transaction

### 2. **📈 Investment Performance App**
- Tracks most active sending/receiving addresses
- Analyzes BTC flow by wallet ID
- Highlights unusual activity clusters among address groups

📂 *Both dashboards are available as PDF exports in the `/reports/` folder.*

---

## 🔍 Key Findings

- Top sender address recorded **993 transactions** with repetitive patterns
- Receiver clusters with **100+ interactions** from multiple sources
- Transaction surges aligned with suspected bot windows
- High-volume microtransaction trends suggesting potential testing or laundering

---

## 👨‍💻 My Contributions

- Developed and deployed both custom Splunk apps
- Configured the ingestion pipeline via HEC for real-time transaction tracking
- Designed visual dashboards using SPL and Trellis layouts
- Interpreted address-level behavioral trends to assess anomaly potential



