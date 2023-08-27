# Fund Management System Documentation

Backend For Fund Management System using Django.

## 1. Libraries and Frameworks

- Django
- Django Rest Framework (DRF)
- PostgreSQL

## 2. How to Run the Project

- Clone the repository from GitHub.
- Create a virtual environment and install project dependencies
- Configure the PostgreSQL database settings in settings.py.
- Run migrations using python manage.py migrate.
- Start the development server with python manage.py runserver.
- Access the API at http://127.0.0.1:8000/api/.

## 3. API Endpoints

### List All Funds:

- Endpoint: /api/funds/
- Method: GET
- Description: Retrieve a list of all investment funds.

Here is the request and response:
![Fund Lists](Fund_Lists.png)

### Retrieve Fund by ID:

- Endpoint: /api/funds/<fund_id>/
- Method: GET
- Description: Retrieve details of a specific investment fund by its ID.

Here is the request and response:
![Fund Lists](Fund_Info.png)

### Create Fund:

- Endpoint: /api/funds/create/
- Method: POST
- Description: Create a new investment fund.

Here is the request and response:
![Fund Lists](Fund_Create.png)

### Update Fund:

- Endpoint: /api/funds/update/<fund_id>/
- Method: PUT
- Description: Update details of a specific investment fund by its ID.

Here is the request and response:
![Fund Lists](Fund_Update.png)

### Delete Fund:

- Endpoint: /api/funds/delete/<fund_id>/
- Method: DELETE
- Description: Delete a specific investment fund by its ID.

Here is the request and response:
![Fund Lists](Fund_Delete.png)

## 4. SQL Database Schema

The Fund Management System utilizes a PostgreSQL database to store investment fund data. Below is an overview the table:

### Table: InvestmentFund

The `InvestmentFund` table serves as the core entity to store information about investment funds.

| Column            | Data Type | Description                              |
| ----------------- | --------- | ---------------------------------------- |
| `id`              | Integer   | Unique identifier for each fund.         |
| `name`            | Text      | Name of the investment fund.             |
| `manager_name`    | Text      | Name of the fund manager.                |
| `description`     | Text      | Description of the fund's objectives.    |
| `net_asset_value` | Decimal   | Current net asset value of the fund.     |
| `creation_date`   | Date      | Date of fund creation.                   |
| `performance`     | Decimal   | Performance of the fund as a percentage. |

![InvestmentFund table](DB_Sample.png)
