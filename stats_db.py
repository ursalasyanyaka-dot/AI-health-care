import sqlite3

def get_stats():
    conn = sqlite3.connect("queries.db")
    c = conn.cursor()

    # Total queries
    c.execute("SELECT COUNT(*) FROM queries")
    total_queries = c.fetchone()[0]

    # Top 3 symptoms
    c.execute("""
        SELECT symptom, COUNT(*) as count
        FROM queries
        GROUP BY symptom
        ORDER BY count DESC
        LIMIT 3
    """)
    top_symptoms = c.fetchall()

    # Busiest district
    c.execute("""
        SELECT district, COUNT(*) as count
        FROM queries
        GROUP BY district
        ORDER BY count DESC
        LIMIT 1
    """)
    busiest_district = c.fetchone()

    conn.close()

    print("📊 Stats Report")
    print(f"Total queries: {total_queries}")
    print("Top 3 symptoms:")
    for symptom, count in top_symptoms:
        print(f" - {symptom}: {count}")
    if busiest_district:
        print(f"Busiest district: {busiest_district[0]} ({busiest_district[1]} queries)")

if __name__ == "__main__":
    get_stats()
