from ctypes.util import find_library

from cffi import FFI
from refract.contrib.apielements import ParseResult, registry
from refract.json import JSONDeserialiser
from semantic_version import Version

drafter4_typedefs = """
typedef enum {
    DRAFTER_SERIALIZE_YAML = 0,
    DRAFTER_SERIALIZE_JSON
} drafter_format;

typedef struct {
    bool requireBlueprintName;
} drafter_parse_options;

typedef struct {
    bool sourcemap;
    drafter_format format;
} drafter_serialize_options;

typedef enum
{
    DRAFTER_OK = 0,
    DRAFTER_EUNKNOWN = -1,
    DRAFTER_EINVALID_INPUT = -2,
    DRAFTER_EINVALID_OUTPUT = -3,
} drafter_error;

drafter_error drafter_parse_blueprint_to(const char* source,
    char** out,
    const drafter_parse_options parse_opts,
    const drafter_serialize_options serialize_opts);
"""

drafter5_typedefs = """
typedef enum
{
    DRAFTER_OK = 0,
    DRAFTER_EUNKNOWN = -1,
    DRAFTER_EINVALID_INPUT = -2,
    DRAFTER_EINVALID_OUTPUT = -3,
} drafter_error;

typedef struct drafter_parse_options drafter_parse_options;
typedef struct drafter_serialize_options drafter_serialize_options;

drafter_serialize_options* drafter_init_serialize_options();
typedef enum {
    DRAFTER_SERIALIZE_YAML = 0,
    DRAFTER_SERIALIZE_JSON
} drafter_format;
void drafter_set_format(drafter_serialize_options*, drafter_format);
void drafter_set_sourcemaps_included(drafter_serialize_options*);
void drafter_free_serialize_options(drafter_serialize_options*);

drafter_error drafter_parse_blueprint_to(const char* source,
    char** out,
    const drafter_parse_options* parse_opts,
    const drafter_serialize_options* serialize_opts);
"""


class Draughtsman:
    def __init__(self, library_path=None):
        self.ffi = FFI()
        self.ffi.cdef("const char* drafter_version_string(void);")
        if not library_path:
            library_path = find_library("drafter")
        self.drafter = self.ffi.dlopen(library_path)
        self.drafter_version = self.get_drafter_version()
        if self.drafter_version.major == 4:
            self.ffi.cdef(drafter4_typedefs)
            self.parse = self.parse_drafter4
        elif self.drafter_version.major == 5:
            self.ffi.cdef(drafter5_typedefs)
            self.parse = self.parse_drafter5
        else:
            raise ImportError(
                "Unsupported version of drafter (found {}), django-apiblueprint-view "
                "requires drafter >=4.0.0,<6".format(self.drafter_version)
            )

    def get_drafter_version(self):
        output = self.drafter.drafter_version_string()
        string = self.ffi.string(output).decode("utf-8")
        return Version(string.replace("v", ""))

    def parse_drafter4(
        self, blueprint: str, generate_source_map: bool = False
    ) -> ParseResult:
        source = self.ffi.new("char []", blueprint.encode("utf-8"))
        output = self.ffi.new("char **")

        parse_options = self.ffi.new("drafter_parse_options *", [False])
        serialize_options = self.ffi.new(
            "drafter_serialize_options *", [generate_source_map, 1]
        )

        result = self.drafter.drafter_parse_blueprint_to(
            source, output, parse_options[0], serialize_options[0]
        )

        if result != 0:
            raise Exception("Unknown Error")

        string = self.ffi.string(output[0]).decode("utf-8")

        deserialiser = JSONDeserialiser(registry=registry)
        return deserialiser.deserialise(string)

    def parse_drafter5(
        self, blueprint: str, generate_source_map: bool = False
    ) -> ParseResult:
        source = self.ffi.new("char []", blueprint.encode("utf-8"))
        output = self.ffi.new("char **")

        serialize_options = self.drafter.drafter_init_serialize_options()
        self.drafter.drafter_set_format(serialize_options, 1)

        if generate_source_map:
            self.drafter.drafter_set_sourcemaps_included(serialize_options)

        try:
            result = self.drafter.drafter_parse_blueprint_to(
                source, output, self.ffi.NULL, serialize_options
            )
        finally:
            self.drafter.drafter_free_serialize_options(serialize_options)

        if result != 0:
            raise Exception("Unknown Error")

        string = self.ffi.string(output[0]).decode("utf-8")

        deserialiser = JSONDeserialiser(registry=registry)
        return deserialiser.deserialise(string)
