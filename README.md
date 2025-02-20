**installation Guide**

1. Clone the Repository
Ensure Git is installed, then run:

sh
Copy
Edit
git clone ***

2. Navigate to the Project Directory
sh
Copy
Edit
cd YOUR_REPOSITORY_NAME
3. Install Node.js and npm
This project requires Node.js and npm.

Check if Node.js is installed:

sh
Copy
Edit
node -v
If not installed, download and install it from Node.js official website.

Check if npm is installed:

sh
Copy
Edit
npm -v
If npm is not recognized, reinstall Node.js.

4. Install Dependencies
Run the following command inside the project directory:

sh
Copy
Edit
npm install
If you encounter issues with package-lock.json, try:

sh
Copy
Edit
rm package-lock.json
npm install
For Windows, use del package-lock.json instead of rm.

5. Start the Development Server
Run the following command:

sh
Copy
Edit
npm start
The application should now be available in your browser at:

http://localhost:3000

Project Structure
/public – Contains static assets such as images and icons.
/src – Main source code, including React components, styles, and scripts.
package.json – Manages dependencies and project scripts.
.gitignore – Specifies files to exclude from version control.
Troubleshooting



some common errors we had running the app:

npm command not recognized
Restart your terminal or reinstall Node.js.

Missing dependencies or module errors
Delete node_modules and reinstall:

sh
Copy
Edit
rm -rf node_modules
npm install
Permission issues when running scripts on Windows
Run the following command in PowerShell:

sh
Copy
Edit
Set-ExecutionPolicy Unrestricted -Scope CurrentUser
