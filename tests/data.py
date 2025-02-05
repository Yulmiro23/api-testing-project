POZ_DATA = [
    {
        "text": "mem with cat",
        "url": "https://surl.li/mkporg",
        "tags": ["cat", "angry", "lol"],
        "info": {"objects": "cat", "colors": "#6a5edb"}
    }
]

NEG_DATA = [
    {
        "text": 676767867,
        "url": "https://surl.li/mkporg",
        "tags": ["cat", "angry", "lol"],
        "info": {"objects": "cat", "colors": "#6a5edb"}
    },
    {
        "text": "mem with cat",
        "url": ["https://surl.li/mkporg"],
        "tags": ["cat", "angry", "lol"],
        "info": {"objects": "cat", "colors": "#6a5edb"}
    },
    {
        "text": "mem with cat",
        "url": "https://surl.li/mkporg",
        "tags": "cat, angry, lol",
        "info": {"objects": "cat", "colors": "#6a5edb"}
    },
    {
        "text": "mem with cat",
        "url": "https://surl.li/mkporg",
        "tags": ["cat", "angry", "lol"],
        "info": ["objects", "cat", "colors", "#6a5edb"]
    }
]

MISSING_DATA = [
    {
        "url": "https://surl.li/mkporg",
        "tags": ["cat", "angry", "lol"],
        "info": {"objects": "cat", "colors": "#6a5edb"}
    },
    {
        "text": "mem with cat",
        "tags": ["cat", "angry", "lol"],
        "info": {"objects": "cat", "colors": "#6a5edb"}
    },
    {
        "text": "mem with cat",
        "url": "https://surl.li/mkporg",
        "info": {"objects": "cat", "colors": "#6a5edb"}
    },
    {
        "text": "mem with cat",
        "url": "https://surl.li/mkporg",
        "tags": ["cat", "angry", "lol"]
    }
]

PUT_DATA = [
    {
        "id": None,
        "text": "mem with cat",
        "url": "https://surl.li/mkporg",
        "tags": ["cat", "angry", "lol"],
        "info": {"objects": "dog", "colors": "orange"}
    }
]

NO_ID = [
    {
        "text": "mem with cat",
        "url": "https://surl.li/mkporg",
        "tags": ["cat", "angry", "lol"],
        "info": {"objects": "dog", "colors": "orange"}
    }
]

NEG_DATA_2 = [
    {
        "id": None,
        "text": 1234,
        "url": ["cat", "angry", "lol"],
        "tags": "https://surl.li/mkporg",
        "info": {"objects": "dog", "colors": "orange"}
    }
]
