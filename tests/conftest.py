from test_code_block_tracker import Scenario


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Scenario) and isinstance(right, list) and op == "==":
        msg = ["Parsed result does not match the expected result:"]
        msg.extend([f"line {i+1:2} | {left.doc[i]:<40} | ans: {str(left.ans[i]):5} | res: {right[i]}" for i in range(len(left))])
        return msg