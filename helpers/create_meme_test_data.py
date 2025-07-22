from endpoints.meme.models.meme_enumerators import Tags

POSITIVE_DATA = [
    {
        "text": "test",
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": [Tags.lol],
        "info": {"test": "test"}
    },
    {
        "text": "",
        "url": "",
        "tags": [Tags.lol],
        "info": {"test": "test"}
    },
    {
        "text": "test 123 !@##$%^&*()_-+= тест 漢字",
        "url": "123",
        "tags": [Tags.lol, Tags.cringe],
        "info": {"test": {"test": "test"}}
    }
]

NEGATIVE_DATA = [
    {
        "text": None,
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": ["test"],
        "info": {"test": "test"}
    },
    {
        "text": "test",
        "url": None,
        "tags": ["test"],
        "info": {"test": "test"}
    },
    {
        "text": "test",
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": None,
        "info": {"test": "test"}
    },
    {
        "text": "test",
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": ["test"],
        "info": None
    },
    {
        "text": None,
        "url": None,
        "tags": None,
        "info": None
    },
    {
        "text": True,
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": ["test"],
        "info": {"test": "test"}
    },
    {
        "text": "test",
        "url": ["https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png"],
        "tags": ["test"],
        "info": {"test": "test"}
    },
    {
        "text": "test",
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": "test",
        "info": {"test": "test"}
    },
    {
        "text": "test",
        "url": "https://miro.medium.com/v2/resize:fit:1400/1*GI-td9gs8D5OKZd19mAOqA.png",
        "tags": ["test"],
        "info": "test"
    },
    {
        "text": 123,
        "url": True,
        "tags": {"test": "test"},
        "info": [123, "test"]
    }
]
