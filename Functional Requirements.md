System Requirements and Specifications
1. Functional Requirements
>  1.1. User Registration
>  Description: Students must be able to register for an account.
>  Input: Student ID, password, first name, last name, course.
>  Output: Login page.
>  Processing: Verify credentials, create user sessions.
>  Security: Password encryption, session management.
>  1.2. User Login
>  Description: Students must be able to log in using their credentials.
  Input: Student ID, password.
Output: User dashboard.
Processing: Verify credentials, create user sessions.
Security: Password encryption, session management.
1.3. Task Management
Description: Students must be able to add, view, and categorize tasks.
Input: Task details (name, description, deadline, course).
Output: List of tasks with their respective deadlines and course categories.
Processing: Store and retrieve task details from the database.
1.4. Expense Recording
Description: Students must be able to record and view their academic-related expenses.
Input: Expense details (amount, description, date).
Output: List of recorded expenses.
Processing: Store and retrieve expense details from the database.
1.5. Deadline Tracking
Description: Students should be able to view upcoming deadlines for their tasks.
Input: None.
Output: List of tasks with their respective deadlines.
Processing: Retrieve task deadlines and sort by date.
1.6. Logout
Description: Students log out of the system.
Input: None.
Output: Redirect to login page.
Processing: End user session and redirect.
2. Non-functional Requirements
2.1. Performance
•	The system must manage up to 5000 concurrent users. The response time should be less than 2-3 seconds.
2.2. Security
•	Implement authentication and authorization mechanisms to prevent unauthorized access.
2.3. Usability
•	The user interface should be intuitive and easy to navigate.
2.4. Reliability
•	Maintain 99.5% uptime; implement redundancy.
2.5. Maintainability
•	Ensure easy updates with comprehensive documentation and modular design.
2.6. Scalability
•	Implement a scalable architecture; conduct regular testing to maintain performance.
2.7. Environment
•	Operating System: Compatible with Windows, macOS, and Linux.
•	Browser Compatibility: Functional across Chrome, Firefox, Safari.
•	Mobile Responsive: Accessible on iOS and Android devices.
•	Database: MySQL.
•	Development Environment: Use modern tools and frameworks

[Gnatt Chart](Gantt-Chart.xlsx)
[ERD]
[UX/UI]
