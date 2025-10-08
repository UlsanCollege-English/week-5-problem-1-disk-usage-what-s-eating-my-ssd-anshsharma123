def total_size(node):
    """
    Compute total size of a nested file/dir tree.
    node format:
      - file: {"type": "file", "name": str, "size": int}
      - dir:  {"type": "dir", "name": str, "children": [nodes]}
    """
    # Handle None or invalid input
    if node is None or not isinstance(node, dict):
        return 0

    node_type = node.get("type")

    # Base case: file node
    if node_type == "file":
        return node.get("size", 0) or 0  # Default to 0 if missing or None

    # Recursive case: directory node
    elif node_type == "dir":
        total = 0
        for child in node.get("children", []):
            total += total_size(child)
        return total

    # Unknown node type → ignore
    return 0
