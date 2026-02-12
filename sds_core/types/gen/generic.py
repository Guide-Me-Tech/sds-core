"""Define a generic Docling type."""

from typing import Optional

from pydantic import Field, StrictStr

from sds_core.search.mapping import es_field
from sds_core.types.base import FileInfoObject
from sds_core.utils.alias import AliasModel


class Generic(AliasModel):
    """A representation of a generic document."""

    name: Optional[StrictStr] = Field(
        default=None,
        description="A short description or summary of the document.",
        alias="_name",
        json_schema_extra=es_field(type="text"),
    )

    file_info: FileInfoObject = Field(
        title="Document information",
        description=("Minimal identification information of the document within a collection."),
        alias="file-info",
    )
