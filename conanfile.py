
from conans import ConanFile, CMake, tools
from conans.tools import os_info, SystemPackageTool
from pathlib import Path
import os
import shutil


class uwebsocketConan(ConanFile):
    name = "uwebsocket"
    version = "0.14.9"
    license = "Apache 2.0"
    author = "uNetworking"
    url = "https://github.com/kindlychung/uWebSockets"
    description = "High performance WebSockets"
    topics = ("cpp", "network", "sockets")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    requires = ("usockets/0.0.5@jzien/dev", )
    generators = "cmake"
    exports_sources = "src/*"

    def package(self):
        self.copy("*.h", dst="include", src="src", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def imports(self):
        self.copy("*", dst="include", src="include")
        self.copy("*", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["usockets"]
