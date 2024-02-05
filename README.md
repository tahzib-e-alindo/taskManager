# taskManager
Assessment Project Using Django


## Setup
1. Clone the repository (`https://github.com/tahzib-e-alindo/taskManager.git` ) or Download
2. open cmd in taskManager Folder
3. Go to Project directory using `cd taskmanager`
4. Install dependencies using `pip install -r requirements.txt`
5. Create a `.env` file and set your environment variables

    1. `touch .env` 

    2. Add Lines into .env - 
        
        ```
        # Database settings
        DB_NAME=yourdatabase
        DB_USER=yourdatabaseuser
        DB_PASSWORD=yourpassword
        DB_HOST=localhost
        DB_PORT=5432
        
        # Secret Key
        SECRET_KEY=yoursecretkey
        ```
6. Set up PostgreSQL database configuration

## Running the Project
cmd - `python manage.py runserver`


## API Endpoints

### 1. `/api/tasks/`

- **GET:** Retrieve a list of all tasks.
  - Example: `GET /api/tasks/`

- **POST:** Create a new task.
  - Example: `POST /api/tasks/`
  - Request Body:
    ```json
    {
        "id": 1,
        "image": "imageFile",
        "title": "title",
        "description": "Description",
        "due_date": "DueDate",
        "priority": "Priority Low=1, Medium=2, High=3",
        "status": "complete or incomplete",
        "created": "creationDate",
        "updated": "UpdateDate",
        "user": 1
    }
    ```

### 2. `/api/tasks/<task_id>/`

- **GET:** Retrieve details of a specific task.
  - Example: `GET /api/tasks/1/`

- **PUT:** Update details of a specific task.
  - Example: `PUT /api/tasks/1/`
  - Request Body:
    ```json
        "id": 1,
        "image": "imageFile",
        "title": "title",
        "description": "Description",
        "due_date": "DueDate",
        "priority": "Priority Low=1, Medium=2, High=3",
        "status": "complete or incomplete",
        "created": "creationDate",
        "updated": "UpdateDate",
        "user": 1
    ```
- **DELETE:** Delete a specific task.
  - Example: `DELETE /api/tasks/1/`
