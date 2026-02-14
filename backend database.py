import sqlite3

# Database connection
def get_db():
    conn = sqlite3.connect('network.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create tables and insert mock data
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    # Create devices table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY,
            name TEXT,
            ip TEXT,
            status TEXT,
            threat_level TEXT,
            last_seen TEXT
        )
    ''')
    
    # Create alerts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY,
            device_name TEXT,
            message TEXT,
            severity TEXT,
            timestamp TEXT,
            is_resolved INTEGER
        )
    ''')
    
    # Insert mock devices data
    cursor.execute("SELECT COUNT(*) as count FROM devices")
    if cursor.fetchone()['count'] == 0:
        devices = [
            (1, 'Main Router', '192.168.1.1', 'online', 'low', 'Just now'),
            (2, 'Firewall-01', '192.168.1.100', 'online', 'medium', '2 mins ago'),
            (3, 'Campus DNS', '192.168.1.53', 'under_attack', 'high', 'Just now'),
            (4, 'Database Server', '192.168.1.50', 'offline', 'low', '5 mins ago'),
            (5, 'Web Server', '192.168.1.60', 'online', 'low', '1 min ago')
        ]
        cursor.executemany("INSERT INTO devices VALUES (?,?,?,?,?,?)", devices)
    
    # Insert mock alerts data
    cursor.execute("SELECT COUNT(*) as count FROM alerts")
    if cursor.fetchone()['count'] == 0:
        alerts = [
            (1, 'Campus DNS', '🚨 DDoS Attack Detected!', 'high', '10:32 AM', 0),
            (2, 'Firewall-01', '⚠️ Unauthorized Access Attempt', 'medium', '10:15 AM', 0),
            (3, 'Main Router', 'ℹ️ Configuration Changed', 'low', '09:45 AM', 1),
            (4, 'Database Server', '🚨 Brute Force Attack', 'high', '09:30 AM', 0)
        ]
        cursor.executemany("INSERT INTO alerts VALUES (?,?,?,?,?,?)", alerts)
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")

# Initialize database
if __name__ == "__main__":
    init_db()
