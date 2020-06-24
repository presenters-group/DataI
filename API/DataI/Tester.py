import json

from DataI.Models.TableModel import TableModel

tableString = '''
{
            "name": "Table1",
            "id": 0,
            "columns": [
                {
                    "name": "السعر",
                    "id": 0,
                    "cells": [
                        {
                            "value": "السعر",
                            "type": "string"
                        },
                        {
                            "value": 10,
                            "type": "numeric"
                        },
                        {
                            "value": 20,
                            "type": "numeric"
                        },
                        {
                            "value": 20,
                            "type": "numeric"
                        },
                        {
                            "value": 20,
                            "type": "numeric"
                        },
                        {
                            "value": 15,
                            "type": "numeric"
                        },
                        {
                            "value": 15,
                            "type": "numeric"
                        },
                        {
                            "value": 10,
                            "type": "numeric"
                        },
                        {
                            "value": 10,
                            "type": "numeric"
                        }
                    ],
                    "style": {
                        "color": "#26C485",
                        "lineWeight": 1.0,
                        "pointWeight": 1.0,
                        "font": "Calibri"
                    },
                    "columnType": "Measures",
                    "valueCategories": [
                        {
                            "value": "السعر",
                            "type": "string"
                        },
                        {
                            "value": 10,
                            "type": "numeric"
                        },
                        {
                            "value": 20,
                            "type": "numeric"
                        },
                        {
                            "value": 15,
                            "type": "numeric"
                        }
                    ],
                    "isDeleted": false
                },
                {
                    "name": "الكمية",
                    "id": 1,
                    "cells": [
                        {
                            "value": "الكمية",
                            "type": "string"
                        },
                        {
                            "value": 40,
                            "type": "numeric"
                        },
                        {
                            "value": 50,
                            "type": "numeric"
                        },
                        {
                            "value": 50,
                            "type": "numeric"
                        },
                        {
                            "value": 50,
                            "type": "numeric"
                        },
                        {
                            "value": 50,
                            "type": "numeric"
                        },
                        {
                            "value": 60,
                            "type": "numeric"
                        },
                        {
                            "value": 50,
                            "type": "numeric"
                        },
                        {
                            "value": 40,
                            "type": "numeric"
                        }
                    ],
                    "style": {
                        "color": "#3066BE",
                        "lineWeight": 1.0,
                        "pointWeight": 1.0,
                        "font": "Calibri"
                    },
                    "columnType": "Measures",
                    "valueCategories": [
                        {
                            "value": "الكمية",
                            "type": "string"
                        },
                        {
                            "value": 40,
                            "type": "numeric"
                        },
                        {
                            "value": 50,
                            "type": "numeric"
                        },
                        {
                            "value": 60,
                            "type": "numeric"
                        }
                    ],
                    "isDeleted": false
                },
                {
                    "name": "النوع",
                    "id": 2,
                    "cells": [
                        {
                            "value": "النوع",
                            "type": "string"
                        },
                        {
                            "value": "Laptop",
                            "type": "string"
                        },
                        {
                            "value": "Laptop",
                            "type": "string"
                        },
                        {
                            "value": "Laptop",
                            "type": "string"
                        },
                        {
                            "value": "Mouse",
                            "type": "string"
                        },
                        {
                            "value": "Mouse",
                            "type": "string"
                        },
                        {
                            "value": "Mouse",
                            "type": "string"
                        },
                        {
                            "value": "Keyboard",
                            "type": "string"
                        },
                        {
                            "value": "Keyboard",
                            "type": "string"
                        }
                    ],
                    "style": {
                        "color": "#DBD56E",
                        "lineWeight": 1.0,
                        "pointWeight": 1.0,
                        "font": "Calibri"
                    },
                    "columnType": "Dimensions",
                    "valueCategories": [
                        {
                            "value": "النوع",
                            "type": "string"
                        },
                        {
                            "value": "Laptop",
                            "type": "string"
                        },
                        {
                            "value": "Mouse",
                            "type": "string"
                        },
                        {
                            "value": "Keyboard",
                            "type": "string"
                        }
                    ],
                    "isDeleted": false
                },
                {
                    "name": "الوزن",
                    "id": 3,
                    "cells": [
                        {
                            "value": "الوزن",
                            "type": "string"
                        },
                        {
                            "value": 10,
                            "type": "string"
                        },
                        {
                            "value": 17,
                            "type": "string"
                        },
                        {
                            "value": 55,
                            "type": "string"
                        },
                        {
                            "value": 39,
                            "type": "string"
                        },
                        {
                            "value": 71,
                            "type": "string"
                        },
                        {
                            "value": 66,
                            "type": "string"
                        },
                        {
                            "value": 55,
                            "type": "string"
                        },
                        {
                            "value": 21,
                            "type": "string"
                        }
                    ],
                    "style": {
                        "color": "#EBD4AE",
                        "lineWeight": 1.5,
                        "pointWeight": 0.0,
                        "font": "Calibri"
                    },
                    "columnType": "Measures",
                    "valueCategories": [
                        {
                            "value": "الوزن",
                            "type": "string"
                        },
                        {
                            "value": 10,
                            "type": "string"
                        },
                        {
                            "value": 17,
                            "type": "string"
                        },
                        {
                            "value": 55,
                            "type": "string"
                        },
                        {
                            "value": 39,
                            "type": "string"
                        },
                        {
                            "value": 71,
                            "type": "string"
                        },
                        {
                            "value": 66,
                            "type": "string"
                        },
                        {
                            "value": 21,
                            "type": "string"
                        }
                    ],
                    "isDeleted": false
                }
            ],
            "columnsVisibility": [
                true,
                true,
                true
            ],
            "rowsVisibility": [
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true,
                true
            ],
            "properties": {
                "sourceFileType": "DataI",
                "zoomValue": 50
            },
            "aggregator": {
                "aggregatedTable": [],
                "aggregationColumn": 0,
                "isActive": false
            },
            "isDeleted": false
        }
'''

table = TableModel.from_json(json.loads(tableString))

print(table)
