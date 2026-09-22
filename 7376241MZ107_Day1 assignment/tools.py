import ast
import operator as op

from config import EQUIPMENT


# --------------------------------------------------
# TOOL 1: Get equipment price
# --------------------------------------------------

def get_equipment_price(equipment_code):

    equipment_code = equipment_code.upper()

    if equipment_code not in EQUIPMENT:
        return f"Unknown equipment code: {equipment_code}"

    return EQUIPMENT[equipment_code]["price"]


# --------------------------------------------------
# TOOL 2: Get equipment status
# --------------------------------------------------

def get_equipment_status(equipment_code):

    equipment_code = equipment_code.upper()

    if equipment_code not in EQUIPMENT:
        return f"Unknown equipment code: {equipment_code}"

    return EQUIPMENT[equipment_code]["status"]


# --------------------------------------------------
# TOOL 3: Safe calculator
# --------------------------------------------------

OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
}


def calculator(expression):

    try:

        tree = ast.parse(expression, mode="eval")

        def evaluate(node):

            if isinstance(node, ast.Constant):

                if isinstance(node.value, (int, float)):
                    return node.value

            if isinstance(node, ast.BinOp):

                left = evaluate(node.left)
                right = evaluate(node.right)

                operation = OPERATORS.get(type(node.op))

                if operation is None:
                    raise ValueError("Unsupported operator")

                return operation(left, right)

            if isinstance(node, ast.UnaryOp):

                value = evaluate(node.operand)

                if isinstance(node.op, ast.USub):
                    return -value

            raise ValueError("Unsupported expression")

        return evaluate(tree.body)

    except Exception as e:

        return f"Calculator error: {e}"


# --------------------------------------------------
# Tool definitions for the LLM
# --------------------------------------------------

TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "get_equipment_price",
            "description": (
                "Get the private price of a Mechatronics "
                "Lab equipment item."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "equipment_code": {
                        "type": "string",
                        "description": (
                            "Equipment code such as ROB01, "
                            "CNC01, PLC01 or 3DPR01."
                        )
                    }
                },
                "required": ["equipment_code"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_equipment_status",
            "description": (
                "Get the current status of a Mechatronics "
                "Lab equipment item."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "equipment_code": {
                        "type": "string",
                        "description": (
                            "Equipment code such as ROB01, "
                            "CNC01, PLC01 or 3DPR01."
                        )
                    }
                },
                "required": ["equipment_code"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform arithmetic calculations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": (
                            "A mathematical expression such as "
                            "(200000 + 75000) * 0.9"
                        )
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


# --------------------------------------------------
# Map tool names to Python functions
# --------------------------------------------------

TOOL_FUNCTIONS = {
    "get_equipment_price": get_equipment_price,
    "get_equipment_status": get_equipment_status,
    "calculator": calculator
}


# --------------------------------------------------
# Test the tools
# --------------------------------------------------

def main():

    print("=" * 60)
    print("TOOL TEST")
    print("=" * 60)

    print(
        "\nget_equipment_price('ROB01') ->",
        get_equipment_price("ROB01")
    )

    print(
        "get_equipment_status('CNC01') ->",
        get_equipment_status("CNC01")
    )

    print(
        "calculator('(200000 + 75000) * 0.9') ->",
        calculator("(200000 + 75000) * 0.9")
    )


if __name__ == "__main__":
    main()