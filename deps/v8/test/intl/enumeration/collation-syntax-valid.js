// Copyright 2021 the V8 project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Flags: --harmony_intl_enumeration

// Test the return items of collation fit 'type'
let regex = /^[a-zA-Z0-9]{3,8}(-[a-zA-Z0-9]{3,8})*$/;
Intl.supportedValuesOf("collation").forEach(
    function(collation) {
      assertTrue(regex.test(collation),
          "Intl.supportedValuesOf('collation') return " + collation +
          " which does not meet 'type: alphanum{3,8}(sep alphanum{3,8})*'");
    });
