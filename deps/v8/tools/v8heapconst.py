# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  96: "SHARED_STRING_TYPE",
  101: "SHARED_THIN_STRING_TYPE",
  104: "SHARED_ONE_BYTE_STRING_TYPE",
  109: "SHARED_THIN_ONE_BYTE_STRING_TYPE",
  128: "SYMBOL_TYPE",
  129: "BIG_INT_BASE_TYPE",
  130: "HEAP_NUMBER_TYPE",
  131: "ODDBALL_TYPE",
  132: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  133: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  134: "CALLABLE_TASK_TYPE",
  135: "CALLBACK_TASK_TYPE",
  136: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  137: "LOAD_HANDLER_TYPE",
  138: "STORE_HANDLER_TYPE",
  139: "FUNCTION_TEMPLATE_INFO_TYPE",
  140: "OBJECT_TEMPLATE_INFO_TYPE",
  141: "ACCESS_CHECK_INFO_TYPE",
  142: "ACCESSOR_INFO_TYPE",
  143: "ACCESSOR_PAIR_TYPE",
  144: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  145: "ALLOCATION_MEMENTO_TYPE",
  146: "ALLOCATION_SITE_TYPE",
  147: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  148: "ASM_WASM_DATA_TYPE",
  149: "ASYNC_GENERATOR_REQUEST_TYPE",
  150: "BREAK_POINT_TYPE",
  151: "BREAK_POINT_INFO_TYPE",
  152: "CACHED_TEMPLATE_OBJECT_TYPE",
  153: "CALL_HANDLER_INFO_TYPE",
  154: "CALL_SITE_INFO_TYPE",
  155: "CLASS_POSITIONS_TYPE",
  156: "DEBUG_INFO_TYPE",
  157: "ENUM_CACHE_TYPE",
  158: "FEEDBACK_CELL_TYPE",
  159: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  160: "INTERCEPTOR_INFO_TYPE",
  161: "INTERPRETER_DATA_TYPE",
  162: "MODULE_REQUEST_TYPE",
  163: "PROMISE_CAPABILITY_TYPE",
  164: "PROMISE_REACTION_TYPE",
  165: "PROPERTY_DESCRIPTOR_OBJECT_TYPE",
  166: "PROTOTYPE_INFO_TYPE",
  167: "REG_EXP_BOILERPLATE_DESCRIPTION_TYPE",
  168: "SCRIPT_TYPE",
  169: "SCRIPT_OR_MODULE_TYPE",
  170: "SOURCE_TEXT_MODULE_INFO_ENTRY_TYPE",
  171: "STACK_FRAME_INFO_TYPE",
  172: "TEMPLATE_OBJECT_DESCRIPTION_TYPE",
  173: "TUPLE2_TYPE",
  174: "WASM_CONTINUATION_OBJECT_TYPE",
  175: "WASM_EXCEPTION_TAG_TYPE",
  176: "WASM_INDIRECT_FUNCTION_TABLE_TYPE",
  177: "FIXED_ARRAY_TYPE",
  178: "HASH_TABLE_TYPE",
  179: "EPHEMERON_HASH_TABLE_TYPE",
  180: "GLOBAL_DICTIONARY_TYPE",
  181: "NAME_DICTIONARY_TYPE",
  182: "NUMBER_DICTIONARY_TYPE",
  183: "ORDERED_HASH_MAP_TYPE",
  184: "ORDERED_HASH_SET_TYPE",
  185: "ORDERED_NAME_DICTIONARY_TYPE",
  186: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  187: "CLOSURE_FEEDBACK_CELL_ARRAY_TYPE",
  188: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  189: "SCRIPT_CONTEXT_TABLE_TYPE",
  190: "BYTE_ARRAY_TYPE",
  191: "BYTECODE_ARRAY_TYPE",
  192: "FIXED_DOUBLE_ARRAY_TYPE",
  193: "INTERNAL_CLASS_WITH_SMI_ELEMENTS_TYPE",
  194: "SLOPPY_ARGUMENTS_ELEMENTS_TYPE",
  195: "TURBOFAN_BITSET_TYPE_TYPE",
  196: "TURBOFAN_HEAP_CONSTANT_TYPE_TYPE",
  197: "TURBOFAN_OTHER_NUMBER_CONSTANT_TYPE_TYPE",
  198: "TURBOFAN_RANGE_TYPE_TYPE",
  199: "TURBOFAN_UNION_TYPE_TYPE",
  200: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  201: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_AND_JOB_TYPE",
  202: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  203: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_WITH_JOB_TYPE",
  204: "FOREIGN_TYPE",
  205: "WASM_INTERNAL_FUNCTION_TYPE",
  206: "WASM_TYPE_INFO_TYPE",
  207: "AWAIT_CONTEXT_TYPE",
  208: "BLOCK_CONTEXT_TYPE",
  209: "CATCH_CONTEXT_TYPE",
  210: "DEBUG_EVALUATE_CONTEXT_TYPE",
  211: "EVAL_CONTEXT_TYPE",
  212: "FUNCTION_CONTEXT_TYPE",
  213: "MODULE_CONTEXT_TYPE",
  214: "NATIVE_CONTEXT_TYPE",
  215: "SCRIPT_CONTEXT_TYPE",
  216: "WITH_CONTEXT_TYPE",
  217: "WASM_FUNCTION_DATA_TYPE",
  218: "WASM_CAPI_FUNCTION_DATA_TYPE",
  219: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  220: "WASM_JS_FUNCTION_DATA_TYPE",
  221: "EXPORTED_SUB_CLASS_BASE_TYPE",
  222: "EXPORTED_SUB_CLASS_TYPE",
  223: "EXPORTED_SUB_CLASS2_TYPE",
  224: "SMALL_ORDERED_HASH_MAP_TYPE",
  225: "SMALL_ORDERED_HASH_SET_TYPE",
  226: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  227: "ABSTRACT_INTERNAL_CLASS_SUBCLASS1_TYPE",
  228: "ABSTRACT_INTERNAL_CLASS_SUBCLASS2_TYPE",
  229: "DESCRIPTOR_ARRAY_TYPE",
  230: "STRONG_DESCRIPTOR_ARRAY_TYPE",
  231: "SOURCE_TEXT_MODULE_TYPE",
  232: "SYNTHETIC_MODULE_TYPE",
  233: "WEAK_FIXED_ARRAY_TYPE",
  234: "TRANSITION_ARRAY_TYPE",
  235: "CELL_TYPE",
  236: "CODE_TYPE",
  237: "CODE_DATA_CONTAINER_TYPE",
  238: "COVERAGE_INFO_TYPE",
  239: "EMBEDDER_DATA_ARRAY_TYPE",
  240: "FEEDBACK_METADATA_TYPE",
  241: "FEEDBACK_VECTOR_TYPE",
  242: "FILLER_TYPE",
  243: "FREE_SPACE_TYPE",
  244: "INTERNAL_CLASS_TYPE",
  245: "INTERNAL_CLASS_WITH_STRUCT_ELEMENTS_TYPE",
  246: "MAP_TYPE",
  247: "MEGA_DOM_HANDLER_TYPE",
  248: "ON_HEAP_BASIC_BLOCK_PROFILER_DATA_TYPE",
  249: "PREPARSE_DATA_TYPE",
  250: "PROPERTY_ARRAY_TYPE",
  251: "PROPERTY_CELL_TYPE",
  252: "SCOPE_INFO_TYPE",
  253: "SHARED_FUNCTION_INFO_TYPE",
  254: "SMI_BOX_TYPE",
  255: "SMI_PAIR_TYPE",
  256: "SORT_STATE_TYPE",
  257: "SWISS_NAME_DICTIONARY_TYPE",
  258: "WASM_API_FUNCTION_REF_TYPE",
  259: "WEAK_ARRAY_LIST_TYPE",
  260: "WEAK_CELL_TYPE",
  261: "WASM_ARRAY_TYPE",
  262: "WASM_STRUCT_TYPE",
  263: "JS_PROXY_TYPE",
  1057: "JS_OBJECT_TYPE",
  264: "JS_GLOBAL_OBJECT_TYPE",
  265: "JS_GLOBAL_PROXY_TYPE",
  266: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_PRIMITIVE_WRAPPER_TYPE",
  1058: "JS_API_OBJECT_TYPE",
  2058: "JS_LAST_DUMMY_API_OBJECT_TYPE",
  2059: "JS_BOUND_FUNCTION_TYPE",
  2060: "JS_FUNCTION_TYPE",
  2061: "BIGINT64_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2062: "BIGUINT64_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2063: "FLOAT32_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2064: "FLOAT64_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2065: "INT16_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2066: "INT32_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2067: "INT8_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2068: "UINT16_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2069: "UINT32_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2070: "UINT8_CLAMPED_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2071: "UINT8_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2072: "JS_ARRAY_CONSTRUCTOR_TYPE",
  2073: "JS_PROMISE_CONSTRUCTOR_TYPE",
  2074: "JS_REG_EXP_CONSTRUCTOR_TYPE",
  2075: "JS_CLASS_CONSTRUCTOR_TYPE",
  2076: "JS_ARRAY_ITERATOR_PROTOTYPE_TYPE",
  2077: "JS_ITERATOR_PROTOTYPE_TYPE",
  2078: "JS_MAP_ITERATOR_PROTOTYPE_TYPE",
  2079: "JS_OBJECT_PROTOTYPE_TYPE",
  2080: "JS_PROMISE_PROTOTYPE_TYPE",
  2081: "JS_REG_EXP_PROTOTYPE_TYPE",
  2082: "JS_SET_ITERATOR_PROTOTYPE_TYPE",
  2083: "JS_SET_PROTOTYPE_TYPE",
  2084: "JS_STRING_ITERATOR_PROTOTYPE_TYPE",
  2085: "JS_TYPED_ARRAY_PROTOTYPE_TYPE",
  2086: "JS_MAP_KEY_ITERATOR_TYPE",
  2087: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  2088: "JS_MAP_VALUE_ITERATOR_TYPE",
  2089: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  2090: "JS_SET_VALUE_ITERATOR_TYPE",
  2091: "JS_GENERATOR_OBJECT_TYPE",
  2092: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  2093: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  2094: "JS_DATA_VIEW_TYPE",
  2095: "JS_TYPED_ARRAY_TYPE",
  2096: "JS_MAP_TYPE",
  2097: "JS_SET_TYPE",
  2098: "JS_WEAK_MAP_TYPE",
  2099: "JS_WEAK_SET_TYPE",
  2100: "JS_ARGUMENTS_OBJECT_TYPE",
  2101: "JS_ARRAY_TYPE",
  2102: "JS_ARRAY_BUFFER_TYPE",
  2103: "JS_ARRAY_ITERATOR_TYPE",
  2104: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  2105: "JS_COLLATOR_TYPE",
  2106: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  2107: "JS_DATE_TYPE",
  2108: "JS_DATE_TIME_FORMAT_TYPE",
  2109: "JS_DISPLAY_NAMES_TYPE",
  2110: "JS_ERROR_TYPE",
  2111: "JS_FINALIZATION_REGISTRY_TYPE",
  2112: "JS_LIST_FORMAT_TYPE",
  2113: "JS_LOCALE_TYPE",
  2114: "JS_MESSAGE_OBJECT_TYPE",
  2115: "JS_NUMBER_FORMAT_TYPE",
  2116: "JS_PLURAL_RULES_TYPE",
  2117: "JS_PROMISE_TYPE",
  2118: "JS_REG_EXP_TYPE",
  2119: "JS_REG_EXP_STRING_ITERATOR_TYPE",
  2120: "JS_RELATIVE_TIME_FORMAT_TYPE",
  2121: "JS_SEGMENT_ITERATOR_TYPE",
  2122: "JS_SEGMENTER_TYPE",
  2123: "JS_SEGMENTS_TYPE",
  2124: "JS_STRING_ITERATOR_TYPE",
  2125: "JS_TEMPORAL_CALENDAR_TYPE",
  2126: "JS_TEMPORAL_DURATION_TYPE",
  2127: "JS_TEMPORAL_INSTANT_TYPE",
  2128: "JS_TEMPORAL_PLAIN_DATE_TYPE",
  2129: "JS_TEMPORAL_PLAIN_DATE_TIME_TYPE",
  2130: "JS_TEMPORAL_PLAIN_MONTH_DAY_TYPE",
  2131: "JS_TEMPORAL_PLAIN_TIME_TYPE",
  2132: "JS_TEMPORAL_PLAIN_YEAR_MONTH_TYPE",
  2133: "JS_TEMPORAL_TIME_ZONE_TYPE",
  2134: "JS_TEMPORAL_ZONED_DATE_TIME_TYPE",
  2135: "JS_V8_BREAK_ITERATOR_TYPE",
  2136: "JS_WEAK_REF_TYPE",
  2137: "WASM_GLOBAL_OBJECT_TYPE",
  2138: "WASM_INSTANCE_OBJECT_TYPE",
  2139: "WASM_MEMORY_OBJECT_TYPE",
  2140: "WASM_MODULE_OBJECT_TYPE",
  2141: "WASM_SUSPENDER_OBJECT_TYPE",
  2142: "WASM_TABLE_OBJECT_TYPE",
  2143: "WASM_TAG_OBJECT_TYPE",
  2144: "WASM_VALUE_OBJECT_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("read_only_space", 0x02131): (246, "MetaMap"),
  ("read_only_space", 0x02159): (131, "NullMap"),
  ("read_only_space", 0x02181): (230, "StrongDescriptorArrayMap"),
  ("read_only_space", 0x021a9): (259, "WeakArrayListMap"),
  ("read_only_space", 0x021ed): (157, "EnumCacheMap"),
  ("read_only_space", 0x02221): (177, "FixedArrayMap"),
  ("read_only_space", 0x0226d): (8, "OneByteInternalizedStringMap"),
  ("read_only_space", 0x022b9): (243, "FreeSpaceMap"),
  ("read_only_space", 0x022e1): (242, "OnePointerFillerMap"),
  ("read_only_space", 0x02309): (242, "TwoPointerFillerMap"),
  ("read_only_space", 0x02331): (131, "UninitializedMap"),
  ("read_only_space", 0x023a9): (131, "UndefinedMap"),
  ("read_only_space", 0x023ed): (130, "HeapNumberMap"),
  ("read_only_space", 0x02421): (131, "TheHoleMap"),
  ("read_only_space", 0x02481): (131, "BooleanMap"),
  ("read_only_space", 0x02525): (190, "ByteArrayMap"),
  ("read_only_space", 0x0254d): (177, "FixedCOWArrayMap"),
  ("read_only_space", 0x02575): (178, "HashTableMap"),
  ("read_only_space", 0x0259d): (128, "SymbolMap"),
  ("read_only_space", 0x025c5): (40, "OneByteStringMap"),
  ("read_only_space", 0x025ed): (252, "ScopeInfoMap"),
  ("read_only_space", 0x02615): (253, "SharedFunctionInfoMap"),
  ("read_only_space", 0x0263d): (236, "CodeMap"),
  ("read_only_space", 0x02665): (235, "CellMap"),
  ("read_only_space", 0x0268d): (251, "GlobalPropertyCellMap"),
  ("read_only_space", 0x026b5): (204, "ForeignMap"),
  ("read_only_space", 0x026dd): (234, "TransitionArrayMap"),
  ("read_only_space", 0x02705): (45, "ThinOneByteStringMap"),
  ("read_only_space", 0x0272d): (241, "FeedbackVectorMap"),
  ("read_only_space", 0x02765): (131, "ArgumentsMarkerMap"),
  ("read_only_space", 0x027c5): (131, "ExceptionMap"),
  ("read_only_space", 0x02821): (131, "TerminationExceptionMap"),
  ("read_only_space", 0x02889): (131, "OptimizedOutMap"),
  ("read_only_space", 0x028e9): (131, "StaleRegisterMap"),
  ("read_only_space", 0x02949): (189, "ScriptContextTableMap"),
  ("read_only_space", 0x02971): (187, "ClosureFeedbackCellArrayMap"),
  ("read_only_space", 0x02999): (240, "FeedbackMetadataArrayMap"),
  ("read_only_space", 0x029c1): (177, "ArrayListMap"),
  ("read_only_space", 0x029e9): (129, "BigIntMap"),
  ("read_only_space", 0x02a11): (188, "ObjectBoilerplateDescriptionMap"),
  ("read_only_space", 0x02a39): (191, "BytecodeArrayMap"),
  ("read_only_space", 0x02a61): (237, "CodeDataContainerMap"),
  ("read_only_space", 0x02a89): (238, "CoverageInfoMap"),
  ("read_only_space", 0x02ab1): (192, "FixedDoubleArrayMap"),
  ("read_only_space", 0x02ad9): (180, "GlobalDictionaryMap"),
  ("read_only_space", 0x02b01): (158, "ManyClosuresCellMap"),
  ("read_only_space", 0x02b29): (247, "MegaDomHandlerMap"),
  ("read_only_space", 0x02b51): (177, "ModuleInfoMap"),
  ("read_only_space", 0x02b79): (181, "NameDictionaryMap"),
  ("read_only_space", 0x02ba1): (158, "NoClosuresCellMap"),
  ("read_only_space", 0x02bc9): (182, "NumberDictionaryMap"),
  ("read_only_space", 0x02bf1): (158, "OneClosureCellMap"),
  ("read_only_space", 0x02c19): (183, "OrderedHashMapMap"),
  ("read_only_space", 0x02c41): (184, "OrderedHashSetMap"),
  ("read_only_space", 0x02c69): (185, "OrderedNameDictionaryMap"),
  ("read_only_space", 0x02c91): (249, "PreparseDataMap"),
  ("read_only_space", 0x02cb9): (250, "PropertyArrayMap"),
  ("read_only_space", 0x02ce1): (153, "SideEffectCallHandlerInfoMap"),
  ("read_only_space", 0x02d09): (153, "SideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x02d31): (153, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x02d59): (186, "SimpleNumberDictionaryMap"),
  ("read_only_space", 0x02d81): (224, "SmallOrderedHashMapMap"),
  ("read_only_space", 0x02da9): (225, "SmallOrderedHashSetMap"),
  ("read_only_space", 0x02dd1): (226, "SmallOrderedNameDictionaryMap"),
  ("read_only_space", 0x02df9): (231, "SourceTextModuleMap"),
  ("read_only_space", 0x02e21): (257, "SwissNameDictionaryMap"),
  ("read_only_space", 0x02e49): (232, "SyntheticModuleMap"),
  ("read_only_space", 0x02e71): (258, "WasmApiFunctionRefMap"),
  ("read_only_space", 0x02e99): (218, "WasmCapiFunctionDataMap"),
  ("read_only_space", 0x02ec1): (219, "WasmExportedFunctionDataMap"),
  ("read_only_space", 0x02ee9): (205, "WasmInternalFunctionMap"),
  ("read_only_space", 0x02f11): (220, "WasmJSFunctionDataMap"),
  ("read_only_space", 0x02f39): (206, "WasmTypeInfoMap"),
  ("read_only_space", 0x02f61): (233, "WeakFixedArrayMap"),
  ("read_only_space", 0x02f89): (179, "EphemeronHashTableMap"),
  ("read_only_space", 0x02fb1): (239, "EmbedderDataArrayMap"),
  ("read_only_space", 0x02fd9): (260, "WeakCellMap"),
  ("read_only_space", 0x03001): (32, "StringMap"),
  ("read_only_space", 0x03029): (41, "ConsOneByteStringMap"),
  ("read_only_space", 0x03051): (33, "ConsStringMap"),
  ("read_only_space", 0x03079): (37, "ThinStringMap"),
  ("read_only_space", 0x030a1): (35, "SlicedStringMap"),
  ("read_only_space", 0x030c9): (43, "SlicedOneByteStringMap"),
  ("read_only_space", 0x030f1): (34, "ExternalStringMap"),
  ("read_only_space", 0x03119): (42, "ExternalOneByteStringMap"),
  ("read_only_space", 0x03141): (50, "UncachedExternalStringMap"),
  ("read_only_space", 0x03169): (0, "InternalizedStringMap"),
  ("read_only_space", 0x03191): (2, "ExternalInternalizedStringMap"),
  ("read_only_space", 0x031b9): (10, "ExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x031e1): (18, "UncachedExternalInternalizedStringMap"),
  ("read_only_space", 0x03209): (26, "UncachedExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x03231): (58, "UncachedExternalOneByteStringMap"),
  ("read_only_space", 0x03259): (104, "SharedOneByteStringMap"),
  ("read_only_space", 0x03281): (96, "SharedStringMap"),
  ("read_only_space", 0x032a9): (109, "SharedThinOneByteStringMap"),
  ("read_only_space", 0x032d1): (101, "SharedThinStringMap"),
  ("read_only_space", 0x032f9): (96, "TwoByteSeqStringMigrationSentinelMap"),
  ("read_only_space", 0x03321): (104, "OneByteSeqStringMigrationSentinelMap"),
  ("read_only_space", 0x03349): (131, "SelfReferenceMarkerMap"),
  ("read_only_space", 0x03371): (131, "BasicBlockCountersMarkerMap"),
  ("read_only_space", 0x033b5): (147, "ArrayBoilerplateDescriptionMap"),
  ("read_only_space", 0x034b5): (160, "InterceptorInfoMap"),
  ("read_only_space", 0x05d29): (132, "PromiseFulfillReactionJobTaskMap"),
  ("read_only_space", 0x05d51): (133, "PromiseRejectReactionJobTaskMap"),
  ("read_only_space", 0x05d79): (134, "CallableTaskMap"),
  ("read_only_space", 0x05da1): (135, "CallbackTaskMap"),
  ("read_only_space", 0x05dc9): (136, "PromiseResolveThenableJobTaskMap"),
  ("read_only_space", 0x05df1): (139, "FunctionTemplateInfoMap"),
  ("read_only_space", 0x05e19): (140, "ObjectTemplateInfoMap"),
  ("read_only_space", 0x05e41): (141, "AccessCheckInfoMap"),
  ("read_only_space", 0x05e69): (142, "AccessorInfoMap"),
  ("read_only_space", 0x05e91): (143, "AccessorPairMap"),
  ("read_only_space", 0x05eb9): (144, "AliasedArgumentsEntryMap"),
  ("read_only_space", 0x05ee1): (145, "AllocationMementoMap"),
  ("read_only_space", 0x05f09): (148, "AsmWasmDataMap"),
  ("read_only_space", 0x05f31): (149, "AsyncGeneratorRequestMap"),
  ("read_only_space", 0x05f59): (150, "BreakPointMap"),
  ("read_only_space", 0x05f81): (151, "BreakPointInfoMap"),
  ("read_only_space", 0x05fa9): (152, "CachedTemplateObjectMap"),
  ("read_only_space", 0x05fd1): (154, "CallSiteInfoMap"),
  ("read_only_space", 0x05ff9): (155, "ClassPositionsMap"),
  ("read_only_space", 0x06021): (156, "DebugInfoMap"),
  ("read_only_space", 0x06049): (159, "FunctionTemplateRareDataMap"),
  ("read_only_space", 0x06071): (161, "InterpreterDataMap"),
  ("read_only_space", 0x06099): (162, "ModuleRequestMap"),
  ("read_only_space", 0x060c1): (163, "PromiseCapabilityMap"),
  ("read_only_space", 0x060e9): (164, "PromiseReactionMap"),
  ("read_only_space", 0x06111): (165, "PropertyDescriptorObjectMap"),
  ("read_only_space", 0x06139): (166, "PrototypeInfoMap"),
  ("read_only_space", 0x06161): (167, "RegExpBoilerplateDescriptionMap"),
  ("read_only_space", 0x06189): (168, "ScriptMap"),
  ("read_only_space", 0x061b1): (169, "ScriptOrModuleMap"),
  ("read_only_space", 0x061d9): (170, "SourceTextModuleInfoEntryMap"),
  ("read_only_space", 0x06201): (171, "StackFrameInfoMap"),
  ("read_only_space", 0x06229): (172, "TemplateObjectDescriptionMap"),
  ("read_only_space", 0x06251): (173, "Tuple2Map"),
  ("read_only_space", 0x06279): (174, "WasmContinuationObjectMap"),
  ("read_only_space", 0x062a1): (175, "WasmExceptionTagMap"),
  ("read_only_space", 0x062c9): (176, "WasmIndirectFunctionTableMap"),
  ("read_only_space", 0x062f1): (194, "SloppyArgumentsElementsMap"),
  ("read_only_space", 0x06319): (229, "DescriptorArrayMap"),
  ("read_only_space", 0x06341): (202, "UncompiledDataWithoutPreparseDataMap"),
  ("read_only_space", 0x06369): (200, "UncompiledDataWithPreparseDataMap"),
  ("read_only_space", 0x06391): (203, "UncompiledDataWithoutPreparseDataWithJobMap"),
  ("read_only_space", 0x063b9): (201, "UncompiledDataWithPreparseDataAndJobMap"),
  ("read_only_space", 0x063e1): (248, "OnHeapBasicBlockProfilerDataMap"),
  ("read_only_space", 0x06409): (195, "TurbofanBitsetTypeMap"),
  ("read_only_space", 0x06431): (199, "TurbofanUnionTypeMap"),
  ("read_only_space", 0x06459): (198, "TurbofanRangeTypeMap"),
  ("read_only_space", 0x06481): (196, "TurbofanHeapConstantTypeMap"),
  ("read_only_space", 0x064a9): (197, "TurbofanOtherNumberConstantTypeMap"),
  ("read_only_space", 0x064d1): (244, "InternalClassMap"),
  ("read_only_space", 0x064f9): (255, "SmiPairMap"),
  ("read_only_space", 0x06521): (254, "SmiBoxMap"),
  ("read_only_space", 0x06549): (221, "ExportedSubClassBaseMap"),
  ("read_only_space", 0x06571): (222, "ExportedSubClassMap"),
  ("read_only_space", 0x06599): (227, "AbstractInternalClassSubclass1Map"),
  ("read_only_space", 0x065c1): (228, "AbstractInternalClassSubclass2Map"),
  ("read_only_space", 0x065e9): (193, "InternalClassWithSmiElementsMap"),
  ("read_only_space", 0x06611): (245, "InternalClassWithStructElementsMap"),
  ("read_only_space", 0x06639): (223, "ExportedSubClass2Map"),
  ("read_only_space", 0x06661): (256, "SortStateMap"),
  ("read_only_space", 0x06689): (146, "AllocationSiteWithWeakNextMap"),
  ("read_only_space", 0x066b1): (146, "AllocationSiteWithoutWeakNextMap"),
  ("read_only_space", 0x066d9): (137, "LoadHandler1Map"),
  ("read_only_space", 0x06701): (137, "LoadHandler2Map"),
  ("read_only_space", 0x06729): (137, "LoadHandler3Map"),
  ("read_only_space", 0x06751): (138, "StoreHandler0Map"),
  ("read_only_space", 0x06779): (138, "StoreHandler1Map"),
  ("read_only_space", 0x067a1): (138, "StoreHandler2Map"),
  ("read_only_space", 0x067c9): (138, "StoreHandler3Map"),
  ("map_space", 0x02131): (1057, "ExternalMap"),
  ("map_space", 0x02159): (2114, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("read_only_space", 0x021d1): "EmptyWeakArrayList",
  ("read_only_space", 0x021dd): "EmptyDescriptorArray",
  ("read_only_space", 0x02215): "EmptyEnumCache",
  ("read_only_space", 0x02249): "EmptyFixedArray",
  ("read_only_space", 0x02251): "NullValue",
  ("read_only_space", 0x02359): "UninitializedValue",
  ("read_only_space", 0x023d1): "UndefinedValue",
  ("read_only_space", 0x02415): "NanValue",
  ("read_only_space", 0x02449): "TheHoleValue",
  ("read_only_space", 0x02475): "HoleNanValue",
  ("read_only_space", 0x024a9): "TrueValue",
  ("read_only_space", 0x024e9): "FalseValue",
  ("read_only_space", 0x02519): "empty_string",
  ("read_only_space", 0x02755): "EmptyScopeInfo",
  ("read_only_space", 0x0278d): "ArgumentsMarker",
  ("read_only_space", 0x027ed): "Exception",
  ("read_only_space", 0x02849): "TerminationException",
  ("read_only_space", 0x028b1): "OptimizedOut",
  ("read_only_space", 0x02911): "StaleRegister",
  ("read_only_space", 0x03399): "EmptyPropertyArray",
  ("read_only_space", 0x033a1): "EmptyByteArray",
  ("read_only_space", 0x033a9): "EmptyObjectBoilerplateDescription",
  ("read_only_space", 0x033dd): "EmptyArrayBoilerplateDescription",
  ("read_only_space", 0x033e9): "EmptyClosureFeedbackCellArray",
  ("read_only_space", 0x033f1): "EmptySlowElementDictionary",
  ("read_only_space", 0x03415): "EmptyOrderedHashMap",
  ("read_only_space", 0x03429): "EmptyOrderedHashSet",
  ("read_only_space", 0x0343d): "EmptyFeedbackMetadata",
  ("read_only_space", 0x03449): "EmptyPropertyDictionary",
  ("read_only_space", 0x03471): "EmptyOrderedPropertyDictionary",
  ("read_only_space", 0x03489): "EmptySwissPropertyDictionary",
  ("read_only_space", 0x034dd): "NoOpInterceptorInfo",
  ("read_only_space", 0x03505): "EmptyWeakFixedArray",
  ("read_only_space", 0x0350d): "InfinityValue",
  ("read_only_space", 0x03519): "MinusZeroValue",
  ("read_only_space", 0x03525): "MinusInfinityValue",
  ("read_only_space", 0x03531): "SelfReferenceMarker",
  ("read_only_space", 0x03571): "BasicBlockCountersMarker",
  ("read_only_space", 0x035b5): "OffHeapTrampolineRelocationInfo",
  ("read_only_space", 0x035c1): "TrampolineTrivialCodeDataContainer",
  ("read_only_space", 0x035cd): "TrampolinePromiseRejectionCodeDataContainer",
  ("read_only_space", 0x035d9): "GlobalThisBindingScopeInfo",
  ("read_only_space", 0x03609): "EmptyFunctionScopeInfo",
  ("read_only_space", 0x0362d): "NativeScopeInfo",
  ("read_only_space", 0x03645): "HashSeed",
  ("old_space", 0x04229): "ArgumentsIteratorAccessor",
  ("old_space", 0x0426d): "ArrayLengthAccessor",
  ("old_space", 0x042b1): "BoundFunctionLengthAccessor",
  ("old_space", 0x042f5): "BoundFunctionNameAccessor",
  ("old_space", 0x04339): "ErrorStackAccessor",
  ("old_space", 0x0437d): "FunctionArgumentsAccessor",
  ("old_space", 0x043c1): "FunctionCallerAccessor",
  ("old_space", 0x04405): "FunctionNameAccessor",
  ("old_space", 0x04449): "FunctionLengthAccessor",
  ("old_space", 0x0448d): "FunctionPrototypeAccessor",
  ("old_space", 0x044d1): "StringLengthAccessor",
  ("old_space", 0x04515): "InvalidPrototypeValidityCell",
  ("old_space", 0x0451d): "EmptyScript",
  ("old_space", 0x0455d): "ManyClosuresCell",
  ("old_space", 0x04569): "ArrayConstructorProtector",
  ("old_space", 0x0457d): "NoElementsProtector",
  ("old_space", 0x04591): "MegaDOMProtector",
  ("old_space", 0x045a5): "IsConcatSpreadableProtector",
  ("old_space", 0x045b9): "ArraySpeciesProtector",
  ("old_space", 0x045cd): "TypedArraySpeciesProtector",
  ("old_space", 0x045e1): "PromiseSpeciesProtector",
  ("old_space", 0x045f5): "RegExpSpeciesProtector",
  ("old_space", 0x04609): "StringLengthProtector",
  ("old_space", 0x0461d): "ArrayIteratorProtector",
  ("old_space", 0x04631): "ArrayBufferDetachingProtector",
  ("old_space", 0x04645): "PromiseHookProtector",
  ("old_space", 0x04659): "PromiseResolveProtector",
  ("old_space", 0x0466d): "MapIteratorProtector",
  ("old_space", 0x04681): "PromiseThenProtector",
  ("old_space", 0x04695): "SetIteratorProtector",
  ("old_space", 0x046a9): "StringIteratorProtector",
  ("old_space", 0x046bd): "SingleCharacterStringCache",
  ("old_space", 0x04ac5): "StringSplitCache",
  ("old_space", 0x04ecd): "RegExpMultipleCache",
  ("old_space", 0x052d5): "BuiltinsConstantsTable",
  ("old_space", 0x056fd): "AsyncFunctionAwaitRejectSharedFun",
  ("old_space", 0x05721): "AsyncFunctionAwaitResolveSharedFun",
  ("old_space", 0x05745): "AsyncGeneratorAwaitRejectSharedFun",
  ("old_space", 0x05769): "AsyncGeneratorAwaitResolveSharedFun",
  ("old_space", 0x0578d): "AsyncGeneratorYieldResolveSharedFun",
  ("old_space", 0x057b1): "AsyncGeneratorReturnResolveSharedFun",
  ("old_space", 0x057d5): "AsyncGeneratorReturnClosedRejectSharedFun",
  ("old_space", 0x057f9): "AsyncGeneratorReturnClosedResolveSharedFun",
  ("old_space", 0x0581d): "AsyncIteratorValueUnwrapSharedFun",
  ("old_space", 0x05841): "PromiseAllResolveElementSharedFun",
  ("old_space", 0x05865): "PromiseAllSettledResolveElementSharedFun",
  ("old_space", 0x05889): "PromiseAllSettledRejectElementSharedFun",
  ("old_space", 0x058ad): "PromiseAnyRejectElementSharedFun",
  ("old_space", 0x058d1): "PromiseCapabilityDefaultRejectSharedFun",
  ("old_space", 0x058f5): "PromiseCapabilityDefaultResolveSharedFun",
  ("old_space", 0x05919): "PromiseCatchFinallySharedFun",
  ("old_space", 0x0593d): "PromiseGetCapabilitiesExecutorSharedFun",
  ("old_space", 0x05961): "PromiseThenFinallySharedFun",
  ("old_space", 0x05985): "PromiseThrowerFinallySharedFun",
  ("old_space", 0x059a9): "PromiseValueThunkFinallySharedFun",
  ("old_space", 0x059cd): "ProxyRevokeSharedFun",
}

# Lower 32 bits of first page addresses for various heap spaces.
HEAP_FIRST_PAGES = {
  0x080c0000: "old_space",
  0x08100000: "map_space",
  0x08000000: "read_only_space",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "WASM",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "RETURN_PROMISE_ON_SUSPEND",
  "WASM_DEBUG_BREAK",
  "C_WASM_ENTRY",
  "WASM_EXIT",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "BASELINE",
  "OPTIMIZED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.