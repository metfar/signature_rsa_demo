# signature_rsa_demo
Signature RSA Demo

# Simple demonstration of digital signature generation using:

1. A toy hash function: h(x) = (x + 3) mod 10;
2. A simplified RSA scheme:
   - private key d = 11;
   - public key e = 5;
   - modulus n = 14;

The message is x = 2.
The signature is computed as:
    s = h(x)^d mod n;

Verification is done by checking that:
    s^e mod n = h(x);

# License

```
#  Copyright 2018- William Martinez Bas <metfar@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
```
```
                                - oOo -
```
