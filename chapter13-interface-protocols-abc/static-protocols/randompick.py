"""
Implementing the Tombola use case but instead of using an ABC we
will use protocols instead
"""

from typing import Protocol, Any, runtime_checkable



"""
Prefer protocols of one method over protocols with multiple methods: in this way, your protocol is more flexible

For more info, read Martin Fowler's article on the subject: https://martinfowler.com/bliki/RoleInterface.html
"""

@runtime_checkable
class RandomPicker(Protocol):
    def pick(self) -> Any: ... # To be changed in later chapter :)
