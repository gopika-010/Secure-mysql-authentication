# Secure-mysql-authentication
A Python-based secure MySQL authentication utility using Fernet encryption for password protection and safe database connectivity.


**Project Description:**

This project demonstrates a secure and production-friendly approach to handling database passwords in Python applications.
It includes:

● Password encryption using Fernet (symmetric encryption)

● Safe decryption at runtime with protection against accidental leaks (print/log masking)

● Actual MySQL database connection using the decrypted password

● Clean modular code organization for real-world project structure


**Tech Stack:**

●Language: Python 3

●Database: MySQL

●Libraries: 
    ● cryptography - for encryption and decryption
    ● mysql-connector-python - to connect to MySQL from python

●Libraries:

○cryptography – for encryption and decryption

mysql-connector-python – to connect to MySQL from Python
