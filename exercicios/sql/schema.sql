-- Fictional insurance brokerage domain: submission -> quote -> policy -> claim.
-- Deterministic seed: the expected results in the challenges depend on these numbers.

CREATE TABLE clients (
    id      INTEGER PRIMARY KEY,
    name    TEXT NOT NULL,
    country TEXT NOT NULL
);

CREATE TABLE carriers (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE submissions (
    id           INTEGER PRIMARY KEY,
    client_id    INTEGER NOT NULL REFERENCES clients(id),
    carrier_id   INTEGER NOT NULL REFERENCES carriers(id),
    submitted_at TEXT NOT NULL,
    status       TEXT NOT NULL CHECK (status IN ('bound', 'declined', 'pending'))
);

CREATE TABLE quotes (
    id            INTEGER PRIMARY KEY,
    submission_id INTEGER NOT NULL REFERENCES submissions(id),
    premium_usd   INTEGER NOT NULL,
    quoted_at     TEXT NOT NULL
);

CREATE TABLE policies (
    id             INTEGER PRIMARY KEY,
    submission_id  INTEGER NOT NULL REFERENCES submissions(id),
    effective_date TEXT NOT NULL,
    premium_usd    INTEGER NOT NULL
);

CREATE TABLE claims (
    id          INTEGER PRIMARY KEY,
    policy_id   INTEGER NOT NULL REFERENCES policies(id),
    reported_at TEXT NOT NULL,
    amount_usd  INTEGER NOT NULL,
    status      TEXT NOT NULL CHECK (status IN ('open', 'closed'))
);

INSERT INTO clients (id, name, country) VALUES
    (1, 'Cliente Alfa',      'BR'),
    (2, 'Cliente Beta', 'BR'),
    (3, 'Cliente Gama',   'BR'),
    (4, 'Cliente Delta',    'BR'),
    (5, 'Cliente Epsilon',    'BR'),
    (6, 'Cliente Zeta',     'BR');

INSERT INTO carriers (id, name) VALUES
    (1, 'Seguradora Alfa'),
    (2, 'Seguradora Beta'),
    (3, 'Seguradora Gama'),
    (4, 'Seguradora Delta');

INSERT INTO submissions (id, client_id, carrier_id, submitted_at, status) VALUES
    (1,  1, 1, '2026-01-15', 'bound'),
    (2,  1, 2, '2026-01-20', 'declined'),
    (3,  2, 1, '2026-02-03', 'bound'),
    (4,  2, 3, '2026-02-05', 'pending'),
    (5,  3, 1, '2026-02-18', 'declined'),
    (6,  3, 2, '2026-03-01', 'bound'),
    (7,  4, 1, '2026-03-11', 'bound'),
    (8,  4, 4, '2026-03-14', 'pending'),
    (9,  5, 2, '2026-04-02', 'bound'),
    (10, 5, 3, '2026-04-09', 'declined'),
    (11, 6, 1, '2026-04-21', 'pending'),
    (12, 6, 2, '2026-05-05', 'bound'),
    (13, 1, 3, '2026-05-12', 'bound'),
    (14, 2, 2, '2026-05-30', 'declined'),
    (15, 3, 3, '2026-06-08', 'bound'),
    (16, 4, 2, '2026-06-15', 'declined'),
    (17, 5, 1, '2026-06-25', 'bound'),
    (18, 6, 4, '2026-07-01', 'declined'),
    (19, 1, 1, '2025-11-10', 'bound'),
    (20, 2, 4, '2025-12-02', 'pending');

INSERT INTO quotes (id, submission_id, premium_usd, quoted_at) VALUES
    (1,  1,  120000, '2026-01-18'),
    (2,  2,   98000, '2026-01-22'),
    (3,  3,  250000, '2026-02-06'),
    (4,  4,  180000, '2026-02-10'),
    (5,  5,   75000, '2026-02-20'),
    (6,  6,   82000, '2026-03-04'),
    (7,  7,  140000, '2026-03-15'),
    (8,  8,  160000, '2026-03-18'),
    (9,  9,   90000, '2026-04-05'),
    (10, 10, 110000, '2026-04-12'),
    (11, 11, 133000, '2026-04-25'),
    (12, 12, 101000, '2026-05-08'),
    (13, 13, 127000, '2026-05-15'),
    (14, 15,  88000, '2026-06-12'),
    (15, 17, 210000, '2026-06-28'),
    (16, 19, 115000, '2025-11-14');

INSERT INTO policies (id, submission_id, effective_date, premium_usd) VALUES
    (1,  1,  '2026-02-01', 120000),
    (2,  3,  '2026-03-01', 250000),
    (3,  6,  '2026-03-15',  82000),
    (4,  7,  '2026-04-01', 140000),
    (5,  9,  '2026-04-15',  90000),
    (6,  12, '2026-05-20', 101000),
    (7,  13, '2026-06-01', 127000),
    (8,  15, '2026-07-01',  88000),
    (9,  17, '2026-07-10', 210000),
    (10, 19, '2025-12-01', 115000);

INSERT INTO claims (id, policy_id, reported_at, amount_usd, status) VALUES
    (1, 1,  '2026-03-10', 35000, 'open'),
    (2, 1,  '2026-05-02', 12000, 'closed'),
    (3, 2,  '2026-04-20', 80000, 'closed'),
    (4, 4,  '2026-06-01',  5000, 'open'),
    (5, 7,  '2026-07-05', 22000, 'open'),
    (6, 10, '2026-01-15', 40000, 'closed'),
    (7, 1,  '2026-06-18',  9000, 'closed');
