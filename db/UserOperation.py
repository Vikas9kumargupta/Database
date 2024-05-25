import sqlite3


def approveUserAccess(id, approved):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE User SET approved = ? WHERE id = ?
    """,
    (approved, id)
    )

    conn.commit()
    conn.close()
    return True

def blockUserAccess(id, blocked):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE User SET  Block = ? WHERE id = ?
    """,
    (blocked, id)
    )

    conn.commit()
    conn.close()
    return True

def levelUpdateUserAccess(id, level):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE User SET  Level = ? WHERE id = ?
    """,
    (level, id)
    )

    conn.commit()
    conn.close()
    return True