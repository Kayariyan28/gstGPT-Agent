from contextvars import ContextVar
from typing import Any, Dict, Optional

# Context variable to store the last tool output for the current request
last_tool_output: ContextVar[Optional[Dict[str, Any]]] = ContextVar("last_tool_output", default=None)
