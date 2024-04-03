[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14588486&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Online Recipe Book
## CS110 Final Project Spring 2024

## Team Members

- [Replace with your team members]

***

## Project Description

The Online Recipe Book is a web-based application where users can search, save, and share recipes. It allows users to browse through a vast collection of recipes, filter them based on various criteria such as cuisine type, ingredients, cooking time, etc. Users can also save their favorite recipes to their profile for quick access and share recipes with friends via social media platforms.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. User registration and authentication system.
2. Browse and search functionality for recipes.
3. Filter recipes by cuisine type, ingredients, cooking time, etc.
4. Save favorite recipes to user profile.
5. Share recipes via social media platforms.

### Classes

- User: Manages user authentication and profile information.
- Recipe: Represents individual recipes with details such as ingredients, cooking instructions, and image.
- RecipeManager: Handles the retrieval, filtering, and saving of recipes.
- DatabaseConnector: Connects the application to the backend database to store and retrieve user and recipe data.

## ATP

| Step                 | Procedure                                 | Expected Results                      |
|----------------------|-------------------------------------------|---------------------------------------|
|  1                   | Run Application                           | Login/Register page displayed         |
|  2                   | Register new user                         | User registered successfully          |
|  3                   | Login with registered credentials        | User logged in                        |
|  4                   | Search for a recipe                       | List of recipes matching search query |
|  5                   | Filter recipes by cuisine type           | Display recipes of selected cuisine   |
|  6                   | Save a recipe to user profile            | Recipe added to user's favorites      |
|  7                   | Share a recipe via social media          | Recipe shared successfully           |

