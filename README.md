# AskAI Flask Application

This project is a Flask web application that integrates with OpenAI's API to answer questions. The application saves the questions and answers in a PostgreSQL database. It also includes Docker support for easy setup and deployment, and uses Alembic for database migrations. Testing is done using pytest.

## Features

- **Flask Server**: A web server that handles POST requests to the `/ask` endpoint.
- **OpenAI API Integration**: Sends user questions to OpenAI and returns answers.
- **PostgreSQL Database**: Stores questions and answers.
- **Alembic**: Manages database migrations.
- **Docker**: Containerizes the application and database.
- **Pytest**: Runs tests to ensure the application works as expected.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker and Docker Compose installed on your machine.
- An OpenAI API key. You can get one by signing up on [OpenAI's website](https://beta.openai.com/signup/).

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a `.env` file** in the root directory of the project and add your environment variables:
   ```
   OPENAI_API_KEY=your_openai_api_key
   DATABASE_URL=postgresql://postgres:password@db:5432/postgres
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=password
   POSTGRES_DB=postgres
   ```

3. **Build and run the containers**:
   ```sh
   docker-compose up --build
   ```

## Usage

Once the containers are up and running, you can access the application at `http://localhost:5000`.

- **To ask a question**:
  Send a POST request to `http://localhost:5000/ask` with a JSON body containing the `prompt`:
  ```json
  {
    "prompt": "What is the capital of France?"
  }
  ```

## Running Tests

To run the tests, use the following command:
```sh
docker-compose run test
```

## Project Structure

```
my_flask_app/
├── alembic/               # Alembic migrations
├── app/
│   ├── __init__.py        # App initialization
│   ├── models.py          # Database models
│   ├── repositories.py    # Data access layer
│   ├── routes.py          # API routes
│   └── utils.py           # Utility functions (if any)
├── tests/
│   ├── __init__.py        # Test initialization
│   ├── test_app.py        # Application tests
├── Dockerfile             # Dockerfile for the app
├── Dockerfile.test        # Dockerfile for running tests
├── docker-compose.yml     # Docker Compose configuration
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .env                   # Environment variables
```

## Contributing

If you want to contribute to this project, please fork the repository and create a pull request with your changes. Ensure that your code follows the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [OpenAI](https://openai.com/) for their amazing API.
- [Flask](https://flask.palletsprojects.com/) for being an awesome web framework.
- [Docker](https://www.docker.com/) for containerization.
- [PostgreSQL](https://www.postgresql.org/) for the robust database.
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) for database migrations.
- [Pytest](https://pytest.org/) for testing.