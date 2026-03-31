# AI-ML Journey
## Goal : Two years to become an AI-ML Engineer.
This repository tracks my daily Progress , Projects and learning as I work toward Becoming a Professional AI-Ml Engineer. 
---
## Day 1_30 Progress Summary:
I have installed Python on my linux using terminal and for all these thirty days I have wrote programs in terminal so that I should get knowlege of simple commands and become familiar with the terminal 
Pyhton Basics were not completely knew to me so I started from creating small projects like progress tracker , daily task planner , file organizer , Screen time monitor etc. All these were simple and begineer friendly.
The overall streak for phase 1 was 29/30 ( I missed day 4 )
#Day 30 Project : 
On Day 30 a python based performance tracking System 
- saves records in database
- asks used for requirement
- checks records and creates report
- rates performance
   As a begineer and fresher in the industry I would say that's a good start , A lot is cooking yet..
  #Month-02
  Project : 🌤️ Weather App - Complete Weather Information System

A comprehensive Python-based weather application that provides real-time weather data, 3-day forecasts, temperature visualization, and personalized features like favorite cities and search history.
📋 Table of Contents
   - Features
   - Demo
   - Technologies Used
   - Installation
   - How to Use
   - API Reference
   - Project Structure
   - Future Enhancements
   - Acknowledgments
Features :
Core Weather Features :

    ✅ Real-time Weather - Current temperature, feels like, humidity, conditions, and wind speed
    ✅ 3-Day Forecast - Daily high/low temperatures, weather conditions, and rain chance
    ✅ Temperature Dashboard - Visual bar graphs showing temperature trends over 3 days
    ✅ Trend Analysis - Shows whether temperatures are rising, falling, or stable

User Features :

    ✅ Favorite Cities - Save cities you frequently check
    ✅ Remove from Favorites - Manage your favorites list
    ✅ View All Favorites - Quick access to saved cities
    ✅ Search History - Automatically saves last 10 searched cities
    ✅ Error Handling - Friendly messages for invalid cities, no internet, and API errors

Visualization :

    ✅ Text-Based Bar Graphs - Visual representation of temperature trends
    ✅ Temperature Statistics - Min, max, and average temperatures
    ✅ Trend Indicators - Up/Down arrows showing temperature changes
    
🎬 Demo :
text

🌤️ WEATHER APP MENU
===================================
1. Current weather
2. 3-day forecast
3. Add to favorites
4. View favorites
5. Remove from favorites
6. Recent searches
7. Temperature Dashboard
8. Exit

Choose (1-8): 7

📍 Enter city name for dashboard: Lahore

🌡️ TEMPERATURE DASHBOARD - LAHORE
==================================================

📊 Temperature Graph:

03-29:  32°C ████████████████████████████░░░░░░░░ (Sunny)
03-30:  34°C ████████████████████████████████░░░░ (Sunny)
03-31:  31°C ████████████████████████████░░░░░░░░ (Partly cloudy)

==================================================
📈 Max: 34°C  |  📉 Min: 31°C  |  📊 Avg: 32.3°C

📉 Trend:
   Day 1 → Day 2: ↑ +2°C (Getting warmer)
   Day 2 → Day 3: ↓ -3°C (Getting cooler)
==================================================

🛠️ Technologies Used :
Technology	Purpose
Python 3.x	Core programming language
Requests Library	API calls to fetch weather data
WeatherAPI.com	Free weather data provider
SQLite3	Local database for storing favorites
File I/O	Search history persistence

📦 Installation Prerequisites :

    Python 3.6 or higher
    pip package manager
Steps:
1: Clone the repository bash
2: Install required packages bash
3: Get API Key
4: Run the application bash


🚀 How to Use
Main Menu Options
Option	Description
1. Current weather: Get real-time weather for any city
2. 3-day forecast: View detailed 3-day weather forecast
3. Add to favorites: Save a city to your favorites list
4. View favorites: Display all your saved favorite cities
5. Remove from favorites: Delete a city from favorites
6. Recent searches:	View your last 10 searched cities
7. Temperature Dashboard:	Visual bar graph with temperature trends
8. Exit:	Close the application

🔌 API Reference

This project uses WeatherAPI.com endpoints:
Endpoint	Purpose	Parameters
/current.json	Current weather	key, q (city)
/forecast.json	3-day forecast	key, q, days=3
Sample API Response Structure
json



📁 Project Structure
text

Month-2/
├── weather-app.py          # Main weather application
├── favorites.txt           # Saved favorite cities (auto-generated)
├── history.txt             # Search history (auto-generated)
└── README.md              # Project documentation

Key Functions: 
Function	Description:
get_weather(city):	Fetches and displays current weather
show_forecast(city):	Displays 3-day weather forecast
show_dashboard(city):	Shows temperature bar graph and trends
add_to_favorites(city):	Saves city to favorites
view_favorites():	Lists all favorite cities
save_to_history(city):	Saves search to history
load_history():	Loads search history
🔮 Future Enhancements

   -Hourly forecast for next 24 hours
   -Weather alerts and notifications
   -Graphical charts using matplotlib
   -GUI version with Tkinter
   -Multiple cities comparison
   -Weather maps integration
   -Voice search capability
   -Export weather reports to PDF

🙏 Acknowledgments

    WeatherAPI.com for providing free weather data
    Requests library developers for making API calls simple
    Python community for excellent documentation

📝 License

This project is part of my AI/ML learning journey. Feel free to use, modify, and learn from it!

📧 Contact

    GitHub: alithecoder-hue
    LinkedIn: linkedin.com/in/muhammad-ali-tahir-47a634350/
    Email: aleeytahir@gmail.com

📅 Project Status

    Current Version: 1.07
    Last Updated: March 2025
    Status: ✅ Active Development
⭐ If you found this project helpful, please give it a star on GitHub!


