## =========================================================
## Copyright 2019 Dietrich Bollmann
## 
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
## 
##      http://www.apache.org/licenses/LICENSE-2.0
## 
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
## ---------------------------------------------------------

"""nsl/go/__main__.py:

Entry point of the shell script 'nslgo'.

"""

from nsl.go.__about__ import (
    __package_name__,
    __version__,
    __status__,
    __description__,
    __author__,
    __authors__,
    __maintainer__,
    __email__,
    __contact__,
    __copyright__,
    __url__,
    __license__,
    __date__,
)

## =========================================================
## Entry point of console script 'nslgo'
## ---------------------------------------------------------
 
from nsl.go.scripts.nslgo import cli

## =========================================================
## =========================================================

## fin.
