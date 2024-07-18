Tkinter-SQLite Data Entry and Retrieval System
This project allows users to enter and retrieve data using a Python-based GUI built with Tkinter and SQLite. The interface enables data entry and displays the stored data through a simple retrieval process.

Features
Data Entry: Use a Tkinter-based GUI to enter details and store them in an SQLite database.
Data Retrieval: Easily retrieve and view all entered data using a separate script.
SQLite Integration: Utilize SQLite for efficient data storage and management.
Image Support: Handle images with the PIL library and ImageTk module.
Getting Started
Prerequisites
Ensure you have the following installed:

Python: Make sure Python is installed on your system. You can download it from python.org.
VS Code: Download and install Visual Studio Code from code.visualstudio.com.
Important Libraries
Install the necessary Python libraries using pip:
pip install tkinter sqlite3 pillow
Important VS Code Extension
To view the entered data in a more readable format, install the following VS Code extension:

SQLite3 Editor: This extension helps you manage and view your SQLite database files.

SQLite Installation
Follow these steps to install and set up SQLite:

Extract the SQLITE.zip file.
Store the extracted folder in your C: drive.
Open the SQLITE folder and copy its path.
Add this path to your system's environment variables.

Usage
Data Entry
Run the Main.py file to open the data entry GUI.
Enter all required details in the provided fields.
Click "Submit" to save the data and then click "Exit" to close the application.
Main.py Interface
![Main Interface](IMAGE\Main.png)

Data Retrieval
To view all the entered data, run the Data_base_Extract.py file.
The script will display all the stored data.
Data_base_Extract.py Interface
![Data Retrieval Interface](IMAGE\DataR.png)

File Structure
Main.py: The main script for data entry.
Data_base_Extract.py: The script for retrieving and displaying entered data.
SQLITE.zip: SQLite installation files.
Contributing
If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

