DROP TABLE IF EXISTS userAccount;
DROP TABLE IF EXISTS bankAccount;

CREATE TABLE userAccount
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    username    TEXT UNIQUE NOT NULL,
    password    TEXT        NOT NULL,
    firstName   TEXT        NOT NULL,
    lastName    TEXT        NOT NULL,
    SSN         INT         NOT NULL,
    phoneNumber BIGINT      NOT NULL,
    address     TEXT        NOT NULL
);

CREATE TABLE bankAccount
(
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    userAccountId INTEGER        NOT NULL,
    balance       DECIMAL(16, 2) NOT NULL,
    FOREIGN KEY (userAccountId) REFERENCES userAccount (id)
);




