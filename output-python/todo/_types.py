# coding=utf-8


from typing import List, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import models as _models
TodoLabels = Union[str, List[str], "_models.TodoLabelRecord", List["_models.TodoLabelRecord"]]
TodoAttachment = Union["_models.TodoFileAttachment", "_models.TodoUrlAttachment"]
