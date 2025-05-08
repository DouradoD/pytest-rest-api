import requests
import jsonschema
from services.mock_service_countries import MockServiceCountries

user_schema = user_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "name": {
                "type": "object",
                "properties": {
                    "common": {"type": "string"},
                    "official": {"type": "string"},
                    "nativeName": {
                        "type": "object",
                        "patternProperties": {
                            "^[a-z]{3}$": {  # Language code (e.g., "por")
                                "type": "object",
                                "properties": {
                                    "official": {"type": "string"},
                                    "common": {"type": "string"}
                                },
                                "required": ["official", "common"]
                            }
                        }
                    }
                },
                "required": ["common", "official"]
            },
            "tld": {
                "type": "array",
                "items": {"type": "string"}
            },
            "cca2": {"type": "string"},
            "ccn3": {"type": "string"},
            "cca3": {"type": "string"},
            "cioc": {"type": "string"},
            "independent": {"type": "boolean"},
            "status": {"type": "string"},
            "unMember": {"type": "boolean"},
            "currencies": {
                "type": "object",
                "patternProperties": {
                    "^[A-Z]{3}$": {  # Currency code (e.g., "BRL")
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "symbol": {"type": "string"}
                        },
                        "required": ["name", "symbol"]
                    }
                }
            },
            "idd": {
                "type": "object",
                "properties": {
                    "root": {"type": "string"},
                    "suffixes": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "required": ["root", "suffixes"]
            },
            "capital": {
                "type": "array",
                "items": {"type": "string"}
            },
            "altSpellings": {
                "type": "array",
                "items": {"type": "string"}
            },
            "region": {"type": "string"},
            "subregion": {"type": "string"},
            "languages": {
                "type": "object",
                "patternProperties": {
                    "^[a-z]{3}$": {"type": "string"}  # Language codes
                }
            },
            "translations": {
                "type": "object",
                "patternProperties": {
                    "^[a-z]{3}$": {  # Language codes (e.g., "ara")
                        "type": "object",
                        "properties": {
                            "official": {"type": "string"},
                            "common": {"type": "string"}
                        },
                        "required": ["official", "common"]
                    }
                }
            },
            "latlng": {
                "type": "array",
                "items": {"type": "number"},
                "minItems": 2,
                "maxItems": 2
            },
            "landlocked": {"type": "boolean"},
            "borders": {
                "type": "array",
                "items": {"type": "string"}
            },
            "area": {"type": "number"},
            "demonyms": {
                "type": "object",
                "properties": {
                    "eng": {
                        "type": "object",
                        "properties": {
                            "f": {"type": "string"},
                            "m": {"type": "string"}
                        },
                        "required": ["f", "m"]
                    },
                    "fra": {
                        "type": "object",
                        "properties": {
                            "f": {"type": "string"},
                            "m": {"type": "string"}
                        },
                        "required": ["f", "m"]
                    }
                }
            },
            "flag": {"type": "string"},
            "maps": {
                "type": "object",
                "properties": {
                    "googleMaps": {"type": "string"},
                    "openStreetMaps": {"type": "string"}
                },
                "required": ["googleMaps", "openStreetMaps"]
            },
            "population": {"type": "integer"},
            "gini": {
                "type": "object",
                "patternProperties": {
                    "^\\d{4}$": {"type": "number"}  # Year (e.g., "2019")
                }
            },
            "fifa": {"type": "string"},
            "car": {
                "type": "object",
                "properties": {
                    "signs": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "side": {"type": "string"}
                },
                "required": ["signs", "side"]
            },
            "timezones": {
                "type": "array",
                "items": {"type": "string"}
            },
            "continents": {
                "type": "array",
                "items": {"type": "string"}
            },
            "flags": {
                "type": "object",
                "properties": {
                    "png": {"type": "string"},
                    "svg": {"type": "string"},
                    "alt": {"type": "string"}
                },
                "required": ["png", "svg", "alt"]
            },
            "coatOfArms": {
                "type": "object",
                "properties": {
                    "png": {"type": "string"},
                    "svg": {"type": "string"}
                },
                "required": ["png", "svg"]
            },
            "startOfWeek": {"type": "string"},
            "capitalInfo": {
                "type": "object",
                "properties": {
                    "latlng": {
                        "type": "array",
                        "items": {"type": "number"},
                        "minItems": 2,
                        "maxItems": 2
                    }
                },
                "required": ["latlng"]
            },
            "postalCode": {
                "type": "object",
                "properties": {
                    "format": {"type": "string"},
                    "regex": {"type": "string"}
                },
                "required": ["format", "regex"]
            }
        },
        "required": [  # Required top-level fields
            "name", "tld", "cca2", "ccn3", "cca3", "independent",
            "unMember", "currencies", "capital", "region", "subregion",
            "languages", "latlng", "landlocked", "area", "demonyms",
            "flag", "maps", "population", "flags", "startOfWeek"
        ]
    }
}

# Real API base URL (not a mock!)
API_BASE_URL = "https://restcountries.com/v3.1"

# Schema to validate the response
user_schema = user_schema

def test_get_country(mocker,country_name='brazil', status_code=200):
    response = MockServiceCountries(base_url=API_BASE_URL).get_mock_country(mocker, endpoint=f'/name/{country_name}')
    assert response.status_code == 200
    
    # Validate schema
    data = response.json()
    jsonschema.validate(data, user_schema)  # Raises exception if invalid
