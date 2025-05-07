# 🔐 Password Strength Checker

A simple, CLI-based Python tool to **evaluate password strength based on entropy**. It analyzes the variety and length of characters in a password and provides feedback and recommendations accordingly.

---

## 🚀 Features

- Calculates password entropy using character pool and length.
- Classifies passwords as:
  - ❌ **Too Weak**
  - ⚠️ **Weak**
  - 🟡 **Decent**
  - ✅ **Strong**
- Offers actionable **recommendations** for improving password strength.
- No internet or external dependencies (other than Python standard library).

---

## 📖 What is Entropy?

Entropy is a measure of unpredictability or randomness. In the context of passwords, higher entropy means it's harder for attackers to guess or brute-force your password.

**Formula used:**
```
Entropy = log2(pool_size) × password_length
```

---

## 💻 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/sinan-ashraf/password-checker.git
cd password-checker
```

### 2. Run the Script

```bash
python password_checker.py
```

> You’ll see a prompt: `Enter password:` — just type in any password to test it.

---

## 📝 Example

```
Enter password: hello123
✗ Weak password (35.4 bits entropy)
Decent, but could be stronger.
```

```
Enter password: @G7vLp#2qR
✓ Strong password (64.2 bits entropy)
Strong password!
```

---

## 🔧 Customization

You can change the minimum acceptable entropy in the code:

```python
MIN_ENTROPY = 30
```

Recommended values:
- 20+: Basic
- 30+: Good
- 40+: Strong

---

## 📂 File Structure

```
password-entropy-checker/
│
├── password_checker.py     # Main password checking script
└── README.md               # Project documentation
```

---

## ✅ Requirements

- Python 3.x


---

## 🛡️ Disclaimer

This is a basic educational tool. It does not check against real-world breached password databases unless you integrate it with one.

---

## 📃 License

MIT License — feel free to use, modify, and distribute.
