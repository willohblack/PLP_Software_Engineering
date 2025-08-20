-- Project: Library Management System
-- File: library_db.sql
-- Description: A relational database to manage books, members, loans, and authors in a library

-- ========================================
-- 1. DATABASE CREATION
-- ========================================
CREATE DATABASE IF NOT EXISTS LibraryDB;
USE LibraryDB;

-- ========================================
-- 2. TABLES CREATION
-- ========================================

-- Table: Members
CREATE TABLE Members (
    memberID INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    joinDate DATE NOT NULL DEFAULT CURRENT_DATE
);

-- Table: Authors
CREATE TABLE Authors (
    authorID INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    birthDate DATE
);

-- Table: Books
CREATE TABLE Books (
    bookID INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    genre VARCHAR(50),
    publishYear YEAR,
    totalCopies INT NOT NULL DEFAULT 1,
    UNIQUE(title, publishYear) -- ensures no duplicate title for the same year
);

-- Table: BookAuthors (many-to-many relationship between Books and Authors)
CREATE TABLE BookAuthors (
    bookID INT NOT NULL,
    authorID INT NOT NULL,
    PRIMARY KEY(bookID, authorID),
    FOREIGN KEY(bookID) REFERENCES Books(bookID) ON DELETE CASCADE,
    FOREIGN KEY(authorID) REFERENCES Authors(authorID) ON DELETE CASCADE
);

-- Table: Loans
CREATE TABLE Loans (
    loanID INT AUTO_INCREMENT PRIMARY KEY,
    memberID INT NOT NULL,
    bookID INT NOT NULL,
    loanDate DATE NOT NULL DEFAULT CURRENT_DATE,
    returnDate DATE,
    status ENUM('On Loan', 'Returned', 'Late') DEFAULT 'On Loan',
    FOREIGN KEY(memberID) REFERENCES Members(memberID) ON DELETE CASCADE,
    FOREIGN KEY(bookID) REFERENCES Books(bookID) ON DELETE CASCADE
);

-- Table: Librarians (1-to-1 relationship with Members who are staff)
CREATE TABLE Librarians (
    librarianID INT PRIMARY KEY,
    hireDate DATE NOT NULL,
    FOREIGN KEY(librarianID) REFERENCES Members(memberID)
);

-- ========================================
-- 3. SAMPLE DATA (Optional for testing)
-- ========================================
INSERT INTO Members (firstName, lastName, email, phone)
VALUES ('John', 'Doe', 'johndoe@example.com', '123-456-7890'),
       ('Jane', 'Smith', 'janesmith@example.com', '234-567-8901');

INSERT INTO Authors (firstName, lastName, birthDate)
VALUES ('George', 'Orwell', '1903-06-25'),
       ('J.K.', 'Rowling', '1965-07-31');

INSERT INTO Books (title, genre, publishYear, totalCopies)
VALUES ('1984', 'Dystopian', 1949, 5),
       ('Harry Potter and the Sorcerer''s Stone', 'Fantasy', 1997, 10);

INSERT INTO BookAuthors (bookID, authorID)
VALUES (1, 1), (2, 2);

INSERT INTO Loans (memberID, bookID, loanDate, status)
VALUES (1, 1, '2025-08-20', 'On Loan');
