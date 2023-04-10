# Intro to SQL

Tools:

- SQLite3 => C-Language library SQL database engine
- SQLite Browser => Visual User Interface for interacting with sql/sqlite3
- chinook database => Microsoft curated Open source database
- PostgreSQL(elephant)
- MySQL(2) => Library that interacts with db

  NoSQL
- MongoDB (Non-Relational Dbs)

## What is SQL?
  - Structured Query Language
  - language used to communicate with a database (db)
  - Are SQL Only jobs
  - Request / Response Cycle 
      - Req => is in the form of a SQL query (just a string with parameters)
      - Res => The return data that satisfies the query 
  - RELATIONAL DATABASE
    - Each Table can communicate with anotyher
    - We can define a RELATIONSHIP/ASSOCIATION between
  - Single Source of Truth!
    - There is one variable of one item
      - NO DUPLICATES
      - If you need to know how many Users exist in the table, you need to Calc instead of holding onto an extra variable
    - Benifits
      - Accurate Data
        - Not relying on updating all associated vars
      - easier to debug
      - Uses less memory

## Why use SQL databases?
  - Great Tool for large datasets
  - Simple to Use
  - Fast
  - Information can Persist
  - Relational Database

## What is SQL used for?
  - Applicant Tracking System
    - Handling User data
  - Assets in a game


## What kind of operations can we do in SQL?
  - Create (Write, add)
  - Read (select, sort, group...)
  - Update
  - Delete

## What are the Datatypes in SQL/db?
  - TEXT
  - INT (INTEGER)
  - BIGINT
  - FLOAT
  - REAL
  - BLOB => BINARY LARGE OBJECT
  - BOOLEAN
  - CHAR
  - DATE
  - DATETIME
  - TIMESTAMP


## How to make SQL Queries

1. .sql files
2. run sqlite3 terminal
3. run sqlite3 browser

## SQLite3 tips

to run the default sqlite terminal:
sqlite3

to run the sqlite terminal with a database:
sqlite3 <chinook.db>

to run a sql query on a database:
sqlite3 <chinook.db> < <file.sql>

## Relational Databasing

Foriegn Keys => table ids (keys) from the parent (hasmany) table on the current table

## SQL Queries

PRAGMA table_info(table_name); => show columns

1. Write a SQL Query to select all the rows in the artists table
```SQL

```

2. Write a SQL Query to select the artist with the name "Black Sabbath"
```SQL

```

3. Write a SQL Query to create a table named "fans" with an auto-incrementing ID that's a primary key and a name field of type text
```SQL

```


4. Write a SQL Query to alter the fans table to have an artistId column of type integer

```SQL

```

5. Write a SQL Query to add yourself as a fan of the Red Hot Chili Peppers ArtistId **_127_**

```SQL

```

6. Write a SQL Query to change your "name" in the fans table.

```SQL

```

7. Write a SQL Query to return all the fans that not fans of the Black Eyed Peas(169)

```SQL

```

8. Write a SQL Query to display artist name, album name, and number of tracks on that album

```SQL

```

9. Write a SQL Query to return the name of all of the artists in the 'Pop' Genre

```SQL

```
