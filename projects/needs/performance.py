parameters = {
    "sphinx": "8.1.3",
    "sphinx_needs": "4.1.0",
    "needs": 10,
    "needtables": 2,
    "dummies": 10,
    "pages": 10,
    "folders": 0,
    "depth": 1
}

info = {
    "#needs": "{{needs * page_amount}}",
    "#needtables": "{{needtables * page_amount}}",
    "#dummies": "{{dummies * page_amount}}",
    '#pages': "{{page_amount}}",
    '#indexes': "{{index_amount}}",
    '#folders': "{{folders ** depth}}"
}
