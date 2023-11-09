# Task Manager Web Application

**Task Manager** is a web application developed using Django, designed to help users effectively manage their tasks and stay organized. It offers a user-friendly interface for creating, updating, and tracking tasks efficiently.

## Key Features

1. **User Registration and Login**
   - The application provides user registration and login functionalities, ensuring secure access to individual task lists.

2. **Dashboard**
   - Upon successful login, users will be directed to their personalized dashboard.
   - The dashboard displays the user's current tasks, sorted by priority or due date.

3. **Task Creation**
   - Authenticated users can add new tasks to their list.
   - They can specify the task title, description, due date, and priority level (e.g., high, medium, low).

4. **Task Filtering and Sorting (Admin only)**
   - Admin can easily filter and sort tasks based on different criteria, such as priority, due date, or completion status.
   - This functionality simplifies task management, especially for users with a large number of tasks.

5. **Task Details and Updates**
   - Clicking on a specific task will lead users to a detailed view of the task.
   - Users can update its details, mark it as complete, or delete it if no longer needed.

6. **Search Functionality**
   - The application includes a search feature, enabling users to find specific tasks by entering keywords.

7. **User Settings (CRUD)**
   - Users have a settings section where they can update their profile information, change passwords, or personalize their preferences.

**Note:** The default admin page is used for admin purposes.

## Getting Started

To run this project locally, follow these steps:

1. Clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/task-manager.git 
```
(or) Download the Project Folder in rar type and Extract it.

1.1. Open VSCode and Open the Project Folder . In VSCode Open Settings.py

Add this things in this settings.py

*In Database - 'default': {'ENGINE': 'django.db.backends.mysql', 'NAME': ' ', 'USER':' ', 'PASSWORD':' ', 'HOST':'<'your localhost'> ', 'PORT':''}
Use Your Database details or use default sqllite3 database

```bash
pip install pymysql
```
#for creating model as Existing Table

2. Install the required dependencies using pip:

```bash
pip install Django
```
and all required pip install.

3. Create a database and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser for admin access:

```bash
python manage.py createsuperuser
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Access the application in your web browser at [http://localhost:8000](http://localhost:8000).
