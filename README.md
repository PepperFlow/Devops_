# Devops_Project description
Weather Application - DevOps_Project
Project Member
Wuttichai Chueaklang
Project Overview
A modern weather application built for simplicity and ease of use. The application allows users to:

1. Search for weather information by entering a city name.
2. Get real-time weather updates, including temperature, wind speed, humidity, and more.
3. Receive a clear error message if the city is not found.

Description
The application uses the OpenWeatherMap API to collect weather data based on the city name entered by the user. When the application runs, several tests are executed in GitHub Actions to validate the data and ensure the functionality of the code. The application is then containerized using Docker and deployed to Render for public access.

Tests
City-based data validation: Ensures that valid city names return the correct weather data.
Error handling validation: Tests that invalid or missing city names return appropriate error messages.
Syntax and code quality validation: Ensures there are no syntax errors or potential bugs in the code using pytest and flake8.
