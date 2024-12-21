## Voter Education App

A web application designed to provide essential voter education, including voter registration guides, election dates, polling locations, and FAQs to help citizens make informed decisions. The app is built using Flask, HTML, CSS, and JavaScript, and aims to simplify the voting process for everyone.

## Features

- Voter Registration Guide: Provides users with state-specific registration information based on their selected state.
- Election Dates and Locations: Displays upcoming election details, including dates and polling locations.
- FAQs and Resources: Includes helpful links and information on how to vote, the meaning of a ballot, and voters' rights.

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- Database: In-memory JSON data (states and registration info)
- APIs: Custom APIs to fetch state data and registration information

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps to Run Locally

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/voter-education-app.git
    cd voter-education-app
    ```

2. Set up the virtual environment(optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:
    ```bash
    python app.py
    ```

5. Open your browser and go to `http://127.0.0.1:5000/` to view the app.

## File Structure

```
voter-education-app/
│
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── static/
│   ├── css/
│   │   └── styles.css        # CSS styles for the frontend
│   └── js/
│       └── script.js         # JavaScript for dynamic data handling
└── templates/
    └── index.html            # HTML structure for the app
```

## Custom Routes

-: Displays the main page of the app.
-: Returns a list of states available for registration.
-: Fetches registration details for the selected state.

## Contributing

Feel free to fork the repository, submit issues, or make pull requests to contribute to the development of this project.

## License

This project is open source and available under the [MIT License](LICENSE).

---

You can replace `your-username` with your actual GitHub username and customize the sections as needed. If you need any more additions or adjustments, let me know!
