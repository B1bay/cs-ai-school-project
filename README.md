# Computer Science & Its Benefits in the Modern AI Evolution

An interactive **Computer Science & Artificial Intelligence Educational Web Portal** built in **Python** with **HTTPS (TLS/SSL)** support for a school project presentation.

---

## 🎯 Project Overview

This project explores how core **Computer Science** foundations make the modern **Artificial Intelligence revolution** possible, and demonstrates the real-world benefits of CS + AI across society:

1. **The 4 Pillars of Computer Science Behind AI:**
   - **Algorithms & Complexity:** Graph search, Backpropagation, and Transformer Self-Attention (`O(n log n)` & matrix optimizations).
   - **Computer Architecture:** GPU/TPU parallel tensor processing and high-bandwidth memory hierarchies.
   - **Python & Software Ecosystems:** Human-readable Python code bridging high-performance C++/CUDA libraries.
   - **Cybersecurity & Cryptography:** HTTPS/TLS encryption and privacy-preserving AI APIs.
2. **Real-World Benefits Interactive Explorer:**
   - **Healthcare & Bioinformatics** (Protein folding with AlphaFold, early medical diagnostics)
   - **Personalized Education & Accessibility** (24/7 adaptive STEM tutors, real-time translation)
   - **Climate Science & Clean Energy** (Extreme weather forecasting, smart renewable grids)
   - **Software Engineering & Cybersecurity** (Automated bug detection, real-time threat defense)
3. **Interactive Classroom Lab:**
   - **Live AI Hyperparameter Simulator:** Adjust neural network layers, dataset quality, and GPU cores to simulate accuracy and epoch speed.
   - **Classroom Quiz:** Interactive multiple-choice quiz with instant explanations.
   - **Student Study Portal Registration:** Backed by Python validation (`validate_registration`) that prevents empty submissions and enforces strong credentials.

---

## 🚀 How to Run

### Option 1: Run the Python HTTPS Server (`main.py`)
```powershell
python main.py
```
- Automatically generates a local SSL/TLS certificate (`certs/cert.pem` & `certs/key.pem`) using OpenSSL.
- Serves the application over **HTTPS** at: `https://localhost:8443`

### Option 2: Direct Browser Preview
- Open [`index.html`](./index.html) directly in any modern web browser for instant classroom presentation mode.

---

## 📁 Project Structure

- [`main.py`](./main.py) — Python HTTPS web server (`EducativeAIRequestHandler`), SSL certificate generator (`ensure_https_certificates`), and student registration validator (`validate_registration`).
- [`index.html`](./index.html) — Interactive educational front page with live Python code examples, AI training simulator, quiz, and registration form.
- [`README.md`](./README.md) — Project documentation and presentation guide.
