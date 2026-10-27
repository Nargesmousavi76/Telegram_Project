# 🎬 Movie Telegram Bot

A Telegram bot built with Python that allows users to search for movies and explore their information using the MoviesAPI.

## 📌 About the Project

This project is a movie information bot developed using Python. It connects to the MoviesAPI to retrieve movie details and provides an interactive interface through Telegram.

Users can search for movies by title, select their preferred movie from the search results, and explore its information directly in the chat.

## ✨ Features

- 🔍 **Movie Search:** Search for movies by name.
- 🎞️ **Multiple Search Results:** Display matching movies as inline buttons.
- 📝 **Movie Details:** View the title, country, director, release year, and IMDb rating.
- 🎭 **Movie Genres:** Display the genres of each movie.
- 🖼️ **Movie Posters:** Show movie posters directly in Telegram.
- 🎲 **Random Movie:** Discover a randomly selected movie.
- ⌨️ **Interactive Menu:** Navigate the bot using Telegram keyboard buttons.
- ⚠️ **Error Handling:** Handle API errors and unsuccessful requests.

## 🛠️ Technologies Used

- Python
- pyTelegramBotAPI (`telebot`)
- Requests
- MoviesAPI
- Telegram Bot API

## 📂 Project Structure

```text
Movie-Telegram-Bot/
│
├── base1.py       # Telegram bot token configuration
├── bot.py         # Main bot application and Telegram handlers
├── bot_api.py     # API requests and movie data processing
└── README.md      # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

Replace `YOUR_REPOSITORY_URL` with your GitHub repository URL.

### 2. Install Dependencies

```bash
pip install pyTelegramBotAPI requests
```

### 3. Configure Your Telegram Bot Token

Create a file named `base1.py` and add your Telegram bot token:

```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

**Important:** Never share your Telegram bot token or upload it to a public repository.

### 4. Run the Bot

Run the following command in your terminal:

```bash
python bot.py
```

Open your bot in Telegram and send `/start` to begin.

## 🔎 How to Use

1. Start the bot using `/start`.
2. Select **Search** to search for a movie by title.
3. Choose a movie from the inline search results.
4. View the movie's information and poster.
5. Select **Popular / Random** to discover a random movie.
6. Select **Help** to access the help option.

## 🌐 API

This project uses [MoviesAPI](https://moviesapi.ir/) to retrieve movie information.

The API provides data such as movie titles, release years, countries, IMDb ratings, genres, and poster URLs.

## 🎯 Project Goals

- Practice working with external APIs using Python.
- Learn how to send HTTP requests using the Requests library.
- Build an interactive Telegram bot using pyTelegramBotAPI.
- Practice functions, dictionaries, lists, loops, and exception handling.
- Work with inline keyboards and callback queries in Telegram.

## 🚀 Future Improvements

- Add movie summaries and language information when supported by the API.
- Improve movie search and filtering.
- Add more movie discovery options.
- Improve error handling and user experience.

## 👩‍💻 Author

Developed as a Python learning project.
