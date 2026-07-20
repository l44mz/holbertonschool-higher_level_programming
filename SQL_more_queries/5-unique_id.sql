-- Create the table unique_id with id INT default 1 unique and name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
