"""Define the model Attribute."""

from typing import Annotated, Generic, Optional

from pydantic import Field

from sds_core.search.mapping import es_field
from sds_core.types.base import (
    IdentifierTypeT,
    PredicateKeyNameT,
    PredicateKeyTypeT,
    PredicateValueTypeT,
    ProvenanceTypeT,
)
from sds_core.types.rec.base import ProvenanceItem
from sds_core.types.rec.predicate import Predicate
from sds_core.utils.alias import AliasModel


class Attribute(
    AliasModel,
    Generic[
        IdentifierTypeT,
        PredicateValueTypeT,
        PredicateKeyNameT,
        PredicateKeyTypeT,
        ProvenanceTypeT,
    ],
    extra="forbid",
):
    """Attribute model that describes a list of characteristics."""

    conf: Annotated[float, Field(strict=True, ge=0.0, le=1.0, allow_inf_nan=False)] = Field(
        ...,
        title="Confidence",
        description="The confidence level of this attribute characteristics.",
        json_schema_extra=es_field(type="float"),
    )

    prov: Optional[list[ProvenanceItem[IdentifierTypeT, ProvenanceTypeT]]] = Field(
        default=None,
        title="Provenance",
        description="The sources of this attribute characteristics.",
    )

    predicates: list[Predicate[PredicateValueTypeT, PredicateKeyNameT, PredicateKeyTypeT]] = Field(
        ..., description="A list of characteristics (type, value, and name)."
    )
