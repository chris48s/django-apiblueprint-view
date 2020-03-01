"""
Copyright (c) 2017, Kyle Fuller
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the {organization} nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from cffi import FFI
from refract.json import LegacyJSONDeserialiser
from refract.contrib.apielements import registry, ParseResult

_all_ = ("parse",)


ffi = FFI()
ffi.cdef(
    """
typedef enum {
    DRAFTER_SERIALIZE_YAML = 0,
    DRAFTER_SERIALIZE_JSON
} drafter_format;

typedef struct {
    bool sourcemap;
    drafter_format format;
} drafter_options;

int drafter_parse_blueprint_to(const char* source,
                               char** out, const drafter_options options);
"""
)


class Draughtsman:
    def __init__(self, library_path="drafter"):
        self.drafter = ffi.dlopen(library_path)

    def parse(self, blueprint: str) -> ParseResult:
        source = ffi.new("char []", blueprint.encode("utf-8"))
        output = ffi.new("char **")
        options = ffi.new("drafter_options *", [False, 1])
        result = self.drafter.drafter_parse_blueprint_to(source, output, options[0])

        if result != 0:
            raise Exception("Unknown Error")

        string = ffi.string(output[0]).decode("utf-8")
        deserialiser = LegacyJSONDeserialiser(registry=registry)
        return deserialiser.deserialise(string)
