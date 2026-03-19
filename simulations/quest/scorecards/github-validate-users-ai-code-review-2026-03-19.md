● skill(review-users)

● List directory .
  └ 13 files found

● Search (glob)
  │ "simulations/**/*"
  └ 27 files found

● Search (glob)
  │ "signals/**/*"
  └ 16 files found

Let me read the key design artifacts to understand what the five personas will be reviewing.

● Read ai-code-review-spec-2026-03-19.md
  │ signals\draft\specs\ai-code-review-spec-2026-03-19.md
  └ 1 line read

● Read ai-code-review-proposal-2026-03-19.md
  │ signals\specify\proposal\ai-code-review-proposal-2026-03-19.md
  └ 122 lines read

● Read ai-code-review-pitch-2026-03-19.md
  │ signals\specify\pitch\ai-code-review-pitch-2026-03-19.md
  └ 219 lines read

Now let me read the spec and commitment artifacts for additional design detail.

● Read ai-code-review-commitment-2026-03-19.md
  │ signals\specify\commitment\ai-code-review-commitment-2026-03-19.md
  └ 230 lines read

● Read ai-code-review-spec-2026-03-19.md
  │ signals\draft\specs\ai-code-review-spec-2026-03-19.md
  └ L1:120 (120 lines read)

Let me read the rest of the spec's design sections and the lifecycle simulation.

● Read ai-code-review-spec-2026-03-19.md
  │ signals\draft\specs\ai-code-review-spec-2026-03-19.md
  └ L120:300 (181 lines read)

● Read ai-code-review-lifecycle-2026-03-19.md
  │ signals\simulate\lifecycle\ai-code-review-lifecycle-2026-03-19.md
  └ L1:80 (79 lines read)

Let me read the remaining spec sections for the full design picture.

● Read ai-code-review-spec-2026-03-19.md
  │ signals\draft\specs\ai-code-review-spec-2026-03-19.md
  └ L300:450 (151 lines read)



#
# Fatal process out of memory: Zone
#
----- Native stack trace -----

 1: 00007FF6B291D52D node::MultiIsolatePlatform::DisposeIsolate+5341
 2: 00007FF6B3D6C206 v8::base::FatalOOM+54
 3: 00007FF6B360D9C5 v8::Function::NewInstance+245
 4: 00007FF6B2F88A46 v8::SnapshotCreator::GetIsolate+56566
 5: 00007FF6B41DF69A v8::base::DiyFp::Multiply+2470186
 6: 00007FF6B41DED8B v8::base::DiyFp::Multiply+2467867
 7: 00007FF6B41DE24D v8::base::DiyFp::Multiply+2464989
 8: 00007FF6B41DDD24 v8::base::DiyFp::Multiply+2463668
 9: 00007FF6B41DD2B1 v8::base::DiyFp::Multiply+2460993
10: 00007FF6B41DD00F v8::base::DiyFp::Multiply+2460319
11: 00007FF6B3FE9A46 v8::base::DiyFp::Multiply+414934
12: 00007FF6B3FE8760 v8::base::DiyFp::Multiply+410096
13: 00007FF6B3DCC4EB v8::internal::compiler::CompilationDependencies::FieldTypeDependencyOffTheRecord+192907
14: 00007FF6B2C82346 DSA_get0_engine+659126
15: 00007FF6B2C7DA83 DSA_get0_engine+640499
16: 00007FF6B2C7D369 DSA_get0_engine+638681
17: 00007FF6B3DDFDDF v8::base::SysInfo::AddressSpaceEnd+3167
18: 00007FF6B29193EE node::GetNodeReport+89326
19: 00007FF6B3662DE6 uv_thread_detach+150
20: 00007FF6B48A4173 v8::base::UnsignedDivisionByConstant<unsigned __int64>+2903907
21: 00007FFA6549E8D7 BaseThreadInitThunk+23
22: 00007FFA6666C53C RtlUserThreadStart+44
