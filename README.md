# OOP Examples in Python

This project demonstrates the use of **Object-Oriented Programming (OOP)** concepts in Python, including:

- **Classes & Objects**
- **Inheritance**
- **Polymorphism (method overriding)**

There are two example files:

---

## 1. `smartphone.py`

This file defines a **base class** `Smartphone` and a **derived class** `GamingPhone`.

### Features:
- **Smartphone class**
  - Stores brand, model, and storage.
  - Can make calls (`call()` method).
  - Displays phone info (`info()` method).

- **GamingPhone class** (inherits from `Smartphone`)
  - Adds an extra attribute `gpu`.
  - Can play games (`play_game()` method).
  - Overrides the `info()` method to include GPU details (**polymorphism**).

### Example Usage:
```python
phone1 = Smartphone("Samsung", "Galaxy S24", 256)
phone2 = GamingPhone("Asus", "ROG Phone 8", 512, "Adreno 740")

phone1.info()           # Displays Smartphone info
phone1.call("0722334455")

phone2.info()           # Displays Gaming Phone info (with GPU)
phone2.play_game("Call of Duty") 

---


