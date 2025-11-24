# Student Performance Analytics System

## Overview

The Student Performance Analytics System is a comprehensive Python-based application designed to help educational institutions manage, analyze, and predict student performance. The system provides powerful analytics tools for tracking grades, identifying trends, generating insights, and creating detailed performance reports.

## Features

### Core Functionality
- **Student Data Management**: Add, update, delete, and search student records
- **Grade Tracking**: Record and manage grades across multiple subjects and assessment types
- **Performance Analytics**: Calculate averages, trends, and statistical insights
- **Grade Prediction**: Forecast future performance based on historical data
- **Report Generation**: Create detailed PDF and CSV reports
- **Data Visualization**: Generate charts and graphs for visual analysis
- **Attendance Integration**: Track and correlate attendance with performance

### Key Modules

1. **main.py** - Application entry point with interactive menu system
2. **student_manager.py** - Student CRUD operations and data management
3. **grade_calculator.py** - Grade calculations, GPA computation, and letter grade assignment
4. **data_handler.py** - File I/O operations for CSV/JSON data persistence
5. **statistics_engine.py** - Statistical analysis including mean, median, standard deviation
6. **predictor.py** - Performance prediction using trend analysis algorithms
7. **report_generator.py** - PDF and CSV report creation with formatting
8. **visualization.py** - Chart generation for performance visualization
9. **config.py** - Centralized configuration and constants management

## Technologies Used

- **Python 3.8+**
- **CSV Module**: Data storage and retrieval
- **JSON Module**: Configuration and structured data handling  
- **Statistics Module**: Built-in statistical calculations
- **Datetime Module**: Timestamp and date management
- **OS Module**: File system operations
- **Logging Module**: Application activity tracking

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/vedant25bce10505/student-performance-analytics.git
cd student-performance-analytics
```

2. Create necessary directories (auto-created on first run):
```bash
mkdir -p data reports logs
```

3. Run the application:
```bash
python main.py
```

## Usage

### Starting the Application

```bash
python main.py
```

The application will present an interactive menu:

```
========================================
Student Performance Analytics System
========================================
1. Add New Student
2. View Student Records
3. Update Student Information
4. Record Grades
5. Calculate Performance Metrics
6. Generate Prediction Report
7. Create Performance Visualization
8. Export Data
9. Settings
0. Exit
========================================
```

### Example Workflows

#### Adding a Student
1. Select option 1 from the main menu
2. Enter student details (ID, name, email, course)
3. System confirms successful addition

#### Recording Grades
1. Select option 4 from the main menu
2. Enter student ID
3. Select subject
4. Enter assessment type (quiz, midterm, final, assignment)
5. Input score

#### Generating Reports
1. Select option 6 for prediction reports
2. Choose report type (individual or class-wide)
3. System generates and saves report to reports/ directory

## Project Structure

```
student-performance-analytics/
├── main.py                    # Application entry point
├── student_manager.py         # Student data management
├── grade_calculator.py        # Grade calculation logic
├── data_handler.py            # Data I/O operations
├── statistics_engine.py       # Statistical analysis
├── predictor.py               # Performance prediction
├── report_generator.py        # Report creation
├── visualization.py           # Chart and graph generation
├── config.py                  # Configuration settings
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore rules
├── README.md                  # Project documentation
├── statement.md               # Problem statement
├── data/                      # Data storage directory
│   ├── students.csv          # Student records
│   └── grades.csv            # Grade records
├── reports/                   # Generated reports
└── logs/                      # Application logs
```

## Non-Functional Requirements

1. **Performance**: Handles up to 10,000 student records efficiently
2. **Security**: Input validation and error handling throughout
3. **Usability**: Clear menu system with input guidance
4. **Reliability**: Data persistence with backup mechanisms
5. **Maintainability**: Modular code structure with clear documentation
6. **Scalability**: Designed to accommodate growing datasets
7. **Error Handling**: Comprehensive exception handling and logging

## Testing

Run the application with sample data:

```bash
python main.py
# Select option 1 to add test students
# Use sample_data.csv for bulk import testing
```

## Future Enhancements

- Web-based dashboard interface
- Machine learning-based predictions
- Multi-user support with authentication
- Real-time notifications for at-risk students
- Integration with Learning Management Systems
- Mobile application development
- Advanced data visualization with interactive charts

## Contributing

This project was developed as part of Python Essentials 2 course at VIT Bhopal.

## Author

Developed by VIT Bhopal Student  
Course: Python Essentials 2  
Academic Year: 2024-2025

## License

This project is created for educational purposes.

## Acknowledgments

- VIT Bhopal Faculty for guidance
- Python documentation and community
- Course materials and resources
