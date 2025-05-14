This is a full-stack assessment application that displays dummy project information. It includes a Python backend and a React (Vite) frontend. MySQL is used as the database.

---

## 📁 Project Structure

- **Backend**: Python FastAPI (Pipenv)
- **Frontend**: React + Vite
- **Database**: MySQL

---

## 🚀 Getting Started

### 🔄 Clone the Repository

```bash
git clone https://github.com/your-username/everest_group_assessment.git
cd everest_group_assessment
```

##Backend setup

1. You need Python 3.7+ on your machine.
2. Run pip install pipenv
3. Run pipenv install (It will install all the required packages and will create a virtual environment for you)
4. Create a .env file with the following content
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_NAME=your_db
6. Execute the start_dev_server.bat file to start the server
7. Your server should now be running at http://localhost:8000
8. You can navigate to http://localhost:8000/docs to access the Swagger

## FrontEnd setup
1. Go to the client directory in the CMD
2. Run command 'npm i'
3. Run command 'npm run dev'
4. You should be able to see the app running at http://localhost:5173

!important
You need mysql server setup on your local with a table named 'projects' in your DB.
   
