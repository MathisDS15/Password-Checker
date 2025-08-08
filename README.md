# Password-Checker

Created by Mathis DA SILVA


## Introduction 
I created this project to see if our passwords are strong and safe. So, I develope this project in 3 phases.
The first represent the base of the project. We find all aspects of password: validity, strrength and entropy. The second add a new fonctionality to know if it is pwned. The third is a web application with Flask.
---

## Password Checker Phase 1
This phase is a simple Python script.
It checks if your password is valid (length, characters), calculates its strength and entropy.

**How to use:**

- Run the script 'passwordCheckerPhase1.py' in your terminal.
- Enter your password when prompted.
- The script will show you the validity, strength, and entropy of your password.

## Password Checker Phase 2
This phase adds a check to see if your password has been found in public data breaches ("pwned").
It uses the Have I Been Pwned API.

**How to use:**

- Run the script 'passwordCheckerPhase2.py' in your terminal.
- Enter your password when prompted.
- The script will show you the validity, strength, entropy, and whether your password has been pwned.

## Password Checker Phase 3
This phase is a web application built with Flask.
You can check your password directly in your browser with a simple and accessible interface.

**How to use:**

---

### Ressources

- [Robustness calculation](https://fr.wikipedia.org/wiki/Robustesse_d%27un_mot_de_passe)
- [Entropy calculation](https://auth0.com/blog/defending-against-password-cracking-understanding-the-math/)
- [Python Documentation](https://gihub.com/Asabeneh/30-Days-Of-Python/tree/master)
- [SHA-1 Hashing](https://https://www.geeksforgeeks.org/java/sha-1-hash-in-java/)
- [Flask Documentation](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/26_Day_Python_web/26_python_web.md#folder-structure)
- [Have I Been Pwned API](https://haveibeenpwned.com/API/v3)