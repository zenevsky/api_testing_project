POSITIVE_DATA = [
    {
        "text": "test",
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": ["test"],
        "info": {"test": "test"}
    },
    {
        "text": "",
        "url": "",
        "tags": ["test"],
        "info": {"test": "test"}
    },
    {
        "text": "test 123 !@##$%^&*()_-+= тест 漢字",
        "url": "123",
        "tags": ["test", 123, True, {"test": "test"}],
        "info": {"test": {"test": "test"}}
    }
]

NEGATIVE_DATA = [
    {
        "id": None,
        "text": "test",
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": ["test"],
        "info": {"test": "test"}
    },
    {
        "id": 999,
        "text": None,
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": ["test"],
        "info": {"test": "test"}
    },
    {
        "id": 999,
        "text": "test",
        "url": None,
        "tags": ["test"],
        "info": {"test": "test"}
    },
    {
        "id": 999,
        "text": "test",
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": None,
        "info": {"test": "test"}
    },
    {
        "id": 999,
        "text": "test",
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": ["test"],
        "info": None
    },
    {
        "id": None,
        "text": None,
        "url": None,
        "tags": None,
        "info": None
    },
    {
        "id": "test",
        "text": "test",
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": ["test"],
        "info": {"test": "test"}
    },
    {
        "id": 999,
        "text": True,
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": ["test"],
        "info": {"test": "test"}
    },
    {
        "id": 999,
        "text": "test",
        "url": ["https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png"],
        "tags": ["test"],
        "info": {"test": "test"}
    },
    {
        "id": 999,
        "text": "test",
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": "test",
        "info": {"test": "test"}
    },
    {
        "id": 999,
        "text": "test",
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": ["test"],
        "info": "test"
    },
    {
        "id": [{"test": "test"}],
        "text": 123,
        "url": True,
        "tags": {"test": "test"},
        "info": [123, "test"]
    }
]
