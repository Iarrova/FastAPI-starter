from uuid import UUID


class AppException(Exception):
    """Base for all domain exceptions"""

    def __init__(self, detail: str, context: dict | None = None):
        self.detail = detail
        self.context = context or {}


class NotFoundException(AppException):
    def __init__(self, resource: str, identifier: str | UUID):
        super().__init__(
            detail=f"{resource} not found",
            context={"resource": resource, "identifier": str(identifier)},
        )


class ConflictException(AppException):
    def __init__(self, detail: str):
        super().__init__(detail=detail)
