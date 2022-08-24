import utils

_RENAME = "_rename"
_APPLY = "_apply"

# Formatters are responsible for changing fields name and values to match the schema
FORMATTERS = {
    "main": {
        _RENAME: {
            "id": "orderId",
            "time": "checkoutTime",
            "item name": "itemName",
            "item amount (USD)": "itemPrice",
            "item quantity": "itemQuantity",
        },
        _APPLY: {
            "time": utils.format_ymd_time_to_unix
        }
    },
    "accounts": {
        _RENAME: {
            "id": "orderId",
            "orderFullAmount": "amountUSD",
        },
    }
}


def format_headers(formatter, headers):
    if not formatter[_RENAME]:
        return headers
    # format headers, if format not required, return as is
    return list(map(lambda header: formatter[_RENAME][header] if header in formatter[_RENAME] else header, headers))


def format_values(formatter, headers, row):
    if _APPLY in formatter and formatter[_APPLY]:
        for header, function in formatter[_APPLY].items():
            applied_index = headers.index(header)
            row[applied_index] = function(row[applied_index])
