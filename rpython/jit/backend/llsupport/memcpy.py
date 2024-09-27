from rpython.rtyper.lltypesystem import lltype, rffi, llmemory

memcpy_fn = rffi.llexternal('memcpy', [rffi.VOIDP, rffi.CONST_VOIDP,
                                       rffi.SIZE_T], rffi.VOIDP,
                            sandboxsafe=True, _nowrapper=True)
memset_fn = rffi.llexternal('memset', [llmemory.Address, rffi.INT,
                                       rffi.SIZE_T], lltype.Void,
                            sandboxsafe=True, _nowrapper=True)
