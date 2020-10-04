from startup.mongo import MongoDB

SUFFIXES = ["comics", "events", "series", "stories"]
DB = MongoDB(
    host="mongodb://db",
    database_name="marvel",
    collection_name="character_info"
)
