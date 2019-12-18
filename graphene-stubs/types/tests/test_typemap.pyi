from ..dynamic import Dynamic as Dynamic
from ..enum import Enum as Enum
from ..field import Field as Field
from ..inputfield import InputField as InputField
from ..inputobjecttype import InputObjectType as InputObjectType
from ..interface import Interface as Interface
from ..objecttype import ObjectType as ObjectType
from ..scalars import Int as Int, String as String
from ..structures import List as List, NonNull as NonNull
from ..typemap import TypeMap as TypeMap, resolve_type as resolve_type

def test_enum() -> Any: ...
def test_objecttype() -> Any: ...
def test_dynamic_objecttype() -> Any: ...
def test_interface() -> Any: ...
def test_inputobject() -> Any: ...
def test_objecttype_camelcase() -> None: ...
def test_objecttype_camelcase_disabled() -> None: ...
def test_objecttype_with_possible_types() -> None: ...
def test_resolve_type_with_missing_type() -> Any: ...
