# Evaluation of ChatGPT Efficiency using MongoDB in an Internet Client-Server Model with FastAPI

## Introduction
This project aims to evaluate the efficiency of OpenAI's ChatGPT using MongoDB in a client-server model implemented with FastAPI. The project consists of several Python scripts that interact with ChatGPT, perform data analysis, and manage a MongoDB database.

## Features
- **ChatGPT Interaction**: Utilizes `chatgpt.py` to interact with ChatGPT, sending queries and receiving responses.
- **Data Analysis**: Analyzes the response data using `analysis.py` for efficiency evaluation.
- **Database Management**: Employs MongoDB for storing and retrieving ChatGPT interaction data using `database.py`.
- **FastAPI Server**: `main.py` sets up a FastAPI server to handle web requests and integrate all components.

## Installation
To set up this project, follow these steps:

1. Install the required Python packages:
   ```shell
   pip install fastapi uvicorn pymongo matplotlib seaborn pandas requests python-dotenv
   ```
2. Set up your MongoDB database and ensure it is running.
3. Add your MongoDB URI and OpenAI API key to your environment variables.

Usage
To run the FastAPI server, execute:
```shell
uvicorn main:app --reload
```
This will start the server, allowing interaction with the ChatGPT model and handling of data analysis and database operations.

## API Endpoints
- `/query-next-unanswered-question:` Fetches and displays the next unanswered question from the database.

## Contributing
Your contributions are welcome! Feel free to fork the repository, make your improvements, and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any queries or suggestions, please reach out to bayolami@outlook.com.


