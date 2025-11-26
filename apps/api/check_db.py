from sqlalchemy import create_engine, text
from app.core.config import settings

SYNC_DATABASE_URL = settings.DATABASE_URL.replace("postgresql+asyncpg", "postgresql")
print(f"Connecting to: {SYNC_DATABASE_URL}")

try:
    engine = create_engine(SYNC_DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Connection successful:", result.scalar())
        
        # Check tables
        result = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"))
        tables = [row[0] for row in result]
        print("Tables:", tables)
        
        if 'invoices' in tables:
            result = conn.execute(text("SELECT count(*) FROM invoices"))
            print("Invoice count:", result.scalar())
        else:
            print("Table 'invoices' NOT FOUND")
except Exception as e:
    print("Connection failed:", e)
